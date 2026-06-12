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
    
    text = '\n'.join(cleaned)
    
    # Fix Pandoc block math parsing: remove ALL blank lines inside $$ ... $$
    # Pandoc requires block math to have no blank lines inside it.
    
    # We will split the text by $$
    parts = text.split('$$')
    new_parts = []
    
    for i, part in enumerate(parts):
        # Every odd index is inside a $$ ... $$ block
        if i % 2 == 1:
            # Inside math block: remove all blank lines
            math_lines = part.split('\n')
            math_lines_cleaned = [line for line in math_lines if line.strip() != '']
            new_parts.append('\n' + '\n'.join(math_lines_cleaned) + '\n')
        else:
            # Outside math block
            new_parts.append(part)
            
    return '$$'.join(new_parts)

def main():
    files = sorted([f for f in os.listdir(BOSS_DIR) if f.endswith('.md') and (f.startswith('A') or f.startswith('B') or f.startswith('C'))])
    
    combined_content = ""
    for f in files:
        with open(os.path.join(BOSS_DIR, f), 'r', encoding='utf-8') as infile:
            content = infile.read()
            combined_content += clean_markdown(content)
            combined_content += "\n\n\\newpage\n\n"
            
    out_md = os.path.join(BASE_DIR, "boss_notes_combined.md")
    with open(out_md, 'w', encoding='utf-8') as outfile:
        outfile.write(combined_content)
        
    print(f"Combined {len(files)} files into {out_md}")
    
    # Create LIGHT metadata
    metadata_light = """---
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
    yaml_light = os.path.join(BASE_DIR, "metadata_light.yaml")
    with open(yaml_light, 'w', encoding='utf-8') as yf:
        yf.write(metadata_light)
        
    # Create DARK metadata
    metadata_dark = """---
title: "Math 2117: Final Exam Boss Notes"
author: "Compiled for Exam Preparation"
date: "June 2026"
geometry: margin=1in
colorlinks: true
linkcolor: cyan
urlcolor: cyan
toccolor: cyan
header-includes:
  - \\usepackage{amsmath}
  - \\usepackage{amssymb}
  - \\usepackage{graphicx}
  - \\usepackage{bm}
  - \\usepackage{xcolor}
  - \\definecolor{darkbg}{HTML}{1E1E1E}
  - \\definecolor{lighttext}{HTML}{E0E0E0}
  - \\pagecolor{darkbg}
  - \\color{lighttext}
---
"""
    yaml_dark = os.path.join(BASE_DIR, "metadata_dark.yaml")
    with open(yaml_dark, 'w', encoding='utf-8') as yf:
        yf.write(metadata_dark)
        
    print("Running Pandoc (Light Theme)...")
    pdf_light = os.path.join(BASE_DIR, "Math_2117_Boss_Notes_Light.pdf")
    cmd_light = ["pandoc", yaml_light, out_md, "-o", pdf_light, "--pdf-engine=pdflatex", "--toc", "-N"]
    res_light = subprocess.run(cmd_light, cwd=BASE_DIR, capture_output=True, text=True)
    if res_light.returncode == 0:
        print(f"Success! Light PDF generated at {pdf_light}")
    else:
        print("Light compilation failed.\n", res_light.stdout, res_light.stderr)
        
    print("Running Pandoc (Dark Theme)...")
    pdf_dark = os.path.join(BASE_DIR, "Math_2117_Boss_Notes_Dark.pdf")
    cmd_dark = ["pandoc", yaml_dark, out_md, "-o", pdf_dark, "--pdf-engine=pdflatex", "--toc", "-N"]
    res_dark = subprocess.run(cmd_dark, cwd=BASE_DIR, capture_output=True, text=True)
    if res_dark.returncode == 0:
        print(f"Success! Dark PDF generated at {pdf_dark}")
    else:
        print("Dark compilation failed.\n", res_dark.stdout, res_dark.stderr)

if __name__ == "__main__":
    main()
