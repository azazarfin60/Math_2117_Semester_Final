# Section A: Vector Spaces and Subspaces

## Q1 (04)
**Question:** **Prove that $\mathbb{R}^n$ with usual operations is a vector space over $\mathbb{R}$.**

**Answer:**
We need to show that $V = \mathbb{R}^n$ satisfies all the axioms of a vector space over the field $\mathbb{R}$. Let $u = (u_1, u_2, \dots, u_n)$, $v = (v_1, v_2, \dots, v_n)$, and $w = (w_1, w_2, \dots, w_n)$ be vectors in $\mathbb{R}^n$, and let $c, d$ be scalars in $\mathbb{R}$. The operations are standard element-wise addition and scalar multiplication.

**Axioms for Addition:**
1. **Closure under addition:** $u + v = (u_1+v_1, \dots, u_n+v_n) \in \mathbb{R}^n$.
2. **Commutativity:** $u + v = (u_1+v_1, \dots) = (v_1+u_1, \dots) = v + u$.
3. **Associativity:** $(u + v) + w = u + (v + w)$ since addition of real numbers is associative.
4. **Additive Identity:** There exists a zero vector $0 = (0, \dots, 0) \in \mathbb{R}^n$ such that $u + 0 = u$.
5. **Additive Inverse:** For every $u \in \mathbb{R}^n$, there exists $-u = (-u_1, \dots, -u_n) \in \mathbb{R}^n$ such that $u + (-u) = 0$.

**Axioms for Scalar Multiplication:**
6. **Closure under scalar multiplication:** $cu = (cu_1, \dots, cu_n) \in \mathbb{R}^n$.
7. **Distributivity over vector addition:** $c(u + v) = (c(u_1+v_1), \dots) = (cu_1+cv_1, \dots) = cu + cv$.
8. **Distributivity over scalar addition:** $(c + d)u = ((c+d)u_1, \dots) = (cu_1+du_1, \dots) = cu + du$.
9. **Associativity of scalar multiplication:** $c(du) = c(du_1, \dots) = (cdu_1, \dots) = (cd)u$.
10. **Multiplicative identity:** $1u = (1u_1, \dots, 1u_n) = u$.

Since all 10 axioms hold true, $\mathbb{R}^n$ is a vector space over $\mathbb{R}$.

## Q2 (04)
**Question:** **Construct a non-trivial subspace of $\mathbb{R}^5$ that is not spanned by standard basis vectors.**

**Answer:**
A subspace is non-trivial if it is neither the zero subspace $\{0\}$ nor the entire space $\mathbb{R}^5$. It is not spanned by standard basis vectors $e_1, e_2, e_3, e_4, e_5$ if its basis vectors are not a subset of these standard vectors.

Let $W = \text{span}\{(1, 1, 1, 1, 1)\}$.

This is a one-dimensional subspace of $\mathbb{R}^5$. The vector $(1, 1, 1, 1, 1)$ cannot be written as a scalar multiple of any single standard basis vector. The space generated is simply all vectors of the form $(a, a, a, a, a)$ for $a \in \mathbb{R}$. This forms a valid non-trivial subspace.

## Q3 (04)
**Question:** **Test whether the set $V = \{(x, y) \in \mathbb{R}^2 : xy = 0\}$ is a vector space.**

**Answer:**
For a subset to be a vector space, it must be closed under vector addition. 

Let $u = (1, 0)$ and $v = (0, 1)$. 
Both $u$ and $v$ belong to $V$ because their components satisfy the condition $x \cdot y = 0$.

Now consider their sum:

$$
u + v = (1, 0) + (0, 1) = (1, 1)
$$

For the sum $(1, 1)$, the product of the coordinates is $1 \cdot 1 = 1 \neq 0$. Thus, $(1, 1) \notin V$.

Since $V$ is not closed under addition, it is not a vector space.

## Q4 (05)
**Question:** **Let $V = \mathbb{R}^4$. Prove that the set $W = \{(x, y, z, w) : x + y + z + w = 0\}$ is a subspace and find its dimension.**

**Answer:**
To prove $W$ is a subspace, we must verify three properties:
1. **Zero vector:** $(0, 0, 0, 0)$ satisfies $0 + 0 + 0 + 0 = 0$, so $0 \in W$.
2. **Closure under addition:** Let $u = (x_1, y_1, z_1, w_1) \in W$ and $v = (x_2, y_2, z_2, w_2) \in W$. Then $x_1+y_1+z_1+w_1 = 0$ and $x_2+y_2+z_2+w_2 = 0$. 
The sum is $u + v = (x_1+x_2, y_1+y_2, z_1+z_2, w_1+w_2)$.
$(x_1+x_2) + (y_1+y_2) + (z_1+z_2) + (w_1+w_2) = (x_1+y_1+z_1+w_1) + (x_2+y_2+z_2+w_2) = 0 + 0 = 0$. So $u + v \in W$.
3. **Closure under scalar multiplication:** Let $c \in \mathbb{R}$. $cu = (cx_1, cy_1, cz_1, cw_1)$.
$cx_1 + cy_1 + cz_1 + cw_1 = c(x_1+y_1+z_1+w_1) = c(0) = 0$. So $cu \in W$.

Thus, $W$ is a subspace.

**Dimension of $W$:**
The condition $x + y + z + w = 0$ implies $w = -x - y - z$. Any vector in $W$ can be written as:

$$
(x, y, z, -x-y-z) = x(1, 0, 0, -1) + y(0, 1, 0, -1) + z(0, 0, 1, -1)
$$

The set of vectors $\{(1, 0, 0, -1), (0, 1, 0, -1), (0, 0, 1, -1)\}$ spans $W$ and is linearly independent. Therefore, the basis has 3 vectors, meaning $\dim(W) = 3$.

## Q5 (05)
**Question:** **Let $W = \{(x, y, z) \in \mathbb{R}^3 : x + 2y + 3z = 0\}$. Show that $W$ is a subspace and find its dimension.**

**Answer:**
**Proof of Subspace:**
1. **Zero vector:** $0 + 2(0) + 3(0) = 0$, so $(0,0,0) \in W$.
2. **Closure under addition:** Let $u = (x_1, y_1, z_1), v = (x_2, y_2, z_2) \in W$.
$(x_1+x_2) + 2(y_1+y_2) + 3(z_1+z_2) = (x_1+2y_1+3z_1) + (x_2+2y_2+3z_2) = 0 + 0 = 0$. Thus $u + v \in W$.
3. **Closure under scalar multiplication:** Let $c \in \mathbb{R}$.
$cx_1 + 2(cy_1) + 3(cz_1) = c(x_1 + 2y_1 + 3z_1) = c(0) = 0$. Thus $cu \in W$.

$W$ is a subspace.

**Dimension of $W$:**
From the equation, $x = -2y - 3z$. Vectors in $W$ are of the form $(-2y - 3z, y, z) = y(-2, 1, 0) + z(-3, 0, 1)$.
The set $\{(-2, 1, 0), (-3, 0, 1)\}$ forms a basis because they are linearly independent and span $W$. Hence, $\dim(W) = 2$.

## Q6 (04)
**Question:** **Give an example of a subset of a vector space that is closed under addition but not scalar multiplication.**

**Answer:**
Consider the vector space $V = \mathbb{R}^2$ over the field $\mathbb{R}$.
Let $W = \{(x, y) \in \mathbb{R}^2 : x \geq 0 \text{ and } y \geq 0\}$. This is the first quadrant of the Cartesian plane.

**Closed under addition:** If $u = (x_1, y_1)$ and $v = (x_2, y_2)$ are in $W$, then $x_1, x_2, y_1, y_2 \geq 0$. Their sum is $u + v = (x_1+x_2, y_1+y_2)$. Since the sum of non-negative numbers is non-negative, $x_1+x_2 \geq 0$ and $y_1+y_2 \geq 0$. Thus $u + v \in W$.

**Not closed under scalar multiplication:** Let $u = (1, 1) \in W$, and choose the scalar $c = -1$.
Then $cu = -1(1, 1) = (-1, -1)$. Since $-1$ is not greater than or equal to $0$, $cu \notin W$.

Therefore, $W$ is closed under addition but not under scalar multiplication.

## Q7 (05)
**Question:** **Prove that the intersection of any collection of subspaces is a subspace.**

**Answer:**
Let $\{W_i\}_{i \in I}$ be a collection of subspaces of a vector space $V$. Let $W = \bigcap_{i \in I} W_i$.

1. Since each $W_i$ is a subspace, the zero vector $0 \in W_i$ for all $i \in I$. Thus $0 \in W$.
2. Let $u, v \in W$. This implies $u, v \in W_i$ for all $i \in I$. Since each $W_i$ is closed under addition, $u + v \in W_i$ for all $i \in I$. Therefore, $u + v \in W$.
3. Let $u \in W$ and let $c$ be a scalar. Then $u \in W_i$ for all $i \in I$. Since each $W_i$ is closed under scalar multiplication, $cu \in W_i$ for all $i \in I$. Therefore, $cu \in W$.

Since $W$ contains the zero vector and is closed under both vector addition and scalar multiplication, it is a subspace of $V$.

## Q8 (05)
**Question:** **Let $U, W \subseteq V$. Prove that $U + W$ is a subspace and $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$**

**Answer:**
**Proof that $U + W$ is a subspace:**
Let $U + W = \{u + w : u \in U, w \in W\}$.
1. Since $0 \in U$ and $0 \in W$, $0 = 0 + 0 \in U + W$.
2. Let $v_1, v_2 \in U + W$. Then $v_1 = u_1 + w_1$ and $v_2 = u_2 + w_2$ for some $u_1, u_2 \in U$ and $w_1, w_2 \in W$.
$v_1 + v_2 = (u_1 + u_2) + (w_1 + w_2)$. Since $U, W$ are subspaces, $u_1+u_2 \in U$ and $w_1+w_2 \in W$. Thus $v_1 + v_2 \in U + W$.
3. Let $c$ be a scalar and $v = u + w \in U + W$.
$cv = c(u + w) = cu + cw$. Since $U, W$ are subspaces, $cu \in U$ and $cw \in W$. Thus $cv \in U + W$.

Hence, $U + W$ is a subspace.

**Dimension Formula:**
Let $\dim(U \cap W) = k$, $\dim U = m$, and $\dim W = n$.
Let $\{v_1, \dots, v_k\}$ be a basis for $U \cap W$.
Extend this to a basis of $U$: $\{v_1, \dots, v_k, u_{k+1}, \dots, u_m\}$.
Extend the same basis to a basis of $W$: $\{v_1, \dots, v_k, w_{k+1}, \dots, w_n\}$.

The set $B = \{v_1, \dots, v_k, u_{k+1}, \dots, u_m, w_{k+1}, \dots, w_n\}$ spans $U + W$.
To show linear independence, suppose:

$$
a_1v_1 + \dots + a_kv_k + b_{k+1}u_{k+1} + \dots + b_mu_m + c_{k+1}w_{k+1} + \dots + c_nw_n = 0
$$

Let $x = b_{k+1}u_{k+1} + \dots + b_mu_m$. Then:

$$
x = -a_1v_1 - \dots - a_kv_k - c_{k+1}w_{k+1} - \dots - c_nw_n
$$

Since the RHS is in $W$, $x \in W$. But $x \in U$ by definition. So $x \in U \cap W$.
Since $x \in U \cap W$, it can be written as a linear combination of $v_1, \dots, v_k$. However, $\{v_1, \dots, u_m\}$ is a basis for $U$, so the $u_i$ coefficients ($b_j$) must be zero. 

Substituting $b_j = 0$ into the original equation leaves only $v_i$ and $w_j$ vectors, which form a basis for $W$, so their coefficients must also be zero. Thus $B$ is linearly independent. The number of vectors in $B$ is $k + (m - k) + (n - k) = m + n - k$.

Therefore, $\dim(U + W) = \dim U + \dim W - \dim(U \cap W)$.

## Q9 (04)
**Question:** **Prove that every subspace of a vector space is itself a vector space.**

**Answer:**
Let $W$ be a subspace of a vector space $V$. 
By definition of a subspace, $W$ is closed under vector addition and scalar multiplication. Since $W \subseteq V$, the operations are inherited from $V$, meaning commutativity, associativity, and distributivity hold automatically for all vectors in $W$.

$W$ contains the zero vector $0 \in V$ because $0 \cdot w = 0$ for any $w \in W$, and closure under scalar multiplication ensures $0 \in W$. For every $w \in W$, its additive inverse $-w$ is also in $W$ because $-1 \cdot w = -w$, which is in $W$ by closure under scalar multiplication.

Since $W$ satisfies all the vector space axioms under the operations of $V$, it is a vector space in its own right.

## Q10 (04)
**Question:** **Show that the union of two subspaces is not necessarily a subspace.**

**Answer:**
Consider the vector space $V = \mathbb{R}^2$. Let $U = \{(x, 0) : x \in \mathbb{R}\}$ (the x-axis) and $W = \{(0, y) : y \in \mathbb{R}\}$ (the y-axis). Both $U$ and $W$ are valid one-dimensional subspaces of $\mathbb{R}^2$.

Now consider their union $U \cup W$, which consists of all vectors lying on either the x-axis or the y-axis. Take the vector $u = (1, 0) \in U$ and $w = (0, 1) \in W$. Both vectors are in $U \cup W$.

Now consider their sum:

$$
u + w = (1, 0) + (0, 1) = (1, 1)
$$

The resulting vector $(1, 1)$ does not lie on the x-axis (since $y \neq 0$) and does not lie on the y-axis (since $x \neq 0$). Therefore, $(1, 1) \notin U \cup W$. 

Since $U \cup W$ is not closed under vector addition, it is not a subspace.
