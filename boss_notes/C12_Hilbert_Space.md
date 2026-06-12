[← Previous: C11 Banach Spaces](C11_Normed_Linear_Space_Banach_Space.md) | [Index](00_Index.md) | 

---

# C12: Hilbert Spaces

> **Exam Weight**: Tier 1-2 | **Appeared in**: Assignment / Final | **Typical Marks**: 4–5

If a Banach space is a complete space with a norm (length), a Hilbert space goes one step further: it is a complete space with an inner product (length and angle).

---

## Definition

A **Hilbert Space** is a complete inner product space. 
- It has an inner product $\langle x, y \rangle$.
- This inner product induces a norm $\|x\| = \sqrt{\langle x, y \rangle}$.
- The space is complete with respect to the metric defined by this induced norm (every Cauchy sequence converges to a limit within the space).

---

## The Hierarchy of Spaces

The spaces you have learned form a strict nested hierarchy:
1. **Vector Space**: Has addition and scalar multiplication.
2. **Normed Space**: A Vector Space that also has a concept of length ($\|x\|$).
3. **Banach Space**: A Normed Space that is "complete" (no missing limits).
4. **Inner Product Space**: A Vector Space that has a dot-product-like operation (angles). *Note: All inner product spaces are automatically Normed Spaces via the induced norm, but they are not necessarily complete.*
5. **Hilbert Space**: An Inner Product Space that is complete.

### Must-Know Proof: Every Hilbert is a Banach (PYQ / Assignment)

**Problem**: Prove that every Hilbert space is a Banach space.

**Proof**:
By definition, a Hilbert space is an inner product space that is complete with respect to the distance metric induced by its inner product. The induced metric is based on the induced norm, defined as $\|x\| = \sqrt{\langle x, x \rangle}$.

As proven previously (see C10), the induced norm $\|x\| = \sqrt{\langle x, x \rangle}$ satisfies all the axioms of a norm (positivity, absolute homogeneity, and the triangle inequality via the Cauchy-Schwarz inequality). Therefore, every inner product space is automatically a **normed linear space** when equipped with this induced norm.

Because a Hilbert space is, by definition, **complete** with respect to this specific induced norm, it fulfills both conditions of a Banach space: 
1. It is a normed linear space.
2. It is complete.
Thus, every Hilbert space is a Banach space. $\blacksquare$
*(Note: The converse is not true. Not all norms are induced by an inner product. If a norm does not satisfy the Parallelogram Law, it cannot come from an inner product, so a space with that norm could be Banach but not Hilbert).*

---

## Worked Example: The Space

**Problem**: Show that the space $\ell^2$ is a Hilbert space.

**Solution Overview**:
The space $\ell^2$ consists of all infinite sequences of complex numbers $x = (x_1, x_2, \dots)$ such that the sum of the squares of their absolute values converges: $\sum_{i=1}^\infty \lvert x_i \rvert^2 < \infty$.

**1. Define the Inner Product**
The inner product is defined as $\langle x, y \rangle = \sum_{i=1}^\infty x_i \overline{y_i}$. 
By the Cauchy-Schwarz inequality for sequences, this series converges absolutely, so the inner product is mathematically well-defined. It trivially satisfies linearity, conjugate symmetry, and positive-definiteness.

**2. Prove Completeness**
Let $(x^{(n)})$ be a Cauchy sequence in $\ell^2$. For $\epsilon > 0$, there is an $N$ such that for $n, m > N$, we have $\|x^{(n)} - x^{(m)}\|_2 < \epsilon$.
This implies that for each coordinate $i$, the sequence $(x_i^{(n)})_{n=1}^\infty$ is a Cauchy sequence in $\mathbb{C}$. Since $\mathbb{C}$ is complete, each coordinate converges to a limit $x_i \in \mathbb{C}$.
Let $x = (x_1, x_2, \dots)$. By taking the limit as $m \to \infty$ in the finite partial sums of the Cauchy condition, and extending to the infinite sum, we find $x^{(n)} - x \in \ell^2$. 
Since $x^{(n)} \in \ell^2$ and $\ell^2$ is a vector space, $x = x^{(n)} - (x^{(n)} - x) \in \ell^2$. 
Finally, this shows $\|x^{(n)} - x\|_2 \to 0$ as $n \to \infty$, meaning the sequence converges to $x$ in the $\ell^2$ norm.
Because every Cauchy sequence converges to an element within $\ell^2$, the space is complete, making it a Hilbert space.

---

## Exam Patterns
- "Define a Hilbert space and give an example" is a highly probable short question. Provide the definition and the $\ell^2$ sequence space example.
- The 4-mark theoretical proof "Every Hilbert is Banach" is very easy if you clearly state definitions.

---

[← Previous: C11 Banach Spaces](C11_Normed_Linear_Space_Banach_Space.md) | [Index](00_Index.md)
