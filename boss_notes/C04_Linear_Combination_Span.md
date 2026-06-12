[← Previous: C03 Direct Sums](C03_Sum_Direct_Sum_Subspaces.md) | [Index](00_Index.md) | [Next: C05 Linear Independence →](C05_Linear_Dependence_Independence.md)

---

# C04: Linear Combination and Span

> **Exam Weight**: Tier 2 | **Appeared in**: 2020, 2021, 2023, 2024 | **Typical Marks**: 3–5

A vector is a **linear combination** of a set of vectors if it can be created by scaling those vectors and adding them together.

---

## The Core Concept

To express a vector $v$ as a linear combination of vectors $e_1, e_2, \dots, e_n$, we set up the equation:

$$
v = c_1 e_1 + c_2 e_2 + \dots + c_n e_n
$$

This generates a system of linear equations where the unknowns are the scalars $c_1, c_2, \dots, c_n$. Solving this system (usually via an augmented matrix and row reduction) gives the required coefficients.

---

## Worked Example 1: Coordinate Vectors (PYQ 2020, 2021)

**Problem**: Write the vector $v = (1, -2, 5)$ as a linear combination of the vectors $e_1 = (1, 1, 1)$, $e_2 = (1, 2, 3)$, and $e_3 = (2, -1, 1)$.

**Solution**:
Set up the relation:

$$
(1, -2, 5) = c_1(1, 1, 1) + c_2(1, 2, 3) + c_3(2, -1, 1)
$$

This gives the system of equations (grouping by components):

$$
c_1 + c_2 + 2c_3 = 1
$$

$$
c_1 + 2c_2 - c_3 = -2
$$

$$
c_1 + 3c_2 + c_3 = 5
$$

Write the augmented matrix and apply row operations to reach row echelon form:

$$
\begin{bmatrix} 1 & 1 & 2 & \lvert  & 1 \\ 1 & 2 & -1 &  \rvert & -2 \\ 1 & 3 & 1 & \lvert  & 5 \end{bmatrix}
$$

Apply $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$:

$$
\begin{bmatrix} 1 & 1 & 2 & \lvert  & 1 \\ 0 & 1 & -3 &  \rvert & -3 \\ 0 & 2 & -1 & \lvert  & 4 \end{bmatrix}
$$

Apply $R_3 \to R_3 - 2R_2$:

$$
\begin{bmatrix} 1 & 1 & 2 & \lvert  & 1 \\ 0 & 1 & -3 &  \rvert & -3 \\ 0 & 0 & 5 & \lvert  & 10 \end{bmatrix}
$$

Solve by back substitution:
- From $R_3$: $5c_3 = 10 \implies c_3 = 2$
- From $R_2$: $c_2 - 3(2) = -3 \implies c_2 = 3$
- From $R_1$: $c_1 + 3 + 2(2) = 1 \implies c_1 = -6$

The linear combination is:

$$
v = -6e_1 + 3e_2 + 2e_3
$$

---

## Worked Example 2: Polynomial Vectors (PYQ 2024)

**Problem**: Express the polynomial $v = 3t^2 + 5t - 5$ as a linear combination of the polynomials $P_1 = t^2 + 2t + 1$, $P_2 = 2t^2 + 5t + 4$, and $P_3 = t^2 + 3t + 6$.

**Solution**:
Set up the relation:

$$
v = c_1 P_1 + c_2 P_2 + c_3 P_3
$$

$$
3t^2 + 5t - 5 = c_1(t^2 + 2t + 1) + c_2(2t^2 + 5t + 4) + c_3(t^2 + 3t + 6)
$$

Expand and group terms by powers of $t$:

$$
3t^2 + 5t - 5 = (c_1 + 2c_2 + c_3)t^2 + (2c_1 + 5c_2 + 3c_3)t + (c_1 + 4c_2 + 6c_3)
$$

Match the coefficients to form a system of equations:
1. $c_1 + 2c_2 + c_3 = 3$
2. $2c_1 + 5c_2 + 3c_3 = 5$
3. $c_1 + 4c_2 + 6c_3 = -5$

You can solve this using substitution or matrix row reduction. Let's use substitution from Eq 1 ($c_1 = 3 - 2c_2 - c_3$):
Substitute into Eq 2:

$$
2(3 - 2c_2 - c_3) + 5c_2 + 3c_3 = 5 \implies 6 - 4c_2 - 2c_3 + 5c_2 + 3c_3 = 5 \implies c_2 + c_3 = -1
$$

Substitute into Eq 3:

$$
(3 - 2c_2 - c_3) + 4c_2 + 6c_3 = -5 \implies 3 + 2c_2 + 5c_3 = -5 \implies 2c_2 + 5c_3 = -8
$$

Now solve the $2 \times 2$ system: $c_2 = -1 - c_3$.

$$
2(-1 - c_3) + 5c_3 = -8 \implies -2 - 2c_3 + 5c_3 = -8 \implies 3c_3 = -6 \implies c_3 = -2
$$

Find $c_2$: $c_2 = -1 - (-2) = 1$.
Find $c_1$: $c_1 = 3 - 2(1) - (-2) = 3$.

The linear combination is:

$$
v = 3P_1 + P_2 - 2P_3
$$

---

## Exam Patterns
- When given polynomials, simply treat their coefficients like a standard vector (e.g., $3t^2 + 5t - 5$ becomes $(3, 5, -5)$). The math is identical to coordinate vector problems.
- If the system of equations is inconsistent (e.g., you get $0 = 5$ during row reduction), then it is *not possible* to write the vector as a linear combination of the given set.

---

[← Previous: C03 Direct Sums](C03_Sum_Direct_Sum_Subspaces.md) | [Index](00_Index.md) | [Next: C05 Linear Independence →](C05_Linear_Dependence_Independence.md)
