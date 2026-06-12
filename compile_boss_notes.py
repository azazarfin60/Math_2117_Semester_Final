#!/usr/bin/env python3
import os
import re
import subprocess

BASE_DIR = "/home/azaz/AntigravityData/Math_2117_Semester_Final"
BOSS_DIR = os.path.join(BASE_DIR, "boss_notes")

def clean_markdown(content):
    lines = content.split('\n')
    cleaned = []
    for line in lines:
        # Remove the navigation bar lines
        if line.startswith('[') and 'Index' in line and '00_Index.md' in line:
            continue
        cleaned.append(line)
    
    # We also want to replace single backslash newlines in equations if they are causing issues, 
    # but Pandoc handles them perfectly.
    
    # Fix Pandoc block math parsing: remove blank lines immediately after $$ or before $$
    text = '\n'.join(cleaned)
    text = re.sub(r'\$\$\n+', '$$\n', text)
    text = re.sub(r'\n+\$\$', '\n$$', text)
    return text

def main():
    files = sorted([f for f in os.listdir(BOSS_DIR) if f.endswith('.md') and (f.startswith('A') or f.startswith('B') or f.startswith('C'))])
    
    combined_content = ""
    for f in files:
        with open(os.path.join(BOSS_DIR, f), 'r', encoding='utf-8') as infile:
            content = infile.read()
            combined_content += clean_markdown(content)
            combined_content += "\n\n\\newpage\n\n" # Page break between chapters
            
    out_md = os.path.join(BASE_DIR, "boss_notes_combined.md")
    with open(out_md, 'w', encoding='utf-8') as outfile:
        outfile.write(combined_content)
        
    print(f"Combined {len(files)} files into {out_md}")
    
    # Create metadata yaml for pandoc
    metadata = """---
title: "Math 2117: Final Exam Boss Notes"
author: "Compiled for Exam Preparation"
date: "June 2026"
geometry: margin=1in
colorlinks: true
toccolor: blue
header-includes:
  - \\usepackage{amsmath}
  - \\usepackage{amssymb}
  - \\usepackage{graphicx}
  - \\usepackage{bm}
---
"""
    yaml_path = os.path.join(BASE_DIR, "metadata.yaml")
    with open(yaml_path, 'w', encoding='utf-8') as yf:
        yf.write(metadata)
        
    print("Running Pandoc...")
    pdf_out = os.path.join(BASE_DIR, "Math_2117_Boss_Notes.pdf")
    
    cmd = [
        "pandoc", 
        yaml_path, 
        out_md, 
        "-o", pdf_out, 
        "--pdf-engine=pdflatex", 
        "--toc", 
        "-N" # Numbered sections
    ]
    
    result = subprocess.run(cmd, cwd=BASE_DIR, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"Success! PDF generated at {pdf_out}")
    else:
        print("Pandoc compilation failed.")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)

if __name__ == "__main__":
    main()
