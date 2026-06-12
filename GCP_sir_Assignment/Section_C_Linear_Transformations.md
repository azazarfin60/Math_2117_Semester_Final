# Section C: Linear Transformations

## Q16 (04)
**Question:** **Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ be defined by $T(x, y) = (x^2, y)$. Check whether $T$ is a linear transformation. Justify your answer.**

**Answer:**
For $T$ to be a linear transformation, it must satisfy the additivity and scalar multiplication properties:
1. $T(u + v) = T(u) + T(v)$
2. $T(cu) = cT(u)$

Let's test the scalar multiplication property.
Let $u = (1, 1)$ and scalar $c = 2$.
$T(u) = T(1, 1) = (1^2, 1) = (1, 1)$.
Then $cT(u) = 2(1, 1) = (2, 2)$.

Now, compute $T(cu)$:
$cu = 2(1, 1) = (2, 2)$.
$T(cu) = T(2, 2) = (2^2, 2) = (4, 2)$.

Since $T(cu) = (4, 2) \neq (2, 2) = cT(u)$, the scalar multiplication property fails. Therefore, $T$ is not a linear transformation.

## Q17 (04)
**Question:** **Define kernel, range, rank, and nullity of a linear transformation.**

**Answer:**
Let $T: V \to W$ be a linear transformation between vector spaces $V$ and $W$.

*   **Kernel (Null Space) of $T$:** The set of all vectors in the domain $V$ that map to the zero vector in $W$.

$$
\text{ker}(T) = \lbrace v \in V \mid T(v) = 0_W\rbrace
$$

*   **Range (Image) of $T$:** The set of all vectors in the codomain $W$ that are the image of at least one vector in $V$ under the transformation $T$.

$$
\text{range}(T) = \lbrace T(v) \mid v \in V\rbrace
$$

*   **Nullity of $T$:** The dimension of the kernel of $T$.

$$
\text{nullity}(T) = \dim(\text{ker}(T))
$$

*   **Rank of $T$:** The dimension of the range of $T$.

$$
\text{rank}(T) = \dim(\text{range}(T))
$$

## Q18 (05)
**Question:** **Let $T: \mathbb{R}^3 \to \mathbb{R}^2$ be given by $T(x, y, z) = (x + y, y + z)$. Is it a linear transformation? Find: (i) Kernel of $T$, (ii) Range of $T$, (iii) Rank and Nullity.**

**Answer:**
**Part 1: Is it a linear transformation?**
Let $u = (x_1, y_1, z_1)$ and $v = (x_2, y_2, z_2)$.
$T(u + v) = T(x_1+x_2, y_1+y_2, z_1+z_2) = (x_1+x_2 + y_1+y_2, y_1+y_2 + z_1+z_2)$.
$= (x_1+y_1, y_1+z_1) + (x_2+y_2, y_2+z_2) = T(u) + T(v)$.
Let $c$ be a scalar.
$T(cu) = T(cx_1, cy_1, cz_1) = (cx_1+cy_1, cy_1+cz_1) = c(x_1+y_1, y_1+z_1) = cT(u)$.
Yes, it is a linear transformation.

**(i) Kernel of $T$**:
Set $T(x,y,z) = (0,0)$. This gives the system:
$x + y = 0 \implies x = -y$
$y + z = 0 \implies z = -y$
Vectors in the kernel are of the form $(-y, y, -y) = y(-1, 1, -1)$.

$$
\text{ker}(T) = \text{span}\lbrace(-1, 1, -1)\rbrace
$$

**(ii) Range of $T$**:
$T(x, y, z) = x(1, 0) + y(1, 1) + z(0, 1)$.
The range is spanned by $\lbrace(1, 0), (1, 1), (0, 1)\rbrace$. The vectors $(1, 0)$ and $(0, 1)$ are linearly independent and span $\mathbb{R}^2$.
Thus, $\text{range}(T) = \mathbb{R}^2$.

**(iii) Rank and Nullity**:
From the basis of the kernel, $\text{nullity}(T) = 1$.
From the basis of the range, $\text{rank}(T) = 2$.
Note: $\text{rank}(T) + \text{nullity}(T) = 2 + 1 = 3 = \dim(\mathbb{R}^3)$, which verifies the Rank-Nullity Theorem.

## Q19 (05)
**Question:** **Let $T: \mathbb{R}^3 \to \mathbb{R}^3$ be defined by $T(x, y, z) = (x + y, y + z, z + x)$. Find the matrix of $T$, its rank, nullity, and verify the rank-nullity theorem.**

**Answer:**
**1. Matrix of $T$**:
Using the standard basis $e_1 = (1,0,0), e_2 = (0,1,0), e_3 = (0,0,1)$:
$T(e_1) = (1+0, 0+0, 0+1) = (1, 0, 1)$
$T(e_2) = (0+1, 1+0, 0+0) = (1, 1, 0)$
$T(e_3) = (0+0, 0+1, 1+0) = (0, 1, 1)$
The matrix $A$ relative to the standard basis is formed by taking these vectors as columns:

$$
A =
\begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
1 & 0 & 1
\end{pmatrix}
$$

**2. Rank and Nullity**:
We find the reduced row echelon form (RREF) of $A$:
$R_3 \to R_3 - R_1$:

$$
\begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
0 & -1 & 1
\end{pmatrix}
$$

$R_3 \to R_3 + R_2$:

$$
\begin{pmatrix}
1 & 1 & 0 \\
0 & 1 & 1 \\
0 & 0 & 2
\end{pmatrix}
$$

The matrix has 3 non-zero rows (pivots in every column). Thus, $\text{rank}(T) = 3$.
Since the rank is 3, the null space only contains the zero vector. Thus, $\text{nullity}(T) = 0$.

**3. Verify Rank-Nullity Theorem**:
The theorem states: $\text{rank}(T) + \text{nullity}(T) = \dim(V)$
$3 + 0 = 3$. The dimension of the domain $\mathbb{R}^3$ is 3. The theorem is verified.

## Q20 (04)
**Question:** **Find the matrix of the linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$, defined by $T(x, y) = (2x + y, x - y)$, with respect to the standard basis.**

**Answer:**
Standard basis vectors for $\mathbb{R}^2$ are $e_1 = (1, 0)$ and $e_2 = (0, 1)$.
Find their images under $T$:
$T(e_1) = T(1, 0) = (2(1) + 0, 1 - 0) = (2, 1)$
$T(e_2) = T(0, 1) = (2(0) + 1, 0 - 1) = (1, -1)$
The standard matrix of $T$ is constructed by using these image vectors as columns.

$$
[T] =
\begin{pmatrix}
2 & 1 \\
1 & -1
\end{pmatrix}
$$

## Q21 (04)
**Question:** **Prove that a linear transformation $T: V \to W$ is injective if and only if $\text{ker}(T) = \lbrace 0\rbrace$.**

**Answer:**
**$(\Rightarrow)$ Assume $T$ is injective (one-to-one):**
We must show $\text{ker}(T) = \lbrace 0\rbrace$.
Let $v \in \text{ker}(T)$. Then $T(v) = 0$. Since $T$ is linear, we also know $T(0) = 0$. So $T(v) = T(0)$.
Because $T$ is injective, this implies $v = 0$. Thus, the only element in the kernel is the zero vector, so $\text{ker}(T) = \lbrace 0\rbrace$.

**$(\Leftarrow)$ Assume $\text{ker}(T) = \lbrace 0\rbrace$:**
We must show $T$ is injective.
Suppose there are vectors $u, v \in V$ such that $T(u) = T(v)$. By linearity, $T(u) - T(v) = 0 \implies T(u - v) = 0$.
This means the vector $(u - v)$ is in the kernel of $T$. Since $\text{ker}(T) = \lbrace 0\rbrace$, it must be that $u - v = 0$, which implies $u = v$.
Therefore, $T$ maps distinct elements to distinct elements, meaning $T$ is injective.

## Q22 (05)
**Question:** **Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ be given by $T(x, y) = (3x + 2y, x + y)$. Determine whether $T$ is invertible. If yes, find $T^{-1}$.**

**Answer:**
To determine invertibility, we can find the standard matrix $[T]$ and check its determinant.
$T(1, 0) = (3, 1)$ and $T(0, 1) = (2, 1)$.
The matrix representation is:

$$
A =
\begin{pmatrix}
3 & 2 \\
1 & 1
\end{pmatrix}
$$

The determinant of $A$ is:

$$
|A| = (3)(1) - (2)(1) = 3 - 2 = 1
$$

Since $|A| \neq 0$, the matrix $A$ is invertible, which means the transformation $T$ is invertible.

To find $T^{-1}$, we find the inverse of the matrix $A$:

$$
A^{-1} = \frac{1}{|A|}
\begin{pmatrix}
1 & -2 \\
-1 & 3
\end{pmatrix} = \begin{pmatrix} 1 & -2 \\ -1 & 3 \end{pmatrix}
$$

Therefore, the inverse transformation $T^{-1}(x, y)$ is given by the matrix multiplication:

$$
\begin{pmatrix}
1 & -2 \\
-1 & 3
\end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} x - 2y \\ -x + 3y \end{pmatrix}
$$

So, $T^{-1}(x, y) = (x - 2y, -x + 3y)$.

## Q23 (05)
**Question:** **Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ be defined by $T(x, y) = (x + y, x - y)$. Let $B = \lbrace(1, 1), (1, -1)\rbrace$. Find the matrix of $T$ with respect to the basis $B$.**

**Answer:**
Let the basis vectors be $b_1 = (1, 1)$ and $b_2 = (1, -1)$.
First, apply $T$ to the basis vectors:
$T(b_1) = T(1, 1) = (1+1, 1-1) = (2, 0)$
$T(b_2) = T(1, -1) = (1-1, 1-(-1)) = (0, 2)$

Next, express these image vectors as linear combinations of the basis $B$:
Let $(2, 0) = c_1b_1 + c_2b_2 = c_1(1, 1) + c_2(1, -1) = (c_1+c_2, c_1-c_2)$.
This gives a system:
$c_1 + c_2 = 2$
$c_1 - c_2 = 0 \implies c_1 = c_2$
So $2c_1 = 2 \implies c_1 = 1$, and $c_2 = 1$.
Therefore,

$$
[T(b_1)]_B =
\begin{pmatrix}
1 \\
1
\end{pmatrix}.
$$

Let $(0, 2) = d_1b_1 + d_2b_2 = (d_1+d_2, d_1-d_2)$.
This gives:
$d_1 + d_2 = 0 \implies d_1 = -d_2$
$d_1 - d_2 = 2 \implies -d_2 - d_2 = 2 \implies -2d_2 = 2 \implies d_2 = -1$.
So $d_1 = 1$.
Therefore,

$$
[T(b_2)]_B =
\begin{pmatrix}
1 \\
-1
\end{pmatrix}.
$$

The matrix of $T$ with respect to $B$ is formed by these coordinate vectors as columns:

$$
[T]_B =
\begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}
$$

## Q24 (04)
**Question:** **Show that a linear transformation is injective if and only if its nullity is zero.**

**Answer:**
Let $T: V \to W$ be a linear transformation. We previously proved that $T$ is injective if and only if its kernel contains only the zero vector: $\text{ker}(T) = \lbrace 0\rbrace$.

The nullity of $T$ is defined as the dimension of the kernel: $\text{nullity}(T) = \dim(\text{ker}(T))$.
The dimension of a vector space is $0$ if and only if the space consists of exactly the zero vector.
Therefore, $\text{ker}(T) = \lbrace 0\rbrace$ is logically equivalent to $\dim(\text{ker}(T)) = 0$, which means $\text{nullity}(T) = 0$.

By transitivity, $T$ is injective if and only if $\text{nullity}(T) = 0$.

## Q25 (05)
**Question:** **Prove that a linear transformation is invertible if and only if it is both one-to-one and onto.**

**Answer:**
**$(\Rightarrow)$ Assume $T: V \to W$ is invertible:**
By definition, there exists a function $T^{-1}: W \to V$ such that $T^{-1}(T(v)) = v$ for all $v \in V$, and $T(T^{-1}(w)) = w$ for all $w \in W$.
- **To show $T$ is one-to-one (injective):** Suppose $T(u) = T(v)$. Applying $T^{-1}$ to both sides gives $T^{-1}(T(u)) = T^{-1}(T(v))$, which simplifies to $u = v$. Thus $T$ is injective.
- **To show $T$ is onto (surjective):** Let $w$ be any element in $W$. Choose $v = T^{-1}(w)$. Then $v \in V$, and by definition of the inverse, $T(v) = T(T^{-1}(w)) = w$. Since every $w \in W$ is the image of some $v \in V$, $T$ is onto.

**$(\Leftarrow)$ Assume $T$ is both one-to-one and onto:**
Since $T$ is onto, for every $w \in W$, there exists at least one $v \in V$ such that $T(v) = w$. Since $T$ is one-to-one, this $v$ is unique (if $T(v_1) = w$ and $T(v_2) = w$, then $T(v_1) = T(v_2) \implies v_1 = v_2$).
Because each $w \in W$ corresponds to a unique $v \in V$, we can define a well-defined function $S: W \to V$ by mapping $w$ to that unique $v$. By this definition, $S(T(v)) = S(w) = v$ for all $v \in V$, and $T(S(w)) = T(v) = w$ for all $w \in W$. Since $T$ has a two-sided inverse function $S$, the transformation $T$ is invertible.