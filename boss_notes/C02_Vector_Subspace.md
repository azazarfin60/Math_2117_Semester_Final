[← Previous: C01 Vector Space Fundamentals](C01_Field_Axioms_Vector_Space_Definition.md) | [Index](00_Index.md) | [Next: C03 Direct Sums →](C03_Sum_Direct_Sum_Subspaces.md)

---

# C02: Vector Subspaces

> **Exam Weight**: Tier 2 | **Appeared in**: 2017, 2018, 2024 | **Typical Marks**: 3–4

A subspace is a smaller vector space entirely contained within a larger one. 

---

## Definition of a Subspace

Let $W$ be a non-empty subset of a vector space $V$ over a field $K$. $W$ is called a **subspace** of $V$ if $W$ is itself a vector space under the same vector addition and scalar multiplication defined on $V$.

### The Subspace Test
To prove that a subset $W$ is a subspace, you do *not* need to check all 10 vector space axioms. You only need to verify three things:

1.  **Non-empty / Zero Vector**: The zero vector of $V$ must be in $W$ ($0 \in W$).
2.  **Closed under Addition**: For any vectors $u, v \in W$, their sum must also be in $W$ ($u + v \in W$).
3.  **Closed under Scalar Multiplication**: For any vector $u \in W$ and any scalar $k \in K$, the scaled vector must also be in $W$ ($ku \in W$).

*Note: Conditions 2 and 3 are sometimes combined into a single condition: For any scalars $a,b$ and vectors $u,v$, $au + bv \in W$.*

---

## Worked Example: Subspace Verification (PYQ 2024)

**Problem**: Let $U$ consist of all vectors in $\mathbb{R}^3$ whose entries are equal, that is $U = \lbrace(a, b, c) \mid a = b = c\rbrace$. Prove that $U$ is a vector space over $\mathbb{R}$.

**Solution**:
Since $U$ is a subset of the known vector space $\mathbb{R}^3$, we only need to show it is a subspace. We apply the subspace test.

**Step 1: Contains the Zero Vector**
The zero vector of $\mathbb{R}^3$ is $(0, 0, 0)$. Since $0 = 0 = 0$ satisfies the condition $a=b=c$, the zero vector is in $U$.

**Step 2: Closed Under Addition**
Let $u_1 = (a_1, a_1, a_1) \in U$ and $u_2 = (a_2, a_2, a_2) \in U$.
We add these vectors:

$$
u_1 + u_2 = (a_1 + a_2, a_1 + a_2, a_1 + a_2)
$$

Since all three components of the sum vector are identical (equal to $a_1 + a_2$), the sum vector is in $U$.

**Step 3: Closed Under Scalar Multiplication**
Let $u = (a, a, a) \in U$ and $k \in \mathbb{R}$ be a scalar.
We multiply the vector by the scalar:

$$
k u = (ka, ka, ka)
$$

Since all three components are identical (equal to $ka$), this vector is in $U$.

Since $U$ satisfies all three conditions, it is a subspace of $\mathbb{R}^3$. Because a subspace is itself a vector space, $U$ is a vector space over $\mathbb{R}$. $\blacksquare$

---

## Common Examples of Subspaces

- **Trivial Subspaces**: For any vector space $V$, the set containing only the zero vector $\lbrace 0\rbrace$ and the entire space $V$ itself are both subspaces.
- **Lines and Planes**: In $\mathbb{R}^3$, any line that passes through the origin is a subspace. Any flat plane that passes through the origin (e.g., $z=0$) is a subspace.
  *Warning: If a line or plane does NOT pass through the origin (e.g., $z=5$), it is NOT a subspace because it fails the zero vector test.*

---

## Exam Patterns
- When asked to prove something is a vector space, usually it is a subset of a known space (like $\mathbb{R}^n$ or the space of polynomials). Do not list all 10 axioms; just use the 3-step subspace test.
- Always check the zero vector first. It is the easiest way to prove a set is *not* a subspace. If plugging in zeros for the variables breaks the given condition, you're done.

---

[← Previous: C01 Vector Space Fundamentals](C01_Field_Axioms_Vector_Space_Definition.md) | [Index](00_Index.md) | [Next: C03 Direct Sums →](C03_Sum_Direct_Sum_Subspaces.md)
