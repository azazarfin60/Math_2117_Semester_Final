[← Previous: C10 Inner Product Spaces](C10_Inner_Product_Spaces.md) | [Index](00_Index.md) | [Next: C12 Hilbert Spaces →](C12_Hilbert_Space.md)

---

# C11: Normed Linear Spaces & Banach Spaces

> **Exam Weight**: Tier 1-2 | **Appeared in**: Assignment / Final | **Typical Marks**: 3–5

While an inner product gives a vector space "angles", a norm gives a vector space "length". When a normed space is mathematically "complete", it is called a Banach Space.

---

## Normed Linear Space Definitions

A normed linear space is a vector space $V$ equipped with a norm $\|\cdot\| : V \to \mathbb{R}$, which assigns a non-negative real length to each vector. It must satisfy three properties for all $x, y \in V$ and scalars $\alpha$:
1.  **Positivity**: $\|x\| \geq 0$, and

$$
\|x\| = 0 \iff x = 0.
$$

2.  **Absolute Homogeneity**:

$$
\|\alpha x\| = \lvert \alpha \rvert \|x\|.
$$

3.  **Triangle Inequality**: $\|x + y\| \leq \|x\| + \|y\|$.

**Example Verification**: Verify whether

$$
\|x\| = \lvert x_1 \rvert + \lvert x_2 \rvert
$$

defines a norm on $\mathbb{R}^2$.
1. **Positivity**: $\lvert x_1 \rvert \geq 0$ and $\lvert x_2 \rvert \geq 0$, so

$$
\lvert x_1 \rvert + \lvert x_2 \rvert \geq 0
$$

. If

$$
\|x\| = 0
$$

, then

$$
\lvert x_1 \rvert=0
$$

and

$$
\lvert x_2 \rvert=0
$$

, so $x=(0,0)$.
2. **Homogeneity**:

$$
\|\alpha x\| = \lvert \alpha x_1 \rvert + \lvert \alpha x_2 \rvert = \lvert \alpha \rvert(\lvert x_1 \rvert + \lvert x_2 \rvert) = \lvert \alpha \rvert\|x\|.
$$

3. **Triangle Inequality**:

$$
\|x + y\| = \lvert x_1 + y_1 \rvert + \lvert x_2 + y_2 \rvert \leq (\lvert x_1 \rvert + \lvert y_1 \rvert) + (\lvert x_2 \rvert + \lvert y_2 \rvert) = \|x\| + \|y\|.
$$

Since all three hold, it is a valid norm (the $L^1$ norm).

---

## Banach Space Definitions

A **Banach space** is defined as a **complete** normed linear space. 
"Complete" means that every Cauchy sequence of vectors in the space successfully converges to a limit that is *also contained within the space*. There are no "missing holes" in the space.

### Example of a Banach Space
The space $\ell^\infty$, which consists of all bounded infinite sequences of complex numbers

$$
x = (x_1, x_2, \dots)
$$

, is equipped with the supremum norm:

$$
\|x\|_\infty = \sup_{i} \lvert x_i \rvert
$$

Because $\mathbb{C}$ is complete, Cauchy sequences of coordinates converge to bounded limits within $\ell^\infty$.

### Example of an INCOMPLETE Normed Space
The space $P[a, b]$ of all polynomial functions on $[a, b]$, equipped with the supremum norm. It is not complete because a Cauchy sequence of polynomials (like the Taylor series expansion for $e^t$) will converge to a limit function ($e^t$) that is continuous but *not* a polynomial. Since the limit escapes the space of polynomials, the space is not complete.

---

## Must-Know Proof: Finite-Dimensional Spaces

**Problem**: Prove that every finite-dimensional normed linear space is complete.

**Proof**:
Let $V$ be an $n$-dimensional normed linear space. Let $\lbrace e_1, \dots, e_n\rbrace$ be a basis. Any vector $x$ can be uniquely written as

$$
x = \sum_{i=1}^n \alpha_i e_i.
$$

Define a reference norm:

$$
\|x\|_1 = \sum_{i=1}^n \lvert \alpha_i \rvert
$$

. In a finite-dimensional space, all norms are equivalent, meaning there exist constants $c, C > 0$ such that

$$
c\|x\|_1 \leq \|x\| \leq C\|x\|_1.
$$

Let $(x^{(m)})$ be a Cauchy sequence in $V$ with respect to $\|\cdot\|$. Because the norms are equivalent, it is also Cauchy with respect to $\|\cdot\|_1$.
Let

$$
x^{(m)} = \sum_{i=1}^n \alpha_i^{(m)} e_i
$$

. Since $(x^{(m)})$ is Cauchy in $\|\cdot\|_1$, for a given $\epsilon > 0$, for large $p, q$:

$$
\|x^{(p)} - x^{(q)}\|_1 = \sum_{i=1}^n \lvert \alpha_i^{(p)} - \alpha_i^{(q)} \rvert < \epsilon
$$

This implies that for each coordinate index $i$, the sequence

$$
(\alpha_i^{(m)})_{m=1}^\infty
$$

is a Cauchy sequence of scalars. Since $\mathbb{R}$ (and $\mathbb{C}$) is complete, each coordinate sequence converges to a limit $\alpha_i$.

Let

$$
x = \sum_{i=1}^n \alpha_i e_i
$$

. Clearly, $x \in V$.
We check convergence:

$$
\|x^{(m)} - x\|_1 = \sum_{i=1}^n \lvert \alpha_i^{(m)} - \alpha_i \rvert \to 0
$$

as $m \to \infty$.
Because norms are equivalent,

$$
\|x^{(m)} - x\| \leq C\|x^{(m)} - x\|_1 \to 0
$$

, meaning the sequence converges to $x$ in the original norm.
Thus, every Cauchy sequence converges within $V$, making $V$ complete. $\blacksquare$

---

## Exam Patterns
- The definitions are highly testable. Remember: Banach = Complete + Normed. 
- You may be asked for a 3-mark definition and example of a Banach space. Provide the $\ell^\infty$ or $C[a,b]$ example.

---

[← Previous: C10 Inner Product Spaces](C10_Inner_Product_Spaces.md) | [Index](00_Index.md) | [Next: C12 Hilbert Spaces →](C12_Hilbert_Space.md)
