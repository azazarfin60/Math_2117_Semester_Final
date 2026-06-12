# Lecture 19: Vector Space - Matrix Representation of Linear Transformation

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 19 of 27
> **Video**: https://www.youtube.com/watch?v=NCsoLIlz_lU

---

**Navigation**
[< Previous Lecture](18_Fundamental_Theorem_Homomorphism.md) | [Index](README.md) | [Next Lecture >](20_Inverse_Linear_Transformation.md)

---

## Prerequisites
We know that linear transformations map vectors from one space to another. But working with abstract mappings is difficult. Today, we bridge the gap between abstract vector spaces and computational linear algebra by representing these transformations as **Matrices**. 
Once a transformation is expressed as a matrix, operations like evaluating images, finding compositions, or finding inverses become simple matrix multiplications.

---

## Theory of Matrix Representation

Let $U(F)$ and $V(F)$ be two vector spaces over the field $F$.
Let $T : U \to V$ be a linear transformation.
To represent $T$ as a matrix, we must fix an **ordered basis** for both spaces:
*   Let

$$
B = \lbrace u_1, u_2, \dots, u_n \rbrace
$$

be the ordered basis for $U$.
*   Let

$$
B' = \lbrace v_1, v_2, \dots, v_m \rbrace
$$

be the ordered basis for $V$.

### The Process
1.  **Find the Images of the Domain Basis**: We take each basis vector of $U$ (that is, each $u_j \in B$) and find its image under $T$, which is $T(u_j)$. This image lives in $V$.
2.  **Express Images using the Co-Domain Basis**: Since $T(u_j) \in V$, we can write it uniquely as a linear combination of the basis vectors in $B'$:

$$
T(u_1) = a_{11}v_1 + a_{12}v_2 + \dots + a_{1m}v_m
$$

$$
T(u_2) = a_{21}v_1 + a_{22}v_2 + \dots + a_{2m}v_m
$$

$$
\vdots
$$

$$
T(u_n) = a_{n1}v_1 + a_{n2}v_2 + \dots + a_{nm}v_m
$$

3.  **Construct the Matrix**: We take the scalar coefficients from each linear combination and place them as **columns** in a matrix. The resulting matrix is the matrix representation of $T$ relative to the bases $B$ and $B'$, denoted as $[T]_{B}^{B'}$.

$$
[T]_{B}^{B'} =
\begin{bmatrix}
a_{11} & a_{21} & \dots & a_{n1} \\
a_{12} & a_{22} & \dots & a_{n2} \\
\vdots & \vdots & \ddots & \vdots \\
a_{1m} & a_{2m} & \dots & a_{nm}
\end{bmatrix}
$$

*(Note: If $T : V \to V$ is an operator mapping a space to itself, we usually use the same basis for both sides, denoted simply as $[T]_B$.)*

---

## Standard Bases

If the problem does not explicitly provide a basis, we assume the **standard basis**.
*   For $V_2(\mathbb{R})$, the standard basis is $B = \lbrace (1, 0), (0, 1) \rbrace$.
*   For $V_3(\mathbb{R})$, the standard basis is $B = \lbrace (1, 0, 0), (0, 1, 0), (0, 0, 1) \rbrace$.

---

## Numerical Example 1

**Problem:** Find the matrix of the linear transformation

$$
T : V_3(\mathbb{R}) \to V_3(\mathbb{R})
$$

defined by:

$$
T(a, b, c) = (2b + c, a - 4b, 3a)
$$

with respect to the standard basis $B$.

**Solution:**
The standard basis is

$$
B = \lbrace e_1(1, 0, 0), e_2(0, 1, 0), e_3(0, 0, 1) \rbrace.
$$

**Step 1: Compute Images of Basis Vectors**
*   $T(1, 0, 0) = (2(0)+0, 1-4(0), 3(1)) = (0, 1, 3)$
*   $T(0, 1, 0) = (2(1)+0, 0-4(1), 3(0)) = (2, -4, 0)$
*   $T(0, 0, 1) = (2(0)+1, 0-4(0), 3(0)) = (1, 0, 0)$

**Step 2: Express as Linear Combinations**
Because we are using the standard basis, the coordinates are simply the components of the vectors:
*   $(0, 1, 3) = 0(1, 0, 0) + 1(0, 1, 0) + 3(0, 0, 1)$
*   $(2, -4, 0) = 2(1, 0, 0) - 4(0, 1, 0) + 0(0, 0, 1)$
*   $(1, 0, 0) = 1(1, 0, 0) + 0(0, 1, 0) + 0(0, 0, 1)$

**Step 3: Compile the Matrix**
Write these coordinates as columns:

$$
[T]_B =
\begin{bmatrix}
0 & 2 & 1 \\
1 & -4 & 0 \\
3 & 0 & 0
\end{bmatrix}
$$

---

## Numerical Example 2 (Non-Standard Basis)

**Problem:** Find the matrix of the *same* linear transformation $T$ from Example 1, but this time with respect to the non-standard basis:

$$
B' = \lbrace v_1(1, 1, 1), v_2(1, 1, 0), v_3(1, 0, 0) \rbrace
$$

**Solution:**
**Step 1: Derive the General Coordinate Formula**
To express any vector $(a, b, c)$ as a combination of $B'$:

$$
(a, b, c) = x(1, 1, 1) + y(1, 1, 0) + z(1, 0, 0) = (x+y+z, x+y, x)
$$

Comparing components:
1.  $x = c$
2.  $x + y = b \implies y = b - c$
3.  $x + y + z = a \implies z = a - b$
Coordinate formula: **$x = c, \quad y = b - c, \quad z = a - b$**

**Step 2: Compute Images and their Coordinates**
*   **For

$$
v_1 = (1, 1, 1)
$$

:**
    $T(1, 1, 1) = (3, -3, 3)$. 
    Using the formula ($a=3, b=-3, c=3$):
    $x = 3$, $y = -3-3 = -6$, $z = 3-(-3) = 6$.

$$
T(v_1) = 3v_1 - 6v_2 + 6v_3
$$

*   **For

$$
v_2 = (1, 1, 0)
$$

:**
    $T(1, 1, 0) = (2, -3, 3)$. 
    Using the formula ($a=2, b=-3, c=3$):
    $x = 3$, $y = -3-3 = -6$, $z = 2-(-3) = 5$.

$$
T(v_2) = 3v_1 - 6v_2 + 5v_3
$$

*   **For

$$
v_3 = (1, 0, 0)
$$

:**
    $T(1, 0, 0) = (0, 1, 3)$. 
    Using the formula ($a=0, b=1, c=3$):
    $x = 3$, $y = 1-3 = -2$, $z = 0-1 = -1$.

$$
T(v_3) = 3v_1 - 2v_2 - 1v_3
$$

**Step 3: Compile the Matrix**
Write the computed coordinates as columns:

$$
[T]_{B'} =
\begin{bmatrix}
3 & 3 & 3 \\
-6 & -6 & -2 \\
6 & 5 & -1
\end{bmatrix}
$$

### The Power of Matrix Representation
With this matrix, we can evaluate the transformation using pure matrix multiplication. For any vector $\alpha$:

$$
[T]_{B'} [\alpha]_{B'} = [T(\alpha)]_{B'}
$$

Multiplying the transformation matrix by the coordinate vector of the input gives the coordinate vector of the output.

---

## Numerical Example 3 (Different Dimensions)

**Problem:** Find the matrix of

$$
T : \mathbb{R}^3 \to \mathbb{R}^2
$$

defined by:

$$
T(x, y, z) = (2x - 4y + 9z, 5x + 3y - 2z)
$$

with respect to the standard bases.

**Solution:**
Domain basis $B = \lbrace (1, 0, 0), (0, 1, 0), (0, 0, 1) \rbrace$. Co-domain basis $B' = \lbrace (1, 0), (0, 1) \rbrace$.
Compute images:
*   $T(1, 0, 0) = (2(1) - 0 + 0, 5(1) + 0 - 0) = (2, 5)$
*   $T(0, 1, 0) = (0 - 4(1) + 0, 0 + 3(1) - 0) = (-4, 3)$
*   $T(0, 0, 1) = (0 - 0 + 9(1), 0 + 0 - 2(1)) = (9, -2)$

Since $B'$ is standard, these components *are* the coordinates. Write them as columns:

$$
[T]_{B}^{B'} =
\begin{bmatrix}
2 & -4 & 9 \\
5 & 3 & -2
\end{bmatrix}
$$

*(Notice that a transformation from $\mathbb{R}^3 \to \mathbb{R}^2$ yields a $2 \times 3$ matrix.)*

## Key Takeaways
*   A linear transformation is completely determined by its action on a basis.
*   To build a transformation matrix, find the images of the domain basis, express them as coordinates relative to the co-domain basis, and stack those coordinates as **columns**.
*   The matrix perfectly encapsulates the transformation:

$$
A\vec{x} = \vec{y}.
$$

## What Comes Next
We will explore the relationship between the matrix representation and the **Rank and Nullity** of a linear transformation, leading into the Rank-Nullity Theorem.

---

**Navigation**
[< Previous Lecture](18_Fundamental_Theorem_Homomorphism.md) | [Index](README.md) | [Next Lecture >](20_Inverse_Linear_Transformation.md)
