# Lecture 21: Vector Space - Rank-Nullity Theorem

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 21 of 27
> **Video**: https://www.youtube.com/watch?v=HnFFuXDi9p8

---

**Navigation**
[< Previous Lecture](20_Inverse_Linear_Transformation.md) | [Index](README.md) | [Next Lecture >](22_Invertible_Singular_Nonsingular.md)

---

## Prerequisites
We know that a linear transformation $T : U \to V$ comes with two critical subspaces: the **Range Space** ($R(T)$, living in $V$) and the **Null Space** ($N(T)$ or Kernel, living in $U$). Today, we will study one of the most celebrated theorems in linear algebra, which reveals a deep dimensional relationship between these two spaces and the domain itself.

---

## Definitions: Rank and Nullity

Let $T : U \to V$ be a linear transformation, and let $U$ be a finite-dimensional vector space.

### 1. The Rank
The range space $R(T)$ is a subspace of $V$. Because it is a subspace, it has a dimension. The **Rank** of $T$, denoted as $\rho(T)$, is simply the dimension of its range space.

$$
\text{Rank}(T) = \rho(T) = \dim(R(T))
$$

### 2. The Nullity
The null space $N(T)$ is a subspace of $U$. Because it is a subspace, it also has a dimension. The **Nullity** of $T$, denoted as $\nu(T)$, is the dimension of its null space.

$$
\text{Nullity}(T) = \nu(T) = \dim(N(T))
$$

*Conceptually: The nullity measures how much "information" the transformation crushes to zero, while the rank measures the number of actual "dimensions" the transformation preserves in the output.*

---

## The Rank-Nullity Theorem

**Statement:** Let $T : U \to V$ be a linear transformation from a finite-dimensional vector space $U$ into a vector space $V$. Then, the sum of the rank and the nullity of $T$ is equal to the dimension of the domain $U$.

$$
\text{Rank}(T) + \text{Nullity}(T) = \dim(U)
$$

### Proof

Let $\dim(U) = n$.
Because $N(T)$ is a subspace of $U$, its dimension must be less than or equal to $n$. Let its dimension be $k$:

$$
\dim(N(T)) = k \quad (k \le n)
$$

Let

$$
S = \lbrace \alpha_1, \alpha_2, \dots, \alpha_k \rbrace
$$

be a basis for the null space $N(T)$.
Because $S$ is a basis, it is a linearly independent set within $U$. By the **Basis Extension Theorem**, any linearly independent set can be extended to form a basis of the entire vector space.
Let's extend $S$ to form a basis $S'$ for the entire domain $U$:

$$
S' = \lbrace \alpha_1, \alpha_2, \dots, \alpha_k, \alpha_{k+1}, \dots, \alpha_n \rbrace
$$

Our goal is to prove that the rank (the dimension of $R(T)$) is exactly $n - k$. To do this, we will prove that the images of the *extended* basis vectors:

$$
B' = \lbrace T(\alpha_{k+1}), T(\alpha_{k+2}), \dots, T(\alpha_n) \rbrace
$$

form a basis for $R(T)$. We must show they span $R(T)$ and are linearly independent.

#### Step 1: Prove Spans
Let $\beta \in R(T)$. By definition, there exists an $\alpha \in U$ such that $T(\alpha) = \beta$.
Because $S'$ is a basis for $U$, we can express $\alpha$ as a linear combination of $S'$:

$$
\alpha = a_1\alpha_1 + \dots + a_k\alpha_k + a_{k+1}\alpha_{k+1} + \dots + a_n\alpha_n
$$

Apply $T$ to both sides:

$$
\beta = T(a_1\alpha_1 + \dots + a_k\alpha_k + a_{k+1}\alpha_{k+1} + \dots + a_n\alpha_n)
$$

Because $T$ is linear, we can pull the scalars out:

$$
\beta = a_1 T(\alpha_1) + \dots + a_k T(\alpha_k) + a_{k+1} T(\alpha_{k+1}) + \dots + a_n T(\alpha_n)
$$

But wait! The vectors $\alpha_1, \dots, \alpha_k$ belong to the null space. This means their images $T(\alpha_i)$ are all the zero vector ($\bar{0}'$). The first $k$ terms completely vanish:

$$
\beta = a_1(\bar{0}') + \dots + a_k(\bar{0}') + a_{k+1} T(\alpha_{k+1}) + \dots + a_n T(\alpha_n)
$$

$$
\beta = a_{k+1} T(\alpha_{k+1}) + \dots + a_n T(\alpha_n)
$$

This proves that *any* vector $\beta \in R(T)$ can be built using only the vectors in $B'$. Therefore, $B'$ spans $R(T)$.

#### Step 2: Prove is Linearly Independent
Set a linear combination of $B'$ equal to the zero vector of $V$:

$$
b_{k+1} T(\alpha_{k+1}) + \dots + b_n T(\alpha_n) = \bar{0}'
$$

Because $T$ is linear, we pull $T$ outside:

$$
T(b_{k+1}\alpha_{k+1} + \dots + b_n\alpha_n) = \bar{0}'
$$

This equation states that the image of the vector

$$
(b_{k+1}\alpha_{k+1} + \dots + b_n\alpha_n)
$$

is the zero vector. By definition, this vector *must* belong to the null space $N(T)$:

$$
b_{k+1}\alpha_{k+1} + \dots + b_n\alpha_n \in N(T)
$$

Because it is in the null space, it can be written as a linear combination of the null space's basis $S$:

$$
b_{k+1}\alpha_{k+1} + \dots + b_n\alpha_n = c_1\alpha_1 + \dots + c_k\alpha_k
$$

Bring all terms to one side:

$$
-c_1\alpha_1 - \dots - c_k\alpha_k + b_{k+1}\alpha_{k+1} + \dots + b_n\alpha_n = \bar{0}
$$

Look at the vectors in this equation: they are exactly the basis vectors of $S'$. Because $S'$ is a basis for $U$, it is a linearly independent set. The *only* way a linear combination of linearly independent vectors equals zero is if every single scalar is zero.

$$
-c_1 = \dots = -c_k = 0 \quad \text{and} \quad b_{k+1} = \dots = b_n = 0
$$

Because

$$
b_{k+1} = \dots = b_n = 0
$$

, the set $B'$ is linearly independent.

#### Step 3: Conclusion
Since $B'$ spans $R(T)$ and is linearly independent, it is a basis for $R(T)$.
Count the vectors in $B'$: there are $(n - k)$ vectors.

$$
\dim(R(T)) = n - k
$$

By definition:

$$
\text{Rank}(T) = n - k
$$

Finally, add the rank and the nullity:

$$
\text{Rank}(T) + \text{Nullity}(T) = (n - k) + k = n
$$

Since $n = \dim(U)$, the theorem is proven:

$$
\text{Rank}(T) + \text{Nullity}(T) = \dim(U)
$$

## Key Takeaways
*   The **Rank-Nullity Theorem** proves that the dimensions of the domain are strictly conserved across a linear mapping.
*   If a transformation crushes a lot of dimensions to zero (high nullity), it must result in a "flattened" output with fewer dimensions (low rank). The total dimensions are always preserved.

## What Comes Next
We will explore the implications of this theorem, define singular and non-singular transformations more formally, and solve numerical problems using the rank-nullity relation.

---

**Navigation**
[< Previous Lecture](20_Inverse_Linear_Transformation.md) | [Index](README.md) | [Next Lecture >](22_Invertible_Singular_Nonsingular.md)
