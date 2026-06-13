# Lecture 04: Rank of Matrix By Normal / Canonical Form

> **Series**: Matrix Theory
> **Lecture**: 04 of 09
> **Video**: https://www.youtube.com/watch?v=gXwEtwX8g8M

---

**Navigation**
[< Previous Lecture](03_Rank_by_Determinant_and_Echelon_Form.md) | [Index](README.md) | [Next Lecture >](05_Consistency_of_Linear_Equations.md)

---

## Prerequisites
- Knowledge of matrix rank.
- Understanding of elementary row and column operations.

---

## 1. Normal (Canonical) Form Review
Every non-zero matrix $A$ of rank $r$ can be reduced, by a sequence of elementary row **and** column operations, to one of the following forms:

$$
\begin{bmatrix} I_r & 0 \\ 0 & 0 \end{bmatrix}, \quad \begin{bmatrix} I_r \\ 0 \end{bmatrix}, \quad \begin{bmatrix} I_r & 0 \end{bmatrix}, \quad \text{or} \quad I_r
$$

where $I_r$ represents an identity matrix of order $r$, and $0$ represents a zero matrix. The value $r$ gives the rank of the original matrix $A$.

---

## 2. Problem 1: Identical Rows

**Problem:** Find the rank and nullity of:

$$
A = \begin{bmatrix} 1 & a & b & 0 \\ 0 & c & d & 1 \\ 1 & a & b & 0 \\ 0 & c & d & 1 \end{bmatrix}
$$

**Solution:**
We can easily spot identical rows. Apply row operations $R_3 \to R_3 - R_1$ and $R_4 \to R_4 - R_2$:

$$
A \sim \begin{bmatrix} 1 & a & b & 0 \\ 0 & c & d & 1 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

The matrix is now in Echelon form with 2 non-zero rows.
*   **Rank**: $\rho(A) = 2$
*   **Nullity**: $\text{Order} - \text{Rank} = 4 - 2 = 2$

---

## 3. Problem 2: Normal Form of a $4 \times 4$ Matrix

**Problem:** Find the rank of the matrix using Normal Form:

$$
A = \begin{bmatrix} -2 & -1 & -3 & -1 \\ 1 & 2 & -3 & -1 \\ 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & -1 \end{bmatrix}
$$

**Solution:**
**Step-by-step Row Operations:**
Swap $R_1 \leftrightarrow R_3$:

$$
A \sim \begin{bmatrix} 1 & 0 & 1 & 1 \\ 1 & 2 & -3 & -1 \\ -2 & -1 & -3 & -1 \\ 0 & 1 & 1 & -1 \end{bmatrix}
$$

Apply $R_2 \to R_2 - R_1$ and $R_3 \to R_3 + 2R_1$:

$$
A \sim \begin{bmatrix} 1 & 0 & 1 & 1 \\ 0 & 2 & -4 & -2 \\ 0 & -1 & -1 & 1 \\ 0 & 1 & 1 & -1 \end{bmatrix}
$$

Divide $R_2$ by 2 ($R_2 \to R_2 / 2$):

$$
A \sim \begin{bmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & -2 & -1 \\ 0 & -1 & -1 & 1 \\ 0 & 1 & 1 & -1 \end{bmatrix}
$$

Apply $R_3 \to R_3 + R_2$ and $R_4 \to R_4 - R_2$:

$$
A \sim \begin{bmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & -2 & -1 \\ 0 & 0 & -3 & 0 \\ 0 & 0 & 3 & 0 \end{bmatrix}
$$

Apply $R_4 \to R_4 + R_3$ and divide $R_3$ by $-3$ ($R_3 \to R_3 / -3$):

$$
A \sim \begin{bmatrix} 1 & 0 & 1 & 1 \\ 0 & 1 & -2 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

*(The matrix is now in Echelon form, and we can already see the rank is 3. We now proceed to Normal Form using column operations.)*

**Step-by-step Column Operations:**
Apply $C_3 \to C_3 - C_1$ and $C_4 \to C_4 - C_1$:

$$
A \sim \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & -2 & -1 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

Apply $C_3 \to C_3 + 2C_2$ and $C_4 \to C_4 + C_2$:

$$
A \sim \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

This is the Normal Form block matrix:

$$
A \sim \begin{bmatrix} I_3 & 0 \\ 0 & 0 \end{bmatrix}
$$

*   **Rank**: $\rho(A) = 3$
*   **Nullity**: $\text{Order} - \text{Rank} = 4 - 3 = 1$

---

## 4. Problem 3: Normal Form of another $4 \times 4$ Matrix

**Problem:** Find the rank and nullity of:

$$
A = \begin{bmatrix} 2 & 3 & -1 & -1 \\ 1 & -1 & -2 & -4 \\ 3 & 1 & 3 & -2 \\ 6 & 3 & 0 & -7 \end{bmatrix}
$$

**Solution:**
**Step-by-step Row Operations:**
Swap $R_1 \leftrightarrow R_2$:

$$
A \sim \begin{bmatrix} 1 & -1 & -2 & -4 \\ 2 & 3 & -1 & -1 \\ 3 & 1 & 3 & -2 \\ 6 & 3 & 0 & -7 \end{bmatrix}
$$

Apply $R_2 \to R_2 - 2R_1$, $R_3 \to R_3 - 3R_1$, $R_4 \to R_4 - 6R_1$:

$$
A \sim \begin{bmatrix} 1 & -1 & -2 & -4 \\ 0 & 5 & 3 & 7 \\ 0 & 4 & 9 & 10 \\ 0 & 9 & 12 & 17 \end{bmatrix}
$$

Apply $R_2 \to R_2 - R_3$:

$$
A \sim \begin{bmatrix} 1 & -1 & -2 & -4 \\ 0 & 1 & -6 & -3 \\ 0 & 4 & 9 & 10 \\ 0 & 9 & 12 & 17 \end{bmatrix}
$$

Apply $R_3 \to R_3 - 4R_2$ and $R_4 \to R_4 - 9R_2$:

$$
A \sim \begin{bmatrix} 1 & -1 & -2 & -4 \\ 0 & 1 & -6 & -3 \\ 0 & 0 & 33 & 22 \\ 0 & 0 & 66 & 44 \end{bmatrix}
$$

Apply $R_4 \to R_4 - 2R_3$ and divide $R_3$ by 11 ($R_3 \to R_3 / 11$):

$$
A \sim \begin{bmatrix} 1 & -1 & -2 & -4 \\ 0 & 1 & -6 & -3 \\ 0 & 0 & 3 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

**Step-by-step Column Operations:**
Apply $C_2 \to C_2 + C_1$, $C_3 \to C_3 + 2C_1$, $C_4 \to C_4 + 4C_1$:

$$
A \sim \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & -6 & -3 \\ 0 & 0 & 3 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

Apply $C_3 \to C_3 + 6C_2$ and $C_4 \to C_4 + 3C_2$:

$$
A \sim \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 3 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

Divide $C_3$ by 3 ($C_3 \to C_3 / 3$):

$$
A \sim \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

Apply $C_4 \to C_4 - 2C_3$:

$$
A \sim \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

This gives the Normal Form:

$$
A \sim \begin{bmatrix} I_3 & 0 \\ 0 & 0 \end{bmatrix}
$$

*   **Rank**: $\rho(A) = 3$
*   **Nullity**: $\text{Order} - \text{Rank} = 4 - 3 = 1$

---

**Navigation**
[< Previous Lecture](03_Rank_by_Determinant_and_Echelon_Form.md) | [Index](README.md) | [Next Lecture >](05_Consistency_of_Linear_Equations.md)
