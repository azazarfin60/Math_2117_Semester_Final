# Lecture 15: Vector Space - Linear Transformation and its Properties

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 15 of 27
> **Video**: https://www.youtube.com/watch?v=EL3fXu9FFII

---

**Navigation**
[< Previous Lecture](14_Quotient_Space_Dimension.md) | [Index](README.md) | [Next Lecture >](16_Kernel_Homomorphism.md)

---

## Prerequisites
Until now, we have studied the internal structure of a single vector space (subspaces, span, basis, dimension). Now, we shift our focus to mappings *between* two different vector spaces.

Just as we study functions between sets in calculus, or homomorphisms between groups in group theory, we study **Linear Transformations** between vector spaces.

---

## Definition of Linear Transformation

Let $U(F)$ and $V(F)$ be two vector spaces over the same underlying field $F$.
A mapping $f : U \to V$ is called a **Linear Transformation** (or **Vector Space Homomorphism**) if it perfectly preserves the two fundamental operations of vector spaces: vector addition and scalar multiplication.

Specifically, it must satisfy two conditions:
1.  **Preservation of Addition**: For any two vectors $x, y \in U$:

$$
f(x + y) = f(x) + f(y)
$$

    *(Adding vectors first then mapping them gives the same result as mapping them first then adding them in the target space.)*

2.  **Preservation of Scalar Multiplication**: For any scalar $a \in F$ and any vector $x \in U$:

$$
f(ax) = a f(x)
$$

    *(Scaling a vector first then mapping it gives the same result as mapping it first then scaling it in the target space.)*

### The Combined Condition
Often, these two conditions are combined into a single, comprehensive rule. A mapping $f$ is a linear transformation if and only if:

$$
f(ax + by) = a f(x) + b f(y) \quad \text{for all } a, b \in F \text{ and } x, y \in U
$$

This means that a linear transformation perfectly preserves linear combinations.

---

## Verifying Linear Transformations

How do we prove if a given mapping is a linear transformation or not? We test the two conditions.

### Example 1: A Valid Linear Transformation
Let $T : V_3(\mathbb{R}) \to V_2(\mathbb{R})$ be defined by:

$$
T(x_1, x_2, x_3) = (x_1 - x_2, x_1 - x_3)
$$

**Check Condition 1 (Addition):**
Let $x = (x_1, x_2, x_3)$ and $y = (y_1, y_2, y_3)$.
Their sum is $x + y = (x_1 + y_1, x_2 + y_2, x_3 + y_3)$.
Apply $T$ to the sum:

$$
T(x + y) = ((x_1 + y_1) - (x_2 + y_2), (x_1 + y_1) - (x_3 + y_3))
$$

Rearrange the terms inside the coordinates:

$$
T(x + y) = (x_1 - x_2 + y_1 - y_2, x_1 - x_3 + y_1 - y_3)
$$

Split the tuple into two separate tuples:

$$
T(x + y) = (x_1 - x_2, x_1 - x_3) + (y_1 - y_2, y_1 - y_3)
$$

Notice that the first part is exactly $T(x)$ and the second part is exactly $T(y)$:

$$
T(x + y) = T(x) + T(y)
$$

Condition 1 holds.

**Check Condition 2 (Scalar Multiplication):**
Let $a \in \mathbb{R}$.
The scaled vector is $ax = (ax_1, ax_2, ax_3)$.
Apply $T$:

$$
T(ax) = (ax_1 - ax_2, ax_1 - ax_3)
$$

Factor out the scalar $a$ from both coordinates:

$$
T(ax) = a(x_1 - x_2, x_1 - x_3)
$$

This is exactly:

$$
T(ax) = a T(x)
$$

Condition 2 holds. Since both conditions are satisfied, $T$ is a linear transformation.

### Example 2: An Invalid Mapping
Consider $T : V_3(\mathbb{R}) \to \mathbb{R}$ defined by:

$$
T(x_1, x_2, x_3) = x_1^2 + x_2^2 + x_3^2
$$

Is this linear? No. Let's test the scalar multiplication condition.

$$
T(ax) = T(ax_1, ax_2, ax_3) = (ax_1)^2 + (ax_2)^2 + (ax_3)^2 = a^2(x_1^2 + x_2^2 + x_3^2) = a^2 T(x)
$$

Because $a^2 T(x) \neq a T(x)$, the mapping fails the scalar multiplication test.
**Tip:** Mappings involving squares, cubes, constant additions (like $+ 5$), or multiplying coordinates together (like $x_1 x_2$) are generally *not* linear transformations.

---

## Algebraic Properties of Linear Transformations

Because vector spaces are abelian groups under addition, linear transformations inherit several elegant properties. Let $f : U \to V$ be a linear transformation.

### Property 1: The Zero Vector Maps to the Zero Vector

$$
f(\bar{0}) = \bar{0}'
$$

*(Where $\bar{0}$ is the zero vector of $U$ and $\bar{0}'$ is the zero vector of $V$)*

**Proof:**
Let $\alpha \in U$. Then $f(\alpha) \in V$.
Add the zero vector of $V$ to $f(\alpha)$:

$$
f(\alpha) + \bar{0}' = f(\alpha)
$$

Now look at the domain $U$. Adding the zero vector changes nothing: $\alpha + \bar{0} = \alpha$.
Apply $f$ to both sides:

$$
f(\alpha + \bar{0}) = f(\alpha)
$$

Use the addition property of the linear transformation on the left side:

$$
f(\alpha) + f(\bar{0}) = f(\alpha)
$$

Equate our two expressions for $f(\alpha)$:

$$
f(\alpha) + \bar{0}' = f(\alpha) + f(\bar{0})
$$

By the cancellation law of groups, we cancel $f(\alpha)$ from both sides to get:

$$
\bar{0}' = f(\bar{0})
$$

### Property 2: Inverses Map to Inverses

$$
f(-\alpha) = -f(\alpha)
$$

**Proof:**
We know that in $U$:

$$
\alpha + (-\alpha) = \bar{0}
$$

Apply $f$ to both sides:

$$
f(\alpha + (-\alpha)) = f(\bar{0})
$$

We just proved $f(\bar{0}) = \bar{0}'$. And we can split the left side using the addition property:

$$
f(\alpha) + f(-\alpha) = \bar{0}'
$$

This equation states that adding $f(-\alpha)$ to $f(\alpha)$ results in the zero vector. By the definition of an additive inverse in a group, $f(-\alpha)$ must be the inverse of $f(\alpha)$. Thus:

$$
f(-\alpha) = -f(\alpha)
$$

### Property 3: Preservation of Subtraction

$$
f(\alpha - \beta) = f(\alpha) - f(\beta)
$$

**Proof:**
Rewrite the subtraction as the addition of an inverse:

$$
f(\alpha - \beta) = f(\alpha + (-\beta))
$$

Use the addition property:

$$
f(\alpha - \beta) = f(\alpha) + f(-\beta)
$$

Substitute the inverse property ($f(-\beta) = -f(\beta)$):

$$
f(\alpha - \beta) = f(\alpha) - f(\beta)
$$

## Key Takeaways
*   A **Linear Transformation** is a function between vector spaces that preserves vector addition and scalar multiplication ($f(ax + by) = af(x) + bf(y)$).
*   Formulas involving powers, constants, or coordinate multiplication are generally not linear.
*   Linear transformations always map the zero vector of the domain to the zero vector of the co-domain ($f(\bar{0}) = \bar{0}'$).
*   They preserve inverses and subtraction directly.

## What Comes Next
We will continue analyzing linear transformations by exploring two critical subspaces associated with them: the **Kernel** (or Null Space) and the **Image Space**.

---

**Navigation**
[< Previous Lecture](14_Quotient_Space_Dimension.md) | [Index](README.md) | [Next Lecture >](16_Kernel_Homomorphism.md)
