# Lecture 02: Vector Space - General Properties

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 02 of 27
> **Video**: https://www.youtube.com/watch?v=yzuoyA2EJPA

---

**Navigation**
[< Previous Lecture](01_Vector_Space_Definition.md) | [Index](README.md) | [Next Lecture >](03_Vector_Subspace.md)

---

## Prerequisites
We already know that a vector space $V(F)$ requires a set of vectors $V$ and a set of scalars $F$. The vectors form an abelian group under addition. They also follow specific distribution and closure rules when multiplied by scalars from $F$.

## Notation: Zero Vector vs. Zero Scalar
Before we prove anything, we must be clear about zeros.
*   We use $\bar{0}$ to represent the **zero vector** in $V$.
*   We use $0$ to represent the **zero scalar** in $F$.

This distinction is important because vectors and scalars are different types of objects.

---

## General Properties of Vector Spaces

Let $V(F)$ be a vector space. The following six general properties always hold true.

1.  $a\bar{0} = \bar{0} \quad \text{for all } a \in F$
2.  $0\alpha = \bar{0} \quad \text{for all } \alpha \in V$
3.  $a(-\alpha) = -(a\alpha) \quad \text{for all } a \in F, \alpha \in V$
4.  $(-a)\alpha = -(a\alpha) \quad \text{for all } a \in F, \alpha \in V$
5.  $a(\alpha - \beta) = a\alpha - a\beta \quad \text{for all } a \in F, \alpha, \beta \in V$
6.  If $a\alpha = \bar{0}$, then either $a = 0$ or $\alpha = \bar{0}$.

Let us prove each property step by step. A common trick in these proofs is knowing where to start. We often start with an identity equation and multiply both sides by a scalar or vector.

---

### Proof of Property 1

We want to multiply a scalar by the zero vector. So we start with a known fact about the zero vector.

We know that adding the zero vector to itself gives the zero vector:

$$
\bar{0} + \bar{0} = \bar{0}
$$

Multiply both sides by scalar $a$:

$$
a(\bar{0} + \bar{0}) = a\bar{0}
$$

Apply the distributive law:

$$
a\bar{0} + a\bar{0} = a\bar{0}
$$

Now, add $\bar{0}$ to the right side. Adding the zero vector does not change a vector.

$$
a\bar{0} + a\bar{0} = a\bar{0} + \bar{0}
$$

By the left cancellation law in the vector group $(V, +)$, we cancel $a\bar{0}$ from the left of both sides:

$$
a\bar{0} = \bar{0}
$$

This completes the first proof.

---

### Proof of Property 2

Here we want to multiply the zero scalar by a vector. We start with the zero scalar.

We know that adding zero to zero gives zero:

$$
0 + 0 = 0
$$

Multiply both sides by vector $\alpha$ from the right:

$$
(0 + 0)\alpha = 0\alpha
$$

Apply the distributive law:

$$
0\alpha + 0\alpha = 0\alpha
$$

Add the zero vector $\bar{0}$ to the right side:

$$
0\alpha + 0\alpha = 0\alpha + \bar{0}
$$

Again, apply the left cancellation law to remove $0\alpha$ from both sides:

$$
0\alpha = \bar{0}
$$

This proves the second property.

---

### Proof of Property 3

We start with a vector and its additive inverse. We know they sum to the zero vector.

$$
\alpha + (-\alpha) = \bar{0}
$$

Multiply both sides by scalar $a$:

$$
a[ \alpha + (-\alpha) ] = a\bar{0}
$$

Apply the distributive law on the left. On the right, use Property 1 ($a\bar{0} = \bar{0}$):

$$
a\alpha + a(-\alpha) = \bar{0}
$$

We want to isolate $a(-\alpha)$. So we add the additive inverse $-(a\alpha)$ to both sides:

$$
-(a\alpha) + [ a\alpha + a(-\alpha) ] = -(a\alpha) + \bar{0}
$$

Use associativity to group the first two terms:

$$
[ -(a\alpha) + a\alpha ] + a(-\alpha) = -(a\alpha)
$$

The terms in the brackets sum to the zero vector $\bar{0}$:

$$
\bar{0} + a(-\alpha) = -(a\alpha)
$$

Adding the zero vector leaves the vector unchanged, giving us our final result:

$$
a(-\alpha) = -(a\alpha)
$$

---

### Proof of Property 4

This proof is very similar to Property 3. But here we start with scalar addition.

We know a scalar and its additive inverse sum to the zero scalar:

$$
a + (-a) = 0
$$

Multiply both sides by vector $\alpha$:

$$
[ a + (-a) ]\alpha = 0\alpha
$$

Distribute on the left, and use Property 2 on the right ($0\alpha = \bar{0}$):

$$
a\alpha + (-a)\alpha = \bar{0}
$$

Add $-(a\alpha)$ to both sides:

$$
-(a\alpha) + [ a\alpha + (-a)\alpha ] = -(a\alpha) + \bar{0}
$$

Group using associativity:

$$
[ -(a\alpha) + a\alpha ] + (-a)\alpha = -(a\alpha)
$$

The terms in brackets sum to $\bar{0}$:

$$
\bar{0} + (-a)\alpha = -(a\alpha)
$$

Which simplifies to:

$$
(-a)\alpha = -(a\alpha)
$$

---

### Proof of Property 5

We only have distributive laws for addition, not subtraction. But we can write vector subtraction as adding an inverse.

Start with the left side:

$$
a(\alpha - \beta) = a[ \alpha + (-\beta) ]
$$

Now we can apply the standard distributive law:

$$
= a\alpha + a(-\beta)
$$

From Property 3, we know $a(-\beta) = -(a\beta)$. Substitute this in:

$$
= a\alpha + [ -(a\beta) ]
$$

Which we simply write as subtraction:

$$
= a\alpha - a\beta
$$

---

### Proof of Property 6: If, then or

This property has two parts. If the product of a scalar and a vector is zero, one of them must be zero.

**Part A: Assume $a \neq 0$**
If the scalar $a$ is not zero, then it must have a multiplicative inverse $a^{-1}$ in the field $F$.
Start with our given equation:

$$
a\alpha = \bar{0}
$$

Multiply both sides by $a^{-1}$:

$$
a^{-1}(a\alpha) = a^{-1}\bar{0}
$$

Use associativity for scalars on the left, and Property 1 on the right:

$$
(a^{-1}a)\alpha = \bar{0}
$$

Since

$$
a^{-1}a = 1:
$$

$$
1 \cdot \alpha = \bar{0}
$$

By the vector space rules, $1 \cdot \alpha = \alpha$. Thus:

$$
\alpha = \bar{0}
$$

So if $a \neq 0$, then $\alpha$ must be $\bar{0}$.

**Part B: Assume $\alpha \neq \bar{0}$**
We want to prove $a = 0$. We will use proof by contradiction. Let us assume $a \neq 0$.

If $a \neq 0$, then $a^{-1}$ exists in $F$.
Starting again with:

$$
a\alpha = \bar{0}
$$

Multiply by $a^{-1}$ on the left:

$$
a^{-1}(a\alpha) = a^{-1}\bar{0}
$$

Following the exact same steps as above, this simplifies to:

$$
1 \cdot \alpha = \bar{0}
$$

$$
\alpha = \bar{0}
$$

But this result contradicts our assumption that $\alpha \neq \bar{0}$.
Because assuming $a \neq 0$ leads to a contradiction, our assumption must be false.
Therefore, $a$ must be $0$.

---

## Key Takeaways
*   Multiplying any scalar by the zero vector gives the zero vector.
*   Multiplying the zero scalar by any vector gives the zero vector.
*   Negative signs factor out smoothly: $a(-\alpha) = (-a)\alpha = -(a\alpha)$.
*   Scalar multiplication distributes over vector subtraction.
*   If the product of a scalar and a vector is the zero vector, it is guaranteed that at least one of them is zero.

## What Comes Next
With the general properties established, the next lecture introduces vector subspaces. We will see how to prove a subset is a vector space using a simple theorem.

---

**Navigation**
[< Previous Lecture](01_Vector_Space_Definition.md) | [Index](README.md) | [Next Lecture >](03_Vector_Subspace.md)
