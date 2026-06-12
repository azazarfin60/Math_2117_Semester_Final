[← Previous: C02 Vector Subspaces](C02_Vector_Subspace.md) | [Index](00_Index.md) | [Next: C04 Linear Dependence →](C04_Linear_Dependence_Independence.md)

---

# C03: Sum and Direct Sum of Subspaces

> **Exam Weight**: Tier 1-2 | **Appeared in**: 2019, 2023, 2024 | **Typical Marks**: 2–6

When you have multiple subspaces within a vector space, you can combine them. The most important way to combine them is via a "Direct Sum", which guarantees a unique decomposition of vectors.

---

## Definitions and Examples

**Sum of Subspaces ($U + W$)**: 
Let $U$ and $W$ be subspaces of a vector space $V$. The sum $U + W$ is the set of all possible vectors $u + w$ where $u \in U$ and $w \in W$.
- *Example*: In $\mathbb{R}^2$, let $U$ be the $x$-axis and $W$ be the line $y=x$. Their sum $U+W$ covers the entire $\mathbb{R}^2$ plane.

**Direct Sum ($U \oplus W$)**: 
The sum $U + W$ is called a **direct sum** (written $U \oplus W$) if every element in the sum can be written *uniquely* as $u + w$.
- This occurs if and only if the only vector shared by both subspaces is the zero vector: $U \cap W = \lbrace 0\rbrace$.
- *Example*: In $\mathbb{R}^2$, let $U$ be the $x$-axis (vectors $(x,0)$) and $W$ be the $y$-axis (vectors $(0,y)$). Their intersection is only the origin $(0,0)$. Thus, $\mathbb{R}^2 = U \oplus W$, because any vector $(x,y)$ has exactly one decomposition: $(x,0) + (0,y)$.

---

## Must-Know Proof (PYQ 2019)

**Problem**: Prove that the vector space $V$ is the direct sum of its subspaces $U$ and $W$ if and only if (i) $V = U + W$, and (ii) $U \cap W = \lbrace 0\rbrace$.

**Proof**:

**Part 1: Forward Direction ($\implies$)**
Assume $V$ is the direct sum of $U$ and $W$ ($V = U \oplus W$).
By definition, every vector $v \in V$ can be *uniquely* written as $v = u + w$ (where $u \in U, w \in W$).
- Since every $v$ can be written as $u+w$, we have $V = U + W$.
- To prove $U \cap W = \lbrace 0\rbrace$, let $v \in U \cap W$.
  Since $v \in U$, we can write it as $v = v + 0$ (where $v \in U$ and $0 \in W$).
  Since $v \in W$, we can write it as $v = 0 + v$ (where $0 \in U$ and $v \in W$).
  Because the decomposition must be unique, these two expressions must be identical. Therefore, $v = 0$.
  Thus, $U \cap W = \lbrace 0\rbrace$.

**Part 2: Reverse Direction ($\impliedby$)**
Assume (i) $V = U + W$ and (ii) $U \cap W = \lbrace 0\rbrace$.
Since $V = U + W$, every $v \in V$ can be written as $v = u + w$. We must show this representation is unique.
Suppose $v$ can be represented in two ways:

$$
v = u_1 + w_1 \quad \text{and} \quad v = u_2 + w_2
$$

Equating them:

$$
u_1 + w_1 = u_2 + w_2 \implies u_1 - u_2 = w_2 - w_1
$$

Let this new vector be $x$.
Because $U$ is a subspace, $x = u_1 - u_2 \in U$.
Because $W$ is a subspace, $x = w_2 - w_1 \in W$.
Therefore, $x \in U \cap W$.
But we are given $U \cap W = \lbrace 0\rbrace$. Thus, $x = 0$.

$$
u_1 - u_2 = 0 \implies u_1 = u_2
$$

$$
w_2 - w_1 = 0 \implies w_1 = w_2
$$

Since the components are identical, the representation is unique. Therefore, $V = U \oplus W$. $\blacksquare$

---

## Exam Patterns
- The proof above is a highly standard 6-mark linear algebra theorem. Memorize the trick for the forward direction ($v=v+0$ vs $v=0+v$) and the reverse direction ($u_1-u_2 = w_2-w_1$).
- When asked to "define" direct sum for 2 marks, always include the mathematical condition $U \cap W = \lbrace 0\rbrace$ and provide the $x$-axis / $y$-axis example in $\mathbb{R}^2$ for full credit.

---

[← Previous: C02 Vector Subspaces](C02_Vector_Subspace.md) | [Index](00_Index.md) | [Next: C04 Linear Dependence →](C04_Linear_Dependence_Independence.md)
