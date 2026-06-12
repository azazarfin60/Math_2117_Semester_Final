[← Previous: C06 Basis and Dimension](C06_Basis_Dimension_Extension.md) | [Index](00_Index.md) | [Next: C08 Kernel and Image →](C08_Kernel_Image_Rank_Nullity.md)

---

# C07: Linear Transformations

> **Exam Weight**: Tier 3 | **Appeared in**: 2023 | **Typical Marks**: 4

A linear transformation (or mapping) is a function between two vector spaces that preserves the operations of vector addition and scalar multiplication.

---

## The Linearity Conditions

Let $V$ and $U$ be vector spaces over the same field $K$. A function $F: V \to U$ is a **linear mapping** if for all vectors $u, v \in V$ and all scalars $k \in K$:

1.  **Preservation of Addition**: $F(u + v) = F(u) + F(v)$
2.  **Preservation of Scalar Multiplication**: $F(ku) = kF(u)$

*Shortcut*: These two conditions can be combined into one: $F(au + bv) = aF(u) + bF(v)$.

**Crucial Property**: Any linear transformation MUST map the zero vector of the domain to the zero vector of the codomain. If $F(0_V) \neq 0_U$, the mapping is definitely not linear.

---

## Worked Example: Verifying Linearity (PYQ 2023)

**Problem**: Identify if the following mappings $F$ are linear or not linear:
(i) $F : \mathbb{R}^3 \to \mathbb{R}$ defined by $F(x, y, z) = 2x - 3y + 4z$
(ii) $F : \mathbb{R}^2 \to \mathbb{R}^3$ defined by $F(x, y) = (x+1, 2y, x+y)$

**Solution**:

**(i) Mapping $F(x, y, z) = 2x - 3y + 4z$**
Let $u = (x_1, y_1, z_1)$ and $v = (x_2, y_2, z_2)$.
*Check Addition*:

$$
F(u + v) = F(x_1 + x_2, y_1 + y_2, z_1 + z_2) = 2(x_1 + x_2) - 3(y_1 + y_2) + 4(z_1 + z_2)
$$

$$
F(u + v) = (2x_1 - 3y_1 + 4z_1) + (2x_2 - 3y_2 + 4z_2) = F(u) + F(v)
$$

*Check Scalar Multiplication*:

$$
F(ku) = F(kx_1, ky_1, kz_1) = 2(kx_1) - 3(ky_1) + 4(kz_1) = k(2x_1 - 3y_1 + 4z_1) = kF(u)
$$

Both conditions hold. The mapping is **linear**.

**(ii) Mapping $F(x, y) = (x+1, 2y, x+y)$**
We use the zero-vector shortcut. A linear mapping must map the zero vector $(0,0)$ to the zero vector $(0,0,0)$.

$$
F(0, 0) = (0 + 1, 2(0), 0 + 0) = (1, 0, 0) \neq (0, 0, 0)
$$

Since $F(0_V) \neq 0_U$, the mapping is **not linear**.

---

## Exam Patterns
- When given a function with a constant addition term (like $x+1$), it is automatically non-linear because it is an "affine" shift, not a linear one. Use the $F(0) \neq 0$ trick to prove it in one line.
- For functions without constants (like $2x-3y$), you must grind out the full $F(u+v)$ and $F(ku)$ proofs.

---

[← Previous: C06 Basis and Dimension](C06_Basis_Dimension_Extension.md) | [Index](00_Index.md) | [Next: C08 Kernel and Image →](C08_Kernel_Image_Rank_Nullity.md)
