# Lecture 03: Vector Space - Vector Subspace

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 03 of 27
> **Video**: https://www.youtube.com/watch?v=5LCO26C-ggo

---

**Navigation**
[< Previous Lecture](02_General_Properties.md) | [Index](README.md) | [Next Lecture >](04_Intersection_Union_Subspaces.md)


---

## Prerequisites
We know the ten axioms required for a set to be a vector space $V(F)$. Checking all ten rules every time is tedious. This lecture introduces subspaces and a shortcut theorem for proving them. Think of a subspace just like a subgroup in group theory.

---

## Definition of a Vector Subspace
Suppose we have a vector space $V(F)$. Let $W$ be a subset of $V$ ($W \subseteq V$).

We say that $W$ is a **vector subspace** of $V$ if $W$ is itself a vector space under the exact same operations defined on $V$.

To be a subspace, $W$ must be a working vector space on its own. While this is the formal definition, we rarely check all vector space properties to prove a subset is a subspace. Instead, we use a single, powerful theorem.

---

## The One-Step Subspace Theorem

This theorem gives us a necessary and sufficient condition. It is the primary tool used to solve numerical questions about subspaces.

**Theorem Statement:**
A non-empty subset $W$ of a vector space $V(F)$ is a subspace of $V(F)$ if and only if for all scalars $a, b \in F$ and all vectors $\alpha, \beta \in W$, their linear combination belongs to $W$:

$$
a\alpha + b\beta \in W
$$

Because this is an "if and only if" theorem, the proof has two parts. We must show the condition is necessary (it must hold if $W$ is a subspace) and sufficient (if it holds, $W$ is guaranteed to be a subspace).

### Part 1: The Condition is Necessary
Let us assume $W$ is a vector subspace of $V(F)$.

Since $W$ is a subspace, it acts as a vector space in its own right. This means $W$ must be closed under scalar multiplication.
For any $\alpha \in W$ and $a \in F$:

$$
a\alpha \in W
$$

Similarly, for another vector $\beta \in W$ and scalar $b \in F$:

$$
b\beta \in W
$$

Because $W$ is a subspace, it must also be closed under vector addition. We can add our two new vectors $a\alpha$ and $b\beta$ together, and the sum must remain in $W$:

$$
a\alpha + b\beta \in W
$$

This proves the condition is necessary.

### Part 2: The Condition is Sufficient
Now we prove the reverse. We assume only that $W$ is a subset and the condition holds:
For all $a, b \in F$ and $\alpha, \beta \in W \Rightarrow a\alpha + b\beta \in W$. Let's call this Condition (1).

We must prove $W$ is a full vector space. We do this by choosing clever values for the scalars $a$ and $b$ to check off the vector space requirements.

**Step 1: Existence of Additive Inverse**
Put $a = 0$ and $b = -1$ into Condition (1):

$$
0\cdot\alpha + (-1)\cdot\beta = \bar{0} - \beta = -\beta \in W
$$

This shows that for every vector $\beta$ in $W$, its additive inverse $-\beta$ is also in $W$.

**Step 2: Existence of Zero Vector (Identity)**
Put $a = 0$ and $b = 0$ into Condition (1):

$$
0\cdot\alpha + 0\cdot\beta = \bar{0} + \bar{0} = \bar{0} \in W
$$

This proves the zero vector is in $W$.

**Step 3: Closure Under Vector Addition**
Put $a = 1$ and $b = 1$ into Condition (1):

$$
1\cdot\alpha + 1\cdot\beta = \alpha + \beta \in W
$$

This proves $W$ is closed under vector addition.

Since $W$ is closed under addition, has a zero vector, and contains additive inverses, $(W, +)$ is an abelian group. The commutative and associative laws for addition hold automatically because the elements in $W$ are also in $V$, where those laws already work.

**Step 4: Closure Under Scalar Multiplication**
Put $a = 0$ (and leave $b$ as any scalar) into Condition (1):

$$
0\cdot\alpha + b\cdot\beta = \bar{0} + b\beta = b\beta \in W
$$

This proves $W$ is closed under scalar multiplication.

Finally, the scalar distribution laws hold automatically in $W$ because they are inherited from the parent space $V$. Since $(W, +)$ is an abelian group, is closed under scalar multiplication, and inherits all distribution laws, $W$ is a vector space.

Therefore, $W$ is a subspace of $V(F)$. The proof is complete.

---

## Numerical Examples

How do we use this theorem in practice? We pick two arbitrary vectors from the subset and two scalars, form the linear combination $a\alpha + b\beta$, and check if the result matches the structural rule of the subset.

### Example 1: A Subspace of 3D Space
**Question:** Show that the set $W = \lbrace (x, y, 0) \mid x, y \in F \rbrace$ is a subspace of $V_3(F)$.

**Solution:**
The subset $W$ contains 3-tuples where the third coordinate is always exactly zero, and the first two coordinates are scalars from $F$.

Let us pick two vectors from $W$:

$$
\alpha = (x_1, y_1, 0) \quad \text{and} \quad \beta = (x_2, y_2, 0)
$$

And choose two scalars $a, b \in F$.

We form the linear combination:

$$
a\alpha + b\beta = a(x_1, y_1, 0) + b(x_2, y_2, 0)
$$

Multiply the scalars into the tuples:

$$
= (ax_1, ay_1, 0) + (bx_2, by_2, 0)
$$

Add the tuples coordinate by coordinate:

$$
= (ax_1 + bx_2, ay_1 + by_2, 0 + 0)
$$

$$
= (ax_1 + bx_2, ay_1 + by_2, 0)
$$

Now, we check the structure of our result. Since $F$ is a field, the sums and products of scalars are also scalars.
So, $(ax_1 + bx_2)$ is a scalar in $F$, and $(ay_1 + by_2)$ is a scalar in $F$.

The resulting tuple has two scalars in the first two positions, and a zero in the third position. This perfectly matches the rule for $W$.

$$
a\alpha + b\beta \in W
$$

Therefore, $W$ is a subspace of $V_3(F)$.

### Example 2: A Subspace of Matrices
**Question:** Show that the set $W = \left\lbrace \begin{pmatrix} x & y \\ -y & x \end{pmatrix} \mid x, y \in F \right\rbrace$ is a subspace of $M_2(F)$.

**Solution:**
$M_2(F)$ is the vector space of all $2 \times 2$ matrices. The subset $W$ has a specific rule: the diagonal elements must match each other, and the off-diagonal elements must be negatives of each other.

Pick two matrices from $W$:

$$
\alpha = \begin{pmatrix} x_1 & y_1 \\ -y_1 & x_1 \end{pmatrix} \quad \text{and} \quad \beta = \begin{pmatrix} x_2 & y_2 \\ -y_2 & x_2 \end{pmatrix}
$$

And pick scalars $a, b \in F$.

Form the combination:

$$
a\alpha + b\beta = a\begin{pmatrix} x_1 & y_1 \\ -y_1 & x_1 \end{pmatrix} + b\begin{pmatrix} x_2 & y_2 \\ -y_2 & x_2 \end{pmatrix}
$$

Multiply the scalars inside:

$$
= \begin{pmatrix} ax_1 & ay_1 \\ -ay_1 & ax_1 \end{pmatrix} + \begin{pmatrix} bx_2 & by_2 \\ -by_2 & bx_2 \end{pmatrix}
$$

Add the matrices element by element:

$$
= \begin{pmatrix} ax_1 + bx_2 & ay_1 + by_2 \\ -ay_1 - by_2 & ax_1 + bx_2 \end{pmatrix}
$$

Factor out the negative sign in the bottom-left corner to check the structure:

$$
= \begin{pmatrix} ax_1 + bx_2 & ay_1 + by_2 \\ -(ay_1 + by_2) & ax_1 + bx_2 \end{pmatrix}
$$

Look at the structure. The diagonal elements $(ax_1 + bx_2)$ are equal. The top-right element is $(ay_1 + by_2)$, and the bottom-left element is its negative. This perfectly matches the rule for $W$.

$$
a\alpha + b\beta \in W
$$

Therefore, $W$ is a subspace of $M_2(F)$.

---

## Key Takeaways
*   A **vector subspace** is a subset that behaves as a full vector space under the parent space's operations.
*   To prove a subset $W$ is a subspace, we use the one-step test: $a\alpha + b\beta \in W$.
*   We can prove the zero vector, additive inverses, and closure exist by cleverly substituting $0$, $1$, and $-1$ for the scalars $a$ and $b$ in the one-step test.
*   For numerical problems, always take two elements structured like $W$, combine them with scalars, and verify the resulting expression shares the exact same structure.

## What Comes Next
We will continue working with subspaces. In the next lecture, we will look at what happens when you combine two different subspaces using intersections and unions.

---

**Navigation**
[< Previous Lecture](02_General_Properties.md) | [Index](README.md) | [Next Lecture >](04_Intersection_Union_Subspaces.md)
