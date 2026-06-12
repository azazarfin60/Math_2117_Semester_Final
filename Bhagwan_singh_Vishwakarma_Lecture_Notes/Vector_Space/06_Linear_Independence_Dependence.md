# Lecture 06: Vector Space - Linear Independence and Dependence of Vectors

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 06 of 27
> **Video**: https://www.youtube.com/watch?v=9WjuLvPT_2A

---

**Navigation**
[< Previous Lecture](05_Linear_Sum_Direct_Sum_Span.md) | [Index](README.md) | [Next Lecture >](07_Basis_Finite_Dimensional.md)


---

## Prerequisites
We know how to form a linear combination of vectors: $a_1\alpha_1 + a_2\alpha_2 + \dots + a_n\alpha_n$. Today, we will ask a specific question: what happens if we set this combination equal to the zero vector? The answer tells us whether the vectors are independent or dependent.

---

## Definitions

Let $V(F)$ be a vector space. Let $S = \lbrace \alpha_1, \alpha_2, \dots, \alpha_n \rbrace$ be a finite set of vectors in $V(F)$.
We form their linear combination and set it equal to the zero vector:

$$
a_1\alpha_1 + a_2\alpha_2 + \cdots + a_n\alpha_n = \bar{0}
$$

where $a_1, a_2, \dots, a_n \in F$ are scalars.

### Linearly Independent (L.I.)
If the **only** way to satisfy this equation is for all the scalars to be zero:

$$
a_1 = 0, a_2 = 0, \ldots, a_n = 0
$$

then the vectors $\alpha_1, \alpha_2, \dots, \alpha_n$ are said to be **Linearly Independent**.
This means none of the vectors can be built using the others. They are completely unique directions in the space.

### Linearly Dependent (L.D.)
If there is at least one scalar $a_i \neq 0$ that satisfies the equation:

$$
a_1\alpha_1 + a_2\alpha_2 + \cdots + a_n\alpha_n = \bar{0}
$$

then the vectors are called **Linearly Dependent**.
This means at least one vector is redundant. It can be formed by mixing the other vectors together.

---

## Theorem: Dependence Means Scalar Multiples
We can prove exactly what it means to be linearly dependent with a simple theorem.

**Theorem:** If two vectors are linearly dependent, then one can be represented as a scalar multiple of the other.

**Proof:**
Let $\alpha, \beta \in V(F)$ be two linearly dependent vectors.
By the definition of linear dependence, there exist scalars $a, b \in F$, which are **not both zero**, such that:

$$
a\alpha + b\beta = \bar{0}
$$

Since at least one scalar is not zero, let us check the cases.

**Case 1: If $a \neq 0$**
We can divide by $a$ because it is non-zero.
Move the $\beta$ term to the right side:

$$
a\alpha = -b\beta
$$

Divide by $a$:

$$
\alpha = -\left(\frac{b}{a}\right)\beta
$$

Here, $\alpha$ is represented as a scalar multiple of $\beta$.

**Case 2: If $b \neq 0$**
We can divide by $b$.
Move the $\alpha$ term to the right side:

$$
b\beta = -a\alpha
$$

Divide by $b$:

$$
\beta = -\left(\frac{a}{b}\right)\alpha
$$

Here, $\beta$ is represented as a scalar multiple of $\alpha$.

In both cases, one vector is just a scaled version of the other. The theorem is proven.

---

## How to Test for Independence (Numerical Methods)

When you are given actual vectors with numbers, you must determine if they are L.I. or L.D. You can do this by solving equations directly, or by using a matrix determinant.

### Method 1: Solving Equations
**Question:** Check if the vectors are L.I. or L.D. in $V_3(\mathbb{R})$:

$$
\alpha_1 = (1, 2, 3), \quad \alpha_2 = (1, 0, 0), \quad \alpha_3 = (0, 1, 0), \quad \alpha_4 = (0, 0, 1)
$$

**Solution:**
Set up the linear combination with scalars $a_1, a_2, a_3, a_4 \in \mathbb{R}$:

$$
a_1\alpha_1 + a_2\alpha_2 + a_3\alpha_3 + a_4\alpha_4 = \bar{0}
$$

Substitute the vectors:

$$
a_1(1, 2, 3) + a_2(1, 0, 0) + a_3(0, 1, 0) + a_4(0, 0, 1) = (0, 0, 0)
$$

Multiply the scalars and add the components:

$$
(a_1 + a_2, 2a_1 + a_3, 3a_1 + a_4) = (0, 0, 0)
$$

Compare components to get three equations:

$$
a_1 + a_2 = 0 \implies a_2 = -a_1
$$

$$
2a_1 + a_3 = 0 \implies a_3 = -2a_1
$$

$$
3a_1 + a_4 = 0 \implies a_4 = -3a_1
$$

Can we find a non-zero solution? Let us assume $a_1 = 1$.
Then we get $a_2 = -1$, $a_3 = -2$, and $a_4 = -3$.
Since we found a valid solution where the scalars are not zero, the vectors are **Linearly Dependent**.

### Method 2: The Determinant and Rank Method
When you have the same number of vectors as dimensions (e.g., three vectors in 3D space), you can use a matrix determinant.

**Question:** Check if the vectors are L.I. or L.D. in $V_3(\mathbb{R})$:

$$
\alpha_1 = (2, 3, -1), \quad \alpha_2 = (-1, 4, -2), \quad \alpha_3 = (1, 18, -4)
$$

**Solution:**
Set up the combination:

$$
a_1(2, 3, -1) + a_2(-1, 4, -2) + a_3(1, 18, -4) = (0, 0, 0)
$$

This gives us a system of homogeneous equations:

$$
2a_1 - a_2 + a_3 = 0
$$

$$
3a_1 + 4a_2 + 18a_3 = 0
$$

$$
-a_1 - 2a_2 - 4a_3 = 0
$$

We build the coefficient matrix $A$:

$$
A = \begin{bmatrix} 2 & -1 & 1 \\ 3 & 4 & 18 \\ -1 & -2 & -4 \end{bmatrix}
$$

Calculate the determinant $\lvert A \rvert$:

$$
|A| = 2(4(-4) - 18(-2)) - (-1)(3(-4) - 18(-1)) + 1(3(-2) - 4(-1))
$$

$$
|A| = 2(-16 + 36) + 1(-12 + 18) + 1(-6 + 4)
$$

$$
|A| = 2(20) + 1(6) + 1(-2) = 40 + 6 - 2 = 44
$$

Because the determinant is not zero ($\lvert A \rvert = 44 \neq 0$), the rank of the matrix is 3.
When the rank equals the number of variables, the only solution to the homogeneous system is the trivial solution ($a_1 = 0, a_2 = 0, a_3 = 0$).
Therefore, the vectors are **Linearly Independent**.

*   If $\lvert A \rvert \neq 0 \implies \text{Rank} = 3 \implies \text{Linearly Independent}$
*   If $\lvert A \rvert = 0 \implies \text{Rank} < 3 \implies \text{Linearly Dependent}$

---

## Key Takeaways
*   **Linearly Independent (L.I.)**: The combination $a_i\alpha_i = \bar{0}$ is only solved by all zeros.
*   **Linearly Dependent (L.D.)**: The combination can be solved with non-zero scalars.
*   L.D. means vectors are redundant and can be written as multiples or combinations of each other.
*   For square systems, check the determinant. Non-zero means independent; zero means dependent.

## What Comes Next
We will soon use the concepts of linear independence and span to define the "Basis" of a vector space, which is the minimal set of vectors needed to build the entire space.

---

**Navigation**
[< Previous Lecture](05_Linear_Sum_Direct_Sum_Span.md) | [Index](README.md) | [Next Lecture >](07_Basis_Finite_Dimensional.md)
