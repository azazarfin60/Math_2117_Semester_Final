[⬅ CT-2 (Vector) Answer](CT2_Vector_answer.md) | [🏠 Index](00-index.md)

---

# Class Test-1 (Matrix) Answers — MATH-2117

---

### Q1. Consider a circuit with three mesh currents. The corresponding equations for the mesh currents $i\_1$, $i\_2$, and $i\_3$ are: (07)

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

So, the mesh currents are

$$
i_1 = -18, \quad i_2 = 19, \quad i_3 = 16
$$

.

---

### Q2. Find the value(s) of $k$ for which the following system of three linear equations in three variables has (i) a unique solution, (ii) no solution, and (iii) infinitely many solutions: (06)

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

### Q3. What is meant by the rank of a matrix? Reduce the matrix

$$
A = \begin{bmatrix}
6 & 3 & -4 \\
-4 & 1 & -6 \\
1 & 2 & -5
\end{bmatrix}
$$

(07)
*   **(i)** to echelon form
*   **(ii)** to row canonical form, and
*   **(iii)** determine the rank of the matrix.

**Answer:**

#### 1. Definition of Rank
The rank of a matrix is the maximum number of linearly independent rows in the matrix. It also equals the number of non-zero rows in its row echelon form.

#### 2. Reduce to Echelon Form
Let the matrix be:

$$
A = \begin{bmatrix}
6 & 3 & -4 \\
-4 & 1 & -6 \\
1 & 2 & -5
\end{bmatrix}
$$

We swap the first and third rows to put a 1 in the top-left corner:

$$
\begin{bmatrix}
1 & 2 & -5 \\
-4 & 1 & -6 \\
6 & 3 & -4
\end{bmatrix}
\quad (R_1 \leftrightarrow R_3)
$$

Now we clear the first column:

$$
R_2 \to R_2 + 4R_1
$$

$$
R_3 \to R_3 - 6R_1
$$

$$
\begin{bmatrix}
1 & 2 & -5 \\
0 & 9 & -26 \\
0 & -9 & 26
\end{bmatrix}
$$

Next, we eliminate the second element in the third row:

$$
R_3 \to R_3 + R_2
$$

$$
\begin{bmatrix}
1 & 2 & -5 \\
0 & 9 & -26 \\
0 & 0 & 0
\end{bmatrix}
$$

We divide the second row by 9 to get a leading 1:

$$
R_2 \to \frac{1}{9} R_2
$$

$$
\begin{bmatrix}
1 & 2 & -5 \\
0 & 1 & -\frac{26}{9} \\
0 & 0 & 0
\end{bmatrix}
$$

This is the echelon form of the matrix.

#### 3. Reduce to Row Canonical Form
Starting from the echelon form:

$$
\begin{bmatrix}
1 & 2 & -5 \\
0 & 1 & -\frac{26}{9} \\
0 & 0 & 0
\end{bmatrix}
$$

We eliminate the element above the leading 1 in the second row:

$$
R_1 \to R_1 - 2R_2
$$

$$
R_1 \to \begin{bmatrix}
1 & 2 - 2(1) & -5 - 2\left(-\frac{26}{9}\right)
\end{bmatrix} = \begin{bmatrix}
1 & 0 & -5 + \frac{52}{9}
\end{bmatrix} = \begin{bmatrix}
1 & 0 & \frac{7}{9}
\end{bmatrix}
$$

This gives the row canonical form:

$$
\begin{bmatrix}
1 & 0 & \frac{7}{9} \\
0 & 1 & -\frac{26}{9} \\
0 & 0 & 0
\end{bmatrix}
$$

#### 4. Determine the Rank
The row echelon form has two non-zero rows. So, the rank of the matrix $A$ is 2.

---

[⬅ CT-2 (Vector) Answer](CT2_Vector_answer.md) | [🏠 Index](00-index.md)