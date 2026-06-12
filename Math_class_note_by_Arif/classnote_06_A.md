<!-- Page 051 -->
5. **Additive inverse law:**
   $x \in F, -x \in F$
   $x - x = 0$
   $a + (-a) = e$
   $2 - 2 = 0$

Field under addition হতে যদি 5 টাই satisfy করত।

**Field under Multiplication:**
1. **Closure property:**
   $a, b \in K \Rightarrow ab \in K$
2. **Commutative:**
   $xy = yx \quad (x, y \in F)$
3. **Associative:**
   $(xy)z = x(yz) \quad (x, y, z \in F)$
4. **Identity law:**
   $1 \cdot x = x$
5. **Multiplicative inverse:**
   $x \in K, x^{-1} \in K \Rightarrow x \cdot x^{-1} = 1$
   $2$ এর inverse $\frac{1}{2}$

$\mathbb{Z} = \lbrace\dots, -3, -2, -1, 0, 1, 2, 3\rbrace$ not satisfy.
$\mathbb{R}$ satisfy (0 বাদ দিতে হবে).

$\mathbb{R} - \lbrace 0\rbrace \rightarrow$ field under multiplication.
$0 \cdot \frac{1}{0} \neq 1$

**# set of all rational numbers is field?**
$\mathbb{Q} = \lbrace\frac{p}{q} \mid p, q \in \mathbb{Z}, q \neq 0\rbrace$
হ্যাঁ, যোগের under এ field.
গুনের check: 0, 1 আছে কিনা $\Rightarrow$ zero বাদে multiply এর under এ field হয়।

<!-- Page 052 -->
**Vector space and subspace**

$V = \lbrace\text{set of vectors defined on a field } K\rbrace$
-

$$
= \left\lbrace  \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix} \right\rbrace
$$

- $= \lbrace x^2, x^2+1 \rbrace$
-

$$
= \left\lbrace  \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 2 \\ 1 \end{pmatrix}, \begin{pmatrix} 3 \\ 1 \end{pmatrix}, \dots \right\rbrace
$$

- $= \lbrace (0, 1), (0, 2), (0, 3), \dots \rbrace$
None of them are vector spaces.

1. **Closure:**
   $v_1, v_2 \in V \Rightarrow v_1 + v_2 \in V$
   -

$$
\begin{pmatrix} 2 & 2 \\ 2 & 2 \end{pmatrix}
$$

not satisfied.
   - $2x^2+1$ not satisfied.

**Scalar Multiplication:**
$v \in V$, $k \in K \Rightarrow kv \in V$
e.g. $\lbrace(0, 1), (0, 2)\rbrace$, $v = (0, 1)$, $k = 2 \Rightarrow kv = (0, 2)$ (scalar multiplication)

**প্রথম শর্ত:** should be closed under addition and scalar multiplication; that's how the set of vectors is a vector space.

<!-- Page 053 -->
**Practice**

**characteristic matrix:** let $A_{n \times n}$ be an $n$-square matrix. Then the characteristics matrix of $A$ is $A - \lambda I$.
**Ch. polynomial:** $|A - \lambda I|$ is ch. poly.
**ch. eqn:** $|A - \lambda I| = 0$ is ch. eqn.

**eigenvalues & eigen vector:** The solutions of ch. eqn are eigen values. And corresponding vectors associated with eigen values are called eigen vectors.

**Applications of eigenvalue / eigen vector:**
1. Differential Eqn and Dynamic systems
2. Mechanical & structural Engineering
3. Electrical Engineering & signal processing
4. Machine learning & Data science
5. Computer vision & Graphics

**Problem: Consider

$$
A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix},
$$

Find eigenvalues & eigen vectors.**
ch. matrix of $A$ is

$$
A - \lambda I = \begin{pmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{pmatrix}
$$

Ch. eqn is $|A-\lambda I| = 0$

<!-- Page 054 -->

$$
\begin{vmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{vmatrix} = 0
$$

$\Rightarrow (4-\lambda)(3-\lambda) - 2 = 0$
$\Rightarrow 12 - 7\lambda + \lambda^2 - 2 = 0$
$\Rightarrow \lambda^2 - 7\lambda + 10 = 0$
$\Rightarrow \lambda = 2, 5$
Thus eigenvalues are 2, 5.

- eigenvalues positive $\Rightarrow$ unstable
- negative $\Rightarrow$ stable
- complex $\Rightarrow$ marginally stable

**Now,**
Let

$$
v = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}
$$

be an eigenvector corresponding to the eigenvalue $\lambda = 2$.
Then $AV = \lambda V \Rightarrow (A-\lambda I)V = 0$

$$
\Rightarrow \begin{pmatrix} 4-2 & 1 \\ 2 & 3-2 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

$$
\Rightarrow \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \Rightarrow \begin{pmatrix} 2v_1+v_2 \\ 2v_1+v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

yielding $2v_1+v_2 = 0$. (many solutions)

set $v_2 = 2 \Rightarrow v_1 = -1$.
Thus

$$
V = \begin{pmatrix} -1 \\ 2 \end{pmatrix}
$$

is an eigenvector corresponding to eigenvalue $\lambda=2$.

**Again,**
Let

$$
w = \begin{pmatrix} w_1 \\ w_2 \end{pmatrix}
$$

be an eigenvector corresponding to the eigenvalue $\lambda = 5$.
Then

$$
(A-\lambda I)W = 0 \Rightarrow \begin{pmatrix} 4-5 & 1 \\ 2 & 3-5 \end{pmatrix} \begin{pmatrix} w_1 \\ w_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

$$
\Rightarrow \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix}\begin{pmatrix} w_1 \\ w_2 \end{pmatrix} = \begin{pmatrix} -w_1+w_2 \\ 2w_1-2w_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

(more solutions)
set

$$
w_1 = 1 \Rightarrow w_2 = 1 \Rightarrow \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

is eigenvector $\lambda=5$.

<!-- Page 055 -->
Then the matrix obtained with the eigenvector is modal matrix,

$$
P = \begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix}
$$

echelon form:
$R_2 \rightarrow 2R_1 + R_2$

$$
\begin{pmatrix} -1 & 1 \\ 0 & 3 \end{pmatrix}
$$

hence eigenvectors are independent. (echelon form এ row zero হলে dependent, না হলে independent).

$$
P^{-1} = \frac{1}{3}\begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix}
$$

$$
P^{-1} A P = \frac{1}{3}\begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix} \begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix}
$$

$$
= \frac{1}{3}\begin{pmatrix} -2 & 2 \\ 10 & 5 \end{pmatrix} \begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix}
$$

$$
= \frac{1}{3}\begin{pmatrix} 6 & 0 \\ 0 & 15 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}
$$

which is diagonalized matrix.

**#

$$
\begin{pmatrix} 2 & 1 \\ -1 & 1 \end{pmatrix}
$$

eigenvalue & vector.**

$$
A = \begin{pmatrix} 2 & 1 \\ -1 & 1 \end{pmatrix}
$$

ch matrix of $A$ is

$$
A-\lambda I = \begin{pmatrix} 2-\lambda & 1 \\ -1 & 1-\lambda \end{pmatrix}
$$

ch eqn of $A$ is

$$
|A-\lambda I| = 0 \Rightarrow \begin{vmatrix} 2-\lambda & 1 \\ -1 & 1-\lambda \end{vmatrix} = 0
$$

$\Rightarrow (2-\lambda)(1-\lambda) + 1 = 0 \Rightarrow \lambda^2 - 3\lambda + 3 = 0$
$\lambda = 1.5 \pm 0.866i$

<!-- Page 056 -->
Let,

$$
V = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}
$$

for $\lambda = \frac{3+i\sqrt{3}}{2}$

$$
(A-\lambda I)V = 0 \Rightarrow \begin{pmatrix} \frac{1-i\sqrt{3}}{2} & 1 \\ -1 & \frac{-1-i\sqrt{3}}{2} \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

$\left(\frac{1-i\sqrt{3}}{2}\right)x + y = 0 \Rightarrow y = -\left(\frac{1-i\sqrt{3}}{2}\right)x$
$-x - \left(\frac{1+i\sqrt{3}}{2}\right)y = 0 \Rightarrow -x = \left(\frac{1+i\sqrt{3}}{2}\right)\left(-\frac{1-i\sqrt{3}}{2}\right)x = -x$

Let $x = 2 \Rightarrow y = -1+i\sqrt{3}$.

$$
V = \begin{pmatrix} 2 \\ -1+i\sqrt{3} \end{pmatrix}
$$

Now,

$$
W = \begin{pmatrix} w_1 \\ w_2 \end{pmatrix}
$$

for $\lambda = \frac{3-i\sqrt{3}}{2}$

$$
W_2 = \begin{pmatrix} 2 \\ -1-i\sqrt{3} \end{pmatrix}
$$

modal matrix

$$
P = \begin{pmatrix} 2 & 2 \\ -1+i\sqrt{3} & -1-i\sqrt{3} \end{pmatrix}
$$

$$
R_1 \rightarrow \frac{1}{2} R_1 \Rightarrow \begin{pmatrix} 1 & 1 \\ -1+i\sqrt{3} & -1-i\sqrt{3} \end{pmatrix}
$$

$$
R_2 \rightarrow R_2 - (-1+i\sqrt{3})R_1 \Rightarrow \begin{pmatrix} 1 & 1 \\ 0 & -2i\sqrt{3} \end{pmatrix}
$$

(row echelon form)
eigenvalues are independent.

<!-- Page 057 -->
**# Find inverse by Cayley-Hamilton**

$$
A = \begin{pmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{pmatrix}
$$

ch. polynomial of $A$ is $|A-\lambda I|$

$$
= \left| \begin{pmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{pmatrix} - \begin{pmatrix} \lambda & 0 & 0 \\ 0 & \lambda & 0 \\ 0 & 0 & \lambda \end{pmatrix} \right| = \begin{vmatrix} 1-\lambda & 2 & 3 \\ -1 & 2-\lambda & 4 \\ 1 & 1 & 2-\lambda \end{vmatrix}
$$

$= (1-\lambda)\lbrace(2-\lambda)(2-\lambda) - 4\rbrace - 2\lbrace-(2-\lambda) - 4\rbrace + 3\lbrace-1 - (2-\lambda)\rbrace$
$|A-\lambda I| = -\lambda^3 + 5\lambda^2 - 3\lambda + 3$

By Cayley-Hamilton theorem, we replace $\lambda$ by $A$:
$-A^3 + 5A^2 - 3A + 3I = 0$
$\Rightarrow -A^{-1}A^3 + 5A^{-1}A^2 - 3A^{-1}A + 3A^{-1}I = 0$
$\Rightarrow -A^2 + 5A - 3I + 3A^{-1} = 0$
$\Rightarrow A^{-1} = \frac{1}{3}[A^2 - 5A + 3I]$

$$
= \frac{1}{3}\left[\begin{pmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{pmatrix}^2 - 5\begin{pmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{pmatrix} + 3\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}\right]
$$

*(Note: The calculation below in the original notes contains arithmetic errors, refer to Page 045 for the correct version)*

$$
A^{-1} = \frac{1}{3}\begin{pmatrix} -2 & 1 & 2 \\ 6 & -3 & -7 \\ -3 & 1 & 2 \end{pmatrix}
$$

<!-- Page 058 -->
<b>Class 25 | sir</b>
<div align="right"><b>04-03-26</b></div>

**Vector space**

**Scalar field:** A field should be closed under binary.
$V = \text{set of vectors defined over a field } K$
$= \lbrace(0, 1, 1), (0, 2, 1), \dots \rbrace$

**set of vectors VS vector spaces:**
$\rightarrow$ closed under vector addition and scalar multiplication.
- মানে দুইটা যোগ করলে যোগফল এবং constant গুণ করলে গুণফলও ঐ set এ থাকবে।
- zero vector থাকবে (identity element)
- inverse $u + (-u) = 0$
- commutative law

**# $\lbrace(0, 0)\rbrace$ is a vector space**
- $k u = 3(0, 0) = (0, 0)$
- $(3+1)(0, 0) + 2(0, 0) = (0, 0)$

**Example:**
$y = x$
$y = 2x$
$(2, 2) + (2, 4) = (4, 6) \Rightarrow y = \frac{3}{2}x$ (যোগ করলে সরে যাবে)

**Case 1:**
$(0, 0) + (1, 1) + (2, 2) = (3, 3)$

<!-- Page 059 -->
**Case 2:**
$(0, 0) + (1, 1) = (1, 1)$

**Case 3:**
$(1, 1) + (-1, -1) = (0, 0)$

$M_1 \rightarrow 3\lbrace(1, 1) + (2, 4)\rbrace = (3, 3) + (6, 12) = (9, 15) \Rightarrow y = \frac{15}{9}x = \frac{5}{3}x$
$M_2 \rightarrow (3+2)(1, 1) = 3(1, 1) + 2(1, 1) = (5, 5)$
$M_3 \rightarrow (ab)v = a(bv) \Rightarrow 2 \times 3(1, 1) = 6(1, 1) = (6, 6)$

**# $\mathbb{R}^3$ কি ভেক্টর space? $\mathbb{R}^2, \mathbb{R}^4$**
$\mathbb{R}^3 = \lbrace(a, b, c) \mid a, b, c \in \mathbb{R}\rbrace$ - Yes.

**# $V = \mathbb{R}^n = \lbrace(a_1, \dots, a_n) \mid a_i \in \mathbb{R}\rbrace$**
$\mathbb{R}^n$ is a vector space (proof).

**Subspaces:**
Vector space এর subset.
(e.g., $2 \times 2$ matrices থেকে শুধু symmetric নিলে subspace).

<!-- Page 060 -->
**Condition**
$W \subset V$, $W$ is subspace of $V$ if:
a) $0 \in W$
b) for every $u, v \in W$, $k \in K$
   i) $u+v \in W$
   ii) $ku \in W$

---

<b>Class 26 | sir</b>
<div align="right"><b>06-04-26</b></div>

**# Vector space এর example:**
- $\mathbb{R}^2$ defined on $\mathbb{R}$
- $\mathbb{R}^n$ defined on $\mathbb{R}$
- set of all straight lines is a vector space (if passing through origin).
- $3 \times 3$ matrices subspace of $n \times n$.

- $y = a_0 + a_1x + \dots + a_nx^n$ (vector space) (Polynomial $\rightarrow$ variable এর power finite & non-negative হতে হবে)
- $y = a_2x^2 + a_4x^4 + \dots$ (subspace)

**Vector space:**
$\rightarrow$ must be closed under vector addition & scalar multiplication.
Under polynomial function: circle, triangle, straight line, matrices.

**Linear combination of vectors:**
$v_1, v_2, \dots, v_n \in V$ defined on $\mathbb{R}$
$u = c_1v_1 + c_2v_2 + \dots + c_nv_n$ (new vector is linear combination)
$c_1, c_2, \dots, c_n \in \mathbb{R}$