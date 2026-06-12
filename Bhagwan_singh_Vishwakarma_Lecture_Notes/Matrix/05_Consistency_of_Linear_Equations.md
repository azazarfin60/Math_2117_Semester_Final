# Consistency of System of Linear Equations

**Series**: Matrix Theory
**Lecture**: 05
**YouTube**: https://www.youtube.com/watch?v=bAJLtUzhBQI

---

**Navigation**
[< Previous Lecture](04_Rank_by_Normal_Canonical_Form.md) | [Index](README.md) | [Next Lecture >](06_Questions_Consistency_of_Linear_Equations.md)

## Prerequisites
- Proficiency in calculating the rank of a matrix.
- Understanding of Echelon form reductions.

## Core Content

A system of linear equations is a collection of one or more linear equations involving the same set of variables. We use matrix theory to determine whether a system has a solution (consistent) or no solution (inconsistent).

### System Representation
Consider a system of $m$ non-homogeneous linear equations with $n$ variables $x_1, x_2, \dots, x_n$:

$$
a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n = b_1
$$

$$
a_{21}x_1 + a_{22}x_2 + \dots + a_{2n}x_n = b_2
$$

$$
\vdots
$$

$$
a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n = b_m
$$

This system can be written in matrix form as $AX = B$:

$$
\begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{bmatrix}
$$

Where:
- $A$ is the coefficient matrix.
- $X$ is the column vector of variables.
- $B$ is the column vector of constants.

### The Augmented Matrix
The augmented matrix $[A:B]$ is formed by appending the constant vector $B$ as an additional column to the coefficient matrix $A$.

$$
[A:B] = \left[ \begin{array}{cccc|c} a_{11} & a_{12} & \dots & a_{1n} & b_1 \\ a_{21} & a_{22} & \dots & a_{2n} & b_2 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} & b_m \end{array} \right]
$$

### Conditions for Consistency (Rouché-Capelli Theorem)
To analyze consistency, we reduce the augmented matrix $[A:B]$ to Echelon form and determine the rank of the coefficient matrix $\rho(A)$ and the rank of the augmented matrix $\rho([A:B])$.

There are three possible outcomes:
1. **Inconsistent System (No Solution)**: If $\rho(A) \neq \rho([A:B])$. The system has no valid solution.
2. **Consistent System (Unique Solution)**: If $\rho(A) = \rho([A:B]) = n$, where $n$ is the number of variables. The system yields exactly one unique solution for each variable.
3. **Consistent System (Infinite Solutions)**: If $\rho(A) = \rho([A:B]) = r < n$. The system has infinitely many solutions. We must choose $n - r$ variables arbitrarily as free parameters (e.g., $k_1, k_2$) and solve for the remaining variables in terms of these parameters.

## What Comes Next
The next lecture provides practical applications of this working rule. We will solve multiple numerical questions to test the consistency of different linear systems.

---

**Navigation**
[< Previous Lecture](04_Rank_by_Normal_Canonical_Form.md) | [Index](README.md) | [Next Lecture >](06_Questions_Consistency_of_Linear_Equations.md)
