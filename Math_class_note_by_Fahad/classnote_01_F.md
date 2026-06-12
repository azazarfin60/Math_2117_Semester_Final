<!-- Page 001 -->
<div align="right"><b>8 November, 2025</b></div>

<b>Math-2117</b>
<b>(GCP Sir)</b>
`gcpaul@ru.ac.bd`

* Linear algebra & Matrices.

### Matrix
- Rectangular / square form
- $[]$ / $()$
- $m \rightarrow \text{rows}$
- $n \rightarrow \text{columns}$
- Size: $m \times n$

$$
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}_{m \times n}
$$

(Row: horizontal, Column: vertical)

* Can be either real & complex numbers.
* $\dots$ Information should be collected from a field.

* A number that can be represented on the real axis $\rightarrow$ Real number.
  (Graph showing vertical axis $y$ and horizontal axis $x$)

* Complex number :-
  (Graph showing imaginary axis "img." and real axis "real")
  Point $(2,3) = 2+3i$

* Square matrix :- $m = n$

* Easy to calculate. $(A+B)$, $(A-B)$

* If 2 matrices have different sizes but equal rows or columns we can concatenate them.

---

<!-- Page 002 -->

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}_{2 \times 2} ; \quad B = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}_{2 \times 3}
$$

$\therefore$ Horizontal concatenation :-

$$
[A:B] = \begin{bmatrix} 1 & 2 & 1 & 2 & 3 \\ 3 & 4 & 4 & 5 & 6 \end{bmatrix}_{2 \times 5}
$$

$$
A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}_{2 \times 2} ; \quad B = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}_{3 \times 2}
$$

$\therefore$ Vertical concat :-

$$
[A:B] = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}_{5 \times 2}
$$

* Concatenation $\rightarrow$ Vertical (Column same)
               $\rightarrow$ Horizontal (Row same)

* Commutative law,
  * $A+B = B+A$ (Tick mark)
  * $A-B \neq B-A$ (Cross mark)
  * $AB \neq BA$ (Cross mark)

---

<!-- Page 003 -->

* multiply :-


$$
A_{m \times n} \times B_{n \times p}
$$

$n = \text{must be equal}$.
  $\therefore$ If Matrix is $n$ square matrix :-
  * $A \times A$
  * $A^2$
  * $A^3$
  * $\vdots$
  * $A^n$

* Symmetry Matrix :- $A^t = A$


$$
A = \begin{bmatrix} a & h & g \\ h & b & f \\ g & f & c \end{bmatrix}
$$

Here, $A$ is a symmetric matrix.


$$
A^t = \begin{bmatrix} a & h & g \\ h & b & f \\ g & f & c \end{bmatrix}
$$

**HW**
* why do we need to study symmetric matrixes

* skew-symmetric / Anti-symmetric :- $A^t = -A$
  $* \text{main-diag} = 0$.


$$
A = \begin{bmatrix} 0 & h & g \\ -h & 0 & f \\ -g & -f & 0 \end{bmatrix}
$$

$$
A^t = \begin{bmatrix} 0 & -h & -g \\ h & 0 & -f \\ g & f & 0 \end{bmatrix}
$$

---

<!-- Page 004 -->
<div align="left"><i>Eigen values special number that describe how they stretch space.</i></div>

* Main-diagonal
* Super-diagonal
* Sub-diagonal

$$
A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \\ a_{31} & a_{32} & a_{33} \end{bmatrix}
$$

- $a_{11}, a_{22}, a_{33} \rightarrow \text{Main-diagonal}$
- $a_{12}, a_{23} \rightarrow \text{Super-diagonal}$
- $a_{21}, a_{32} \rightarrow \text{Sub-diagonal}$

- $\text{row} > \text{column} \rightarrow \text{Sub-diagonal}$
- $\text{row} < \text{column} \rightarrow \text{Super-diagonal}$

* Tris-sis (Tri-diagonal matrix) :-


$$
A = \begin{bmatrix} 1 & 5 & 0 & 0 \\ 8 & 2 & 6 & 0 \\ 0 & 9 & 3 & 7 \\ 0 & 0 & 10 & 4 \end{bmatrix}
$$

- Only one Super diagonal, one sub diagonal, and one main diagonal, and all others are zero.
  - Only super, sub & main diagonal এ মান থাকবে। বাকিগুলো '0' থাকবে।

* why do we study symmetric matrices? (Not Sir's note, part of HW)
  1. Easier to work with.
  2. Eigen values are real (not complex).
  3. Very common in physics, engineering, and data science, machine learning.

---

<!-- Page 005 -->
<div align="right"><b>10 Nov, 25</b></div>

<b>Math-2117</b>
<b>(Rupali Maam)</b>

* Book:- Vector analysis (Spiegel)
  (Murray R. Spiegel)
  (1-6 chap)

- Vector representation: initial point $\rightarrow$ terminal point.
- slide and chap (1,2) etc.

---
<div align="right"><b>11 Nov, 25</b></div>

<b>Math-2117</b>
<b>(Rupali maam)</b>

**(chap-2)**
- Dot product:


$$
\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}| \cos\theta
$$

(showing angle $\theta$ between vectors $\vec{A}$ and $\vec{B}$)
- If perpendicular ($\vec{A} \perp \vec{B}$):


$$
\vec{A} \cdot \vec{B} = 0
$$

- If parallel (same direction):


$$
\vec{A} \cdot \vec{B} = AB
$$

* Dot product mean করে ২টা ভেক্টর পরস্পর কতটা Parallel.
* Dot product = একটির উপর অন্যটির Projection (ছায়া)
* Physical significance of DOT product.
* Cross product.
* Reciprocal set of vectors (crossed out in notes)
- List of problems: 1, 6, 7, 8, 9, 10, 12, 13, 16, 17, (18), 19, 21, 22, 28, 29, 30, 32, 38, (45)

---

<!-- Page 006 -->
<div align="right"><b>15 Nov, 25</b></div>

<b>Math-2117</b>
<b>(GCP Sir)</b>

### Echelon Matrix:-
If in a matrix, the number of 0's preceding the (first non-zero / pivot) entry increases row by row.

- Example 1:


$$
\begin{bmatrix} 1 & 2 & 3 & 4 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{bmatrix}
$$

is an echelon matrix.
  $\rightarrow \text{Rank} \rightarrow 4$.
  (Note on page: at least 2 zeros, could be more under the pivot of row 2).

- Example 2:


$$
\begin{bmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 2 \end{bmatrix}
$$

is NOT an echelon matrix. (Notes state: "if 2 then not echelon matrix" pointing to the 2 in the last row, as the zero row is not at the bottom).
  $\text{Rank} = 2$. (if the last row were all zeros).

* Use of echelon matrix:
  * Rank of a matrix.

* Rank of a matrix:-
  Rank of a matrix is the number of non-zero rows in its echelon form.

  - Example:


$$
\begin{bmatrix} 1 & 2 & 3 & 4 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 1 \end{bmatrix} \rightarrow \text{rank} = 4
$$

- Example:


$$
\begin{bmatrix} 1 & 2 & 3 & 4 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix} \rightarrow \text{rank} = 3
$$

---

<!-- Page 007 -->

$$
R^1 \rightarrow \text{Real line (x axis)}
$$

$$
R^2 \rightarrow (x,y) \text{ plane}
$$

$$
R^3 \rightarrow (a,b,c)
$$

$$
R^4 \rightarrow (a,b,c,d)
$$

* Converting a matrix to its echelon form:-
* Reduce the matrix

$$
\begin{bmatrix} 1 & 2 & 4 & 5 \\ 6 & 7 & 1 & 1 \\ -1 & 3 & 4 & 5 \end{bmatrix}
$$

to its echelon form. ($\star \rightarrow R^4$ থেকে নেওয়া)

Ans:-
Perform elementary row operations (transformations).
* Replacing $R_2$ by $6R_1 - R_2$ ($R_2 \rightarrow 6R_1 - R_2$)
* $R_3 \rightarrow R_1 + R_3$

(equivalent sign: $\sim$)

$$
\sim \begin{bmatrix} 1 & 2 & 4 & 5 \\ 0 & 5 & 23 & 29 \\ 0 & 5 & 8 & 10 \end{bmatrix}
$$

* $R_3 \rightarrow R_2 - R_3$

$$
\sim \begin{bmatrix} 1 & 2 & 4 & 5 \\ 0 & 5 & 23 & 29 \\ 0 & 0 & 15 & 19 \end{bmatrix}
$$

which is an echelon matrix.

Rank = 3.

---

<!-- Page 008 -->

* Row canonical form / Row reduced echelon form:-
  Echelon + Pivot must be 1 + pivot is the only non-zero entry in that column.

  Example:


$$
\begin{bmatrix} 1 & 0 & 0 & 5 \\ 0 & 1 & 0 & 5 \\ 0 & 0 & 1 & 6 \end{bmatrix}
$$

$\star$ important in image processing.

* Write down the workflow of converting a matrix to its row canonical form.
* Convert the matrix to its row canonical form.


$$
\begin{bmatrix} 1 & 2 & 3 & 5 \\ -1 & 1 & 2 & 1 \\ 1 & 1 & 2 & 3 \end{bmatrix}
$$

- Step 1: Convert to echelon form:


$$
R_2 \rightarrow R_1 + R_2
$$

$$
R_3 \rightarrow R_1 - R_3
$$

$$
\sim \begin{bmatrix} 1 & 2 & 3 & 5 \\ 0 & 3 & 5 & 6 \\ 0 & 1 & 1 & 2 \end{bmatrix}
$$

$$
R_3 \rightarrow R_2 - 3R_3
$$

$$
\sim \begin{bmatrix} 1 & 2 & 3 & 5 \\ 0 & 3 & 5 & 6 \\ 0 & 0 & 2 & 0 \end{bmatrix}
$$

which is an echelon matrix.

---

<!-- Page 009 -->

  - Step 2: Convert to row canonical form:


$$
R_1 \rightarrow 3R_1 - 2R_2
$$

$$
\sim \begin{bmatrix} 3 & 0 & -1 & 3 \\ 0 & 3 & 5 & 6 \\ 0 & 0 & 2 & 0 \end{bmatrix}
$$

$$
R_1 \rightarrow 2R_1 + R_3
$$

$$
\sim \begin{bmatrix} 6 & 0 & 0 & 6 \\ 0 & 3 & 5 & 6 \\ 0 & 0 & 2 & 0 \end{bmatrix}
$$

$$
R_2 \rightarrow 2R_2 - 5R_3
$$

$$
\sim \begin{bmatrix} 6 & 0 & 0 & 6 \\ 0 & 6 & 0 & 12 \\ 0 & 0 & 2 & 0 \end{bmatrix}
$$

- Dividing each row to get pivots of 1:


$$
R_1 \rightarrow \frac{R_1}{6}
$$

$$
R_2 \rightarrow \frac{1}{6} \times R_2
$$

$$
R_3 \rightarrow \frac{1}{2} \times R_3
$$

$$
\sim \begin{bmatrix} 1 & 0 & 0 & 1 \\ 0 & 1 & 0 & 2 \\ 0 & 0 & 1 & 0 \end{bmatrix}
$$

which is row canonical matrix / row-reduced echelon matrix.

---

<!-- Page 010 -->
<div align="right"><b>17 Nov, 25</b></div>

<b>Math-2117</b>
<b>(PDF Maam)</b>

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

* Vector differentiation:- (space curve)
  - Ordinary derivations of vectors:
    - Continuity and differentiability
    - Differentiation formulas
    - Partial derivative
    - Differentials of vectors
    - Differential geometry

<div align="left"><i>Kappa-kappa (written vertically)</i></div>