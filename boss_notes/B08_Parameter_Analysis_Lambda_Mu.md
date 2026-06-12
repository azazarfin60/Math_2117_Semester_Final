[← Previous: B07 System of Linear Equations](B07_System_of_Linear_Equations.md) | [Index](00_Index.md) | [Next: B09 Homogeneous Systems →](B09_Homogeneous_Systems.md)

---

# B08: Parameter Analysis for Systems of Equations

> **Exam Weight**: Tier 1 | **Appeared in**: 2018, 2020, 2021, 2024 + CT | **Typical Marks**: 5–7

Parameter analysis problems are a favourite of the examiners. The classic question asks: "For what values of $\lambda$ and $\mu$ does the system have no solution, a unique solution, or infinitely many solutions?" One specific problem has appeared word-for-word in multiple years.

---

## The General Approach

### What the Problem Looks Like

You are given a system of equations where one or more coefficients are replaced by parameters ($\lambda$, $\mu$, $k$, etc.). You must find which values of these parameters lead to each of the three cases:

1. **Unique solution**: The system behaves normally. One answer for each variable.
2. **No solution**: The system is contradictory. No set of values can satisfy all equations.
3. **Infinitely many solutions**: The system is underdetermined. Whole families of solutions exist.

### The Method

1. Write the augmented matrix $[A:B]$.
2. Row-reduce to echelon form. The parameter will survive in the last row.
3. The last row will look like $[0 \; 0 \; f(\lambda) \; \lvert  \; g(\lambda, \mu)]$.
4. Analyze three cases based on $f(\lambda)$ and $g(\lambda, \mu)$.

### The Decision Table

After row reduction, the critical row has the form:

$$
[0 \quad 0 \quad f(\lambda) \quad | \quad g(\lambda, \mu)]
$$

| Condition | Result |
|-----------|--------|
| $f(\lambda) \neq 0$ | Unique solution (for any $\mu$) |
| $f(\lambda) = 0$ and $g(\lambda, \mu) \neq 0$ | No solution (contradiction: $0 = c$) |
| $f(\lambda) = 0$ and $g(\lambda, \mu) = 0$ | Infinitely many solutions |

---

## Must-Know Problem 1: The Classic (PYQ 2020, 2024 — Repeated)

**Problem**: Investigate for what values of $\lambda$ and $\mu$ the system has (i) no solution, (ii) unique solution, (iii) infinitely many solutions:

$$
\begin{aligned}
x + y + z &= 6 \\
x + 2y + 3z &= 10 \\
x + 2y + \lambda z &= \mu
\end{aligned}
$$

This exact problem appeared in 2020 (7 marks) and 2024 (5 marks).

**Solution**:

Write the augmented matrix:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 6 \\
1 & 2 & 3 & | & 10 \\
1 & 2 & \lambda & | & \mu
\end{bmatrix}
$$

Apply $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 6 \\
0 & 1 & 2 & | & 4 \\
0 & 1 & \lambda - 1 & | & \mu - 6
\end{bmatrix}
$$

Apply $R_3 \to R_3 - R_2$:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 6 \\
0 & 1 & 2 & | & 4 \\
0 & 0 & \lambda - 3 & | & \mu - 10
\end{bmatrix}
$$

Now analyze the last row:

**(i) No solution**: Need $\lambda - 3 = 0$ and $\mu - 10 \neq 0$:

$$
\lambda = 3 \quad \text{and} \quad \mu \neq 10
$$

The last row becomes $[0 \; 0 \; 0 \; \lvert  \; \mu - 10]$, which says $0 = \mu - 10$. This is a contradiction since $\mu \neq 10$.

**(ii) Unique solution**: Need $\lambda - 3 \neq 0$:

$$
\lambda \neq 3 \quad \text{(for any value of } \mu\text{)}
$$

All three rows have pivots. Rank = 3 = number of unknowns.

**(iii) Infinitely many solutions**: Need $\lambda - 3 = 0$ and $\mu - 10 = 0$:

$$
\lambda = 3 \quad \text{and} \quad \mu = 10
$$

The last row becomes all zeros. Rank = 2 < 3 unknowns. One free variable.

---

## Must-Know Problem 2: Single Parameter (PYQ 2021)

**Problem**: For what values of $\lambda$ does the system have (i) no solution, (ii) unique solution, (iii) infinitely many solutions?

$$
\begin{aligned}
\lambda x + y + z &= 1 \\
x + \lambda y + z &= \lambda \\
x + y + \lambda z &= \lambda^2
\end{aligned}
$$

**Solution**:

This system has $\lambda$ in the coefficient matrix AND the constant vector. We use the determinant approach.

The coefficient matrix determinant is:

$$
D =
\begin{vmatrix}
\lambda & 1 & 1 \\
1 & \lambda & 1 \\
1 & 1 & \lambda
\end{vmatrix}
$$

Add all three rows to $R_1$:

$$
R_1 \to [\lambda + 2, \lambda + 2, \lambda + 2]
$$

Factor out $(\lambda + 2)$:

$$
D = (\lambda + 2)
\begin{vmatrix}
1 & 1 & 1 \\
1 & \lambda & 1 \\
1 & 1 & \lambda
\end{vmatrix}
$$

Apply $C_2 \to C_2 - C_1$ and $C_3 \to C_3 - C_1$:

$$
D = (\lambda + 2)
\begin{vmatrix}
1 & 0 & 0 \\
1 & \lambda - 1 & 0 \\
1 & 0 & \lambda - 1
\end{vmatrix} = (\lambda + 2)(\lambda - 1)^2
$$

**Analysis**:

**(ii) Unique solution**: $D \neq 0$, which means $\lambda \neq 1$ and $\lambda \neq -2$.

**(iii) Infinitely many solutions**: When $\lambda = 1$, all three equations become $x + y + z = 1$. They are identical. Infinitely many solutions.

**(i) No solution**: When $\lambda = -2$, the system becomes:

$$
\begin{aligned}
-2x + y + z &= 1 \\
x - 2y + z &= -2 \\
x + y - 2z &= 4
\end{aligned}
$$

Add all three equations: $0 = 3$. Contradiction. No solution.

---

## Must-Know Problem 3: CT Problem

**Problem**: Find the values of $k$ for which the system has (i) unique solution, (ii) no solution, (iii) infinitely many solutions:

$$
\begin{aligned}
x + y + z &= 1 \\
x + 2y + 3z &= k \\
x + 5y + 9z &= k^2
\end{aligned}
$$

**Solution**:

Augmented matrix:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
1 & 2 & 3 & | & k \\
1 & 5 & 9 & | & k^2
\end{bmatrix}
$$

Apply $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
0 & 1 & 2 & | & k - 1 \\
0 & 4 & 8 & | & k^2 - 1
\end{bmatrix}
$$

Apply $R_3 \to R_3 - 4R_2$:

$$
\begin{bmatrix}
1 & 1 & 1 & | & 1 \\
0 & 1 & 2 & | & k - 1 \\
0 & 0 & 0 & | & k^2 - 4k + 3
\end{bmatrix}
$$

Factor the last entry: $k^2 - 4k + 3 = (k - 1)(k - 3)$.

**(i) Unique solution**: The coefficient part has rank 2 (not 3) because the last row of coefficients is all zeros. So this system can NEVER have a unique solution.

Wait. Let me re-examine. The coefficient matrix after reduction is:

$$
\begin{bmatrix}
1 & 1 & 1 \\
0 & 1 & 2 \\
0 & 0 & 0
\end{bmatrix}
$$

Rank of coefficient matrix = 2. Since rank < 3 (number of unknowns), a unique solution is impossible regardless of $k$.

**(ii) No solution**: $(k - 1)(k - 3) \neq 0 \implies k \neq 1$ and $k \neq 3$.

**(iii) Infinitely many solutions**: $(k - 1)(k - 3) = 0 \implies k = 1$ or $k = 3$.

When $k = 1$: Let $z = t$. From row 2: $y = -2t$. From row 1: $x = 1 - y - z = 1 + 2t - t = 1 + t$.

$$
x = 1 + t, \quad y = -2t, \quad z = t
$$

When $k = 3$: Let $z = t$. From row 2: $y = 2 - 2t$. From row 1: $x = 1 - y - z = 1 - (2 - 2t) - t = -1 + t$.

$$
x = -1 + t, \quad y = 2 - 2t, \quad z = t
$$

---

## Key Observations

### When Two Parameters Appear

If the system has both $\lambda$ (in the coefficient matrix) and $\mu$ (in the constant vector), you get a 2D analysis. The answer typically looks like:
- Unique: $\lambda \neq$ some value, $\mu$ = anything
- No solution: $\lambda =$ that value, $\mu \neq$ some other value
- Infinite: $\lambda$ and $\mu$ both equal specific values

### When One Parameter Appears

If $\lambda$ appears only in the coefficient matrix, the analysis is simpler. You compute the determinant and find where it is zero. At those zero-points, check if the system is consistent or not.

### The Determinant Shortcut

For a 3x3 system with parameter $\lambda$:
- Compute $D = \lvert A \rvert$ as a function of $\lambda$.
- $D \neq 0$ means unique solution.
- $D = 0$ means either no solution or infinite solutions. You must check further.

---

## Exam Patterns

- **This appears about every other year.** It has shown up in 2018, 2020, 2021, 2024, and CTs.
- The $x+y+z=6$, $x+2y+3z=10$, $x+2y+\lambda z=\mu$ problem is the most repeated. Memorize it.
- Always show the complete row reduction. Marks are given for the steps.
- State all three cases clearly: (i), (ii), (iii) with the exact conditions on $\lambda$ and $\mu$.
- If the problem asks to "solve completely," you must also give the general solution in the infinite-solutions case.

---

[← Previous: B07 System of Linear Equations](B07_System_of_Linear_Equations.md) | [Index](00_Index.md) | [Next: B09 Homogeneous Systems →](B09_Homogeneous_Systems.md)
