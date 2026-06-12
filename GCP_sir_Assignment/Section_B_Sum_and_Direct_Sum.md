# Section B: Sum and Direct Sum

## Q11 (03)
**Question:** **Define the sum of two subspaces and give an example.**

**Answer:**
Let $U$ and $W$ be subspaces of a vector space $V$. The sum of the two subspaces, denoted as $U + W$, is defined as the set of all possible sums of a vector from $U$ and a vector from $W$:

$$
U + W = \lbrace u + w : u \in U, w \in W\rbrace
$$

**Example:** Consider

$$
V = \mathbb{R}^3
$$

. Let $U$ be the x-axis, $U = \lbrace(x, 0, 0) : x \in \mathbb{R}\rbrace$, and $W$ be the y-axis, $W = \lbrace(0, y, 0) : y \in \mathbb{R}\rbrace$. The sum $U + W$ consists of vectors of the form $(x, 0, 0) + (0, y, 0) = (x, y, 0)$. Thus, $U + W$ is the xy-plane in $\mathbb{R}^3$.

## Q12 (04)
**Question:** **Prove that the sum of two subspaces is a subspace.**

**Answer:**
Let $U$ and $W$ be subspaces of $V$. We want to show that $U + W$ is a subspace.
1. **The zero vector:** Since $0 \in U$ and $0 \in W$, $0 = 0 + 0 \in U + W$.
2. **Closure under addition:** Let $x, y \in U + W$. Then

$$
x = u_1 + w_1
$$

and

$$
y = u_2 + w_2
$$

for some $u_1, u_2 \in U$ and $w_1, w_2 \in W$.

$$
x + y = (u_1 + w_1) + (u_2 + w_2) = (u_1 + u_2) + (w_1 + w_2)
$$

Since $U$ and $W$ are subspaces, $u_1 + u_2 \in U$ and $w_1 + w_2 \in W$. Thus $x + y \in U + W$.
3. **Closure under scalar multiplication:** Let $x = u + w \in U + W$ and $c$ be a scalar.

$$
cx = c(u + w) = cu + cw
$$

Since $U$ and $W$ are subspaces, $cu \in U$ and $cw \in W$. Thus $cx \in U + W$.

Therefore, $U + W$ is a subspace of $V$.

## Q13 (05)
**Question:** **Show that $V = U \oplus W$ if and only if $V = U + W$ and $U \cap W = \lbrace 0\rbrace$.**

**Answer:**
**$(\Rightarrow)$ Assume $V = U \oplus W$:**
By definition of direct sum, every vector $v \in V$ can be uniquely expressed as $v = u + w$ where $u \in U$ and $w \in W$. This immediately implies $V = U + W$.

Now, let $x \in U \cap W$. This means $x \in U$ and $x \in W$. We can write the zero vector in two ways: $0 = 0 + 0$ (where $0 \in U, 0 \in W$) and $0 = x + (-x)$ (where $x \in U, -x \in W$). Because the representation must be unique in a direct sum, we must have $x = 0$. Thus $U \cap W = \lbrace 0\rbrace$.

**$(\Leftarrow)$ Assume $V = U + W$ and $U \cap W = \lbrace 0\rbrace$:**
Since $V = U + W$, any $v \in V$ can be written as $v = u + w$ for some $u \in U$ and $w \in W$. We must show this representation is unique.
Suppose there are two representations:

$$
v = u_1 + w_1
$$

and

$$
v = u_2 + w_2.
$$

Then

$$
u_1 + w_1 = u_2 + w_2
$$

, which rearranges to

$$
u_1 - u_2 = w_2 - w_1.
$$

Since $U$ is a subspace, $u_1 - u_2 \in U$. Since $W$ is a subspace, $w_2 - w_1 \in W$. Let

$$
x = u_1 - u_2 = w_2 - w_1
$$

. The vector $x$ belongs to both $U$ and $W$, so $x \in U \cap W$.
Since $U \cap W = \lbrace 0\rbrace$, it follows that $x = 0$.
Therefore,

$$
u_1 - u_2 = 0 \Rightarrow u_1 = u_2
$$

and

$$
w_2 - w_1 = 0 \Rightarrow w_1 = w_2.
$$

The representation is unique, meaning $V = U \oplus W$.

## Q14 (04)
**Question:** **Let $U = \text{span}\lbrace(1, 0, 0), (0, 1, 0)\rbrace$, $W = \text{span}\lbrace(0, 0, 1)\rbrace$. Show that

$$
\mathbb{R}^3 = U \oplus W
$$

.**

**Answer:**
To show

$$
\mathbb{R}^3 = U \oplus W
$$

, we must prove that

$$
\mathbb{R}^3 = U + W
$$

and $U \cap W = \lbrace 0\rbrace$.

1. **Show

$$
\mathbb{R}^3 = U + W
$$

:**
Any vector in $U$ is of the form $u = (x, y, 0)$ for some $x, y \in \mathbb{R}$. Any vector in $W$ is of the form $w = (0, 0, z)$ for some $z \in \mathbb{R}$. Then:

$$
u + w = (x, y, 0) + (0, 0, z) = (x, y, z)
$$

Since $x, y, z$ can be any real numbers, $U + W$ produces all of $\mathbb{R}^3$. Thus

$$
\mathbb{R}^3 = U + W.
$$

2. **Show $U \cap W = \lbrace 0\rbrace$:**
Let $v \in U \cap W$. Since $v \in U$, $v = (x, y, 0)$. Since $v \in W$, $v = (0, 0, z)$.
Equating them: $(x, y, 0) = (0, 0, z)$. This implies $x = 0, y = 0, z = 0$. So $v = (0, 0, 0)$. Thus $U \cap W = \lbrace 0\rbrace$.

Since both conditions hold,

$$
\mathbb{R}^3 = U \oplus W.
$$

## Q15 (03)
**Question:** **Give an example where $U + W \neq U \oplus W$.**

**Answer:**
Consider the vector space

$$
V = \mathbb{R}^2
$$

. Let $U = \text{span}\lbrace(1, 0)\rbrace$ and $W = \text{span}\lbrace(1, 0), (0, 1)\rbrace$. Here, $U$ is the x-axis, and $W$ is the entire $\mathbb{R}^2$ plane.

The sum $U + W$ consists of all vectors formed by adding a vector from $U$ to a vector from $W$. Since

$$
W = \mathbb{R}^2
$$

, adding vectors from $U$ simply results in $\mathbb{R}^2$. Thus,

$$
U + W = \mathbb{R}^2.
$$

However, the intersection $U \cap W$ is the set of vectors in both $U$ and $W$. Since $U \subset W$, their intersection is simply $U$.

$$
U \cap W = \text{span}\lbrace(1, 0)\rbrace \neq \lbrace(0, 0)\rbrace
$$

Because the intersection is not merely the zero vector, the sum is not a direct sum. Therefore, $U + W \neq U \oplus W$.