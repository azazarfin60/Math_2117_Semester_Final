# Questions Consistency of System of Linear Equations

**Series**: Matrix Theory
**Lecture**: 06
**YouTube**: https://www.youtube.com/watch?v=sV3-43kkvSo

---

**Navigation**
[< Previous Lecture](05_Consistency_of_Linear_Equations.md) | [Index](README.md) | [Next Lecture >](07_Concept_of_Eigen_Values_and_Vectors.md)

## Prerequisites
- Understanding of the conditions for consistency (Rouché-Capelli theorem).
- Proficiency in reducing augmented matrices to Echelon form.

## Core Content

This lecture applies the consistency rules to solve practical systems of non-homogeneous linear equations.

### Problem Solving Approach
1. Form the augmented matrix $[A:B]$ from the given system $AX = B$.
2. Apply elementary row operations to reduce $[A:B]$ to Echelon form.
3. Compare the rank of the coefficient matrix $\rho(A)$ with the rank of the augmented matrix $\rho([A:B])$.
4. Conclude the nature of the solution (unique, infinite, or none) based on the ranks and the number of variables $n$.
5. If consistent, perform back-substitution from the Echelon form equations to find the variable values.

### Solved Problem: Unique Solution
Test the consistency and solve:

$$
3x + y + 2z = 11
$$

$$
2x + 3y + z = 11
$$

$$
x + 2y + 3z = 14
$$

The augmented matrix is:

$$
[A:B] = \left[ \begin{array}{ccc|c} 3 & 1 & 2 & 11 \\ 2 & 3 & 1 & 11 \\ 1 & 2 & 3 & 14 \end{array} \right]
$$

After interchanging $R_1 \leftrightarrow R_3$ to bring $1$ to the pivot and performing row reductions to Echelon form:

$$
[A:B] \sim \left[ \begin{array}{ccc|c} 1 & 2 & 3 & 14 \\ 0 & 1 & 5 & 17 \\ 0 & 0 & 1 & 3 \end{array} \right]
$$

Here, $\rho(A) = 3$ and $\rho([A:B]) = 3$. The number of variables is $n = 3$.
Since $\rho(A) = \rho([A:B]) = 3$, the system is consistent with a unique solution.

By back-substitution:

$$
z = 3
$$

$$
y + 5(3) = 17 \implies y = 2
$$

$$
x + 2(2) + 3(3) = 14 \implies x = 1
$$

The unique solution is $x=1, y=2, z=3$.

### Solved Problem: Infinite Solutions
Test the consistency and solve:

$$
5x + 3y + 7z = 4
$$

$$
3x + 26y + 2z = 9
$$

$$
7x + 2y + 10z = 5
$$

The augmented matrix is:

$$
[A:B] = \left[ \begin{array}{ccc|c} 5 & 3 & 7 & 4 \\ 3 & 26 & 2 & 9 \\ 7 & 2 & 10 & 5 \end{array} \right]
$$

Reducing to Echelon form yields:

$$
[A:B] \sim \left[ \begin{array}{ccc|c} 1 & 49 & -3 & 14 \\ 0 & 11 & -1 & 3 \\ 0 & 0 & 0 & 0 \end{array} \right]
$$

Here, $\rho(A) = 2$ and $\rho([A:B]) = 2$.
Since $\rho(A) = \rho([A:B]) = 2 < 3$ (number of variables), the system has infinitely many solutions.
We choose $3 - 2 = 1$ arbitrary variable. Let $z = k$.

$$
11y - k = 3 \implies y = \frac{k+3}{11}
$$

Substituting back into the first row gives

$$
x = \frac{7-16k}{11}.
$$

## What Comes Next
The next lecture introduces the concept of Eigenvalues and Eigenvectors, transitioning from systems of linear equations to advanced matrix transformations.

---

**Navigation**
[< Previous Lecture](05_Consistency_of_Linear_Equations.md) | [Index](README.md) | [Next Lecture >](07_Concept_of_Eigen_Values_and_Vectors.md)
