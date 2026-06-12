[← Previous: C09 Matrix Representation](C09_Matrix_Representation_Change_of_Basis.md) | [Index](00_Index.md) | [Next: C11 Banach Spaces →](C11_Normed_Linear_Space_Banach_Space.md)

---

# C10: Inner Product Spaces

> **Exam Weight**: Tier 2 | **Appeared in**: Assignment / Final | **Typical Marks**: 4–5

An inner product space is a vector space equipped with a way to multiply vectors together, resulting in a scalar. This generalizes the concept of the dot product, allowing us to define angles and lengths in abstract spaces.

---

## Inner Product Axioms

Let $V$ be a vector space over the complex numbers $\mathbb{C}$ (or real numbers $\mathbb{R}$). An inner product is a function $\langle x, y \rangle$ that maps two vectors to a scalar, satisfying the following axioms for all $x, y, z \in V$ and scalar $\alpha$:

1.  **Conjugate Symmetry**: $\langle x, y \rangle = \overline{\langle y, x \rangle}$
    *(If the field is real, this is simply commutativity: $\langle x, y \rangle = \langle y, x \rangle$)*
2.  **Linearity in the First Argument**:
    $\langle x + y, z \rangle = \langle x, z \rangle + \langle y, z \rangle$
    $\langle \alpha x, y \rangle = \alpha \langle x, y \rangle$
3.  **Positive-Definiteness**: $\langle x, x \rangle \geq 0$, and $\langle x, x \rangle = 0$ if and only if $x = 0$.

---

## Must-Know Proof 1: The Induced Norm

**Problem**: Prove that every inner product space is a normed space.

**Proof**:
Let $V$ be an inner product space. We define the induced norm as

$$
\|x\| = \sqrt{\langle x, x \rangle}
$$

. We must prove that this satisfies the three axioms of a norm.

1.  **Positivity**: By the positive-definite axiom of inner products, $\langle x, x \rangle \geq 0$. Thus,

$$
\|x\| = \sqrt{\langle x, x \rangle} \geq 0
$$

. Additionally, $\langle x, x \rangle = 0 \iff x = 0$, so

$$
\|x\| = 0 \iff x = 0.
$$

2.  **Absolute Homogeneity**:

$$
\|\alpha x\| = \sqrt{\langle \alpha x, \alpha x \rangle} = \sqrt{\alpha \overline{\alpha} \langle x, x \rangle} = \sqrt{\lvert \alpha \rvert^2 \langle x, x \rangle} = \lvert \alpha \rvert \sqrt{\langle x, x \rangle} = \lvert \alpha \rvert \|x\|
$$

3.  **Triangle Inequality**:

$$
\|x + y\|^2 = \langle x + y, x + y \rangle = \langle x, x \rangle + \langle x, y \rangle + \langle y, x \rangle + \langle y, y \rangle
$$

$$
\|x + y\|^2 = \|x\|^2 + \langle x, y \rangle + \overline{\langle x, y \rangle} + \|y\|^2 = \|x\|^2 + 2\text{Re}(\langle x, y \rangle) + \|y\|^2
$$

By the Cauchy-Schwarz inequality (

$$
\lvert \langle x, y \rangle \rvert \leq \|x\| \|y\|
$$

) and knowing

$$
\text{Re}(z) \leq \lvert z \rvert:
$$

$$
2\text{Re}(\langle x, y \rangle) \leq 2\lvert \langle x, y \rangle \rvert \leq 2\|x\|\|y\|
$$

    Substituting this back:

$$
\|x + y\|^2 \leq \|x\|^2 + 2\|x\|\|y\| + \|y\|^2 = (\|x\| + \|y\|)^2
$$

    Taking the square root gives $\|x + y\| \leq \|x\| + \|y\|$.

Since all three axioms hold, the induced norm makes the inner product space a normed space. $\blacksquare$

---

## Must-Know Proof 2: The Parallelogram Law

**Problem**: Prove the parallelogram law in an inner product space.

**Proof**:
The parallelogram law states that the sum of the squares of the lengths of the four sides of a parallelogram equals the sum of the squares of the lengths of the two diagonals:

$$
\|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2
$$

Expand the left-hand side using the inner product:

$$
\|x + y\|^2 = \langle x + y, x + y \rangle = \langle x, x \rangle + \langle x, y \rangle + \langle y, x \rangle + \langle y, y \rangle
$$

$$
= \|x\|^2 + \langle x, y \rangle + \langle y, x \rangle + \|y\|^2
$$

Expand the second term:

$$
\|x - y\|^2 = \langle x - y, x - y \rangle = \langle x, x \rangle - \langle x, y \rangle - \langle y, x \rangle + \langle y, y \rangle
$$

$$
= \|x\|^2 - \langle x, y \rangle - \langle y, x \rangle + \|y\|^2
$$

Add the two equations together:

$$
\|x + y\|^2 + \|x - y\|^2 = (\|x\|^2 + \langle x, y \rangle + \langle y, x \rangle + \|y\|^2) + (\|x\|^2 - \langle x, y \rangle - \langle y, x \rangle + \|y\|^2)
$$

The cross terms $\langle x, y \rangle$ and $-\langle x, y \rangle$ cancel out, as do $\langle y, x \rangle$ and $-\langle y, x \rangle$.

$$
\|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2
$$

$\blacksquare$

---

## Exam Patterns
- If asked to prove something is an inner product space, you just need to grind through the 3 axioms (linearity, symmetry, positive-definite).
- The Parallelogram Law proof is incredibly straightforward and a very easy 5 marks if it appears.

---

[← Previous: C09 Matrix Representation](C09_Matrix_Representation_Change_of_Basis.md) | [Index](00_Index.md) | [Next: C11 Banach Spaces →](C11_Normed_Linear_Space_Banach_Space.md)
