# Topic 02: System of Linear Equations

This file contains the organized questions and answers for **System of Linear Equations**, priority ranked as **Priority 2** based on frequency and exam weight.

---

## Q1. Solve by elementary transformation: (06)

| | |
|---|---|
| **ID** | PYQ-2017-6b |
| **Source** | 2017 Q6(b) [06 marks] |

**Answer:**

$$2x_1 + 2x_2 + x_3 = 2$$
$$3x_1 + x_2 - 2x_3 = 1$$
$$4x_1 - 3x_2 - x_3 = 3$$

**Answer:**

We write the augmented matrix of the system:

$$
\begin{bmatrix} 2 & 2 & 1 & | & 2 \\ 3 & 1 & -2 & | & 1 \\ 4 & -3 & -1 & | & 3 \end{bmatrix}
$$

We perform row operations to reduce it:
*   $R_2 \to 2R_2 - 3R_1$
*   $R_3 \to R_3 - 2R_1$

This gives:

$$
\begin{bmatrix} 2 & 2 & 1 & | & 2 \\ 0 & -4 & -7 & | & -4 \\ 0 & -7 & -3 & | & -1 \end{bmatrix}
$$

Multiply the second and third rows by $-1$:

$$
\begin{bmatrix} 2 & 2 & 1 & | & 2 \\ 0 & 4 & 7 & | & 4 \\ 0 & 7 & 3 & | & 1 \end{bmatrix}
$$

Now perform row operation $R_3 \to 4R_3 - 7R_2$:

$$
\begin{bmatrix} 2 & 2 & 1 & | & 2 \\ 0 & 4 & 7 & | & 4 \\ 0 & 0 & -37 & | & -24 \end{bmatrix}
$$

Now we solve the variables by back substitution. From the third row:

$$
-37x_3 = -24 \implies x_3 = \frac{24}{37}
$$

From the second row:

$$
4x_2 + 7x_3 = 4 \implies 4x_2 + 7\left( \frac{24}{37} \right) = 4
$$

$$
4x_2 = 4 - \frac{168}{37} = \frac{148 - 168}{37} = -\frac{20}{37} \implies x_2 = -\frac{5}{37}
$$

From the first row:

$$
2x_1 + 2x_2 + x_3 = 2 \implies 2x_1 + 2\left( -\frac{5}{37} \right) + \frac{24}{37} = 2
$$

$$
2x_1 - \frac{10}{37} + \frac{24}{37} = 2 \implies 2x_1 + \frac{14}{37} = 2
$$

$$
2x_1 = 2 - \frac{14}{37} = \frac{74 - 14}{37} = \frac{60}{37} \implies x_1 = \frac{30}{37}
$$

So the unique solution is:

$$
x_1 = \frac{30}{37}, \quad x_2 = -\frac{5}{37}, \quad x_3 = \frac{24}{37}
$$

---

## Q2. Find the value of $\lambda$ so that the following equations have a solution and solve completely in each case: (06)

| | |
|---|---|
| **ID** | PYQ-2018-6a |
| **Source** | 2018 Q6(a) [06 marks] |

**Answer:**

$$x + y + z = 1$$
$$x + 2y + 4z = \lambda$$
$$x + 4y + 10z = \lambda^2$$

**Answer:**

We write the augmented matrix of the system:

$$
\begin{bmatrix} 1 & 1 & 1 & | & 1 \\ 1 & 2 & 4 & | & \lambda \\ 1 & 4 & 10 & | & \lambda^2 \end{bmatrix}
$$

Apply row operations:
*   $R_2 \to R_2 - R_1$
*   $R_3 \to R_3 - R_1$

This gives:

$$
\begin{bmatrix} 1 & 1 & 1 & | & 1 \\ 0 & 1 & 3 & | & \lambda - 1 \\ 0 & 3 & 9 & | & \lambda^2 - 1 \end{bmatrix}
$$

Now eliminate row 3 using row 2 ($R_3 \to R_3 - 3R_2$):

$$
\begin{bmatrix} 1 & 1 & 1 & | & 1 \\ 0 & 1 & 3 & | & \lambda - 1 \\ 0 & 0 & 0 & | & \lambda^2 - 3\lambda + 2 \end{bmatrix}
$$

A solution exists if the system is consistent:

$$
\lambda^2 - 3\lambda + 2 = 0 \implies (\lambda - 1)(\lambda - 2) = 0 \implies \lambda = 1 \quad \text{or} \quad \lambda = 2
$$

We solve the system for each case:

#### Case 1: For $\lambda = 1$

The augmented matrix is:

$$
\begin{bmatrix} 1 & 1 & 1 & | & 1 \\ 0 & 1 & 3 & | & 0 \\ 0 & 0 & 0 & | & 0 \end{bmatrix}
$$

From row 2:

$$
y + 3z = 0 \implies y = -3z
$$

From row 1:

$$
x + y + z = 1 \implies x - 3z + z = 1 \implies x = 2z + 1
$$

Let $z = t$ be a parameter. The general solution is:

$$
x = 2t + 1, \quad y = -3t, \quad z = t
$$

#### Case 2: For $\lambda = 2$

The augmented matrix is:

$$
\begin{bmatrix} 1 & 1 & 1 & | & 1 \\ 0 & 1 & 3 & | & 1 \\ 0 & 0 & 0 & | & 0 \end{bmatrix}
$$

From row 2:

$$
y + 3z = 1 \implies y = 1 - 3z
$$

From row 1:

$$
x + y + z = 1 \implies x + (1 - 3z) + z = 1 \implies x = 2z
$$

Let $z = t$ be a parameter. The general solution is:

$$
x = 2t, \quad y = 1 - 3t, \quad z = t
$$

---

## Q3. Solve: (06)

| | |
|---|---|
| **ID** | PYQ-2018-6b |
| **Source** | 2018 Q6(b) [06 marks] |

**Answer:**

$$2x_1 - x_2 + x_3 = 0$$
$$3x_1 + 2x_2 + x_3 = 0$$
$$x_1 - 3x_2 + 5x_3 = 0$$

**Answer:**

We write the augmented matrix of this homogeneous system:

$$
\begin{bmatrix} 2 & -1 & 1 & | & 0 \\ 3 & 2 & 1 & | & 0 \\ 1 & -3 & 5 & | & 0 \end{bmatrix}
$$

We swap row 1 and row 3 ($R_1 \leftrightarrow R_3$):

$$
\begin{bmatrix} 1 & -3 & 5 & | & 0 \\ 3 & 2 & 1 & | & 0 \\ 2 & -1 & 1 & | & 0 \end{bmatrix}
$$

Apply row operations:
*   $R_2 \to R_2 - 3R_1$
*   $R_3 \to R_3 - 2R_1$

This gives:

$$
\begin{bmatrix} 1 & -3 & 5 & | & 0 \\ 0 & 11 & -14 & | & 0 \\ 0 & 5 & -9 & | & 0 \end{bmatrix}
$$

Perform the operation $R_3 \to 11R_3 - 5R_2$:

$$
\begin{bmatrix} 1 & -3 & 5 & | & 0 \\ 0 & 11 & -14 & | & 0 \\ 0 & 0 & -29 & | & 0 \end{bmatrix}
$$

By back substitution, we solve the system:
*   From the third row: $-29x_3 = 0 \implies x_3 = 0$.
*   From the second row: $11x_2 - 14(0) = 0 \implies x_2 = 0$.
*   From the first row: $x_1 - 3(0) + 5(0) = 0 \implies x_1 = 0$.

So the system only has the trivial solution:

$$
x_1 = 0, \quad x_2 = 0, \quad x_3 = 0
$$

---

## Q4. Discuss about the consistency of a system and then find the solution set of the system: (06)

| | |
|---|---|
| **ID** | PYQ-2019-6a |
| **Source** | 2019 Q6(a) [06 marks] |

**Answer:**

$$
\begin{aligned}
x + 2y + 2z &= 1 \\
2x + y + z &= 2 \\
3x + 2y + 2z &= 3 \\
y + z &= 0
\end{aligned}
$$

**Answer:**

#### 1. Discuss Consistency

A system of linear equations $AX = B$ is consistent if there exists at least one set of values for the unknowns that satisfies all equations simultaneously. In terms of rank:
*   The system is consistent if $\text{Rank}(A) = \text{Rank}([A|B])$, where $A$ is the coefficient matrix and $[A|B]$ is the augmented matrix.
*   If $\text{Rank}(A) = \text{Rank}([A|B]) = n$ (number of variables), the system has a unique solution.
*   If $\text{Rank}(A) = \text{Rank}([A|B]) < n$, the system has infinitely many solutions (with $n - r$ free parameters).
*   If $\text{Rank}(A) \neq \text{Rank}([A|B])$, the system is inconsistent (no solution).

#### 2. Solve the System

We write the augmented matrix $[A|B]$:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
2 & 1 & 1 & | & 2 \\
3 & 2 & 2 & | & 3 \\
0 & 1 & 1 & | & 0
\end{bmatrix}
$$

Apply row operations to clear the first column:
*   $R_2 \to R_2 - 2R_1$
*   $R_3 \to R_3 - 3R_1$

This gives:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
0 & -3 & -3 & | & 0 \\
0 & -4 & -4 & | & 0 \\
0 & 1 & 1 & | & 0
\end{bmatrix}
$$

Scale row 2 and row 3:
*   $R_2 \to -\frac{1}{3} R_2$
*   $R_3 \to -\frac{1}{4} R_3$

This gives:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
0 & 1 & 1 & | & 0 \\
0 & 1 & 1 & | & 0 \\
0 & 1 & 1 & | & 0
\end{bmatrix}
$$

Apply row operations:
*   $R_3 \to R_3 - R_2$
*   $R_4 \to R_4 - R_2$

This yields the row echelon form:

$$
\begin{bmatrix}
1 & 2 & 2 & | & 1 \\
0 & 1 & 1 & | & 0 \\
0 & 0 & 0 & | & 0 \\
0 & 0 & 0 & | & 0
\end{bmatrix}
$$

The rank of the coefficient matrix $A$ is 2, and the rank of the augmented matrix $[A|B]$ is also 2. Since $\text{Rank}(A) = \text{Rank}([A|B]) = 2$, the system is consistent.

Since there are 3 variables ($x, y, z$) and the rank is 2, there is $3 - 2 = 1$ free variable.

From row 2:

$$
y + z = 0 \implies y = -z
$$

From row 1:

$$
x + 2y + 2z = 1 \implies x + 2(-z) + 2z = 1 \implies x = 1
$$

Let $z = k$ (where $k \in \mathbb{R}$ is a parameter). The solution set is:

$$
x = 1, \quad y = -k, \quad z = k \quad (k \in \mathbb{R})
$$

---

## Q5. Find the trivial solution of: (06)

| | |
|---|---|
| **ID** | PYQ-2019-6b |
| **Source** | 2019 Q6(b) [06 marks] |

**Answer:**

$$
\begin{aligned}
x + y + z + w &= 0 \\
x + 3y - 2z + 4w &= 0 \\
2x + y - z - w &= 0
\end{aligned}
$$

**Answer:**

For any homogeneous linear system $AX = 0$, the trivial solution is the solution where all variables are zero:

$$
x = 0, \quad y = 0, \quad z = 0, \quad w = 0
$$

To find if there are non-trivial solutions (which is the mathematical intent of the question), we write the coefficient matrix:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 3 & -2 & 4 \\
2 & 1 & -1 & -1
\end{bmatrix}
$$

Apply row operations:
*   $R_2 \to R_2 - R_1$
*   $R_3 \to R_3 - 2R_1$

This gives:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 2 & -3 & 3 \\
0 & -1 & -3 & -3
\end{bmatrix}
$$

Swap row 2 and row 3 ($R_2 \leftrightarrow R_3$) and multiply the new row 2 by $-1$ ($R_2 \to -R_2$):

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 3 & 3 \\
0 & 2 & -3 & 3
\end{bmatrix}
$$

Apply row operation:
*   $R_3 \to R_3 - 2R_2$

This gives:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 3 & 3 \\
0 & 0 & -9 & -3
\end{bmatrix}
$$

Scale row 3 ($R_3 \to -\frac{1}{3} R_3$):

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 1 & 3 & 3 \\
0 & 0 & 3 & 1
\end{bmatrix}
$$

The rank of the matrix is 3. Since there are 4 variables ($x, y, z, w$) and the rank is 3, there is $4 - 3 = 1$ free variable.

From row 3:

$$
3z + w = 0 \implies w = -3z
$$

From row 2:

$$
y + 3z + 3w = 0 \implies y + 3z + 3(-3z) = 0 \implies y - 6z = 0 \implies y = 6z
$$

From row 1:

$$
x + y + z + w = 0 \implies x + 6z + z - 3z = 0 \implies x + 4z = 0 \implies x = -4z
$$

Let $z = k$ (where $k \in \mathbb{R}$ is a parameter). The complete solution set is:

$$
x = -4k, \quad y = 6k, \quad z = k, \quad w = -3k \quad (k \in \mathbb{R})
$$

*   The **trivial solution** corresponds to $k = 0$, giving $(0, 0, 0, 0)$.
*   For any $k \neq 0$, we obtain **non-trivial solutions**.

---

## Q6. Investigate for what values of $\lambda$ and $\mu$ the following system of equations have (i) no solution, (ii) unique solution, (iii) infinite number of solutions: (07)

| | |
|---|---|
| **ID** | PYQ-2020-6b | PYQ-2024-5b |
| **Appeared in** | 2020 Q6(b) [07 marks], 2024 Q5(b) [05 marks] |
| **Frequency** | ⭐⭐ (2 times) |

**Answer:**

$$x + y + z = 6$$
$$x + 2y + 3z = 10$$
$$x + 2y + \lambda z = \mu$$

**Answer:**

We write the augmented matrix of the system:

$$
\begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 1 & 2 & 3 & | & 10 \\ 1 & 2 & \lambda & | & \mu \end{bmatrix}
$$

Apply row operations:
*   $R_2 \to R_2 - R_1$
*   $R_3 \to R_3 - R_1$

This gives:

$$
\begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 0 & 1 & 2 & | & 4 \\ 0 & 1 & \lambda - 1 & | & \mu - 6 \end{bmatrix}
$$

Now eliminate row 3 using row 2 ($R_3 \to R_3 - R_2$):

$$
\begin{bmatrix} 1 & 1 & 1 & | & 6 \\ 0 & 1 & 2 & | & 4 \\ 0 & 0 & \lambda - 3 & | & \mu - 10 \end{bmatrix}
$$

Now we investigate:

#### (i) No Solution

A contradiction occurs if the last row is of the form $[0, 0, 0 | c]$ with $c \neq 0$:

$$
\lambda - 3 = 0 \quad \text{and} \quad \mu - 10 \neq 0 \implies \lambda = 3 \quad \text{and} \quad \mu \neq 10
$$

#### (ii) Unique Solution

A unique solution exists if the rank of the coefficient matrix is 3:

$$
\lambda - 3 \neq 0 \implies \lambda \neq 3
$$

for any value of $\mu$.

#### (iii) Infinite Solutions

Infinite solutions exist if the last row is entirely zero:

$$
\lambda - 3 = 0 \quad \text{and} \quad \mu - 10 = 0 \implies \lambda = 3 \quad \text{and} \quad \mu = 10
$$

---

## Q7. Discuss for what values of $\lambda$ the following system of equations have (i) no solution (ii) unique solution and (iii) infinite number of solutions: (06)

| | |
|---|---|
| **ID** | PYQ-2021-6b |
| **Source** | 2021 Q6(b) [06 marks] |

**Answer:**

$$\lambda x + y + z = 1$$
$$x + \lambda y + z = \lambda$$
$$x + y + \lambda z = \lambda^2$$

**Answer:**

We write the determinant of the coefficient matrix:

$$
D = \begin{vmatrix} \lambda & 1 & 1 \\ 1 & \lambda & 1 \\ 1 & 1 & \lambda \end{vmatrix}
$$

Add rows 2 and 3 to row 1:

$$
D = \begin{vmatrix} \lambda+2 & \lambda+2 & \lambda+2 \\ 1 & \lambda & 1 \\ 1 & 1 & \lambda \end{vmatrix} = (\lambda + 2) \begin{vmatrix} 1 & 1 & 1 \\ 1 & \lambda & 1 \\ 1 & 1 & \lambda \end{vmatrix}
$$

Apply column operations ($C_2 \to C_2 - C_1$, $C_3 \to C_3 - C_1$):

$$
D = (\lambda + 2) \begin{vmatrix} 1 & 0 & 0 \\ 1 & \lambda-1 & 0 \\ 1 & 0 & \lambda-1 \end{vmatrix} = (\lambda + 2)(\lambda - 1)^2
$$

We investigate the cases:

#### (i) Unique Solution

A unique solution exists if the determinant is not zero:

$$
D \neq 0 \implies \lambda \neq 1 \quad \text{and} \quad \lambda \neq -2
$$

#### (ii) Infinite Solutions

If $\lambda = 1$, the system of equations becomes:

$$
x + y + z = 1
$$

$$
x + y + z = 1
$$

$$
x + y + z = 1
$$

All three equations are identical. The system is consistent and has an infinite number of solutions.

#### (iii) No Solution

If $\lambda = -2$, the system becomes:

$$
-2x + y + z = 1 \quad \dots \text{(1)}
$$

$$
x - 2y + z = -2 \quad \dots \text{(2)}
$$

$$
x + y - 2z = 4 \quad \dots \text{(3)}
$$

Add these three equations:

$$
(-2x + x + x) + (y - 2y + y) + (z + z - 2z) = 1 - 2 + 4 \implies 0 = 3
$$

This is a contradiction. So there is no solution when $\lambda = -2$.

---

## Q8. Solve the following system of linear equations: (05)

| | |
|---|---|
| **ID** | PYQ-2023-6b |
| **Source** | 2023 Q6(b) [05 marks] |

**Answer:**

$$x + 2y - z = 2$$
$$2x + y + z = 1$$
$$x + 5y - 4z = 5$$

**Answer:**

We write the augmented matrix:

$$
\begin{bmatrix} 1 & 2 & -1 & | & 2 \\ 2 & 1 & 1 & | & 1 \\ 1 & 5 & -4 & | & 5 \end{bmatrix}
$$

Apply row operations:
*   $R_2 \to R_2 - 2R_1$
*   $R_3 \to R_3 - R_1$

This gives:

$$
\begin{bmatrix} 1 & 2 & -1 & | & 2 \\ 0 & -3 & 3 & | & -3 \\ 0 & 3 & -3 & | & 3 \end{bmatrix}
$$

Perform the operation $R_3 \to R_3 + R_2$:

$$
\begin{bmatrix} 1 & 2 & -1 & | & 2 \\ 0 & -3 & 3 & | & -3 \\ 0 & 0 & 0 & | & 0 \end{bmatrix}
$$

Scale row 2 ($R_2 \to -1/3 R_2$):

$$
\begin{bmatrix} 1 & 2 & -1 & | & 2 \\ 0 & 1 & -1 & | & 1 \\ 0 & 0 & 0 & | & 0 \end{bmatrix}
$$

This system is consistent. From row 2:

$$
y - z = 1 \implies y = 1 + z
$$

From row 1:

$$
x + 2y - z = 2 \implies x + 2(1 + z) - z = 2 \implies x + 2 + z = 2 \implies x = -z
$$

Let $z = t$ be a parameter. The general solution is:

$$
x = -t, \quad y = 1 + t, \quad z = t
$$

---

## Q9. Consider a circuit with three mesh currents. The corresponding equations for the mesh currents $i_1$, $i_2$, and $i_3$ are: (07)

| | |
|---|---|
| **ID** | CT1M-1 |
| **Source** | CT1M Q1 [07 marks] |

**Answer:**

$$
2i_1 + 3i_2 - i_3 = 5
$$
$$
i_1 - 2i_2 + 4i_3 = 8
$$
$$
3i_1 + i_2 + 2i_3 = -3
$$
Solve this system of linear equations by reducing its augmented matrix to echelon form to find the mesh currents.

**Answer:**

First, we write the augmented matrix for this system:
$$
\begin{bmatrix}
2 & 3 & -1 & | & 5 \\
1 & -2 & 4 & | & 8 \\
3 & 1 & 2 & | & -3
\end{bmatrix}
$$

We swap the first and second rows to get a pivot of 1 in the top-left:
$$
\begin{bmatrix}
1 & -2 & 4 & | & 8 \\
2 & 3 & -1 & | & 5 \\
3 & 1 & 2 & | & -3
\end{bmatrix}
\quad (R_1 \leftrightarrow R_2)
$$

Now we make the elements below the first pivot zero. We apply two row operations:
$$
R_2 \to R_2 - 2R_1
$$
$$
R_3 \to R_3 - 3R_1
$$

This gives the following matrix:
$$
\begin{bmatrix}
1 & -2 & 4 & | & 8 \\
0 & 7 & -9 & | & -11 \\
0 & 7 & -10 & | & -27
\end{bmatrix}
$$

Next, we make the element below the second pivot zero. We subtract the second row from the third row:
$$
R_3 \to R_3 - R_2
$$

This gives:
$$
\begin{bmatrix}
1 & -2 & 4 & | & 8 \\
0 & 7 & -9 & | & -11 \\
0 & 0 & -1 & | & -16
\end{bmatrix}
$$

We multiply the third row by $-1$ to make the pivot positive:
$$
R_3 \to -R_3
$$
$$
\begin{bmatrix}
1 & -2 & 4 & | & 8 \\
0 & 7 & -9 & | & -11 \\
0 & 0 & 1 & | & 16
\end{bmatrix}
$$
This is the echelon form.

Now we use back substitution to find the currents.

From the third row:
$$
i_3 = 16
$$

From the second row:
$$
7i_2 - 9i_3 = -11
$$
$$
7i_2 - 9(16) = -11
$$
$$
7i_2 - 144 = -11
$$
$$
7i_2 = 133 \implies i_2 = 19
$$

From the first row:
$$
i_1 - 2i_2 + 4i_3 = 8
$$
$$
i_1 - 2(19) + 4(16) = 8
$$
$$
i_1 - 38 + 64 = 8
$$
$$
i_1 + 26 = 8 \implies i_1 = -18
$$

So, the mesh currents are $i_1 = -18$, $i_2 = 19$, and $i_3 = 16$.

---

## Q10. Find the value(s) of $k$ for which the following system of three linear equations in three variables has (i) a unique solution, (ii) no solution, and (iii) infinitely many solutions: (06)

| | |
|---|---|
| **ID** | CT1M-2 |
| **Source** | CT1M Q2 [06 marks] |

**Answer:**

$$
x + y + z = 3
$$
$$
2x + 3y + z = 7
$$
$$
3x + 5y + kz = 10
$$

**Answer:**

We write the augmented matrix for the system:
$$
\begin{bmatrix}
1 & 1 & 1 & | & 3 \\
2 & 3 & 1 & | & 7 \\
3 & 5 & k & | & 10
\end{bmatrix}
$$

We reduce the matrix to echelon form. First, we clear the first column below the pivot:
$$
R_2 \to R_2 - 2R_1
$$
$$
R_3 \to R_3 - 3R_1
$$

This gives:
$$
\begin{bmatrix}
1 & 1 & 1 & | & 3 \\
0 & 1 & -1 & | & 1 \\
0 & 2 & k - 3 & | & 1
\end{bmatrix}
$$

Next, we clear the second column below the pivot:
$$
R_3 \to R_3 - 2R_2
$$

This gives the echelon form:
$$
\begin{bmatrix}
1 & 1 & 1 & | & 3 \\
0 & 1 & -1 & | & 1 \\
0 & 0 & k - 1 & | & -1
\end{bmatrix}
$$

Now we analyze the solutions:

#### (i) Unique Solution
A unique solution exists when the rank of the coefficient matrix equals the number of variables. This means the third pivot must not be zero:
$$
k - 1 \neq 0 \implies k \neq 1
$$
So, the system has a unique solution for any value $k \neq 1$.

#### (ii) No Solution
No solution exists when the rank of the coefficient matrix is less than the rank of the augmented matrix. This happens when the last row has a zero coefficient for $z$ but a non-zero constant:
$$
k - 1 = 0 \implies k = 1
$$
When $k = 1$, the last row represents $0z = -1$, which is impossible. So, the system has no solution when $k = 1$.

#### (iii) Infinitely Many Solutions
Infinitely many solutions exist when the rank of the coefficient matrix equals the rank of the augmented matrix, and this rank is less than 3. This requires the entire last row to be all zeros.
However, the right-hand side of the last row is $-1$, which is never zero.
So, there is no value of $k$ that gives infinitely many solutions.

---

