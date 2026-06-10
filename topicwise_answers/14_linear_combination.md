# Topic 14: Linear Combination

This file contains the organized questions and answers for **Linear Combination**, priority ranked as **Priority 14** based on frequency and exam weight.

---

## Q1. Write the vector $v = (1, -2, 5)$ as a linear combination of the vectors $e_1 = (1, 1, 1)$, $e_2 = (1, 2, 3)$ and $e_3 = (2, -1, 1)$. (04)

| | |
|---|---|
| **ID** | PYQ-2020-8a | PYQ-2021-8a |
| **Appeared in** | 2020 Q8(a) [04 marks], 2021 Q8(a) [04 marks] |
| **Frequency** | ⭐⭐ (2 times) |

**Answer:**

We write the relation:

$$
v = c_1 e_1 + c_2 e_2 + c_3 e_3 \implies (1, -2, 5) = c_1(1, 1, 1) + c_2(1, 2, 3) + c_3(2, -1, 1)
$$

This gives the system of equations:

$$
c_1 + c_2 + 2c_3 = 1
$$

$$
c_1 + 2c_2 - c_3 = -2
$$

$$
c_1 + 3c_2 + c_3 = 5
$$

We write the augmented matrix of this system:

$$
\begin{bmatrix} 1 & 1 & 2 & | & 1 \\ 1 & 2 & -1 & | & -2 \\ 1 & 3 & 1 & | & 5 \end{bmatrix}
$$

Apply row operations:
*   $R_2 \to R_2 - R_1$
*   $R_3 \to R_3 - R_1$

This gives:

$$
\begin{bmatrix} 1 & 1 & 2 & | & 1 \\ 0 & 1 & -3 & | & -3 \\ 0 & 2 & -1 & | & 4 \end{bmatrix}
$$

Now perform the operation $R_3 \to R_3 - 2R_2$:

$$
\begin{bmatrix} 1 & 1 & 2 & | & 1 \\ 0 & 1 & -3 & | & -3 \\ 0 & 0 & 5 & | & 10 \end{bmatrix}
$$

By back substitution, we solve the coefficients:
*   From the third row: $5c_3 = 10 \implies c_3 = 2$.
*   From the second row: $c_2 - 3(2) = -3 \implies c_2 = 3$.
*   From the first row: $c_1 + 3 + 2(2) = 1 \implies c_1 = -6$.

So the linear combination is:

$$
v = -6e_1 + 3e_2 + 2e_3
$$

---

## Q2. Consider the vectors $v_1 = (2, 1, 4), v_2 = (1, -1, 3)$ and $v_3 = (3, 2, 5)$ in $\mathbb{R}^3$. Show that $v = (5, 9, 5)$ is a linear combination of $v_1, v_2$, and $v_3$. (05)

| | |
|---|---|
| **ID** | PYQ-2023-7a |
| **Source** | 2023 Q7(a) [05 marks] |

**Answer:**

We set up the relation:

$$
v = c_1 v_1 + c_2 v_2 + c_3 v_3 \implies (5, 9, 5) = c_1(2, 1, 4) + c_2(1, -1, 3) + c_3(3, 2, 5)
$$

This gives the system:

$$
2c_1 + c_2 + 3c_3 = 5
$$

$$
c_1 - c_2 + 2c_3 = 9
$$

$$
4c_1 + 3c_2 + 5c_3 = 5
$$

We write the augmented matrix and swap row 1 and row 2 ($R_1 \leftrightarrow R_2$):

$$
\begin{bmatrix} 1 & -1 & 2 & | & 9 \\ 2 & 1 & 3 & | & 5 \\ 4 & 3 & 5 & | & 5 \end{bmatrix}
$$

Apply row operations:
*   $R_2 \to R_2 - 2R_1$
*   $R_3 \to R_3 - 4R_1$

This gives:

$$
\begin{bmatrix} 1 & -1 & 2 & | & 9 \\ 0 & 3 & -1 & | & -13 \\ 0 & 7 & -3 & | & -31 \end{bmatrix}
$$

Perform the operation $R_3 \to 3R_3 - 7R_2$:

$$
\begin{bmatrix} 1 & -1 & 2 & | & 9 \\ 0 & 3 & -1 & | & -13 \\ 0 & 0 & -2 & | & -2 \end{bmatrix}
$$

Now solve for the coefficients by back substitution:
*   From row 3: $-2c_3 = -2 \implies c_3 = 1$.
*   From row 2: $3c_2 - 1 = -13 \implies 3c_2 = -12 \implies c_2 = -4$.
*   From row 1: $c_1 - (-4) + 2(1) = 9 \implies c_1 + 6 = 9 \implies c_1 = 3$.

So we can write $v$ as:

$$
v = 3v_1 - 4v_2 + v_3
$$

This shows that the vector is a linear combination of the given vectors.

---

## Q3. Express the polynomial $v = 3t^2 + 5t - 5$ as a linear combination of the polynomials $P_1 = t^2 + 2t + 1$, $P_2 = 2t^2 + 5t + 4$ and $P_3 = t^2 + 3t + 6$. (03)

| | |
|---|---|
| **ID** | PYQ-2024-7a |
| **Source** | 2024 Q7(a) [03 marks] |

**Answer:**

We write $v$ as a linear combination:

$$
v = c_1 P_1 + c_2 P_2 + c_3 P_3
$$

We substitute the polynomials:

$$
3t^2 + 5t - 5 = c_1(t^2 + 2t + 1) + c_2(2t^2 + 5t + 4) + c_3(t^2 + 3t + 6)
$$

We expand the terms and group them by powers of $t$:

$$
3t^2 + 5t - 5 = (c_1 + 2c_2 + c_3)t^2 + (2c_1 + 5c_2 + 3c_3)t + (c_1 + 4c_2 + 6c_3)
$$

We match the coefficients of $t^2$, $t$, and the constant terms:
1.  $c_1 + 2c_2 + c_3 = 3$
2.  $2c_1 + 5c_2 + 3c_3 = 5$
3.  $c_1 + 4c_2 + 6c_3 = -5$

We solve this system. From equation (1):

$$
c_1 = 3 - 2c_2 - c_3
$$

We substitute this expression for $c_1$ into equations (2) and (3):

In equation (2):

$$
2(3 - 2c_2 - c_3) + 5c_2 + 3c_3 = 5
$$

$$
6 - 4c_2 - 2c_3 + 5c_2 + 3c_3 = 5 \implies c_2 + c_3 = -1 \implies c_2 = -1 - c_3 \quad \dots (4)
$$

In equation (3):

$$
(3 - 2c_2 - c_3) + 4c_2 + 6c_3 = -5
$$

$$
3 + 2c_2 + 5c_3 = -5 \implies 2c_2 + 5c_3 = -8 \quad \dots (5)
$$

We substitute equation (4) into equation (5):

$$
2(-1 - c_3) + 5c_3 = -8
$$

$$
-2 - 2c_3 + 5c_3 = -8
$$

$$
3c_3 = -6 \implies c_3 = -2
$$

We use $c_3 = -2$ in equation (4):

$$
c_2 = -1 - (-2) = 1
$$

We use $c_2 = 1$ and $c_3 = -2$ to find $c_1$:

$$
c_1 = 3 - 2(1) - (-2) = 3
$$

Thus, the linear combination is:

$$
v = 3P_1 + P_2 - 2P_3
$$

---

