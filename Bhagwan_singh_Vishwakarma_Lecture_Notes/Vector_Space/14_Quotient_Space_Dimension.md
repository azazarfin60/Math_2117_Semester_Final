# Lecture 14: Vector Space - Dimension of Quotient Space

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 14 of 27
> **Video**: https://www.youtube.com/watch?v=HZxJtGqkJLM

---

**Navigation**
[< Previous Lecture](13_Dimension_Sum_Proof.md) | [Index](README.md) | [Next Lecture >](15_Linear_Transformation.md)

---

## Prerequisites
We are familiar with vector subspaces and their dimensions. Today, we will introduce a new mathematical structure built from a vector space and its subspace, known as a **Quotient Space**. We will define its operations and prove a fundamental theorem regarding its dimension.

---

## Understanding Quotient Spaces

Let $V(F)$ be a vector space, and let $W$ be a subspace of $V$. 
A quotient space is built by grouping vectors of $V$ into "slices" or "cosets" based on the subspace $W$.

**Definition:** The quotient space $V/W$ is the set of all cosets of $W$ in $V$.

$$
V/W = \lbrace W + \alpha \mid \alpha \in V \rbrace
$$

Here, $W + \alpha$ is a coset formed by taking every vector in $W$ and adding the specific vector $\alpha$ to it. You can think of it as shifting the entire subspace $W$ by the vector $\alpha$.

### Operations in
To make $V/W$ a vector space itself, we must define vector addition and scalar multiplication for these cosets.

1.  **Vector Addition**: To add two cosets, you simply add their representative vectors.

$$
(W + \alpha) + (W + \beta) = W + (\alpha + \beta)
$$

2.  **Scalar Multiplication**: To scale a coset, you scale its representative vector.

$$
a(W + \alpha) = W + a\alpha
$$

**The Identity Element (The Zero Vector):**
In standard vector spaces, adding the zero vector changes nothing ($\alpha + \bar{0} = \alpha$).
In the quotient space $V/W$, the "zero vector" is the subspace $W$ itself (which is the same as $W + \bar{0}$).
If you add $W$ to any coset, nothing changes:

$$
W + (W + \alpha) = (W + W) + \alpha = W + \alpha
$$

Thus, $W$ is the additive identity of the quotient space.

---

## The Dimension of a Quotient Space

Since $V/W$ is a vector space, it has a dimension. How is its dimension related to the dimensions of $V$ and $W$?

**Theorem:** If $W$ is a subspace of a finite-dimensional vector space $V(F)$, then:

$$
\dim(V/W) = \dim(V) - \dim(W)
$$

### Proof:

**Step 1: Setup Bases for $W$ and $V$**
Let $\dim(W) = n$. This means $W$ has a basis $S$ with $n$ elements:

$$
S = \lbrace \beta_1, \beta_2, \dots, \beta_n \rbrace
$$

Because $S$ is linearly independent in $V$, we can use the Extension Theorem to extend it to a full basis for $V$ by adding $m$ new vectors:

$$
S' = \lbrace \beta_1, \dots, \beta_n, \alpha_1, \alpha_2, \dots, \alpha_m \rbrace
$$

Because $S'$ has $n + m$ elements, we know $\dim(V) = n + m$.

If we look at the formula we want to prove:

$$
\dim(V) - \dim(W) = (n + m) - n = m
$$

We need to prove that $\dim(V/W) = m$. To do this, we must find a basis for $V/W$ that has exactly $m$ elements.

**Step 2: Propose a Basis for $V/W$**
We propose that the cosets formed by the newly added $\alpha$ vectors form the basis for $V/W$.

$$
S_1 = \lbrace W + \alpha_1, W + \alpha_2, \dots, W + \alpha_m \rbrace
$$

We must prove that $S_1$ is linearly independent and that it spans $V/W$.

**Step 3: Prove $S_1$ is Linearly Independent**
Set a linear combination of the elements of $S_1$ to the zero element of the quotient space (which is $W$):

$$
a_1(W + \alpha_1) + a_2(W + \alpha_2) + \dots + a_m(W + \alpha_m) = W
$$

Apply the operations of scalar multiplication and addition:

$$
W + (a_1\alpha_1 + a_2\alpha_2 + \dots + a_m\alpha_m) = W
$$

We know from group theory that $H + x = H$ if and only if $x \in H$. Therefore, the vector inside the parenthesis must belong to $W$:

$$
a_1\alpha_1 + a_2\alpha_2 + \dots + a_m\alpha_m \in W
$$

Since it belongs to $W$, it can be written as a linear combination of the basis vectors of $W$ (the $\beta$ vectors):

$$
a_1\alpha_1 + \dots + a_m\alpha_m = b_1\beta_1 + \dots + b_n\beta_n \quad \text{(for some scalars } b_i)
$$

Bring all terms to one side:

$$
a_1\alpha_1 + \dots + a_m\alpha_m - b_1\beta_1 - \dots - b_n\beta_n = \bar{0}
$$

This is a combination of vectors from $S'$ equating to zero. Because $S'$ is the basis of $V$, its vectors are linearly independent. Thus, every single scalar in this equation must be exactly zero:

$$
a_1 = \dots = a_m = 0 \quad \text{and} \quad b_1 = \dots = b_n = 0
$$

Because all $a_i = 0$, our set of cosets $S_1$ is linearly independent.

**Step 4: Prove $S_1$ Spans $V/W$**
Take any arbitrary coset $W + \alpha \in V/W$.
Because $\alpha \in V$, we can write $\alpha$ using the basis $S'$:

$$
\alpha = (a_1\alpha_1 + \dots + a_m\alpha_m) + (b_1\beta_1 + \dots + b_n\beta_n)
$$

Let the second grouped part be $w = b_1\beta_1 + \dots + b_n\beta_n$. Since this is built only from $\beta$ vectors, $w \in W$.
So, $\alpha = a_1\alpha_1 + \dots + a_m\alpha_m + w$.

Now substitute this into our coset:

$$
W + \alpha = W + (a_1\alpha_1 + \dots + a_m\alpha_m + w)
$$

Because $w \in W$, adding it to $W$ absorbs it ($W + w = W$):

$$
W + \alpha = W + (a_1\alpha_1 + \dots + a_m\alpha_m)
$$

Using our quotient space operations, we can break this apart:

$$
W + \alpha = a_1(W + \alpha_1) + a_2(W + \alpha_2) + \dots + a_m(W + \alpha_m)
$$

This proves that any coset $W + \alpha$ can be built as a linear combination of the elements in $S_1$. Thus, $S_1$ spans $V/W$.

Because $S_1$ is independent and spans $V/W$, it is a basis. Because $S_1$ has $m$ elements:

$$
\dim(V/W) = m = \dim(V) - \dim(W)
$$

---

## Numerical Application: Dimensions of Sums and Intersections
Let's use our skills to solve a matrix rank problem relating to subspace dimensions.

**Question:** Let $W_1$ and $W_2$ be two subspaces of $V_4(\mathbb{R})$.
$W_1$ is generated by $S_1 = \lbrace (1, 1, 0, -1), (1, 2, 3, 0), (2, 3, 3, -1) \rbrace$
$W_2$ is generated by $S_2 = \lbrace (1, 2, 2, -2), (2, 3, 2, -3), (1, 3, 4, -3) \rbrace$
Find $\dim(W_1 + W_2)$ and $\dim(W_1 \cap W_2)$.

**Solution:**
The dimension of a subspace generated by a set of vectors is exactly equal to the rank of the matrix formed by those vectors.

1.  **Find $\dim(W_1)$**:
    Place the vectors of $S_1$ into a matrix and reduce to Echelon form:

$$
A = \begin{bmatrix} 1 & 1 & 0 & -1 \\ 1 & 2 & 3 & 0 \\ 2 & 3 & 3 & -1 \end{bmatrix} \to \begin{bmatrix} 1 & 1 & 0 & -1 \\ 0 & 1 & 3 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

    Since there are 2 non-zero rows, Rank($A$) = 2. Thus, $\dim(W_1) = 2$.

2.  **Find $\dim(W_2)$**:
    Place vectors of $S_2$ into a matrix:

$$
B = \begin{bmatrix} 1 & 2 & 2 & -2 \\ 2 & 3 & 2 & -3 \\ 1 & 3 & 4 & -3 \end{bmatrix} \to \begin{bmatrix} 1 & 2 & 2 & -2 \\ 0 & -1 & -2 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}
$$

    Rank($B$) = 2. Thus, $\dim(W_2) = 2$.

3.  **Find $\dim(W_1 + W_2)$**:
    The subspace $W_1 + W_2$ is generated by combining *all* the vectors from $S_1$ and $S_2$. We place all 6 vectors into a large $6 \times 4$ matrix. Upon reducing this matrix to Echelon form, we find the rank is 3.
    Thus, $\dim(W_1 + W_2) = 3$.

4.  **Find $\dim(W_1 \cap W_2)$**:
    We use the dimension sum theorem:

$$
\dim(W_1 + W_2) = \dim(W_1) + \dim(W_2) - \dim(W_1 \cap W_2)
$$

$$
3 = 2 + 2 - \dim(W_1 \cap W_2)
$$

$$
\dim(W_1 \cap W_2) = 4 - 3 = 1
$$

## What Comes Next
We have completed our extensive look into the structural dimensions of vector spaces, subspaces, and quotient spaces. Next, we will introduce **Linear Transformations**, which are functions that map vectors from one space to another while preserving their linear structure.

---

**Navigation**
[< Previous Lecture](13_Dimension_Sum_Proof.md) | [Index](README.md) | [Next Lecture >](15_Linear_Transformation.md)
