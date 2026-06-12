# Lecture 23: Vector Space - Numerical Questions on Rank-Nullity Theorem

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 23 of 27
> **Video**: https://www.youtube.com/watch?v=3HoSPQmpzKc

---

**Navigation**
[< Previous Lecture](22_Invertible_Singular_Nonsingular.md) | [Index](README.md) | [Next Lecture >](24_Eigenvalue_Eigenvector_Theory.md)

---

## Prerequisites
Before tackling numerical problems, we recall two quick but powerful theorems regarding linear transformations $T : U \to V$:
1.  **Invertibility**: $T$ is invertible if and only if $T$ is non-singular. (A direct consequence of our previous theorems).
2.  **Generators of Range**: If a set of vectors $S = \lbrace u_1, u_2, \dots, u_n \rbrace$ spans the domain $U$, then their images under $T$, which are $\lbrace T(u_1), T(u_2), \dots, T(u_n) \rbrace$, will span the range space $R(T)$.

We will use the second theorem extensively: to find the range space of a transformation, we simply find the images of the standard basis vectors of the domain.

---

## Numerical Example 1

**Problem Statement:**
Show that the transformation $T : \mathbb{R}^2 \to \mathbb{R}^3$ defined by:

$$
T(a, b) = (a + b, a - b, b)
$$

is a linear transformation. Then find its range space, rank, null space, and nullity, and verify the Rank-Nullity Theorem.

### 1. Prove Linearity
Let $\alpha = (a_1, b_1)$ and $\beta = (a_2, b_2)$ be vectors in $\mathbb{R}^2$, and let $x, y \in \mathbb{R}$ be scalars.
Evaluate $T(x\alpha + y\beta)$:

$$
T(x\alpha + y\beta) = T(xa_1 + ya_2, xb_1 + yb_2)
$$

Apply the definition of $T$:

$$
= ((xa_1 + ya_2) + (xb_1 + yb_2), (xa_1 + ya_2) - (xb_1 + yb_2), xb_1 + yb_2)
$$

Group the $x$ terms and $y$ terms together:

$$
= (x(a_1 + b_1) + y(a_2 + b_2), x(a_1 - b_1) + y(a_2 - b_2), xb_1 + yb_2)
$$

Split the tuple:

$$
= x(a_1 + b_1, a_1 - b_1, b_1) + y(a_2 + b_2, a_2 - b_2, b_2)
$$

$$
= x T(\alpha) + y T(\beta)
$$

Thus, $T$ is a linear transformation.

### 2. Range Space and Rank
The domain is $\mathbb{R}^2$. Its standard basis is $S = \lbrace e_1(1, 0), e_2(0, 1) \rbrace$. Let's find their images:
*   $T(1, 0) = (1+0, 1-0, 0) = (1, 1, 0)$
*   $T(0, 1) = (0+1, 0-1, 1) = (1, -1, 1)$

These two vectors generate the range space $R(T)$:

$$
R(T) = \lbrace c_1(1, 1, 0) + c_2(1, -1, 1) \mid c_1, c_2 \in \mathbb{R} \rbrace
$$

Since $(1, 1, 0)$ and $(1, -1, 1)$ are not scalar multiples of each other, they are linearly independent and thus form a basis for $R(T)$.
*   **Rank $\rho(T)$** = Dimension of $R(T)$ = **2**

### 3. Null Space and Nullity
The null space contains all vectors $(a,b)$ that map to $(0,0,0)$:

$$
T(a, b) = (0, 0, 0) \implies (a + b, a - b, b) = (0, 0, 0)
$$

This gives the system:
1.  $a + b = 0$
2.  $a - b = 0$
3.  $b = 0$

From equation 3, $b = 0$. Substituting into 1 gives $a = 0$. The only solution is the zero vector.

$$
N(T) = \lbrace (0, 0) \rbrace
$$

Because the null space contains only the zero vector, its basis is empty.
*   **Nullity $\eta(T)$** = Dimension of $N(T)$ = **0**

### 4. Verification

$$
\text{Rank}(T) + \text{Nullity}(T) = 2 + 0 = 2
$$

The dimension of the domain $\mathbb{R}^2$ is 2. The theorem holds perfectly.

---

## Numerical Example 2

**Problem Statement:**
Verify the Rank-Nullity Theorem for the linear transformation $T : \mathbb{R}^3 \to \mathbb{R}^3$ defined by its action on the standard basis $\lbrace e_1, e_2, e_3 \rbrace$:

$$
T(e_1) = e_1 - e_2, \quad T(e_2) = 2e_2 + e_3, \quad T(e_3) = e_1 + e_2 + e_3
$$

### 1. Range Space and Rank
Write the given images as coordinate vectors:
*   $T(e_1) = (1, -1, 0)$
*   $T(e_2) = (0, 2, 1)$
*   $T(e_3) = (1, 1, 1)$

These vectors span $R(T)$. However, observe that:

$$
T(e_1) + T(e_2) = (1, -1, 0) + (0, 2, 1) = (1, 1, 1) = T(e_3)
$$

Because $T(e_3)$ is a linear combination of the other two, it is linearly dependent. We discard it from the basis.
The remaining set $\lbrace (1, -1, 0), (0, 2, 1) \rbrace$ is linearly independent and forms the basis.
*   **Rank $\rho(T)$** = **2**

### 2. Null Space and Nullity
Let $\alpha = (x, y, z) = xe_1 + ye_2 + ze_3 \in N(T)$.

$$
T(\alpha) = (0, 0, 0) \implies xT(e_1) + yT(e_2) + zT(e_3) = (0, 0, 0)
$$

$$
x(1, -1, 0) + y(0, 2, 1) + z(1, 1, 1) = (0, 0, 0)
$$

$$
(x + z, -x + 2y + z, y + z) = (0, 0, 0)
$$

This gives the system:
1.  $x + z = 0 \implies x = -z$
2.  $y + z = 0 \implies y = -z$
3.  $-x + 2y + z = 0 \implies -(-z) + 2(-z) + z = z - 2z + z = 0$ (Consistent)

Any vector in the null space has the form $(-z, -z, z) = z(-1, -1, 1)$.
The null space is spanned by a single vector $\lbrace (-1, -1, 1) \rbrace$.
*   **Nullity $\eta(T)$** = **1**

### 3. Verification

$$
\text{Rank}(T) + \text{Nullity}(T) = 2 + 1 = 3
$$

The dimension of the domain $\mathbb{R}^3$ is 3. The theorem holds.

---

## Numerical Example 3

**Problem Statement:**
Let $T$ be a linear operator on $\mathbb{R}^3$ defined by:

$$
T(x_1, x_2, x_3) = (3x_1 + x_3, -2x_1 + x_2, -x_1 + 2x_2 + 4x_3)
$$

Show that $T$ is non-singular and invertible, and find a formula for $T^{-1}$.

### 1. Prove Non-Singularity
Set $T(x_1, x_2, x_3) = (0, 0, 0)$ to find the null space. This creates a homogeneous system $AX = 0$:

$$
A =
\begin{pmatrix}
3 & 0 & 1 \\
-2 & 1 & 0 \\
-1 & 2 & 4
\end{pmatrix}
$$

Find the determinant of the coefficient matrix $A$:

$$
\det(A) = 3(4 - 0) - 0 + 1(-4 - (-1)) = 12 - 3 = 9
$$

Since $\det(A) = 9 \neq 0$, the matrix is non-singular, meaning the homogeneous system has only the trivial solution $x_1 = 0, x_2 = 0, x_3 = 0$.
Thus, $N(T) = \lbrace (0, 0, 0) \rbrace$, proving that $T$ is non-singular. By our theorem, since it is an operator on a finite-dimensional space and is non-singular, it is invertible.

### 2. Find Inverse Formula
Set up the inverse relation: $T^{-1}(x_1, x_2, x_3) = (y_1, y_2, y_3) \iff T(y_1, y_2, y_3) = (x_1, x_2, x_3)$.
Substitute $(y_1, y_2, y_3)$ into the definition of $T$:
1.  $3y_1 + y_3 = x_1 \implies y_3 = x_1 - 3y_1$
2.  $-2y_1 + y_2 = x_2 \implies y_2 = x_2 + 2y_1$
3.  $-y_1 + 2y_2 + 4y_3 = x_3$

Substitute (1) and (2) into (3):

$$
-y_1 + 2(x_2 + 2y_1) + 4(x_1 - 3y_1) = x_3
$$

$$
-y_1 + 2x_2 + 4y_1 + 4x_1 - 12y_1 = x_3
$$

$$
-9y_1 + 4x_1 + 2x_2 = x_3 \implies 9y_1 = 4x_1 + 2x_2 - x_3 \implies \mathbf{y_1 = \frac{1}{9}(4x_1 + 2x_2 - x_3)}
$$

Substitute $y_1$ back to find $y_2$:

$$
y_2 = x_2 + 2y_1 = x_2 + \frac{2}{9}(4x_1 + 2x_2 - x_3) \implies \mathbf{y_2 = \frac{1}{9}(8x_1 + 13x_2 - 2x_3)}
$$

Substitute $y_1$ back to find $y_3$:

$$
y_3 = x_1 - 3y_1 = x_1 - \frac{3}{9}(4x_1 + 2x_2 - x_3) \implies \mathbf{y_3 = \frac{1}{9}(-3x_1 - 6x_2 + 3x_3)}
$$

Thus, the final formula for the inverse mapping is:

$$
T^{-1}(x_1, x_2, x_3) = \frac{1}{9}(4x_1 + 2x_2 - x_3, 8x_1 + 13x_2 - 2x_3, -3x_1 - 6x_2 + 3x_3)
$$

---

**Navigation**
[< Previous Lecture](22_Invertible_Singular_Nonsingular.md) | [Index](README.md) | [Next Lecture >](24_Eigenvalue_Eigenvector_Theory.md)
