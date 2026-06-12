[← Previous: A06 Curvature and Torsion](A06_Curvature_Torsion_Frenet_Serret.md) | [Index](00_Index.md) | [Next: C02 Vector Subspaces →](C02_Vector_Subspace.md)

---

# C01: Vector Space Definition and Properties

> **Exam Weight**: Tier 1-2 | **Appeared in**: 2017, 2018, 2024 | **Typical Marks**: 2–8

A vector space is the fundamental structure of linear algebra. It is a set of elements (vectors) that can be scaled and added together according to specific mathematical rules.

---

## Formal Definition

Let $V$ be a non-empty set of objects called vectors. Let $K$ be a field of scalars (usually real numbers $\mathbb{R}$ or complex numbers $\mathbb{C}$). 

The set $V$ is a **vector space** over the field $K$ if it satisfies two closure conditions and eight axioms under vector addition and scalar multiplication:

**Closure Properties**:
1.  **Closure under Addition:** If $u, v \in V$, then $u + v \in V$.
2.  **Closure under Scalar Multiplication:** If $u \in V$ and $k \in K$, then $k u \in V$.

**Addition Axioms**:
3.  **Commutativity:** $u + v = v + u$
4.  **Associativity:** $(u + v) + w = u + (v + w)$
5.  **Additive Identity:** There exists a zero vector $0 \in V$ such that $u + 0 = u$.
6.  **Additive Inverse:** For every $u \in V$, there exists $-u \in V$ such that $u + (-u) = 0$.

**Scalar Multiplication Axioms**:
7.  **Distributivity (Scalar over Vector Addition):** $k(u + v) = ku + kv$
8.  **Distributivity (Vector over Scalar Addition):** $(a + b)u = au + bu$
9.  **Associativity of Multiplication:** $a(bu) = (ab)u$
10. **Unitary Identity:** $1u = u$, where $1$ is the multiplicative identity in $K$.

---

## Must-Know Proofs: Basic Properties (PYQ 2017)

You must be able to prove four basic properties of vector spaces using *only* the axioms above. This is an 8-mark question.

### Proof 1
We know $0 + 0 = 0$.
Multiply by scalar $k$: $k(0 + 0) = k0$.
By distributivity: $k0 + k0 = k0$.
Add the additive inverse $-(k0)$ to both sides:
$(k0 + k0) + (-(k0)) = k0 + (-(k0))$
$k0 + (k0 - k0) = 0$
$k0 + 0 = 0 \implies k0 = 0$. $\blacksquare$

### Proof 2
In the scalar field, $0 + 0 = 0$.
Multiply by vector $u$: $(0 + 0)u = 0u$.
By distributivity: $0u + 0u = 0u$.
Add the additive inverse $-(0u)$ to both sides:
$(0u + 0u) + (-(0u)) = 0u + (-(0u))$
$0u + (0u - 0u) = 0$
$0u + 0 = 0 \implies 0u = 0$. $\blacksquare$

### Proof 3: If, then or
Assume $ku = 0$. If $k = 0$, the statement holds.
If $k \neq 0$, then its multiplicative inverse $k^{-1}$ exists in the field $K$.
Multiply both sides by $k^{-1}$:

$$
k^{-1}(ku) = k^{-1}(0)
$$

By associativity and Proof 1:

$$
(k^{-1}k)u = 0
$$

$1u = 0$
By the unitary axiom: $u = 0$.
Thus, either $k=0$ or $u=0$. $\blacksquare$

### Proof 4
The vector $-ku$ is the unique additive inverse of $ku$, meaning $ku + (-ku) = 0$.
Show that $(-k)u$ is the additive inverse:
$ku + (-k)u = (k + (-k))u = 0u = 0$ (by Proof 2).
Thus, $(-k)u = -ku$.

Show that $k(-u)$ is the additive inverse:
$ku + k(-u) = k(u + (-u)) = k(0) = 0$ (by Proof 1).
Thus, $k(-u) = -ku$.
Therefore, $(-k)u = k(-u) = -ku$. $\blacksquare$

---

## Exam Patterns
- When asked to "define a vector space", you must list the properties clearly. Bullet points are fine, but be sure to mention the field $K$, the closure properties, and the 8 axioms.
- The 4-part proof from 2017 is a classic test of abstract algebra logic. Always explicitly state which axiom you are using at each step (e.g., "by distributivity").

---

[← Previous: A06 Curvature and Torsion](A06_Curvature_Torsion_Frenet_Serret.md) | [Index](00_Index.md) | [Next: C02 Vector Subspaces →](C02_Vector_Subspace.md)
