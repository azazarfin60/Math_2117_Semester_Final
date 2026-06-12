# Math Formatting Rules for GitHub Rendering

**This file is the single source of truth for all LaTeX math formatting in this repository.**

Every agent or contributor writing markdown files with math equations MUST follow these rules. GitHub uses MathJax to render math. Its markdown parser (GFM) pre-processes the raw text *before* the math engine runs. Most rendering bugs come from GFM interfering with LaTeX syntax. These rules prevent that.

---

## Quick Reference (Copy-Paste Checklist)

Before committing any file, verify ALL of the following:

- [ ] No `$` or `$$` inside markdown headings (`#`, `##`, etc.)
- [ ] No `\_` inside math blocks — use plain `_` for subscripts
- [ ] No `\{` or `\}` anywhere — use `\lbrace` and `\rbrace` instead
- [ ] Every `\lbrace` or `\rbrace` has a **space** before the next letter/digit
- [ ] Every `\begin{pmatrix}`, `\begin{bmatrix}`, `\begin{vmatrix}`, `\begin{array}` is inside `$$ ... $$`, never `$ ... $`
- [ ] Every `\int`, `\iint`, `\iiint`, `\oint` equation is inside `$$ ... $$`
- [ ] Every vector equation with `\hat{i}`, `\hat{j}`, `\hat{k}` and operators is inside `$$ ... $$`
- [ ] Every `$$` starts at column 0 (no leading spaces or tabs)
- [ ] A blank line exists before every opening `$$` and after every closing `$$`
- [ ] No blank lines exist *inside* a `$$ ... $$` block
- [ ] No line inside `$$` starts with `+ `, `- `, or `* ` (operator then space)
- [ ] Trailing punctuation (`.`, `,`) is inside the block math, not dangling outside

---

## Rule 1: No Math in Headings

**Bad:**
```markdown
## Find $\vec{F} = 3\hat{i} + 2\hat{j}$
```

**Good:**
```markdown
## Q1 (04)
**Question:** Find $\vec{F} = 3\hat{i} + 2\hat{j}$
```

GFM forces heading content into a strict line-height. Tall math symbols (fractions, integrals, hats) overflow and overlap with other text.

---

## Rule 2: Use Plain `_` for Subscripts in Math

**Bad:** `$A\_1$`, `$x\_{ij}$`
**Good:** `$A_1$`, `$x_{ij}$`

Inside `$ ... $` and `$$ ... $$`, the backslash-escaped underscore `\_` renders as a literal underscore character instead of a subscript. Use plain `_` only.

---

## Rule 3: Use `\lbrace` and `\rbrace` Instead of `\{` and `\}`

This is the #1 cause of recurring bugs. GFM's text parser strips the backslash from `\{` before MathJax sees it. The math engine then receives a raw `{` which breaks parsing.

**Bad:**
```latex
S = \{ v \in V \mid T(v) = 0 \}
\left\{ x \right\}
```

**Good:**
```latex
S = \lbrace v \in V \mid T(v) = 0 \rbrace
\left\lbrace x \right\rbrace
```

### Critical: Add a Space After `\lbrace` / `\rbrace` Before Letters or Digits

If `\lbrace` directly touches an alphanumeric character, LaTeX treats it as a single unknown command and throws an error.

**Bad:** `\lbracev`, `\lbrace1`, `\lbraceT(v)`, `\rbrace\mathbf`
**Good:** `\lbrace v`, `\lbrace 1`, `\lbrace T(v)`, `\rbrace \mathbf`

If the next character is a space, parenthesis, backslash-command, or end-of-line, no extra space is needed:
- `\lbrace (1,0)` — OK (parenthesis follows)
- `\lbrace \vec{A}` — OK (backslash-command follows)
- `\rbrace$` — OK (delimiter follows)
- `\rbrace.` — OK (punctuation follows)

---

## Rule 4: Block Math for Matrices and Arrays

Any `\begin{pmatrix}`, `\begin{bmatrix}`, `\begin{vmatrix}`, `\begin{matrix}`, or `\begin{array}` MUST be in display block math.

**Bad:**
```markdown
The eigenvector is $v = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$.
```

**Good:**
```markdown
The eigenvector is

$$
v = \begin{pmatrix} 1 \\ 0 \end{pmatrix}.
$$
```

Note: the trailing period goes *inside* the block, before `$$`.

---

## Rule 5: Block Math for Integrals

Display integrals (`\int`, `\iint`, `\iiint`, `\oint`) inline causes line-height distortion.

**Bad:**
```markdown
We compute $\int_0^1 x^2 dx = \frac{1}{3}$.
```

**Good:**
```markdown
We compute

$$
\int_0^1 x^2 dx = \frac{1}{3}.
$$
```

Short references like "apply $\int$" or "using $\oint_C$" (no full equation) are fine inline.

---

## Rule 6: Block Math for Long Vector Equations

When a vector equation with `\hat{i}`, `\hat{j}`, `\hat{k}` wraps across lines, the baseline breaks. The hat characters drop below the text line.

**Bad:**
```markdown
$\vec{F} = 3xy\hat{i} - y^2\hat{j} + 2z\hat{k}$
```

**Good:**
```markdown
$$
\vec{F} = 3xy\hat{i} - y^2\hat{j} + 2z\hat{k}
$$
```

Short standalone vector names like $\vec{A}$ or $\hat{i}$ can stay inline.

---

## Rule 7: `$$` Must Start at Column 0

If `$$` is indented (e.g. under a list item), GFM may treat it as a code block or skip it entirely.

**Bad:**
```markdown
* Kernel of T:
    $$
    \text{ker}(T) = \lbrace v \mid T(v) = 0 \rbrace
    $$
```

**Good:**
```markdown
* Kernel of T:

$$
\text{ker}(T) = \lbrace v \mid T(v) = 0 \rbrace
$$
```

Both the opening `$$` and closing `$$` must be at column 0 on their own lines.

---

## Rule 8: Blank Lines Around `$$` Blocks, Never Inside

**Required:** One blank line before opening `$$` and one blank line after closing `$$`.

**Forbidden:** Blank lines *inside* a `$$ ... $$` block. GFM interprets a blank line as the end of a paragraph, which splits the math block.

**Bad:**
```markdown
$$
x + y = z

a + b = c
$$
```

**Good:**
```markdown
$$
x + y = z \\
a + b = c
$$
```

Use `\\` or `\\[6pt]` for line breaks within a math block. Or use `\begin{aligned}`.

---

## Rule 9: No Leading `+ `, `- `, `* ` Inside Math Blocks

If a line inside `$$` starts with `+`, `-`, or `*` followed by a space, GFM treats it as a list item bullet.

**Bad:**
```latex
$$
a
+ b
- c
$$
```

**Good (remove the space):**
```latex
$$
a
+b
-c
$$
```

**Also Good (keep operator on previous line):**
```latex
$$
a +
b -
c
$$
```

---

## Rule 10: Trailing Punctuation Goes Inside Block Math

When converting inline math to block math, move any trailing period/comma inside.

**Bad:**
```markdown
$$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}
$$
.
```

**Good:**
```markdown
$$
A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}.
$$
```

---

## Rule 11: Pipe Characters `|` in Inline Math

GFM may interpret `|` as a markdown table column separator. Inside inline math `$ ... $`, absolute value bars `|x|` can trigger this.

**Safe alternatives:**
- Use `\lvert x \rvert` instead of `|x|`
- Use `\mid` for set-builder notation (e.g. `\lbrace x \mid x > 0 \rbrace`)
- Block math `$$ ... $$` does not have this problem — pipes are safe inside `$$`

---

## Rule 12: Dollar Sign Spacing

The opening `$` must touch the first character of the math expression. The closing `$` must touch the last character. Spaces around the dollar sign can cause GFM to not recognize it as math.

**Bad:** `$ x + y $` (spaces inside), `$x +y$` (may work but inconsistent)
**Good:** `$x + y$`

For block math, `$$` must be on its own line with nothing else on that line.

---

## Template: Correct Block Math Layout

```markdown
Some text before the equation.

$$
\text{ker}(T) = \lbrace v \in V \mid T(v) = 0 \rbrace
$$

Some text after the equation.
```

Structure:
1. Text paragraph
2. Blank line
3. `$$` alone on its own line at column 0
4. Math content (no blank lines, no leading `+ `)
5. `$$` alone on its own line at column 0
6. Blank line
7. Next text paragraph

---

## Template: Correct Inline Math

```markdown
The eigenvalue is $\lambda = 3$ and the set is $S = \lbrace v_1, v_2 \rbrace$.
```

Keep inline math short. If it contains matrices, integrals, or vector equations with hats, convert to block math.
