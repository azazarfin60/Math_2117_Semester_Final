[← Previous: B05 Row Echelon Form and Rank](B05_Row_Echelon_Form_Rank.md) | [Index](00_Index.md) | [Next: B07 System of Linear Equations →](B07_System_of_Linear_Equations.md)

---

# B06: Normal (Canonical) Form of a Matrix

> **Exam Weight**: Tier 1-2 | **Appeared in**: 2019, 2021, 2023 | **Typical Marks**: 3–6

The normal form reduces a matrix using both row AND column operations to reach the identity block form. The rank is then read directly from the size of the identity block.

---

## Definition of Normal Form

A non-zero matrix $A$ of rank $r$ can be reduced to one of these forms using row and column operations:

$$
[I_r], \quad [I_r \mid 0], \quad
\begin{bmatrix}
I_r \\
0
\end{bmatrix}, \quad \begin{bmatrix} I_r & 0 \\ 0 & 0 \end{bmatrix}
$$

where $I_r$ is the identity matrix of order $r$. This is the **normal form** (or **canonical form**).

The rank equals $r$ (the order of $I_r$ in the normal form).

---

## Difference from Echelon Form

| Feature | Echelon Form | Normal Form |
|---------|-------------|-------------|
| Operations used | Row operations only | Row AND column operations |
| Result | Staircase pattern | Identity block |
| Off-diagonal entries | May be non-zero above pivots | All zero except $I_r$ |
| Rank reading | Count non-zero rows | Read order of $I_r$ |

---

## The Method

1. Start with the given matrix.
2. Use row operations to get echelon form (upper triangular with pivots).
3. Scale each pivot to 1.
4. Use column operations to clear all non-zero entries above and beside each pivot.
5. If needed, swap columns to group the 1s together into $I_r$.

---

## Worked Example 1: 4x4 Matrix to Normal Form (PYQ 2019)

**Problem**: Find the rank by reducing to normal form:

$$
A =
\begin{pmatrix}
3 & -2 & 0 & -7 \\
0 & 2 & 1 & -5 \\
1 & -2 & -2 & 1 \\
0 & 1 & 1 & -6
\end{pmatrix}
$$

**Solution**:

Swap $R_1 \leftrightarrow R_3$ for leading 1. Then $R_3 \to R_3 - 3R_1$:

$$
\begin{pmatrix}
1 & -2 & -2 & 1 \\
0 & 2 & 1 & -5 \\
0 & 4 & 6 & -10 \\
0 & 1 & 1 & -6
\end{pmatrix}
$$

Swap $R_2 \leftrightarrow R_4$. Then $R_3 \to R_3 - 4R_2$ and $R_4 \to R_4 - 2R_2$:

$$
\begin{pmatrix}
1 & -2 & -2 & 1 \\
0 & 1 & 1 & -6 \\
0 & 0 & 2 & 14 \\
0 & 0 & -1 & 7
\end{pmatrix}
$$

Scale $R_3 \to \frac{1}{2}R_3$. Then $R_4 \to R_4 + R_3$:

$$
\begin{pmatrix}
1 & -2 & -2 & 1 \\
0 & 1 & 1 & -6 \\
0 & 0 & 1 & 7 \\
0 & 0 & 0 & 14
\end{pmatrix}
$$

Scale $R_4 \to \frac{1}{14}R_4$. Now clear upward using column operations.

$C_2 \to C_2 + 2C_1$, $C_3 \to C_3 + 2C_1$, $C_4 \to C_4 - C_1$:

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 1 & -6 \\
0 & 0 & 1 & 7 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

$C_3 \to C_3 - C_2$, $C_4 \to C_4 + 6C_2$:

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 7 \\
0 & 0 & 0 & 1
\end{pmatrix}
$$

$C_4 \to C_4 - 7C_3$:

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix} = I_4
$$

Normal form is $I_4$. Rank = 4.

---

## Worked Example 2: 4x4 to Normal Form (PYQ 2021)

**Problem**: Reduce to canonical form and find rank:

$$
A =
\begin{pmatrix}
2 & 3 & -1 & -1 \\
1 & -1 & -2 & -4 \\
3 & 1 & 3 & -2 \\
6 & 3 & 0 & -7
\end{pmatrix}
$$

**Solution**: After row operations, the echelon form has 3 non-zero rows. After column operations to clear off-diagonal entries:

$$
\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix} = \begin{bmatrix} I_3 & 0 \\ 0 & 0 \end{bmatrix}
$$

Normal form is $[I_3 \mid 0]$-type. Rank = 3.

---

## Exam Patterns

- "Reduce to normal/canonical form and find rank" appears regularly.
- Always show row operations first to reach echelon form. Then show column operations to reach the identity block.
- Write each operation clearly ($R_i \to ...$, $C_j \to ...$).
- State the final rank explicitly.

---

[← Previous: B05 Row Echelon Form and Rank](B05_Row_Echelon_Form_Rank.md) | [Index](00_Index.md) | [Next: B07 System of Linear Equations →](B07_System_of_Linear_Equations.md)
