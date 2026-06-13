# Lecture 06: Questions Consistency of System of Linear Equations

> **Series**: Matrix Theory
> **Lecture**: 06 of 09
> **Video**: https://www.youtube.com/watch?v=sV3-43kkvSo

---

**Navigation**
[< Previous Lecture](05_Consistency_of_Linear_Equations.md) | [Index](README.md) | [Next Lecture >](07_Concept_of_Eigen_Values_and_Vectors.md)

---

## Prerequisites
- Understanding of the conditions for consistency (Rouché-Capelli theorem).
- Proficiency in reducing augmented matrices to Echelon form.

---

## 1. Problem 1: Unique Solution

**Problem:** Test the consistency of the system of equations and solve if consistent:
$$
3x + y + 2z = 11
$$
$$
2x + 3y + z = 11
$$
$$
x + 2y + 3z = 14
$$

**Solution:**
**Augmented Matrix representation:**
$$
[A : B] = \left[ \begin{array}{ccc|c} 3 & 1 & 2 & 11 \\ 2 & 3 & 1 & 11 \\ 1 & 2 & 3 & 14 \end{array} \right]
$$

Swap $R_1 \leftrightarrow R_3$ to get a leading 1:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 2 & 3 & 14 \\ 2 & 3 & 1 & 11 \\ 3 & 1 & 2 & 11 \end{array} \right]
$$

Apply $R_2 \to R_2 - 2R_1$ and $R_3 \to R_3 - 3R_1$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 2 & 3 & 14 \\ 0 & -1 & -5 & -17 \\ 0 & -5 & -7 & -31 \end{array} \right]
$$

Apply $R_2 \to -R_2$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 2 & 3 & 14 \\ 0 & 1 & 5 & 17 \\ 0 & -5 & -7 & -31 \end{array} \right]
$$

Apply $R_3 \to R_3 + 5R_2$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 2 & 3 & 14 \\ 0 & 1 & 5 & 17 \\ 0 & 0 & 18 & 54 \end{array} \right]
$$

Apply $R_3 \to R_3 / 18$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 2 & 3 & 14 \\ 0 & 1 & 5 & 17 \\ 0 & 0 & 1 & 3 \end{array} \right]
$$

**Ranks and Solution:**
*   $\rho(A) = 3$ and $\rho([A:B]) = 3$.
*   Since $\rho(A) = \rho([A:B]) = 3$ (number of unknowns), the system is consistent and has a unique solution.

**Back Substitution:**
$$
z = 3
$$
$$
y + 5(3) = 17 \implies y = 2
$$
$$
x + 2(2) + 3(3) = 14 \implies x = 1
$$
**Unique Solution:** $x=1, y=2, z=3$.

---

## 2. Problem 2: 4 Equations, 3 Unknowns

**Problem:** Test the consistency of the system of equations and solve if consistent:
$$
x + 2y - z = 3
$$
$$
3x - y + 2z = 1
$$
$$
2x - 2y + 3z = 2
$$
$$
x - y + z = -1
$$

**Solution:**
**Augmented Matrix representation:**
$$
[A : B] = \left[ \begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 3 & -1 & 2 & 1 \\ 2 & -2 & 3 & 2 \\ 1 & -1 & 1 & -1 \end{array} \right]
$$

Apply $R_2 \to R_2 - 3R_1$, $R_3 \to R_3 - 2R_1$, and $R_4 \to R_4 - R_1$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & -7 & 5 & -8 \\ 0 & -6 & 5 & -4 \\ 0 & -3 & 2 & -4 \end{array} \right]
$$

*(Note: The lecturer warns against arithmetic mistakes here which can lead to falsely concluding the system is inconsistent. We follow the correct, robust path).*

Apply $R_2 \to -(R_2 - 2R_4)$ and $R_3 \to R_3 - 2R_4$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & 4 \\ 0 & -3 & 2 & -4 \end{array} \right]
$$

Apply $R_4 \to R_4 + 3R_2$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & 4 \\ 0 & 0 & -1 & -4 \end{array} \right]
$$

Apply $R_4 \to R_4 + R_3$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 0 & 1 & -1 & 0 \\ 0 & 0 & 1 & 4 \\ 0 & 0 & 0 & 0 \end{array} \right]
$$

**Ranks and Solution:**
*   Rank of $A$ is $\rho(A) = 3$, rank of $[A:B] = 3$.
*   Consistent system with a unique solution.

**Back Substitution:**
$$
z = 4
$$
$$
y - 4 = 0 \implies y = 4
$$
$$
x + 2(4) - 4 = 3 \implies x = -1
$$
**Unique Solution:** $x=-1, y=4, z=4$.

---

## 3. Problem 3: Infinitely Many Solutions

**Problem:** Test the consistency and solve:
$$
5x + 3y + 7z = 4
$$
$$
3x + 26y + 2z = 9
$$
$$
7x + 2y + 10z = 5
$$

**Solution:**
**Augmented Matrix representation:**
$$
[A : B] = \left[ \begin{array}{ccc|c} 5 & 3 & 7 & 4 \\ 3 & 26 & 2 & 9 \\ 7 & 2 & 10 & 5 \end{array} \right]
$$

Apply $R_1 \to 2R_2 - R_1$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 49 & -3 & 14 \\ 3 & 26 & 2 & 9 \\ 7 & 2 & 10 & 5 \end{array} \right]
$$

Apply $R_2 \to R_2 - 3R_1$ and $R_3 \to R_3 - 7R_1$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 49 & -3 & 14 \\ 0 & -121 & 11 & -33 \\ 0 & -341 & 31 & -93 \end{array} \right]
$$

Apply $R_2 \to -R_2 / 11$ and $R_3 \to -R_3 / 31$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 49 & -3 & 14 \\ 0 & 11 & -1 & 3 \\ 0 & 11 & -1 & 3 \end{array} \right]
$$

Apply $R_3 \to R_3 - R_2$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 49 & -3 & 14 \\ 0 & 11 & -1 & 3 \\ 0 & 0 & 0 & 0 \end{array} \right]
$$

**Ranks and Solution:**
*   $\rho(A) = \rho([A:B]) = 2 < 3$ (number of unknowns).
*   Consistent system with infinitely many solutions.

**Parametric Formulation:**
From $R_2$: $11y - z = 3$. Let $z = k$ (where $k \in \mathbb{R}$).
$$
y = \frac{k+3}{11}
$$

From $R_1$: $x + 49y - 3z = 14$.
$$
x = 14 - 49\left(\frac{k+3}{11}\right) + 3k \implies x = \frac{7-16k}{11}
$$
**Infinite Solutions:** $x = \frac{7-16k}{11}, y = \frac{k+3}{11}, z = k$.

---

## 4. Problem 4: Parameter Analysis ($\lambda, \mu$)

**Problem:** For what values of $\lambda$ and $\mu$ do the equations have: (i) no solution, (ii) a unique solution, (iii) infinitely many solutions?
$$
x + y + z = 6
$$
$$
x + 2y + 3z = 10
$$
$$
x + 2y + \lambda z = \mu
$$

**Solution:**
**Augmented Matrix representation:**
$$
[A : B] = \left[ \begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 1 & 2 & 3 & 10 \\ 1 & 2 & \lambda & \mu \end{array} \right]
$$

Apply $R_2 \to R_2 - R_1$ and $R_3 \to R_3 - R_1$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 1 & 2 & 4 \\ 0 & 1 & \lambda-1 & \mu-6 \end{array} \right]
$$

Apply $R_3 \to R_3 - R_2$:
$$
[A : B] \sim \left[ \begin{array}{ccc|c} 1 & 1 & 1 & 6 \\ 0 & 1 & 2 & 4 \\ 0 & 0 & \lambda-3 & \mu-10 \end{array} \right]
$$

**Consistency Analysis:**
1.  **Case 1: No Solution**
    Requires $\rho(A) \neq \rho([A:B])$. This happens if $\rho(A) = 2$ and $\rho([A:B]) = 3$.
    $$
    \lambda - 3 = 0 \implies \lambda = 3
    $$
    $$
    \mu - 10 \neq 0 \implies \mu \neq 10
    $$

2.  **Case 2: Unique Solution**
    Requires $\rho(A) = \rho([A:B]) = 3$.
    $$
    \lambda - 3 \neq 0 \implies \lambda \neq 3
    $$
    *$\mu$ can be any real value ($\mu \in \mathbb{R}$).*

3.  **Case 3: Infinitely Many Solutions**
    Requires $\rho(A) = \rho([A:B]) = 2 < 3$.
    $$
    \lambda - 3 = 0 \implies \lambda = 3
    $$
    $$
    \mu - 10 = 0 \implies \mu = 10
    $$

---

**Navigation**
[< Previous Lecture](05_Consistency_of_Linear_Equations.md) | [Index](README.md) | [Next Lecture >](07_Concept_of_Eigen_Values_and_Vectors.md)
