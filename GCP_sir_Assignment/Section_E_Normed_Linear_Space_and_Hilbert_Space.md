# Section E: Normed Linear Space & Hilbert Space

## Q28 (04)
**Question:** **Define a normed linear space and give two examples.**

**Answer:**
A normed linear space is a vector space $V$ over a field (usually $\mathbb{R}$ or $\mathbb{C}$) equipped with a function called a norm, denoted as $\|\cdot\| : V \to \mathbb{R}$, which assigns a non-negative real length to each vector. The norm must satisfy the following properties for all vectors $x, y \in V$ and all scalars $\alpha$:
1. **Positivity:** $\|x\| \geq 0$, and $\|x\| = 0$ if and only if $x = 0$.
2. **Absolute Homogeneity:** $\|\alpha x\| = |\alpha| \|x\|$.
3. **Triangle Inequality:** $\|x + y\| \leq \|x\| + \|y\|$.

**Examples:**
1. $\mathbb{R}^n$ with the Euclidean norm: $\|x\|_2 = \sqrt{x_1^2 + x_2^2 + \dots + x_n^2}$.
2. $\mathbb{R}^n$ with the Manhattan/Taxicab norm: $\|x\|_1 = |x_1| + |x_2| + \dots + |x_n|$.

## Q29 (05)
**Question:** **Verify whether $\|x\| = |x_1| + |x_2|$ defines a norm on $\mathbb{R}^2$.**

**Answer:**
Let $x = (x_1, x_2)$ and $y = (y_1, y_2)$ be vectors in $\mathbb{R}^2$, and let $\alpha$ be a scalar. We check the three norm axioms for the function $\|x\| = |x_1| + |x_2|$.

1. **Positivity:** Since absolute values are non-negative, $|x_1| \geq 0$ and $|x_2| \geq 0$, so $\|x\| = |x_1| + |x_2| \geq 0$. Furthermore, if $\|x\| = 0$, then $|x_1| + |x_2| = 0$, which implies $|x_1| = 0$ and $|x_2| = 0$, meaning $x = (0, 0) = 0$. Conversely, if $x = 0$, $\|0\| = |0| + |0| = 0$. Axiom holds.
2. **Homogeneity:** $\|\alpha x\| = |\alpha x_1| + |\alpha x_2| = |\alpha||x_1| + |\alpha||x_2| = |\alpha|(|x_1| + |x_2|) = |\alpha|\|x\|$. Axiom holds.
3. **Triangle Inequality:** $\|x + y\| = |x_1 + y_1| + |x_2 + y_2|$. By the standard triangle inequality for real numbers, $|x_1 + y_1| \leq |x_1| + |y_1|$ and $|x_2 + y_2| \leq |x_2| + |y_2|$. Adding these inequalities gives $\|x + y\| \leq (|x_1| + |x_2|) + (|y_1| + |y_2|) = \|x\| + \|y\|$. Axiom holds.

Since all properties are satisfied, $\|x\| = |x_1| + |x_2|$ (which is the $L^1$ norm) defines a valid norm on $\mathbb{R}^2$.

## Q30 (04)
**Question:** **Prove that every inner product space is a normed space.**

**Answer:**
Let $V$ be an inner product space with inner product $\langle x, y \rangle$. We define the induced norm as $\|x\| = \sqrt{\langle x, x \rangle}$. We must prove that this function satisfies the three axioms of a norm.

1. **Positivity:** By the definition of an inner product, $\langle x, x \rangle \geq 0$, so $\|x\| = \sqrt{\langle x, x \rangle} \geq 0$. Moreover, $\langle x, x \rangle = 0$ if and only if $x = 0$, so $\|x\| = 0 \iff x = 0$.
2. **Homogeneity:** For any scalar $\alpha$ and vector $x$:



$$
\|\alpha x\| = \sqrt{\langle \alpha x, \alpha x \rangle} = \sqrt{\alpha \bar{\alpha} \langle x, x \rangle} = \sqrt{|\alpha|^2 \langle x, x \rangle} = |\alpha| \sqrt{\langle x, x \rangle} = |\alpha| \|x\|
$$

3. **Triangle Inequality:** Consider $\|x + y\|^2$:



$$
\|x + y\|^2 = \langle x + y, x + y \rangle = \langle x, x \rangle + \langle x, y \rangle + \langle y, x \rangle + \langle y, y \rangle
$$

$$
\|x + y\|^2 = \|x\|^2 + \langle x, y \rangle + \overline{\langle x, y \rangle} + \|y\|^2 = \|x\|^2 + 2\text{Re}(\langle x, y \rangle) + \|y\|^2
$$

By the Cauchy-Schwarz inequality ($|\langle x, y \rangle| \leq \|x\| \|y\|$) and the fact that $\text{Re}(z) \leq |z|$, we have:



$$
2\text{Re}(\langle x, y \rangle) \leq 2|\langle x, y \rangle| \leq 2\|x\|\|y\|
$$

Substituting this back:



$$
\|x + y\|^2 \leq \|x\|^2 + 2\|x\|\|y\| + \|y\|^2 = (\|x\| + \|y\|)^2
$$

Taking the square root of both sides gives $\|x + y\| \leq \|x\| + \|y\|$.

Since all three axioms hold, the induced norm makes the inner product space a normed linear space.

## Q31 (05)
**Question:** **Show that the space $\ell^2$ is a Hilbert space.**

**Answer:**
A Hilbert space is defined as a complete inner product space. The space $\ell^2$ consists of all infinite sequences of complex numbers $x = (x_1, x_2, \dots)$ such that the sum of the squares of their absolute values converges: $\sum_{i=1}^\infty |x_i|^2 < \infty$.

1. **Inner Product:** The inner product on $\ell^2$ is defined as $\langle x, y \rangle = \sum_{i=1}^\infty x_i \overline{y_i}$. By the Cauchy-Schwarz inequality for sequences, this series converges absolutely, so the inner product is well-defined. It trivially satisfies linearity, conjugate symmetry, and positive-definiteness.
2. **Completeness:** To show it is a Hilbert space, we must show $\ell^2$ is complete under the metric induced by this inner product ($d(x,y) = \|x - y\|_2$). Let $(x^{(n)})$ be a Cauchy sequence in $\ell^2$. Thus, for every $\epsilon > 0$, there is an $N$ such that for $n, m > N$, we have $\|x^{(n)} - x^{(m)}\|_2 < \epsilon$.
   This implies that for each coordinate $i$, the sequence $(x_i^{(n)})_{n=1}^\infty$ is a Cauchy sequence in $\mathbb{C}$. Since $\mathbb{C}$ is complete, each coordinate sequence converges to some limit $x_i \in \mathbb{C}$.
   Let $x = (x_1, x_2, \dots)$. By taking the limit as $m \to \infty$ in the Cauchy condition $\sum_{i=1}^k |x_i^{(n)} - x_i^{(m)}|^2 < \epsilon^2$, we find $\sum_{i=1}^k |x_i^{(n)} - x_i|^2 \leq \epsilon^2$. Since this holds for all $k$, it holds for the infinite sum. Thus $x^{(n)} - x \in \ell^2$. Since $x^{(n)} \in \ell^2$ and $\ell^2$ is a vector space, it follows that $x = x^{(n)} - (x^{(n)} - x) \in \ell^2$.
   Furthermore, this shows $\|x^{(n)} - x\|_2 \to 0$ as $n \to \infty$, meaning the sequence converges to $x$ in the $\ell^2$ norm.

Since every Cauchy sequence converges to an element within $\ell^2$, the space is complete, making it a Hilbert space.

## Q32 (05)
**Question:** **Prove the parallelogram law in an inner product space.**

**Answer:**
Let $V$ be an inner product space with norm $\|x\| = \sqrt{\langle x, x \rangle}$. The parallelogram law states that for any vectors $x, y \in V$:

$$
\|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2
$$

We evaluate the left-hand side by expanding the squared norms using the inner product:

$$
\|x + y\|^2 = \langle x + y, x + y \rangle = \langle x, x \rangle + \langle x, y \rangle + \langle y, x \rangle + \langle y, y \rangle
$$

$$
\|x + y\|^2 = \|x\|^2 + \langle x, y \rangle + \langle y, x \rangle + \|y\|^2
$$

Now, expand the second term:

$$
\|x - y\|^2 = \langle x - y, x - y \rangle = \langle x, x \rangle - \langle x, y \rangle - \langle y, x \rangle + \langle y, y \rangle
$$

$$
\|x - y\|^2 = \|x\|^2 - \langle x, y \rangle - \langle y, x \rangle + \|y\|^2
$$

Adding the two equations together:

$$
\|x + y\|^2 + \|x - y\|^2 = (\|x\|^2 + \langle x, y \rangle + \langle y, x \rangle + \|y\|^2) + (\|x\|^2 - \langle x, y \rangle - \langle y, x \rangle + \|y\|^2)
$$

The cross terms $\langle x, y \rangle$ and $-\langle x, y \rangle$ cancel out, as do $\langle y, x \rangle$ and $-\langle y, x \rangle$.

$$
\|x + y\|^2 + \|x - y\|^2 = 2\|x\|^2 + 2\|y\|^2
$$

This completes the proof.