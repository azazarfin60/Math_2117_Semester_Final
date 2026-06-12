# Basics of Matrix and Determinant

**Series**: Matrix Theory
**Lecture**: 01
**YouTube**: https://www.youtube.com/watch?v=2NRTmf4SrlI

---

**Navigation**
[Index](README.md) | [Next Lecture >](02_Rank_of_Matrix_Concept.md)

## Prerequisites
- Basic algebra and arithmetic operations.
- Familiarity with basic mathematical notations.

## Core Content

A matrix is a rectangular array of numbers arranged in rows and columns. Matrices provide a compact way to represent and work with linear transformations and systems of equations.

### Definition of a Matrix
An $m \times n$ matrix contains $m$ rows and $n$ columns. The elements are denoted by $a_{ij}$, representing the entry in the $i$-th row and $j$-th column.

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{bmatrix}
$$

### Types of Matrices
- **Square Matrix**: A matrix with an equal number of rows and columns ($m = n$).
- **Rectangular Matrix**: A matrix where the number of rows is not equal to the number of columns ($m \neq n$).
- **Diagonal Matrix**: A square matrix where all off-diagonal elements are zero.
- **Identity Matrix**: A diagonal matrix where all main diagonal elements are equal to $1$.

### Matrix Determinant
The determinant is a scalar value calculated from a square matrix. It provides important properties about the matrix, such as invertibility. A matrix with a non-zero determinant is non-singular and invertible.

For a $2 \times 2$ matrix:

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

The determinant is:

$$
\left| A \right| = ad - bc
$$

For a $3 \times 3$ matrix, expansion by minors along the first row gives:

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
$$

The determinant calculation follows:

$$
\left| A \right| = a_{11}(a_{22}a_{33} - a_{23}a_{32}) - a_{12}(a_{21}a_{33} - a_{23}a_{31}) + a_{13}(a_{21}a_{32} - a_{22}a_{31})
$$

### Matrix Operations
- **Addition**: Add corresponding elements of matrices of the same dimensions.
- **Scalar Multiplication**: Multiply every element of the matrix by a constant scalar.
- **Matrix Multiplication**: The sum of products of elements from rows of the first matrix and columns of the second matrix. This requires the number of columns in the first matrix to match the number of rows in the second.

## What Comes Next
The next lecture covers the concept of the rank of a matrix. We will define rank using minors and explore the concept of nullity.

---

**Navigation**
[Index](README.md) | [Next Lecture >](02_Rank_of_Matrix_Concept.md)
