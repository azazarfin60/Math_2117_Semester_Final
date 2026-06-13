# Lecture 05: Consistency of System of Linear Equations

> **Series**: Matrix Theory
> **Lecture**: 05 of 09
> **Video**: https://www.youtube.com/watch?v=bAJLtUzhBQI

---

**Navigation**
[< Previous Lecture](04_Rank_by_Normal_Canonical_Form.md) | [Index](README.md) | [Next Lecture >](06_Questions_Consistency_of_Linear_Equations.md)

---

## Prerequisites
- Proficiency in calculating the rank of a matrix.
- Understanding of Echelon form reductions.

---

## 1. Recalling School Concepts: 2 Simultaneous Equations

Before generalizing to matrices, let's recall the algebraic conditions for a system of 2 simultaneous linear equations in two variables:

$$
a_1 x + b_1 y + c_1 = 0
$$

$$
a_2 x + b_2 y + c_2 = 0
$$

**Three Algebraic Conditions:**
*   **Case 1: Unique Solution** (Lines intersect)
    
    $$
    \frac{a_1}{a_2} \neq \frac{b_1}{b_2}
    $$

*   **Case 2: No Solution** (Lines are parallel)
    
    $$
    \frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}
    $$

*   **Case 3: Infinite Solutions** (Lines are coincident)
    
    $$
    \frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}
    $$

### Determinant Link for Case 1
The unique solution condition directly links to matrices. If we rearrange:

$$
\frac{a_1}{a_2} \neq \frac{b_1}{b_2} \implies a_1 b_2 - a_2 b_1 \neq 0
$$

This is the determinant of the coefficient matrix:

$$
\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix} \neq 0
$$

---

## 2. Terminology and System Representation

### Definitions
*   **Consistent System**: A system of equations having one or more valid solutions (i.e., it has either a unique solution or infinite solutions).
*   **Inconsistent System**: A system of equations having absolutely no solution.

### System of 3 Equations in 3 Variables
Consider the standard system:

$$
a_1 x + b_1 y + c_1 z = d_1
$$

$$
a_2 x + b_2 y + c_2 z = d_2
$$

$$
a_3 x + b_3 y + c_3 z = d_3
$$

This system can be written compactly in matrix form as $A X = B$:

$$
\begin{bmatrix} a_1 & b_1 & c_1 \\ a_2 & b_2 & c_2 \\ a_3 & b_3 & c_3 \end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} d_1 \\ d_2 \\ d_3 \end{bmatrix}
$$

*   **Homogeneous vs. Non-homogeneous**:
    *   **Non-homogeneous system**: When the constant matrix $B$ is not entirely zero ($B \neq O$). The system is $A X = B$.
    *   **Homogeneous system**: When the constant matrix $B$ is the zero matrix ($B = O$). The system is $A X = O$.

### The Augmented Matrix
The augmented matrix is formed by combining the coefficient matrix $A$ and the constant column matrix $B$, separated by a line:

$$
[A : B] = \left[ \begin{array}{ccc|c} a_1 & b_1 & c_1 & d_1 \\ a_2 & b_2 & c_2 & d_2 \\ a_3 & b_3 & c_3 & d_3 \end{array} \right]
$$

The order of this augmented matrix is $3 \times 4$.

---

## 3. Working Rule to Test Consistency ($A X = B$)

To test the consistency of a non-homogeneous system of linear equations using matrix rank, follow this procedure:

1.  Write the given system of equations in matrix form $A X = B$.
2.  Form the augmented matrix $[A : B]$.
3.  Transform the augmented matrix $[A : B]$ into **Echelon form** using row operations only.
4.  Find the rank of the coefficient matrix $A$, denoted as $\rho(A)$, and the rank of the augmented matrix $[A : B]$, denoted as $\rho([A : B])$.
5.  Apply the following criteria to conclude:
    *   **Case 3.1**: If $\rho(A) \neq \rho([A : B])$, the system is **Inconsistent** (No Solution).
    *   **Case 3.2**: If $\rho(A) = \rho([A : B])$, the system is **Consistent**.
        *   **Subcase 3.2 (a)**: If $\rho(A) = \rho([A : B]) = n$ (where $n$ is the total number of unknown variables), the system has a **Unique Solution**.
        *   **Subcase 3.2 (b)**: If $\rho(A) = \rho([A : B]) = r < n$, the system has **Infinite Solutions**. To solve it, we must choose $n - r$ variables arbitrarily.

---

## What Comes Next
The next lecture provides practical applications of this working rule. We will solve multiple numerical questions to test the consistency of different linear systems.

---

**Navigation**
[< Previous Lecture](04_Rank_by_Normal_Canonical_Form.md) | [Index](README.md) | [Next Lecture >](06_Questions_Consistency_of_Linear_Equations.md)
