[← Previous: B08 Parameter Analysis](B08_Parameter_Analysis_Lambda_Mu.md) | [Index](00_Index.md) | [Next: B10 Eigenvalues and Eigenvectors →](B10_Eigenvalues_Eigenvectors.md)

---

# B09: Homogeneous Systems of Equations

> **Exam Weight**: Tier 2 | **Appeared in**: 2018, 2019 | **Typical Marks**: 5–6

A homogeneous system always has the trivial solution. The real question is whether non-trivial solutions exist.

---

## What is a Homogeneous System?

A system $AX = 0$ where the constant vector is all zeros:

$$
\begin{aligned}
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n &= 0 \\
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n &= 0 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n &= 0
\end{aligned}
$$

The trivial solution $x_1 = x_2 = \dots = x_n = 0$ always exists. It always satisfies every equation.

---

## When Do Non-Trivial Solutions Exist?

Let $\rho(A)$ be the rank of the coefficient matrix and $n$ be the number of unknowns.

| Condition | Result |
|-----------|--------|
| $\rho(A) = n$ | Only the trivial solution (zero solution) |
| $\rho(A) < n$ | Non-trivial solutions exist. The solution space has dimension $n - \rho(A)$ |

For a square system ($m = n$):
- $\lvert A \rvert \neq 0$ means only the trivial solution.
- $\lvert A \rvert = 0$ means non-trivial solutions exist.

---

## The Solution Space

The set of all solutions to $AX = 0$ forms a vector subspace called the **null space** of $A$. Its dimension is the **nullity** = $n - \rho(A)$.

When non-trivial solutions exist, you express the solution in terms of free variables (parameters). Each free variable gives one dimension.

---

## Worked Example 1: Only Trivial Solution (PYQ 2018)

**Problem**: Solve the homogeneous system:

$$
\begin{aligned}
2x_1 - x_2 + x_3 &= 0 \\
3x_1 + 2x_2 + x_3 &= 0 \\
x_1 - 3x_2 + 5x_3 &= 0
\end{aligned}
$$

**Solution**:

Swap $R_1 \leftrightarrow R_3$:

$$
\begin{bmatrix} 1 & -3 & 5 \\ 3 & 2 & 1 \\ 2 & -1 & 1 \end{bmatrix}
$$

Apply $R_2 \to R_2 - 3R_1$ and $R_3 \to R_3 - 2R_1$:

$$
\begin{bmatrix} 1 & -3 & 5 \\ 0 & 11 & -14 \\ 0 & 5 & -9 \end{bmatrix}
$$

Apply $R_3 \to 11R_3 - 5R_2$:

$$
\begin{bmatrix} 1 & -3 & 5 \\ 0 & 11 & -14 \\ 0 & 0 & -29 \end{bmatrix}
$$

Rank = 3 = number of unknowns. Only the trivial solution:

$$
x_1 = 0, \quad x_2 = 0, \quad x_3 = 0
$$

---

## Worked Example 2: Non-Trivial Solutions (PYQ 2019)

**Problem**: Find the complete solution of:

$$
\begin{aligned}
x + y + z + w &= 0 \\
x + 3y - 2z + 4w &= 0 \\
2x + y - z - w &= 0
\end{aligned}
$$

**Solution**:

After row reduction:

$$
\begin{bmatrix} 1 & 1 & 1 & 1 \\ 0 & 1 & 3 & 3 \\ 0 & 0 & 3 & 1 \end{bmatrix}
$$

Rank = 3. Variables = 4. So $4 - 3 = 1$ free variable.

From row 3: $3z + w = 0 \implies w = -3z$.

From row 2: $y + 3z + 3(-3z) = 0 \implies y = 6z$.

From row 1: $x + 6z + z - 3z = 0 \implies x = -4z$.

Let $z = k$. The general solution is:

$$
x = -4k, \quad y = 6k, \quad z = k, \quad w = -3k
$$

In vector form:

$$
\begin{bmatrix} x \\ y \\ z \\ w \end{bmatrix} = k \begin{bmatrix} -4 \\ 6 \\ 1 \\ -3 \end{bmatrix}
$$

The null space is one-dimensional, spanned by $(-4, 6, 1, -3)^T$.

---

## Exam Patterns

- Homogeneous systems appear as standalone problems or as part of eigenvalue problems (when solving $(A - \lambda I)X = 0$).
- The key test: compare rank with number of unknowns.
- If the problem says "find the trivial solution," the mathematical intent is usually to find ALL solutions.
- Express solutions in vector form when possible.

---

[← Previous: B08 Parameter Analysis](B08_Parameter_Analysis_Lambda_Mu.md) | [Index](00_Index.md) | [Next: B10 Eigenvalues and Eigenvectors →](B10_Eigenvalues_Eigenvectors.md)
