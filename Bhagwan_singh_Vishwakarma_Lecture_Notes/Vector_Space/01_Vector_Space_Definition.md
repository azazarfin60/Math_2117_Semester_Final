# Lecture 01: Vector Space - Concept and Definition

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 01 of 27
> **Video**: https://www.youtube.com/watch?v=_6oRqxY6O5w

---

**Navigation**
[Index](README.md) | [Next Lecture >](02_General_Properties.md)

---

## Prerequisites
Before we define a vector space, we need to understand two key types of operations. These operations tell us how elements combine.

### Internal Composition
Internal composition is an operation where you combine two elements from the same set, and the result stays in that set.

Imagine a non-empty set $A$. Take two elements $\alpha$ and $\beta$ from $A$. If you add them together using an operation $+$, and the new element $\gamma$ also belongs to $A$, then $+$ is an internal composition for $A$.

$$
\alpha + \beta = \gamma \in A
$$

### External Composition
External composition involves two different sets. You take an element from one set, apply an operation using an element from a second set, and the result belongs to the first set.

Let $A$ be our main set and $B$ be another set (which we will later call a field). Take an element $\alpha$ from $A$ and an element $a$ from $B$. If you multiply them and the result $\beta$ belongs to $A$, then this multiplication is an external composition for $A$.

$$
a \cdot \alpha = \beta \in A
$$

This means the operation is defined using elements from $B$, but the output always lands back in $A$.

---

## What is a Vector Space?

Now we can formally define a vector space. To build a vector space, we need two sets:
1. A set $V$, whose elements are called **vectors**.
2. A field $F$ (usually real numbers $\mathbb{R}$ or complex numbers $\mathbb{C}$), whose elements are called **scalars**.

The set $V$ is called a **Vector Space** over the field $F$ if it satisfies certain conditions under two operations: vector addition (internal) and scalar multiplication (external). We denote this as $V(F)$.

Here are the conditions $V(F)$ must satisfy:

### 1. Abelian Group under Vector Addition
The set $V$ must be an abelian group with respect to the internal composition $+$. This means:
*   **Closure**: Adding two vectors gives a vector in $V$.
*   **Associativity**: $(\alpha + \beta) + \gamma = \alpha + (\beta + \gamma)$.
*   **Identity**: There is a zero vector $\bar{0}$ such that $\alpha + \bar{0} = \alpha$.
*   **Inverse**: Every vector $\alpha$ has an additive inverse $-\alpha$ such that $\alpha + (-\alpha) = \bar{0}$.
*   **Commutativity**: $\alpha + \beta = \beta + \alpha$.

### 2. Closure under Scalar Multiplication
The set $V$ must be closed under external composition. If you multiply a scalar from $F$ with a vector from $V$, the result must be a vector in $V$.

For all $a \in F$ and for all $\alpha \in V$:

$$
a \cdot \alpha \in V
$$

### 3. Distribution and Associative Laws
The vector space must follow these rules connecting scalars and vectors:

*   **Distributive Law over Vector Addition**:

$$
    a \cdot (\alpha + \beta) = a \cdot \alpha + a \cdot \beta \quad \text{for all } a \in F, \alpha, \beta \in V
$$

*   **Distributive Law over Scalar Addition**:

$$
    (a + b) \cdot \alpha = a \cdot \alpha + b \cdot \alpha \quad \text{for all } a, b \in F, \alpha \in V
$$

*   **Associative Law for Scalar Multiplication**:

$$
    (ab) \cdot \alpha = a \cdot (b \cdot \alpha) \quad \text{for all } a, b \in F, \alpha \in V
$$

*   **Identity Scalar Multiplication**:

$$
    1 \cdot \alpha = \alpha \quad \text{for all } \alpha \in V
$$

    where $1$ is the multiplicative identity of the field $F$.

If a set $V$ combined with a field $F$ meets all these rules, we proudly call $V$ a vector space. The vectors in $V$ do not have to be traditional directed lines. They can be points on a plane, matrices, or even polynomials.

---

## Example: The 2D Plane as a Vector Space

Let us verify that the 2D Cartesian plane is a vector space over the field of real numbers.

*   **Vectors**: $V = \mathbb{R}^2 = \lbrace (x, y) \mid x, y \in \mathbb{R} \rbrace$
*   **Scalars**: $F = \mathbb{R}$

Let us check the conditions.

### Check 1: Is an Abelian Group?
Take two vectors $(x_1, y_1)$ and $(x_2, y_2)$ from $V$.
*   **Closure**: $(x_1, y_1) + (x_2, y_2) = (x_1 + x_2, y_1 + y_2)$. Since the sum of two real numbers is a real number, this new tuple is in $V$.
*   **Identity**: The element $(0, 0)$ works as the identity because $(x, y) + (0, 0) = (x, y)$.
*   **Inverse**: The inverse of $(x, y)$ is $(-x, -y)$ because $(x, y) + (-x, -y) = (0, 0)$.
*   **Commutativity**: $(x_1, y_1) + (x_2, y_2) = (x_2, y_2) + (x_1, y_1)$ is naturally true for real numbers.

### Check 2: Closure under Scalar Multiplication
Take a scalar $a$ from $\mathbb{R}$ and a vector $(x, y)$ from $V$.

$$
a(x, y) = (ax, ay)
$$

Since $ax$ and $ay$ are real numbers, the result $(ax, ay)$ is in $V$.

### Check 3: Distributive Laws
Let us prove the first distributive law. We want to show $a(\alpha + \beta) = a\alpha + a\beta$.
Let $\alpha = (x_1, y_1)$ and $\beta = (x_2, y_2)$.

$$
a(\alpha + \beta) = a( (x_1, y_1) + (x_2, y_2) )
$$

First, add the vectors inside the bracket:

$$
= a(x_1 + x_2, y_1 + y_2)
$$

Now, multiply the scalar $a$ inside:

$$
= (a(x_1 + x_2), a(y_1 + y_2))
$$

Expand using basic algebra:

$$
= (ax_1 + ax_2, ay_1 + ay_2)
$$

Split this back into two tuples:

$$
= (ax_1, ay_1) + (ax_2, ay_2)
$$

Factor out the scalar $a$:

$$
= a(x_1, y_1) + a(x_2, y_2)
$$

Which gives us our final result:

$$
= a\alpha + a\beta
$$

The other distribution and associative laws can be proven using the exact same simple algebra. Since all conditions are met, $\mathbb{R}^2$ is a vector space over $\mathbb{R}$.

Other common examples include the complex plane $\mathbb{C}$ over $\mathbb{R}$, or 3D space $\mathbb{R}^3$ over $\mathbb{R}$.

---

## Key Takeaways
*   An **internal composition** maps elements within the same set.
*   An **external composition** maps an element from a scalar field and an element from a vector set back into the vector set.
*   A **Vector Space** is a set of vectors that forms an abelian group under addition and is closed under scalar multiplication with elements from a field.
*   The vectors must obey specific distributive and associative rules connecting vector addition and scalar multiplication.

## What Comes Next
Now that we know what a vector space is, we will look at its general properties. We will prove rules about multiplying by zero and negative scalars in the next lecture.

---

**Navigation**
[Index](README.md) | [Next Lecture >](02_General_Properties.md)
