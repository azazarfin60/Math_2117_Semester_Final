[← Previous: C07 Linear Transformations](C07_Linear_Transformation_Definition.md) | [Index](00_Index.md) | [Next: C09 Matrix Representation →](C09_Matrix_Representation_Change_of_Basis.md)

---

# C08: Kernel, Image, Rank, and Nullity

> **Exam Weight**: Tier 1-2 | **Appeared in**: 2019 | **Typical Marks**: 6

Every linear mapping $F: V \to U$ is associated with two crucial subspaces: the Kernel (inside the domain $V$) and the Image (inside the codomain $U$).

---

## Definitions

- **Kernel (Null Space)**: The set of all vectors in $V$ that map exactly to the zero vector in $U$.

$$
\text{Ker}(F) = \lbrace v \in V \mid F(v) = 0_U \rbrace
$$

- **Image (Range Space)**: The set of all vectors in $U$ that are "hit" by the mapping (i.e., they have at least one pre-image in $V$).

$$
\text{Im}(F) = \lbrace u \in U \mid \exists v \in V \text{ such that } F(v) = u \rbrace
$$

---

## Must-Know Proof (PYQ 2019)

**Problem**: Let $F : V \to U$ be a linear mapping. Show that the Kernel of $F$ is a subspace of $V$ and the Image of $F$ is a subspace of $U$.

**Part 1: Prove $\text{Ker}(F)$ is a subspace of $V$**
We must verify the three subspace properties for $\text{Ker}(F)$:
1. **Zero Vector**: Since $F$ is linear, $F(0_V) = 0_U$. Therefore, $0_V \in \text{Ker}(F)$.
2. **Closure under Addition**: Let $v_1, v_2 \in \text{Ker}(F)$. By definition, $F(v_1) = 0_U$ and $F(v_2) = 0_U$.
   $F(v_1 + v_2) = F(v_1) + F(v_2) = 0_U + 0_U = 0_U$. Thus, $v_1 + v_2 \in \text{Ker}(F)$.
3. **Closure under Scalar Multiplication**: Let $v \in \text{Ker}(F)$ and let $k$ be a scalar.
   $F(kv) = kF(v) = k(0_U) = 0_U$. Thus, $kv \in \text{Ker}(F)$.
Since all three hold, $\text{Ker}(F)$ is a subspace. $\blacksquare$

**Part 2: Prove $\text{Im}(F)$ is a subspace of $U$**
We must verify the three subspace properties for $\text{Im}(F)$:
1. **Zero Vector**: Since $F(0_V) = 0_U$, the zero vector $0_U$ has a pre-image. Thus, $0_U \in \text{Im}(F)$.
2. **Closure under Addition**: Let $u_1, u_2 \in \text{Im}(F)$. Then there exist $v_1, v_2 \in V$ such that $F(v_1) = u_1$ and $F(v_2) = u_2$.
   $u_1 + u_2 = F(v_1) + F(v_2) = F(v_1 + v_2)$. 
   Since $v_1 + v_2 \in V$, the sum $u_1 + u_2$ is the image of a vector in $V$. Thus, $u_1 + u_2 \in \text{Im}(F)$.
3. **Closure under Scalar Multiplication**: Let $u \in \text{Im}(F)$ and let $k$ be a scalar. There exists $v \in V$ such that $F(v) = u$.
   $ku = kF(v) = F(kv)$.
   Since $kv \in V$, $ku$ is the image of a vector in $V$. Thus, $ku \in \text{Im}(F)$.
Since all three hold, $\text{Im}(F)$ is a subspace. $\blacksquare$

---

## Rank-Nullity Theorem

The dimensions of these two subspaces are given special names:
- **Nullity**: The dimension of the Kernel.
- **Rank**: The dimension of the Image.

The Rank-Nullity Theorem states that for any linear mapping $F: V \to U$, the dimensions perfectly balance out to equal the dimension of the starting domain $V$:

$$
\dim(\text{Ker}(F)) + \dim(\text{Im}(F)) = \dim(V)
$$

$$
\text{Nullity} + \text{Rank} = \dim(V)
$$

---

## Exam Patterns
- The proof that the Kernel and Image are subspaces is a classic 6-mark theoretical question. Memorize the 3-step subspace check for both.
- If asked to find the Kernel of a matrix mapping, set the matrix times a vector $\vec{x}$ to the zero vector:

$$
A\vec{x} = 0
$$

Then solve for $\vec{x}$ using row reduction.

---

[← Previous: C07 Linear Transformations](C07_Linear_Transformation_Definition.md) | [Index](00_Index.md) | [Next: C09 Matrix Representation →](C09_Matrix_Representation_Change_of_Basis.md)
