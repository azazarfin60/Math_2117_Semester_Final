[← Previous: B04 Matrix Proofs](B04_Matrix_Proofs.md) | [Index](00_Index.md) | [Next: B06 Normal Canonical Form →](B06_Normal_Canonical_Form.md)

---

# B05: Row Echelon Form and Rank of a Matrix

> **Exam Weight**: Tier 1 | **Appeared in**: 2017, 2018, 2019, 2020, 2021, 2023, 2024 (all 7 papers) + CT | **Typical Marks**: 3–6

This topic has appeared in every single exam paper. It is the most consistent topic in the entire course. You cannot afford to skip it.

---

## What is the Rank of a Matrix?

### Definition

The rank of a matrix $A$ is the maximum number of linearly independent row vectors in it. It also equals the maximum number of linearly independent column vectors. We write it as $\rho(A)$ or $\text{rank}(A)$.

### Key Idea

Think of rank as "how many rows actually carry new information." Some rows in a matrix might just be multiples or combinations of other rows. Those rows add no new information. The rank counts only the rows that are truly independent from each other.

A zero matrix has rank 0. A non-zero matrix has rank at least 1.

For an $m \times n$ matrix, the rank can be at most $\min(m, n)$. So a $3 \times 4$ matrix has rank at most 3. A $4 \times 3$ matrix also has rank at most 3.

### Why Rank Matters

Rank shows up everywhere in this course:
- It decides if a system of equations has a solution (rank conditions)
- It tells you the dimension of the column space and row space
- It connects to the number of free variables in a system
- It is the order of the largest non-zero minor

---

## Elementary Row Operations

Before we find rank, we need row operations. These are tools that change a matrix into a simpler form without changing its rank.

Three types of elementary row operations exist:

1. **Swap two rows**: $R_i \leftrightarrow R_j$
2. **Multiply a row by a non-zero scalar**: $R_i \to kR_i$ where $k \neq 0$
3. **Add a scalar multiple of one row to another**: $R_i \to R_i + kR_j$

Two matrices are called **equivalent** (written $A \sim B$) if one can be reached from the other through row operations. Equivalent matrices always have the same rank.

---

## Row Echelon Form

### Definition

A matrix is in row echelon form if it satisfies these three rules:

1. All zero rows are at the bottom.
2. The first non-zero entry in each row (called the **pivot**) is strictly to the right of the pivot in the row above it.
3. All entries below each pivot are zero.

### Example of Echelon Form

This matrix is in echelon form:

$$
\begin{bmatrix}
1 & 2 & 3 & 4 \\
0 & 1 & 2 & 3 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

Notice how the pivots (the leading 1s) staircase to the right. The zero row sits at the bottom.

This matrix is NOT in echelon form:

$$
\begin{bmatrix}
1 & 0 & 1 & 1 \\
0 & 1 & 1 & 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 2
\end{bmatrix}
$$

The zero row is not at the bottom. The last row's pivot is not to the right of the row above it.

---

## Finding Rank by Echelon Form

### The Method

1. Use elementary row operations to convert the matrix to echelon form.
2. Count the number of non-zero rows.
3. That count is the rank.

This is the fastest and most exam-friendly method for finding rank. Every exam question on rank uses this approach.

### Worked Example 1: Rank of a 3x4 Matrix

**Problem**: Find the rank of the matrix (PYQ 2020):

$$
A =
\begin{bmatrix}
6 & 1 & 8 & 3 \\
2 & 1 & 0 & 2 \\
4 & -1 & -8 & -3
\end{bmatrix}
$$

**Solution**:

Swap $R_1$ and $R_2$ to get a small leading entry:

$$
\begin{bmatrix}
2 & 1 & 0 & 2 \\
6 & 1 & 8 & 3 \\
4 & -1 & -8 & -3
\end{bmatrix}
$$

Clear the first column. Apply $R_2 \to R_2 - 3R_1$ and $R_3 \to R_3 - 2R_1$:

$$
\begin{bmatrix}
2 & 1 & 0 & 2 \\
0 & -2 & 8 & -3 \\
0 & -3 & -8 & -7
\end{bmatrix}
$$

Clear the second column in row 3. Apply $R_3 \to 2R_3 - 3R_2$:

$$
\begin{bmatrix}
2 & 1 & 0 & 2 \\
0 & -2 & 8 & -3 \\
0 & 0 & -40 & -5
\end{bmatrix}
$$

All three rows are non-zero. So:

$$
\rho(A) = 3
$$

---

### Worked Example 2: Rank of a 4x4 Matrix

**Problem**: Find the rank of the matrix (PYQ 2018):

$$
A =
\begin{pmatrix}
1 & -2 & 1 & -1 \\
1 & 1 & -2 & 3 \\
4 & 1 & -5 & 8 \\
5 & -7 & 2 & -1
\end{pmatrix}
$$

**Solution**:

Clear the first column. Apply $R_2 \to R_2 - R_1$, $R_3 \to R_3 - 4R_1$, $R_4 \to R_4 - 5R_1$:

$$
\begin{pmatrix}
1 & -2 & 1 & -1 \\
0 & 3 & -3 & 4 \\
0 & 9 & -9 & 12 \\
0 & 3 & -3 & 4
\end{pmatrix}
$$

Clear the second column. Apply $R_3 \to R_3 - 3R_2$ and $R_4 \to R_4 - R_2$:

$$
\begin{pmatrix}
1 & -2 & 1 & -1 \\
0 & 3 & -3 & 4 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

Two non-zero rows remain. So:

$$
\rho(A) = 2
$$

Notice that rows 3 and 4 were multiples of row 2 after the first set of operations. So they carried no new information.

---

### Worked Example 3: Rank of a 4x5 Matrix

**Problem**: Find the rank of the matrix (PYQ 2017):

$$
A =
\begin{bmatrix}
0 & 0 & 1 & -3 & -2 \\
0 & 1 & 2 & 6 & 0 \\
0 & 2 & 3 & 9 & 2 \\
0 & 1 & 1 & 3 & 2
\end{bmatrix}
$$

**Solution**:

The first column is all zeros. Swap $R_1 \leftrightarrow R_2$ to put a non-zero entry first:

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & -3 & -2 \\
0 & 2 & 3 & 9 & 2 \\
0 & 1 & 1 & 3 & 2
\end{bmatrix}
$$

Clear below the first pivot. Apply $R_3 \to R_3 - 2R_1$ and $R_4 \to R_4 - R_1$:

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & -3 & -2 \\
0 & 0 & -1 & -3 & 2 \\
0 & 0 & -1 & -3 & 2
\end{bmatrix}
$$

Clear below the second pivot. Apply $R_3 \to R_3 + R_2$ and $R_4 \to R_4 + R_2$:

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & -3 & -2 \\
0 & 0 & 0 & -6 & 0 \\
0 & 0 & 0 & -6 & 0
\end{bmatrix}
$$

Apply $R_4 \to R_4 - R_3$:

$$
\begin{bmatrix}
0 & 1 & 2 & 6 & 0 \\
0 & 0 & 1 & -3 & -2 \\
0 & 0 & 0 & -6 & 0 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

Three non-zero rows remain. So:

$$
\rho(A) = 3
$$

---

## Finding Rank by Minor Method

### Definition of a Minor

Take any $r$ rows and $r$ columns from an $m \times n$ matrix. The determinant of the resulting $r \times r$ submatrix is a minor of order $r$.

### The Method

1. Start with the highest possible order of a square submatrix.
2. Compute its determinant. If it is non-zero, the rank equals this order.
3. If all minors of that order are zero, drop down one order and check again.
4. The rank is the order of the largest non-zero minor.

### When to Use This

The minor method is slower than echelon form for large matrices. But it is useful for small matrices or when the problem specifically asks for "rank by minors." In exams, the echelon method is almost always preferred.

### Worked Example: Minor Method

**Problem**: Find the rank of:

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
2 & 3 & 4 \\
3 & 4 & 5
\end{bmatrix}
$$

**Solution**:

The matrix is $3 \times 3$. Start by checking if the full $3 \times 3$ determinant is non-zero:

$$
|A| = 1(15 - 16) - 2(10 - 12) + 3(8 - 9) = -1 + 4 - 3 = 0
$$

The $3 \times 3$ minor is zero. So rank is not 3.

Check a $2 \times 2$ minor. Take the top-left $2 \times 2$ submatrix:

$$
\begin{vmatrix}
1 & 2 \\
2 & 3
\end{vmatrix} = 3 - 4 = -1 \neq 0
$$

A non-zero $2 \times 2$ minor exists. So:

$$
\rho(A) = 2
$$

---

## Nullity

### Definition

For a square matrix of order $n$, the nullity is defined as:

$$
N(A) = n - \rho(A)
$$

Nullity tells you the dimension of the null space (the set of all solutions to $AX = 0$). It equals the number of free variables in the system.

### Example

If $A$ is a $4 \times 4$ matrix with $\rho(A) = 3$, then:

$$
N(A) = 4 - 3 = 1
$$

This means the system $AX = 0$ has one free variable and its solution space is one-dimensional.

---

## Important Properties of Rank

1. $\rho(A) = 0$ if and only if $A$ is the zero matrix.
2. For an $m \times n$ matrix, $\rho(A) \leq \min(m, n)$.
3.

$$
\rho(A) = \rho(A^T)
$$

. Row rank equals column rank.
4. Row operations do not change the rank.
5. If $A$ is an $n \times n$ matrix, then $\rho(A) = n$ if and only if $A$ is invertible (non-singular).
6. If $\rho(A) < n$ for a square matrix of order $n$, then

$$
\lvert A \rvert = 0.
$$

---

## Exam Patterns

- **Every paper asks rank.** The typical phrasing is: "Define rank of a matrix. Find the rank of..." This gives you 2 marks for the definition and 3–4 marks for the computation.
- Matrices in exams are usually $3 \times 4$, $4 \times 4$, or $4 \times 5$.
- The definition they expect is: "The rank of a matrix is the number of non-zero rows in its row echelon form" or "the maximum number of linearly independent rows."
- Always swap rows first to get a 1 (or the smallest non-zero number) in the top-left corner. This makes arithmetic easier.
- Watch for rows that become identical during reduction. They collapse to zeros and lower the rank.

---

## Must-Know Problems

### Problem 4: Rank of a 4x4 Matrix (PYQ 2024)

**Question**: Define rank. Find the rank of:

$$
A =
\begin{bmatrix}
1 & 1 & 1 & 1 \\
1 & 3 & -2 & 1 \\
2 & 0 & -3 & 2 \\
3 & 3 & -3 & 3
\end{bmatrix}
$$

**Solution**:

Apply $R_2 \to R_2 - R_1$, $R_3 \to R_3 - 2R_1$, $R_4 \to R_4 - 3R_1$:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 2 & -3 & 0 \\
0 & -2 & -5 & 0 \\
0 & 0 & -6 & 0
\end{bmatrix}
$$

Apply $R_3 \to R_3 + R_2$:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 2 & -3 & 0 \\
0 & 0 & -8 & 0 \\
0 & 0 & -6 & 0
\end{bmatrix}
$$

Apply $R_4 \to 4R_4 - 3R_3$:

$$
\begin{bmatrix}
1 & 1 & 1 & 1 \\
0 & 2 & -3 & 0 \\
0 & 0 & -8 & 0 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

Three non-zero rows. So $\rho(A) = 3$.

---

### Problem 5: Rank of a 3x4 Matrix (PYQ 2023)

**Question**: Find the rank of:

$$
A =
\begin{bmatrix}
1 & 2 & 3 & 2 \\
2 & 3 & 5 & 1 \\
1 & 3 & 4 & 5
\end{bmatrix}
$$

**Solution**:

Apply $R_2 \to R_2 - 2R_1$ and $R_3 \to R_3 - R_1$:

$$
\begin{bmatrix}
1 & 2 & 3 & 2 \\
0 & -1 & -1 & -3 \\
0 & 1 & 1 & 3
\end{bmatrix}
$$

Apply $R_3 \to R_3 + R_2$:

$$
\begin{bmatrix}
1 & 2 & 3 & 2 \\
0 & -1 & -1 & -3 \\
0 & 0 & 0 & 0
\end{bmatrix}
$$

Two non-zero rows. So $\rho(A) = 2$.

---

### Problem 6: Echelon Form and Canonical Form (CT)

**Question**: Find the echelon form, row canonical form, and rank of:

$$
A =
\begin{bmatrix}
6 & 3 & -4 \\
-4 & 1 & -6 \\
1 & 2 & -5
\end{bmatrix}
$$

**Solution**:

**Step 1: Echelon form.**

Swap $R_1 \leftrightarrow R_3$:

$$
\begin{bmatrix}
1 & 2 & -5 \\
-4 & 1 & -6 \\
6 & 3 & -4
\end{bmatrix}
$$

Apply $R_2 \to R_2 + 4R_1$ and $R_3 \to R_3 - 6R_1$:

$$
\begin{bmatrix}
1 & 2 & -5 \\
0 & 9 & -26 \\
0 & -9 & 26
\end{bmatrix}
$$

Apply $R_3 \to R_3 + R_2$:

$$
\begin{bmatrix}
1 & 2 & -5 \\
0 & 9 & -26 \\
0 & 0 & 0
\end{bmatrix}
$$

Scale

$$
R_2 \to \frac{1}{9}R_2:
$$

$$
\begin{bmatrix}
1 & 2 & -5 \\
0 & 1 & -\frac{26}{9} \\
0 & 0 & 0
\end{bmatrix}
$$

This is the echelon form.

**Step 2: Row canonical form.**

Clear above the second pivot. Apply $R_1 \to R_1 - 2R_2$:

$$
R_1 = \begin{bmatrix} 1 & 0 & -5 + \frac{52}{9} \end{bmatrix} = \begin{bmatrix} 1 & 0 & \frac{7}{9} \end{bmatrix}
$$

The row canonical form is:

$$
\begin{bmatrix}
1 & 0 & \frac{7}{9} \\
0 & 1 & -\frac{26}{9} \\
0 & 0 & 0
\end{bmatrix}
$$

**Step 3: Rank.**

Two non-zero rows in echelon form. So $\rho(A) = 2$.

---

[← Previous: B04 Matrix Proofs](B04_Matrix_Proofs.md) | [Index](00_Index.md) | [Next: B06 Normal Canonical Form →](B06_Normal_Canonical_Form.md)
