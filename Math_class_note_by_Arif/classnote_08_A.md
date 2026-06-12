<!-- Page 071 -->
**# $2 \times 2$ matrices:**

$$
\sigma_1 = \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}, \quad \sigma_2 = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}, \quad \sigma_3 = \begin{pmatrix} 2 & 2 \\ 0 & 0 \end{pmatrix}
$$

Check whether the vectors are linearly independent.

*Ans:*
$c_1 v_1 + c_2 v_2 + \dots + c_n v_n = [0]$
- সবগুলো $0$ হলে $\rightarrow$ independent.
- $0$ না হলে (at least one non-zero) $\rightarrow$ dependent.

Set,

$$
c_1 \sigma_1 + c_2 \sigma_2 + c_3 \sigma_3 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}
$$

(zero matrix of $2 \times 2$)

$$
\Rightarrow c_1 \begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix} + c_2 \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} + c_3 \begin{pmatrix} 2 & 2 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}
$$

$$
\Rightarrow \begin{pmatrix} 2c_1 + 2c_2 + 2c_3 & 2c_1 + 2c_3 \\ 2c_1 & 2c_1 + 2c_2 \end{pmatrix} = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}
$$

From the matrix equation:
- $2c_1 = 0 \Rightarrow c_1 = 0$
- $2c_1 + 2c_2 = 0 \Rightarrow c_2 = 0$
- $2c_1 + 2c_3 = 0 \Rightarrow c_3 = 0$
- $2c_1 + 2c_2 + 2c_3 = 0$ (satisfied)

Yielding:
$c_1 = 0, \quad c_2 = 0, \quad c_3 = 0$

Thus, the vectors (matrices) are linearly independent.

> [!NOTE]
> $3 \times 3$ matrix ও independent হতে পারে।

---

**# Check whether the vectors are linearly dependent/independent:**
$v_1 = (2, 3, 3)$
$v_2 = (4, 5, -1)$
$v_3 = (4, 4, 1)$

<!-- Page 072 -->
*Ans:*
$c_1 v_1 + c_2 v_2 + c_3 v_3 = 0$
$c_1(2, 3, 3) + c_2(4, 5, -1) + c_3(4, 4, 1) = (0, 0, 0)$

$\Rightarrow$
- $2c_1 + 4c_2 + 4c_3 = 0$
- $3c_1 + 5c_2 + 4c_3 = 0$
- $3c_1 - c_2 + c_3 = 0$

Solving this system yields:
$c_1 = 0, \quad c_2 = 0, \quad c_3 = 0$

> [!NOTE]
> $v_2 = (1, 6, 6)$ হলে $c_1 = c_2 = c_3 = 0$ হতো না (dependent হতো)।

---

### Image and Kernel of a Linear Mapping

Let $T: \mathbb{R}^3 \rightarrow \mathbb{R}^3$ (or in general $T: V(\mathbb{R}) \rightarrow W(\mathbb{R})$).

**Image of $T$ ($\text{Im } T$):**
সেই সকল সেট of image are called $\text{Im } T$.
The set of $\lbrace w_1, w_2, \dots, w_n\rbrace$ are called the image of the linear mapping.

```
       Domain (V)                      Codomain (W)
     +------------+                  +--------------+
     |     v1     | ---------------> | T(v1) = w1   |
     |     v2     | ---------------> | T(v2) = w2   |
     |     v3     | ---------------> | T(v3) = w3   |
     |     v4     | ---------------> | T(v4) = w4   |
     +------------+                  +--------------+
```

**Example:**
$y = x^2$ mapping from $\mathbb{R} \rightarrow \mathbb{R}$
- $1 \rightarrow 1$
- $2 \rightarrow 4$
- $3 \rightarrow 9$
- $4 \rightarrow 16$
$\lbrace 1, 4, 9, 16\rbrace$ image তৈরি করবে। যে vector গুলো image তৈরি করবে তাদের সেটই হলো Image of $T$.

**Kernel of $T$ ($\text{Ker } T$):**
ডোমেইনের vector গুলোর মধ্যে যে vector গুলো zero $(0,0,0)$ তে mapping করবে তারাই kernel.
যেমন: $T(x, y, z) = (x, y, 0)$ mapping এর ক্ষেত্রে, $(0, 0, z)$ আকারের vector গুলো (যেমন $(0,0,3), (0,0,1), (0,0,2)$) $(0,0,0)$ তে mapping করবে (cause $xy$-plane এর projection mapping এ $z$-axis এর vector গুলো zero vector এ রূপান্তর হয়)।

<!-- Page 073 -->
$\rightarrow$ যারা $(0,0,0)$ তে ম্যাপ করবে।

- **Kernel of vector** is the set of vectors that map to the $(0, 0, 0)$ vector. Basis একটাই, dimension এক।
- **Image of mapping** (যেগুলো সেট তৈরি করে তাকে) $\rightarrow$ যে vector গুলো map করে তাদের সেট।

$$
\text{Ker}(T) = \lbrace v \in V \mid T(v) = 0 \rbrace
$$

---

<b>Class 31 | sir</b>
<div align="right"><b>15-04-26</b></div>

**# What is meant by kernel of a linear mapping and image?**
**# Linear mapping কে matrix এ represent করব।**

**Problem:** Let $T: \mathbb{R}^3 \rightarrow \mathbb{R}^3$ be a linear mapping defined by:
$T(x, y, z) = (x+2y, y-z, x+2z)$
Find a basis and dimension of:
(i) $\text{Im } T$
(ii) $\text{Ker } T$

> [!NOTE]
> $T: \mathbb{R}^3 \rightarrow \mathbb{R}^3$ is a mapping from $\mathbb{R}^3$ into $\mathbb{R}^3$. Linearly independent vector গুলোর সেটই হলো basis.

*Ans:*
The usual basis (or standard basis) of $\mathbb{R}^3$ is:
$\lbrace(1, 0, 0), (0, 1, 0), (0, 0, 1)\rbrace$
which generates $\mathbb{R}^3$.
(cause these 3 vectors can generate the whole vectors of $\mathbb{R}^3$, সব vector কে নিচ্ছি না)

<!-- Page 074 -->
Then the basis images $\lbrace T(1, 0, 0), T(0, 1, 0), T(0, 0, 1)\rbrace$ will generate $\text{Im } T$.
- $V \in \mathbb{R}^3 \rightarrow$ Domain
- $T(v) \in \mathbb{R}^3 \rightarrow$ Codomain

Now,
$T(1, 0, 0) = (1, 0, 1)$
$T(0, 1, 0) = (2, 1, 0)$
$T(0, 0, 1) = (0, -1, 2)$

So the image set generators are $\lbrace(1, 0, 1), (2, 1, 0), (0, -1, 2)\rbrace$.

Now, we will generate a matrix and reduce it to its echelon form to find the linearly independent vectors:

$$
A = \begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 0 \\ 0 & -1 & 2 \end{pmatrix}
$$

Applying row operation $R_2 \rightarrow 2R_1 - R_2$:

$$
\sim \begin{pmatrix} 1 & 0 & 1 \\ 0 & -1 & 2 \\ 0 & -1 & 2 \end{pmatrix}
$$

Applying row operation $R_3 \rightarrow R_2 - R_3$:

$$
\sim \begin{pmatrix} 1 & 0 & 1 \\ 0 & -1 & 2 \\ 0 & 0 & 0 \end{pmatrix}
$$

We see there are two independent vectors: $(1, 0, 1)$ and $(0, -1, 2)$.
Hence, $\lbrace(1, 0, 1), (0, -1, 2)\rbrace$ is a basis of $\text{Im } T$.
The number of elements in the basis is 2, so:

$$
\text{dim}(\text{Im } T) = 2
$$

<!-- Page 075 -->
**(ii) Finding basis and dimension of $\text{Ker } T$:**

$$
\text{Ker } T = \lbrace (x, y, z) \in \mathbb{R}^3 \mid T(x, y, z) = (0, 0, 0) \rbrace
$$

$\text{Ker } T$ is the set of vectors whose image contains the zero $(0, 0, 0)$ vector.

i.e.,
- $x + 2y = 0$
- $y - z = 0$
- $x + 2z = 0$

Using row operations on the system of equations ($L_3 \rightarrow L_1 - L_3$):
- $x + 2y = 0$
- $y - z = 0$
- $2y - 2z = 0$

This simplifies to:
- $x + 2y = 0$
- $y - z = 0$

The system has two independent equations and three variables/unknowns.
So we need to let one of them be a free variable: $\text{number of free variables} = 3 - 2 = 1$.

Say, $z$ is the free variable. Set $z = 1$:
$\Rightarrow y = 1$
$\Rightarrow x = -2$

Thus, $\lbrace(-2, 1, 1)\rbrace$ is a basis of $\text{Ker } T$.
The number of elements in the basis is 1, so:

$$
\text{dim}(\text{Ker } T) = 1
$$

---

<!-- Page 076 -->
**# Let $T: \mathbb{R}^3 \rightarrow \mathbb{R}^3$ defined by $T(x, y, z) = (x+2y-z, y+z, x+y-2z)$.**

**# Let $T: \mathbb{R}^2 \rightarrow \mathbb{R}^2$ and $T': \mathbb{R}^2 \rightarrow \mathbb{R}^2$ be defined by:**
$T(x, y) = (x, 0)$
$T'(x, y) = (y, x)$

Find:
(i) $3T + 3T'(x, y)$
(ii) $TT'(x, y)$
(iii) $T^2 T'(x, y)$
(iv) $T T'^2(x, y)$
(v) $3T^2(x, y)$

> [!NOTE]
> $T^2(x, y) = T(T(x, y))$

*Proof for (i):*
The standard basis of $\mathbb{R}^2$ is $\lbrace(1, 0), (0, 1)\rbrace$ which generates $\mathbb{R}^2$.
Then $\lbrace T(1, 0), T(0, 1)\rbrace$ will generate $\text{Im } T$.

Now,
- $T(1, 0) = (1, 0)$
- $T(0, 1) = (0, 0)$
So, $3T = \lbrace(3, 0), (0, 0)\rbrace$

And,
- $T'(1, 0) = (0, 1)$
- $T'(0, 1) = (1, 0)$
So, $3T' = \lbrace(0, 3), (3, 0)\rbrace$

<!-- Page 077 -->

$$
3T + 3T' = \lbrace(3, 3), (3, 0)\rbrace
$$

**Final answer:**
$3T(x, y) + 3T'(x, y) = 3(x, 0) + 3(y, x) = (3x + 3y, 3x)$

---

**# What is meant by domain basis?**

### Matrix Representation of a Linear Mapping

Let $T: \mathbb{R}^2 \rightarrow \mathbb{R}^2$ be defined by $T(x, y) = (5x+y, -4x+3y)$.
Find the matrix representation of $T$ with respect to the basis $\lbrace v_1 = (3, 1), v_2 = (5, 2)\rbrace$.

```
      Domain A                        Codomain B
    (domain basis)                 (codomain basis)
     A = {v1, v2}                    B = {w1, w2}
          |                               |
          v                               v
    f: A ----------> B (m-dimensional independent vectors)
```

In general, let $T(v_1), T(v_2), \dots, T(v_n)$ be the images of the domain basis vectors. Express them as linear combinations of the codomain basis $\lbrace w_1, w_2, \dots, w_m\rbrace$:
$T(v_1) = a_{11}w_1 + a_{12}w_2 + \dots + a_{1m}w_m$
$T(v_2) = a_{21}w_1 + a_{22}w_2 + \dots + a_{2m}w_m$
$\vdots$
$T(v_n) = a_{n1}w_1 + a_{n2}w_2 + \dots + a_{nm}w_m$

<!-- Page 078 -->
Then the matrix representation is the transpose of the coefficient matrix:

$$
T_W = \begin{pmatrix}
a_{11} & a_{12} & \dots & a_{1m} \\
a_{21} & a_{22} & \dots & a_{2m} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \dots & a_{nm}
\end{pmatrix}^t
$$

> [!TIP]
> constant দিয়ে matrix form এর transpose নিতে হবে।

*Ans:*
Here $v_1 = (3, 1)$ and $v_2 = (5, 2)$.
$T(v_1) = T(3, 1) = (5(3)+1, -4(3)+3(1)) = (16, -9)$
$T(v_2) = T(5, 2) = (5(5)+2, -4(5)+3(2)) = (27, -14)$

Expressing $T(v_1)$ and $T(v_2)$ as linear combinations of the basis $\lbrace v_1, v_2\rbrace$:
Let $T(v_1) = a v_1 + b v_2$
$\Rightarrow (16, -9) = a(3, 1) + b(5, 2) = (3a + 5b, a + 2b)$

Equating components:
- $3a + 5b = 16$
- $a + 2b = -9$

Solving the system:
$a = 77, \quad b = -43$
So, $(16, -9) = 77(3, 1) - 43(5, 2)$ ---- (i)

Again, let $T(v_2) = c v_1 + d v_2$
$\Rightarrow (27, -14) = c(3, 1) + d(5, 2) = (3c + 5d, c + 2d)$

Equating components:
- $3c + 5d = 27$
- $c + 2d = -14$

Solving the system:
$c = 124, \quad d = -69$
So, $(27, -14) = 124(3, 1) - 69(5, 2)$ ---- (ii)

<!-- Page 079 -->
The required matrix representation is:

$$
T = \begin{pmatrix} 77 & -43 \\ 124 & -69 \end{pmatrix}^t = \begin{pmatrix} 77 & 124 \\ -43 & -69 \end{pmatrix}
$$

> [!NOTE]
> $T: V \rightarrow W$
> Expressing images as linear combinations:
> $T(v_1) = c_1 w_1 + c_2 w_2$
> $T(v_2) = c_3 w_1 + c_4 w_2$

---

<b>Class 32 | sir</b>
<div align="right"><b>21-04-26</b></div>

### Inner Product Space

**Inner product of two vectors:**
$\langle u, v \rangle: V \times V \rightarrow \mathbb{R} \text{ or } \mathbb{C}$

Axioms of Inner Product (for real/complex vector space):
1. **Linearity:** $\langle \alpha u + v, w \rangle = \alpha \langle u, w \rangle + \langle v, w \rangle$
2. **Conjugate Symmetry:** $\langle u, v \rangle = \overline{\langle v, u \rangle}$
3. **Positivity:** $\langle u, u \rangle \ge 0$
4. **Positive Definiteness:** $\langle u, u \rangle = 0 \iff u = 0$

**Norm:**

$$
\|v\| = \sqrt{\langle v, v \rangle}
$$

**Angle between two vectors:**

$$
\cos\theta = \frac{\langle u, v \rangle}{\|u\| \|v\|}
$$

<!-- Page 080 -->
**# Find the angle between $v_1 = (1, 2, 3)$ and $v_2 = (1, 1, 1)$.**

*Ans:*
$\langle v_1, v_2 \rangle = 1(1) + 2(1) + 3(1) = 6$
$\|v_1\| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14}$
$\|v_2\| = \sqrt{1^2 + 1^2 + 1^2} = \sqrt{3}$

$$
\cos\theta = \frac{6}{\sqrt{14}\sqrt{3}} = \frac{6}{\sqrt{42}}
$$

$$
\theta = \cos^{-1}\left( \frac{6}{\sqrt{42}} \right)
$$

- If $\theta = 90^\circ$, then the vectors are **orthogonal**.
- If the norm of each orthogonal vector is 1, they are called **orthonormal** vectors.

**Example of orthogonal but not orthonormal:**
$(2, 0, 0)$ and $(0, 2, 0)$ since $\langle u, v \rangle = 0$, but $\|u\| = 2$ and $\|v\| = 2$.

---

**# Find the angle between the matrices

$$
u = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}
$$

and

$$
v = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix}.
$$

**

*Ans:*
$\langle u, v \rangle = \text{sum of products of corresponding elements} = 1(1) + 0(1) + 0(1) + 1(1) = 2$
$\|u\| = \sqrt{1^2 + 0^2 + 0^2 + 1^2} = \sqrt{2}$
$\|v\| = \sqrt{1^2 + 1^2 + 1^2 + 1^2} = \sqrt{4} = 2$

$$
\cos\theta = \frac{2}{\sqrt{2}\sqrt{4}} = \frac{2}{2\sqrt{2}} = \frac{1}{\sqrt{2}}
$$

$$
\theta = 45^\circ
$$
