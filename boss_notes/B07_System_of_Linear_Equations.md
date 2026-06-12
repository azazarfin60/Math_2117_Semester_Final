[← Previous: B06 Normal Canonical Form](B06_Normal_Canonical_Form.md) | [Index](00_Index.md) | [Next: B08 Parameter Analysis →](B08_Parameter_Analysis_Lambda_Mu.md)

---

# B07: System of Linear Equations

> **Exam Weight**: Tier 1 | **Appeared in**: 2017, 2018, 2019, 2020, 2021, 2023, 2024 (all 7 papers) + CT | **Typical Marks**: 5–7

This topic has appeared in every single exam paper. Together with rank and eigenvalues, it forms the trio of guaranteed exam topics.

---

## Matrix Form of a System

### Setting Up the System

Any system of linear equations can be written in matrix form as:

$$
AX = B
$$

Here:
- $A$ is the coefficient matrix (contains the coefficients of the variables)
- $X$ is the column vector of unknowns
- $B$ is the column vector of constants

For example, the system:

$$
\begin{aligned}
x - 2y - 5z &= 2 \\
-x + y + 3z &= -2 \\
2x + y + z &= 3
\end{aligned}

$$

becomes:

$$

\begin{bmatrix}
1 & -2 & -5 \\
-1 & 1 & 3 \\
2 & 1 & 1
\end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 2 \\ -2 \\ 3 \end{bmatrix}
$$

### The Augmented Matrix

We combine $A$ and $B$ into one matrix called the augmented matrix. We write it as $[A : B]$ or $[A \lvert  B]$:

$$
[A : B] =
\begin{bmatrix}
1 & -2 & -5 & | & 2 \\
-1 & 1 & 3 & | & -2 \\
2 & 1 & 1 & | & 3
\end{bmatrix}
$$

The vertical line separates the coefficients from the constants. We apply row operations to this augmented matrix to solve the system.

---

## Consistency Conditions

### The Rank Test

A system $AX = B$ is either consistent (has at least one solution) or inconsistent (has no solution). The rank decides which case applies.

Let $n$ = number of unknowns, $\rho(A)$ = rank of coefficient matrix, $\rho[A:B]$ = rank of augmented matrix.

| Condition | Result |
|-----------|--------|
| $\rho(A) \neq \rho[A:B]$ | **No solution** (inconsistent) |
| $\rho(A) = \rho[A:B] = n$ | **Unique solution** |
| $\rho(A) = \rho[A:B] < n$ | **Infinitely many solutions** (with $n - \rho(A)$ free variables) |

### Key Idea

When we reduce $[A:B]$ to echelon form, a contradiction row looks like $[0 \; 0 \; 0 \; \lvert  \; c]$ where $c \neq 0$. This says $0 = c$, which is impossible. Such a row means the system has no solution.

If no contradiction row appears, the system is consistent. Count the non-zero rows in the coefficient part. That is $\rho(A)$. If it equals the number of variables, you get a unique solution. If it is less, you get infinitely many solutions.

---

## Solving by Row Reduction

### The Method

1. Write the augmented matrix $[A:B]$.
2. Use elementary row operations to reach echelon form.
3. Check for contradiction rows.
4. Back-substitute from the bottom row upward.

### Worked Example 1: Unique Solution (PYQ 2017)

**Problem**: Solve by elementary transformation:

$$
\begin{aligned}
2x_1 + 2x_2 + x_3 &= 2 \\
3x_1 + x_2 - 2x_3 &= 1 \\
4x_1 - 3x_2 - x_3 &= 3
\end{aligned}
$$

**Solution**:

Write the augmented matrix:

$$
\begin{bmatrix}
2 & 2 & 1 & | & 2 \\
3 & 1 & -2 & | & 1 \\
4 & -3 & -1 & | & 3
\end{bmatrix}
$$

Apply $R_2 \to 2R_2 - 3R_1$ and $R_3 \to R_3 - 2R_1$:

$$
\begin{bmatrix}
2 & 2 & 1 & | & 2 \\
0 & -4 & -7 & | & -4 \\
0 & -7 & -3 & | & -1
\end{bmatrix}
$$

Apply $R_3 \to 4R_3 - 7R_2$:

$$
\begin{bmatrix}
2 & 2 & 1 & | & 2 \\
0 & 4 & 7 & | & 4 \\
0 & 0 & 37 & | & 24
\end{bmatrix}
$$

Back-substitute. From row 3:

$$
37x_3 = 24 \implies x_3 = \frac{24}{37}
$$

From row 2:

$$
4x_2 + 7 \cdot \frac{24}{37} = 4 \implies 4x_2 = 4 - \frac{168}{37} = \frac{-20}{37} \implies x_2 = -\frac{5}{37}
$$

From row 1:

$$
2x_1 + 2 \cdot \left(-\frac{5}{37}\right) + \frac{24}{37} = 2 \implies 2x_1 + \frac{14}{37} = 2 \implies x_1 = \frac{30}{37}
$$

The unique solution is:

$$
x_1 = \frac{30}{37}, \quad x_2 = -\frac{5}{37}, \quad x_3 = \frac{24}{37}
$$

---

### Worked Example 2: Infinite Solutions with Free Variables (PYQ 2019)

**Problem**: Discuss consistency and find the solution set:

$$
\begin{aligned}
x + 2y + 2z &= 1 \\
2x + y + z &= 2 \\
3x + 2y + 2z &= 3 \\
y + z &= 0
\end{aligned}
$$

**Solution**:

Write the augmented matrix:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
2 & 1 & 1 & | & 2 \\
3 & 2 & 2 & | & 3 \\
0 & 1 & 1 & | & 0
\end{bmatrix}
$$

Apply $R_2 \to R_2 - 2R_1$ and $R_3 \to R_3 - 3R_1$:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
0 & -3 & -3 & | & 0 \\
0 & -4 & -4 & | & 0 \\
0 & 1 & 1 & | & 0
\end{bmatrix}
$$

Scale: $R_2 \to -\frac{1}{3}R_2$ and $R_3 \to -\frac{1}{4}R_3$:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
0 & 1 & 1 & | & 0 \\
0 & 1 & 1 & | & 0 \\
0 & 1 & 1 & | & 0
\end{bmatrix}
$$

Apply $R_3 \to R_3 - R_2$ and $R_4 \to R_4 - R_2$:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
0 & 1 & 1 & | & 0 \\
0 & 0 & 0 & | & 0 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$

**Check consistency**: $\rho(A) = 2$ and $\rho[A:B] = 2$. So the system is consistent.

Since there are 3 variables and rank is 2, we have $3 - 2 = 1$ free variable.

From row 2: $y + z = 0 \implies y = -z$.

From row 1: $x + 2(-z) + 2z = 1 \implies x = 1$.

Let $z = k$ where $k \in \mathbb{R}$. The solution set is:

$$
x = 1, \quad y = -k, \quad z = k
$$

---

### Worked Example 3: Solving a System (PYQ 2023)

**Problem**: Solve:

$$
\begin{aligned}
x + 2y - z &= 2 \\
2x + y + z &= 1 \\
x + 5y - 4z &= 5
\end{aligned}
$$

**Solution**:

Write the augmented matrix:

$$
\begin{bmatrix}
1 & 2 & -1 & | & 2 \\
2 & 1 & 1 & | & 1 \\
1 & 5 & -4 & | & 5
\end{bmatrix}
$$

Apply $R_2 \to R_2 - 2R_1$ and $R_3 \to R_3 - R_1$:

$$
\begin{bmatrix}
1 & 2 & -1 & | & 2 \\
0 & -3 & 3 & | & -3 \\
0 & 3 & -3 & | & 3
\end{bmatrix}
$$

Apply $R_3 \to R_3 + R_2$:

$$
\begin{bmatrix}
1 & 2 & -1 & | & 2 \\
0 & -3 & 3 & | & -3 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$

Rank is 2 with 3 variables. So there is 1 free variable.

From row 2: $-3y + 3z = -3 \implies y - z = 1 \implies y = z + 1$.

From row 1: $x + 2(z + 1) - z = 2 \implies x + z + 2 = 2 \implies x = -z$.

Let $z = t$. The general solution is:

$$
x = -t, \quad y = t + 1, \quad z = t
$$

---

## Finding a System with Parameters (PYQ 2018)

Sometimes the system contains a parameter $\lambda$ and you must find the values of $\lambda$ that allow solutions.

### Worked Example 4: Parameter in the System

**Problem**: Find the value of $\lambda$ so that the system has a solution. Solve completely in each case.

$$
\begin{aligned}
x + y + z &= 1 \\
x + 2y + 4z &= \lambda \\
x + 4y + 10z &= \lambda^2
\end{aligned}
$$

**Solution**:

Write the augmented matrix:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
1 & 2 & 4 & | & \lambda \\
1 & 4 & 10 & | & \lambda^2
\end{bmatrix}
$$

Apply $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
0 & 1 & 3 & | & \lambda - 1 \\
0 & 3 & 9 & | & \lambda^2 - 1
\end{bmatrix}
$$

Apply $R_3 \to R_3 - 3R_2$:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
0 & 1 & 3 & | & \lambda - 1 \\
0 & 0 & 0 & | & \lambda^2 - 3\lambda + 2
\end{bmatrix}
$$

For consistency, the last row must not be a contradiction. So we need:

$$
\lambda^2 - 3\lambda + 2 = 0 \implies (\lambda - 1)(\lambda - 2) = 0
$$

So $\lambda = 1$ or $\lambda = 2$.

**Case 1**: $\lambda = 1$.

The augmented matrix becomes:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
0 & 1 & 3 & | & 0 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$

Let $z = t$. From row 2: $y = -3t$. From row 1: $x = 1 - y - z = 1 + 3t - t = 1 + 2t$.

$$
x = 1 + 2t, \quad y = -3t, \quad z = t
$$

**Case 2**: $\lambda = 2$.

The augmented matrix becomes:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
0 & 1 & 3 & | & 1 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$

Let $z = t$. From row 2: $y = 1 - 3t$. From row 1: $x = 1 - y - z = 1 - (1 - 3t) - t = 2t$.

$$
x = 2t, \quad y = 1 - 3t, \quad z = t
$$

---

## Key Concepts to Remember

### Consistent vs Inconsistent

A system is **consistent** if it has at least one solution. It is **inconsistent** if it has no solution at all.

### Free Variables

When the rank is less than the number of unknowns, the difference gives the number of free variables. You assign parameters ($t$, $k$, etc.) to these free variables and express all other variables in terms of them.

### Choosing Free Variables

In echelon form, the columns without pivots correspond to free variables. The columns with pivots correspond to basic (determined) variables.

---

## Exam Patterns

- **This topic appears every year.** Usually as "Solve the following system by elementary transformation" or "Discuss the consistency and find the solution."
- Marks range from 5 to 7 per question.
- The most common format is 3 equations in 3 unknowns. Sometimes 4 equations appear.
- **Parameter problems** (with $\lambda$) appear frequently. See B08 for more on those.
- Always show the augmented matrix and every row operation step. This is where marks are given.
- Write the final answer clearly with a box or line. State the solution as $(x, y, z) = (a, b, c)$ or in parametric form.

---

## Must-Know Problems

### Problem 5: Class Note System

**Problem**: Solve:

$$
\begin{aligned}
x - 2y - 5z &= 2 \\
-x + y + 3z &= -2 \\
2x + y + z &= 3
\end{aligned}
$$

**Solution**:

Augmented matrix:

$$
\begin{bmatrix}
1 & -2 & -5 & | & 2 \\
-1 & 1 & 3 & | & -2 \\
2 & 1 & 1 & | & 3
\end{bmatrix}
$$

Apply $R_2 \to R_1 + R_2$ and $R_3 \to 2R_1 - R_3$:

$$
\begin{bmatrix}
1 & -2 & -5 & | & 2 \\
0 & -1 & -2 & | & 0 \\
0 & -5 & -11 & | & 1
\end{bmatrix}
$$

Apply $R_3 \to 5R_2 - R_3$:

$$
\begin{bmatrix}
1 & -2 & -5 & | & 2 \\
0 & -1 & -2 & | & 0 \\
0 & 0 & 1 & | & -1
\end{bmatrix}
$$

Back-substitute. From row 3: $z = -1$.

From row 2: $-y - 2(-1) = 0 \implies y = 2$.

From row 1: $x - 2(2) - 5(-1) = 2 \implies x = 1$.

$$
(x, y, z) = (1, 2, -1)
$$

---

### Problem 6: Homogeneous System (PYQ 2018)

**Problem**: Solve:

$$
\begin{aligned}
2x_1 - x_2 + x_3 &= 0 \\
3x_1 + 2x_2 + x_3 &= 0 \\
x_1 - 3x_2 + 5x_3 &= 0
\end{aligned}
$$

**Solution**:

For a homogeneous system $AX = 0$, the trivial solution $x_1 = x_2 = x_3 = 0$ always exists.

Write the coefficient matrix and reduce:

$$
\begin{bmatrix}
1 & -3 & 5 \\
3 & 2 & 1 \\
2 & -1 & 1
\end{bmatrix}
$$

(We swapped $R_1 \leftrightarrow R_3$ to get a leading 1.)

Apply $R_2 \to R_2 - 3R_1$ and $R_3 \to R_3 - 2R_1$:

$$
\begin{bmatrix}
1 & -3 & 5 \\
0 & 11 & -14 \\
0 & 5 & -9
\end{bmatrix}
$$

Apply $R_3 \to 11R_3 - 5R_2$:

$$
\begin{bmatrix}
1 & -3 & 5 \\
0 & 11 & -14 \\
0 & 0 & -29
\end{bmatrix}
$$

Rank = 3 = number of variables. So the system has only the trivial solution:

$$
x_1 = 0, \quad x_2 = 0, \quad x_3 = 0
$$

---

### Problem 7: Homogeneous System with Non-Trivial Solution (PYQ 2019)

**Problem**: Find the complete solution of:

$$
\begin{aligned}
x + y + z + w &= 0 \\
x + 3y - 2z + 4w &= 0 \\
2x + y - z - w &= 0
\end{aligned}
$$

**Solution**:

Coefficient matrix:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 3 & -2 & 4 \\
2 & 1 & -1 & -1
\end{bmatrix}
$$

Apply $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - 2R_1$:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 2 & -3 & 3 \\
0 & -1 & -3 & -3
\end{bmatrix}
$$

Apply $R_3 \to 2R_3 + R_2$:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 2 & -3 & 3 \\
0 & 0 & -9 & -3
\end{bmatrix}
$$

Rank = 3. Number of variables = 4. So there is $4 - 3 = 1$ free variable.

From row 3: $-9z - 3w = 0 \implies w = -3z$.

From row 2: $2y - 3z + 3(-3z) = 0 \implies 2y = 12z \implies y = 6z$.

From row 1: $x + 6z + z + (-3z) = 0 \implies x = -4z$.

Let $z = k$:

$$
x = -4k, \quad y = 6k, \quad z = k, \quad w = -3k
$$

The trivial solution is $k = 0$. Any $k \neq 0$ gives a non-trivial solution.

---

[← Previous: B06 Normal Canonical Form](B06_Normal_Canonical_Form.md) | [Index](00_Index.md) | [Next: B08 Parameter Analysis →](B08_Parameter_Analysis_Lambda_Mu.md)
