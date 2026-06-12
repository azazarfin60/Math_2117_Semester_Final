# Rank of Matrix A Concept

**Series**: Matrix Theory
**Lecture**: 02
**YouTube**: https://www.youtube.com/watch?v=h1FgjMdIEJ0

---

**Navigation**
[< Previous Lecture](01_Basics_of_Matrix_and_Determinant.md) | [Index](README.md) | [Next Lecture >](03_Rank_by_Determinant_and_Echelon_Form.md)

## Prerequisites
- Understanding of square matrices and determinants.
- Familiarity with expansion of determinants by minors.

## Core Content

The rank of a matrix is a fundamental property that provides insight into the linear independence of its rows and columns. It is central to solving systems of linear equations.

### Definition of a Minor
Consider an $m \times n$ matrix $A$. If we retain any $r$ rows and $r$ columns from $A$ and delete the rest, the determinant of the resulting $r \times r$ submatrix is called a minor of $A$ of order $r$.

### Definition of Rank
The rank of a matrix $A$ is denoted by $\rho(A)$. A number $r$ is the rank of matrix $A$ if it satisfies two conditions:
1. There exists at least one non-zero minor of order $r$.
2. Every minor of order greater than $r$ is equal to zero.

If $A$ is a non-zero matrix, then its rank is at least $1$. The rank of a zero matrix is defined as $0$.

### Finding Rank using Minors
To find the rank of a matrix using the minor method, follow these steps:
1. Start with the highest possible order of a square submatrix.
2. Calculate the determinant (minor) of this submatrix.
3. If the determinant is non-zero, the rank is the order of this submatrix.
4. If all minors of this highest order are zero, step down to the next lower order and check its minors.
5. The rank is the order of the highest order non-zero minor.

### Nullity
The nullity of a square matrix of order $n$ is defined as the difference between its order and its rank.

$$
N(A) = n - \rho(A)
$$

Nullity represents the dimension of the null space of the matrix.

## What Comes Next
The minor method can be tedious for large matrices. The next lecture introduces alternative, more efficient methods for calculating the rank of a matrix, including the determinant method and Echelon form.

---

**Navigation**
[< Previous Lecture](01_Basics_of_Matrix_and_Determinant.md) | [Index](README.md) | [Next Lecture >](03_Rank_by_Determinant_and_Echelon_Form.md)
