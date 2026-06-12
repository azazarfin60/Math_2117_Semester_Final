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
        if line.startswith('[') and 'Index' in line and '00_Index.md' in line:
            continue
        cleaned.append(line)
    
    text = '\n'.join(cleaned)
    
    # Fix math block spacing for Pandoc
    parts = text.split('$$')
    new_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            math_lines = part.split('\n')
            math_lines_cleaned = [l for l in math_lines if l.strip() != '']
            new_parts.append('\n' + '\n'.join(math_lines_cleaned) + '\n')
        else:
            new_parts.append(part)
            
    return '$$'.join(new_parts)

def post_process_tex(tex_content, theme="light"):
    # 1. Remove the center horizontal rules that add massive vertical spaces
    tex_content = re.sub(r'\\begin\{center\}\\rule\{0\.5\\linewidth\}\{0\.5pt\}\\end\{center\}', '', tex_content)
    
    # 2. Fix the double-dollar (\$\$) escaping issue from leftover pandoc parsing
    tex_content = tex_content.replace(r'\$\$', '')
    
    # 3. Strip all manual \newpage commands to let content flow naturally
    tex_content = tex_content.replace(r'\newpage', '')
    
    # 4. Remove blank lines around LaTeX math blocks to prevent paragraph separation & extra parskip spacing
    lines = tex_content.split('\n')
    cleaned = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # If we see a blank line followed by \[
        if stripped == '' and i + 1 < len(lines) and lines[i+1].strip() == '\\[':
            cleaned.append(lines[i+1])
            i += 2
            continue
        # If we see \] followed by a blank line
        if stripped == '\\]' and i + 1 < len(lines) and lines[i+1].strip() == '':
            cleaned.append(line)
            i += 2
            continue
        cleaned.append(line)
        i += 1
    
    tex_content = '\n'.join(cleaned)
    
    # 5. Clean up multiple consecutive newlines in the generated LaTeX
    tex_content = re.sub(r'\n{3,}', '\n\n', tex_content)
    
    # 6. Redefine quote environment to look like a premium callout box using tcolorbox
    tcolorbox_setup = r"""
\usepackage[most]{tcolorbox}
\renewenvironment{quote}
  {\begin{tcolorbox}[colback=calloutbg,colframe=calloutframe,arc=3pt,boxrule=0.5pt,leftrule=3pt,left=8pt,right=8pt,top=6pt,bottom=6pt]}
  {\end{tcolorbox}}
"""
    
    # 7. Setup enumitem to eliminate spaces in all itemize/enumerate lists
    list_setup = r"""
\usepackage{enumitem}
\setlist{nosep}
\setlist[itemize]{leftmargin=15pt}
\setlist[enumerate]{leftmargin=15pt}
"""
    
    # 8. Adjust parskip to be tighter (3pt instead of 6pt)
    parskip_setup = r"""
\setlength{\parskip}{3pt plus 1pt minus 1pt}
"""

    # 9. Headings color styling
    headings_setup = r"""
\usepackage{sectsty}
\sectionfont{\color{headercolor}}
\subsectionfont{\color{headercolor}}
\subsubsectionfont{\color{headercolor}}
"""
    
    if theme == "dark":
        color_setup = r"""
\usepackage{xcolor}
\usepackage{eso-pic}
\definecolor{darkbg}{HTML}{1E1E1E}
\definecolor{lighttext}{HTML}{E0E0E0}
\definecolor{calloutbg}{HTML}{2D3748}
\definecolor{calloutframe}{HTML}{3182CE}
\definecolor{headercolor}{HTML}{63B3ED}
\AddToShipoutPictureBG{\color{darkbg}\AtPageLowerLeft{\rule{\paperwidth}{\paperheight}}}
\color{lighttext}
\hypersetup{
  colorlinks=true,
  linkcolor=cyan,
  filecolor=cyan,
  citecolor=cyan,
  urlcolor=cyan
}
"""
    else:
        color_setup = r"""
\usepackage{xcolor}
\definecolor{calloutbg}{HTML}{F0F8FF}
\definecolor{calloutframe}{HTML}{1D4ED8}
\definecolor{headercolor}{HTML}{1E3A8A}
\hypersetup{
  colorlinks=true,
  linkcolor=blue,
  filecolor=blue,
  citecolor=blue,
  urlcolor=blue
}
"""
    
    # Inject all setups before \begin{document}
    insertion = color_setup + tcolorbox_setup + list_setup + parskip_setup + headings_setup
    tex_content = tex_content.replace(r'\begin{document}', insertion + '\n\\begin{document}')
    
    return tex_content

def main():
    files = sorted([f for f in os.listdir(BOSS_DIR) if f.endswith('.md') and (f.startswith('A') or f.startswith('B') or f.startswith('C'))])
    
    combined_content = ""
    for f in files:
        with open(os.path.join(BOSS_DIR, f), 'r', encoding='utf-8') as infile:
            content = infile.read()
            combined_content += clean_markdown(content)
            combined_content += "\n\n"
            
    out_md = os.path.join(BASE_DIR, "boss_notes_combined.md")
    with open(out_md, 'w', encoding='utf-8') as outfile:
        outfile.write(combined_content)
        
    print(f"Combined {len(files)} files.")
    
    # Generate base tex file
    print("Generating base .tex file...")
    yaml_dummy = os.path.join(BASE_DIR, "dummy.yaml")
    with open(yaml_dummy, 'w') as f:
        f.write("""---
title: "Math 2117: Final Exam Boss Notes"
author: "Compiled for Exam Preparation"
date: "June 2026"
geometry: margin=1in
header-includes:
  - \\usepackage{amsmath}
  - \\usepackage{amssymb}
  - \\usepackage{graphicx}
  - \\usepackage{bm}
---
""")
        
    tex_base = os.path.join(BASE_DIR, "Math_2117_Boss_Notes_Base.tex")
    subprocess.run([
        "pandoc", yaml_dummy, out_md, 
        "-o", tex_base, 
        "--pdf-engine=pdflatex", 
        "--standalone", 
        "--toc", "-N"
    ], cwd=BASE_DIR)
    
    # Read the base tex
    with open(tex_base, 'r', encoding='utf-8') as f:
        base_tex_content = f.read()
        
    # --- Light PDF ---
    print("Creating Light Theme Tex and PDF...")
    light_tex = post_process_tex(base_tex_content, "light")
    light_tex_path = os.path.join(BASE_DIR, "Math_2117_Boss_Notes_Light.tex")
    with open(light_tex_path, 'w', encoding='utf-8') as f:
        f.write(light_tex)
        
    subprocess.run([
        "pdflatex", "-interaction=nonstopmode", "Math_2117_Boss_Notes_Light.tex"
    ], cwd=BASE_DIR)
    subprocess.run([
        "pdflatex", "-interaction=nonstopmode", "Math_2117_Boss_Notes_Light.tex"
    ], cwd=BASE_DIR)
    
    # --- Dark PDF ---
    print("Creating Dark Theme Tex and PDF...")
    dark_tex = post_process_tex(base_tex_content, "dark")
    dark_tex_path = os.path.join(BASE_DIR, "Math_2117_Boss_Notes_Dark.tex")
    with open(dark_tex_path, 'w', encoding='utf-8') as f:
        f.write(dark_tex)
        
    subprocess.run([
        "pdflatex", "-interaction=nonstopmode", "Math_2117_Boss_Notes_Dark.tex"
    ], cwd=BASE_DIR)
    subprocess.run([
        "pdflatex", "-interaction=nonstopmode", "Math_2117_Boss_Notes_Dark.tex"
    ], cwd=BASE_DIR)
    
    print("Cleanup temporary files...")
    for ext in ["aux", "log", "out", "toc"]:
        for prefix in ["Math_2117_Boss_Notes_Light", "Math_2117_Boss_Notes_Dark"]:
            file_to_rem = os.path.join(BASE_DIR, f"{prefix}.{ext}")
            if os.path.exists(file_to_rem):
                os.remove(file_to_rem)
                
    if os.path.exists(tex_base):
        os.remove(tex_base)
    if os.path.exists(yaml_dummy):
        os.remove(yaml_dummy)
        
    print("Done! PDFs successfully generated and polished.")

if __name__ == "__main__":
    main()
