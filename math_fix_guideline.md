# Math Formatting & Rendering Fixes Guideline

This document serves as a comprehensive checklist and guideline for all the LaTeX and Markdown rendering issues that were identified and fixed across the `Math_2117_Semester_Final` repository. 

Review this guideline before making your final commit to ensure you understand the changes and can maintain these standards in future additions.

---

## 1. Math Expressions in Markdown Headings
**The Problem:**
Placing complex LaTeX expressions (such as vectors, integrals, or fractions) directly inside Markdown headings (e.g., `## $\vec{F}$`) caused severe rendering issues. The viewer attempted to force the tall mathematical symbols into the strict line-height of a heading, resulting in vertical overlapping and unreadable text.

**The Fix:**
- **Extrication:** All LaTeX math was programmatically removed from heading lines.
- **Standardization:** Headings were rewritten to clean, plain-text titles containing only the question number and marks (e.g., `## Q1 (04)`).
- **Relocation:** The actual mathematical questions were moved to standard paragraph text immediately below the heading. 

## 2. Subscripts inside Math Blocks
**The Problem:**
Escaping underscores as `\_` inside mathematical equations (both inline `$ ... $` and block math `$$ ... $$`) causes LaTeX engines (like MathJax/KaTeX) to render them as literal underscore characters (e.g. $A_1$ displaying with a visible underscore `A_1`), rather than subscripts.

**The Fix:**
- **Unescaped Standard Subscripts:** Always use standard LaTeX subscript notation `_` (e.g., `$A_1$`, `$$ A_1 $$`) inside math environments.
- **Italics Conflict resolution:** In modern Markdown editors (like VS Code or Obsidian), math blocks are parsed as math and are inherently immune to the italics conflict. If an italics conflict occurs in other environments due to multiple underscores, wrap the expressions in block math or ensure they are isolated from standard Markdown italics indicators.


## 3. Multi-line Inline Matrices
**The Problem:**
Matrices defined over multiple lines using `\begin{vmatrix} ... \end{vmatrix}` but wrapped in inline math delimiters (`$ ... $`) failed to render. The parser choked on the line breaks inside an inline string, displaying raw LaTeX source code instead of a formatted matrix.

**The Fix:**
- **Block Conversion:** Any inline math block containing multi-line environments (like matrices or arrays) was upgraded to display block math using double dollar signs (`$$ ... $$`).

## 4. Inline Integrals Stretching Line Heights
**The Problem:**
Mathematical operators with large vertical heights—such as double integrals (`\iint`), triple integrals (`\iiint`), line integrals (`\int`), and closed integrals (`\oint`)—caused layout distortion when used inside standard text paragraphs. The viewer struggled to balance the line heights, pushing the surrounding text out of alignment.

**The Fix:**
- **Block Conversion:** Every inline integral was extracted from the paragraph and converted into display block math (`$$ ... $$`) on its own line.
- **Punctuation:** Surrounding punctuation (like commas or periods) was cleanly separated, preserving grammatical correctness without compromising the math render.

## 5. The "Wrapping Hat" Bug (Unit Vectors Dropping Down)
**The Problem:**
This was the most visually jarring bug. When a long inline vector equation (e.g., `$\vec{F} = 3xy\hat{i} - y^2\hat{j}$`) reached the edge of the viewer window, it automatically wrapped the text at an operator like `+` or `-`. However, the viewer miscalculated the baseline of the wrapped text. As a result, tall accented characters like `\hat{j}` or `\hat{k}` on the new line dropped entirely below the text baseline or overlapped with sentences below them.

**The Fix:**
- **Targeted Block Conversion:** A script was executed across the repository to locate **all** inline math expressions that defined vector equations (containing both an equals sign `=` or operators like `+`/`-` AND a hat symbol `\hat`).
- These long inline vector definitions were converted into display block math (`$$ ... $$`), which natively handles wrapping and vertical alignment perfectly.
- **Vector Lists:** Sequences of three inline vectors (e.g., $\vec{A} = ...$, $\vec{B} = ...$, $\vec{C} = ...$) were combined into a single, highly readable display math block separated by `\quad`.

---

## Maintenance Checklist for Future Updates

If you add new questions or answers to the repository, please adhere to these formatting rules to prevent rendering bugs from returning:

1. [ ] **Keep headings clean:** Never put `$` or `$$` inside a `#` or `##` heading.
2. [ ] **Use unescaped subscripts inside math:** Use standard `_` (not `\_`) inside all `$ ... $` and `$$ ... $$` math blocks.
3. [ ] **Use block math for matrices:** Always use `$$ ... $$` for `\begin{pmatrix}` or `\begin{vmatrix}`.
4. [ ] **Use block math for integrals:** Always use `$$ ... $$` for `\int`, `\iint`, `\iiint`, and `\oint`.
5. [ ] **Use block math for vector equations:** If you are defining a vector with unit vectors like `\hat{i}, \hat{j}, \hat{k}` (e.g., $\vec{A} = x\hat{i} + y\hat{j}$), put it in `$$ ... $$` to prevent the wrapping baseline bug. Standalone short vectors (like $\vec{A}$) can remain inline.
