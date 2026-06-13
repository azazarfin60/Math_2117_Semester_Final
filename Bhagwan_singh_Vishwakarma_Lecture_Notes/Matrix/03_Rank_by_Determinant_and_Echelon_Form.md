# Lecture 03: Rank of Matrix By Determinant and Echelon Form

> **Series**: Matrix Theory
> **Lecture**: 03 of 09
> **Video**: https://www.youtube.com/watch?v=DNFrfWb7RpM

---

**Navigation**
[< Previous Lecture](02_Rank_of_Matrix_Concept.md) | [Index](README.md) | [Next Lecture >](04_Rank_by_Normal_Canonical_Form.md)

---

## Prerequisites
- Understanding of matrix rank and minors.
- Familiarity with elementary row operations.

---

## 1. Problem 1: Determinant vs Echelon Form

**Problem:** Find the rank of the matrix using both the Determinant method and the Echelon form method:

$$
A = \begin{bmatrix} 1 & 2 & 3 \\ 1 & 4 & 2 \\ 2 & 6 & 5 \end{bmatrix}
$$

### Method 1: Determinant Method
Calculate the largest minor (the determinant of the $3 \times 3$ matrix):

$$
|A| = \begin{vmatrix} 1 & 2 & 3 \\ 1 & 4 & 2 \\ 2 & 6 & 5 \end{vmatrix}
$$

Expanding along the first row:

$$
|A| = 1(20 - 12) - 2(5 - 4) + 3(6 - 8)
$$

$$
|A| = 8 - 2(1) + 3(-2) = 8 - 2 - 6 = 0
$$

Since $|A| = 0$, the rank cannot be 3 ($\rho(A) < 3$). We now choose a minor of order 2:

$$
M = \begin{vmatrix} 1 & 2 \\ 1 & 4 \end{vmatrix} = 4 - 2 = 2 \neq 0
$$

Since a non-zero minor of order 2 exists, the rank is:
$$
\rho(A) = 2
$$

### Method 2: Echelon Form Method
Apply elementary row operations to $A$:
**Step 1:** $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - 2R_1$:

$$
A \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & 2 & -1 \\ 0 & 2 & -1 \end{bmatrix}
$$

**Step 2:** $R_3 \to R_3 - R_2$:

$$
A \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & 2 & -1 \\ 0 & 0 & 0 \end{bmatrix}
$$

**Step 3:** Divide $R_2$ by 2 ($R_2 \to R_2 / 2$):

$$
A \sim \begin{bmatrix} 1 & 2 & 3 \\ 0 & 1 & -1/2 \\ 0 & 0 & 0 \end{bmatrix}
$$

The matrix is now in Echelon form.
*   **Number of non-zero rows**: 2
*   **Rank**: $\rho(A) = 2$
*   **Nullity**: $\text{Order} - \text{Rank} = 3 - 2 = 1$

---

## 2. Problem 2: Echelon Form of a $4 \times 4$ Matrix

**Problem:** Find the rank and nullity of:

$$
A = \begin{bmatrix} 1^2 & 2^2 & 3^2 & 4^2 \\ 2^2 & 3^2 & 4^2 & 5^2 \\ 3^2 & 4^2 & 5^2 & 6^2 \\ 4^2 & 5^2 & 6^2 & 7^2 \end{bmatrix} = \begin{bmatrix} 1 & 4 & 9 & 16 \\ 4 & 9 & 16 & 25 \\ 9 & 16 & 25 & 36 \\ 16 & 25 & 36 & 49 \end{bmatrix}
$$

**Solution (Simplification):**
Apply $R_2 \to R_2 - R_1$, $R_3 \to R_3 - R_2$, $R_4 \to R_4 - R_3$:

$$
A \sim \begin{bmatrix} 1 & 4 & 9 & 16 \\ 3 & 5 & 7 & 9 \\ 5 & 7 & 9 & 11 \\ 7 & 9 & 11 & 13 \end{bmatrix}
$$

Apply $R_3 \to R_3 - R_2$, $R_4 \to R_4 - R_3$:

$$
A \sim \begin{bmatrix} 1 & 4 & 9 & 16 \\ 3 & 5 & 7 & 9 \\ 2 & 2 & 2 & 2 \\ 2 & 2 & 2 & 2 \end{bmatrix}
$$

Apply $R_4 \to R_4 - R_3$ and $R_3 \to R_3 / 2$:

$$
A \sim \begin{bmatrix} 1 & 4 & 9 & 16 \\ 3 & 5 & 7 & 9 \\ 1 & 1 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

**Converting to Echelon Form:**
Swap $R_1$ and $R_3$ ($R_1 \leftrightarrow R_3$):

$$
A \sim \begin{bmatrix} 1 & 1 & 1 & 1 \\ 3 & 5 & 7 & 9 \\ 1 & 4 & 9 & 16 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

Apply $R_2 \to R_2 - 3R_1$ and $R_3 \to R_3 - R_1$:

$$
A \sim \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 2 & 4 & 6 \\ 0 & 3 & 8 & 15 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

Divide $R_2$ by 2 ($R_2 \to R_2 / 2$):

$$
A \sim \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \\ 0 & 3 & 8 & 15 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

Apply $R_3 \to R_3 - 3R_2$:

$$
A \sim \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 2 & 6 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

Divide $R_3$ by 2 ($R_3 \to R_3 / 2$):

$$
A \sim \begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 2 & 3 \\ 0 & 0 & 1 & 3 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

*   **Number of non-zero rows**: 3
*   **Rank**: $\rho(A) = 3$
*   **Nullity**: $\text{Order} - \text{Rank} = 4 - 3 = 1$

---

## 3. Problem 3: Rank of a Rectangular Matrix

**Problem:** Find the rank and nullity of the $3 \times 4$ matrix:

$$
A = \begin{bmatrix} 1 & 3 & 4 & 3 \\ 3 & 9 & 12 & 9 \\ 1 & 3 & 4 & 1 \end{bmatrix}
$$

**Solution:**
Apply $R_2 \to R_2 - 3R_1$ and $R_3 \to R_3 - R_1$:

$$
A \sim \begin{bmatrix} 1 & 3 & 4 & 3 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & -2 \end{bmatrix}
$$

Divide $R_3$ by $-2$ ($R_3 \to R_3 / -2$) and swap $R_2$ and $R_3$ ($R_2 \leftrightarrow R_3$):

$$
A \sim \begin{bmatrix} 1 & 3 & 4 & 3 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

*   **Number of non-zero rows**: 2
*   **Rank**: $\rho(A) = 2$
*   *(Note: Nullity is strictly defined for square matrices, but conceptually using the maximum square submatrix order, it is $3 - 2 = 1$.)*

---

## 4. Problem 4: Rank of another $4 \times 4$ Matrix

**Problem:** Find the rank and nullity of:

$$
A = \begin{bmatrix} 1 & 2 & 1 & 2 \\ 1 & 3 & 2 & 2 \\ 2 & 4 & 3 & 4 \\ 3 & 7 & 4 & 6 \end{bmatrix}
$$

**Solution:**
Apply $R_2 \to R_2 - R_1$, $R_3 \to R_3 - 2R_1$, $R_4 \to R_4 - 3R_1$:

$$
A \sim \begin{bmatrix} 1 & 2 & 1 & 2 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 1 & 0 \end{bmatrix}
$$

Apply $R_4 \to R_4 - R_2$:

$$
A \sim \begin{bmatrix} 1 & 2 & 1 & 2 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

*   **Number of non-zero rows**: 3
*   **Rank**: $\rho(A) = 3$
*   **Nullity**: $\text{Order} - \text{Rank} = 4 - 3 = 1$

---

**Navigation**
[< Previous Lecture](02_Rank_of_Matrix_Concept.md) | [Index](README.md) | [Next Lecture >](04_Rank_by_Normal_Canonical_Form.md)
