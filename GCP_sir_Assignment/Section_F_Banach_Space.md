# Section F: Banach Space (Branch Space)

## Q33 (03)
**Question:** **Define a Banach space and give an example.**

**Answer:**
A Banach space is defined as a complete normed linear space. That is, it is a vector space equipped with a norm, and every Cauchy sequence of vectors in the space converges to a limit that is also within the space.

**Example:**
The space $C[a, b]$ consisting of all continuous real-valued functions on the closed interval $[a, b]$, equipped with the supremum norm (or uniform norm):

$$
\|f\|_\infty = \sup_{t \in [a, b]} |f(t)|
$$

This forms a Banach space because the uniform limit of a Cauchy sequence of continuous functions is guaranteed to be a continuous function, thus remaining in the space.

## Q34 (05)
**Question:** **Prove that every finite-dimensional normed linear space is complete.**

**Answer:**
Let $V$ be an $n$-dimensional normed linear space with norm $\|\cdot\|$. We must show every Cauchy sequence in $V$ converges to a limit in $V$.
Let $\{e_1, e_2, \dots, e_n\}$ be a basis for $V$. Any vector $x \in V$ can be uniquely written as $x = \sum_{i=1}^n \alpha_i e_i$.

Define a standard reference norm on $V$, such as $\|x\|_1 = \sum_{i=1}^n |\alpha_i|$. In a finite-dimensional space, all norms are equivalent. Thus, there exist constants $c, C > 0$ such that $c\|x\|_1 \leq \|x\| \leq C\|x\|_1$ for all $x \in V$.

Let $(x^{(m)})$ be a Cauchy sequence in $V$ with respect to the given norm $\|\cdot\|$. Because the norms are equivalent, it is also a Cauchy sequence with respect to $\|\cdot\|_1$.
Let $x^{(m)} = \sum_{i=1}^n \alpha_i^{(m)} e_i$. Since $(x^{(m)})$ is Cauchy in $\|\cdot\|_1$, for any given $\epsilon > 0$, there exists $N$ such that for $p, q > N$:

$$
\|x^{(p)} - x^{(q)}\|_1 = \sum_{i=1}^n |\alpha_i^{(p)} - \alpha_i^{(q)}| < \epsilon
$$

This implies that for each fixed $i$, the coordinate sequence $(\alpha_i^{(m)})_{m=1}^\infty$ is a Cauchy sequence of real (or complex) numbers. Since $\mathbb{R}$ (and $\mathbb{C}$) is complete, each coordinate sequence converges to a limit $\alpha_i$.

Let $x = \sum_{i=1}^n \alpha_i e_i$. Clearly, $x \in V$.
We now check convergence: $\|x^{(m)} - x\|_1 = \sum_{i=1}^n |\alpha_i^{(m)} - \alpha_i| \to 0$ as $m \to \infty$.
Because the norms are equivalent, $\|x^{(m)} - x\| \leq C\|x^{(m)} - x\|_1 \to 0$, meaning the sequence $(x^{(m)})$ converges to $x$ in the original norm. Thus, $V$ is complete.

## Q35 (05)
**Question:** **Show that $\ell^\infty$ is a Banach space.**

**Answer:**
The space $\ell^\infty$ consists of all bounded sequences of complex (or real) numbers $x = (x_1, x_2, \dots)$ equipped with the supremum norm $\|x\|_\infty = \sup_{i} |x_i|$.
To show it is a Banach space, we must show it is complete.

Let $(x^{(n)})$ be a Cauchy sequence in $\ell^\infty$. For any $\epsilon > 0$, there exists an integer $N$ such that for all $n, m > N$, we have:

$$
\|x^{(n)} - x^{(m)}\|_\infty = \sup_{i} |x_i^{(n)} - x_i^{(m)}| < \epsilon
$$

For each fixed coordinate $i$, $|x_i^{(n)} - x_i^{(m)}| \leq \|x^{(n)} - x^{(m)}\|_\infty < \epsilon$.
Thus, for every fixed $i$, the sequence of scalars $(x_i^{(n)})_{n=1}^\infty$ is a Cauchy sequence in $\mathbb{C}$. Since $\mathbb{C}$ is complete, it converges to a limit $x_i$.

Let $x = (x_1, x_2, \dots)$. We must show $x \in \ell^\infty$ and $x^{(n)} \to x$ in the supremum norm.
Taking the limit as $m \to \infty$ in the inequality $|x_i^{(n)} - x_i^{(m)}| < \epsilon$, we get $|x_i^{(n)} - x_i| \leq \epsilon$ for all $n > N$ and for all $i$.
This shows that $\sup_{i} |x_i^{(n)} - x_i| \leq \epsilon$, which implies $\|x^{(n)} - x\|_\infty \to 0$. Thus, $x^{(n)}$ converges to $x$.

Since $x^{(n)}$ is a bounded sequence (being in $\ell^\infty$) and it is within a finite distance $\epsilon$ of $x$, the limit sequence $x$ must also be bounded. So $x \in \ell^\infty$.
Since every Cauchy sequence converges to a point in $\ell^\infty$, the space is complete and therefore a Banach space.

## Q36 (03)
**Question:** **Give an example of a normed space that is not complete.**

**Answer:**
Consider the space $P[a, b]$ of all polynomial functions on the closed interval $[a, b]$, equipped with the supremum norm $\|f\|_\infty = \sup_{t \in [a, b]} |f(t)|$.

This space is a valid normed linear space because polynomials form a vector space and the supremum norm satisfies all norm properties. However, it is not complete. We can construct a sequence of polynomials that converges to a non-polynomial function. For example, consider the Taylor polynomials for the exponential function on $[0, 1]$:

$$
P_n(t) = 1 + t + \frac{t^2}{2!} + \dots + \frac{t^n}{n!}
$$

The sequence $(P_n)$ is a Cauchy sequence in the supremum norm because the series converges uniformly on the compact interval $[0, 1]$. However, the limit of this sequence is the exponential function $e^t$, which is not a polynomial. Since the limit is not contained within the space $P[a, b]$, the space is not complete.

## Q37 (04)
**Question:** **Prove that every Hilbert space is a Banach space.**

**Answer:**
By definition, a Hilbert space is an inner product space that is complete with respect to the distance metric induced by its inner product. The induced metric is based on the induced norm, defined as $\|x\| = \sqrt{\langle x, x \rangle}$.

As proven previously, the induced norm $\|x\| = \sqrt{\langle x, x \rangle}$ satisfies all the axioms of a norm (positivity, absolute homogeneity, and the triangle inequality via the Cauchy-Schwarz inequality). Therefore, every inner product space is automatically a normed linear space when equipped with this induced norm.

Because a Hilbert space is, by definition, complete with respect to this specific induced norm, it fulfills both conditions of a Banach space: it is a normed linear space, and it is complete. Thus, every Hilbert space is a Banach space. (Note: The converse is not generally true, as not all norms are induced by an inner product).
