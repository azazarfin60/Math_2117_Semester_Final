[← Previous: B12 Adjoint and Inverse](B12_Adjoint_Inverse_Matrix.md) | [Index](00_Index.md)

---

# B13: Diagonalization, Matrix Exponential, and Matrix ODE

> **Exam Weight**: Tier 2-3 | **Appeared in**: 2017, 2020, 2021 | **Typical Marks**: 6–12

This topic combines eigenvalues with differential equations. The matrix ODE problem appeared identically in 2020 and 2021.

---

## Diagonalization

### What is Diagonalization?

A square matrix $A$ is diagonalizable if there exists an invertible matrix $P$ such that:

$$
P^{-1}AP = D
$$

where $D$ is a diagonal matrix. The diagonal entries of $D$ are the eigenvalues of $A$. The columns of $P$ are the corresponding eigenvectors.

### When is Diagonalization Possible?

An $n \times n$ matrix is diagonalizable if and only if it has $n$ linearly independent eigenvectors.

- If all $n$ eigenvalues are distinct, the matrix is always diagonalizable.
- If eigenvalues are repeated, diagonalization depends on whether enough independent eigenvectors exist. If the geometric multiplicity (number of independent eigenvectors) equals the algebraic multiplicity (repeat count) for each eigenvalue, the matrix is diagonalizable.

### The Modal Matrix

The matrix $P$ whose columns are the eigenvectors is called the **modal matrix**:

$$
P = [X_1 \; X_2 \; \dots \; X_n]
$$

Then $A = PDP^{-1}$.

---

## When Diagonalization Fails (PYQ 2017)

The matrix

$$
A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}
$$

 has eigenvalue $\lambda = 1$ with algebraic multiplicity 2.

Solving $(A - I)X = 0$:

$$
\begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}X = 0
$$

This gives only one eigenvector:

$$
X = \begin{bmatrix} 1 \\ 0 \end{bmatrix}.
$$

Geometric multiplicity = 1 < algebraic multiplicity = 2. So $A$ is NOT diagonalizable.

---

## Matrix Exponential

### Definition

The matrix exponential $e^A$ is defined by the power series:

$$
e^A = I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \dots
$$

### Computation Using Diagonalization

If $A = PDP^{-1}$:

$$
e^A = Pe^D P^{-1}
$$

where $e^D$ is simply:

$$
e^D = \begin{bmatrix} e^{\lambda_1} & 0 & \dots \\ 0 & e^{\lambda_2} & \dots \\ \vdots & \vdots & \ddots \end{bmatrix}
$$

### Computation Using Decomposition (PYQ 2017)

When diagonalization fails, decompose $A = I + B$ where $B$ is nilpotent.

For

$$
A = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}:
$$

Set

$$
B = \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}.
$$

Then $B^2 = O$.

$$
e^A = e^{I+B} = e^I \cdot e^B = e(I + B) = e\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} e & e \\ 0 & e \end{bmatrix}
$$

For time-dependent version:

$$
e^{At} = e^t(I + Bt) = e^t\begin{bmatrix} 1 & t \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} e^t & te^t \\ 0 & e^t \end{bmatrix}
$$

---

## Solving Matrix ODE

### The System

Given a system of first-order linear ODEs:

$$
\frac{dX}{dt} = MX
$$

where $M$ is a constant matrix and $X$ is the vector of unknowns.

### The Method

1. Find eigenvalues of $M$.
2. Find eigenvectors of $M$.
3. The general solution is:

$$
X(t) = C_1 e^{\lambda_1 t} v_1 + C_2 e^{\lambda_2 t} v_2 + \dots
$$

where $\lambda_i$ are eigenvalues and $v_i$ are corresponding eigenvectors.

---

## Must-Know Problem: Matrix ODE (PYQ 2020, 2021 — Repeated)

**Problem**: Solve by matrix method:

$$
\frac{dx}{dt} = 6x - 3y, \quad \frac{dy}{dt} = 2x + y
$$

**Solution**:

Write in matrix form $\frac{dX}{dt} = MX$ where:

$$
M = \begin{bmatrix} 6 & -3 \\ 2 & 1 \end{bmatrix}
$$

**Step 1**: Eigenvalues. $\lvert M - \lambda I \rvert = 0$:

$$
(6-\lambda)(1-\lambda) + 6 = \lambda^2 - 7\lambda + 12 = (\lambda - 3)(\lambda - 4) = 0
$$

So $\lambda_1 = 3$ and $\lambda_2 = 4$.

**Step 2**: Eigenvectors.

For $\lambda = 3$: $3x - 3y = 0 \implies x = y$. Eigenvector:

$$
v_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}.
$$

For $\lambda = 4$: $2x - 3y = 0 \implies x = \frac{3}{2}y$. Eigenvector:

$$
v_2 = \begin{bmatrix} 3 \\ 2 \end{bmatrix}.
$$

**Step 3**: General solution:

$$
\begin{bmatrix} x(t) \\ y(t) \end{bmatrix} = C_1 e^{3t}\begin{bmatrix} 1 \\ 1 \end{bmatrix} + C_2 e^{4t}\begin{bmatrix} 3 \\ 2 \end{bmatrix}
$$

Component form:

$$
x(t) = C_1 e^{3t} + 3C_2 e^{4t}
$$

$$
y(t) = C_1 e^{3t} + 2C_2 e^{4t}
$$

---

## Exam Patterns

- Matrix ODE ($dx/dt = 6x - 3y$, $dy/dt = 2x + y$) appeared identically in 2020 and 2021. Memorize it.
- The 2017 paper had a 12-mark diagonalization + $e^A$ + ODE problem.
- The method is always: eigenvalues then eigenvectors then write the general solution.
- If the matrix is not diagonalizable, mention it and use the decomposition method for $e^A$.

---

[← Previous: B12 Adjoint and Inverse](B12_Adjoint_Inverse_Matrix.md) | [Index](00_Index.md)
