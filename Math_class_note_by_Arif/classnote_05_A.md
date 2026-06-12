<!-- Page 041 -->

$$
\begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}
$$

Let,

$$
V = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}
$$

be an eigenvector corresponding to the eigenvalue $\lambda = 2$.

Then,
$AV = \lambda V \Rightarrow AV - \lambda V = [0]$ (zero matrix, বেয়াকে 0)

$$
\begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = 2 \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}
$$

$$
\Rightarrow (A-\lambda I)V = 0 \Rightarrow \begin{pmatrix} 4-2 & 1 \\ 2 & 3-2 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

$$
\Rightarrow \begin{pmatrix} 2 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \Rightarrow \begin{pmatrix} 2v_1+v_2 \\ 2v_1+v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

$2v_1+v_2 = 0$ yielding $2v_1+v_2 = 0$
অনেকগুলা solution পাওয়া যাবে।

Set, $v_2 = 2 \Rightarrow v_1 = -1$.
Thus

$$
V = \begin{pmatrix} -1 \\ 2 \end{pmatrix}
$$

is an eigenvector corresponding to the eigenvalue $\lambda = 2$.

Again, let

$$
W = \begin{pmatrix} w_1 \\ w_2 \end{pmatrix}
$$

be an eigenvector corresponding to the eigenvalue $\lambda = 5$.

Then, eigenvalue equation will be:
$AW = \lambda W \Rightarrow (A-\lambda I)W = 0$

$$
\Rightarrow \begin{pmatrix} 4-5 & 1 \\ 2 & 3-5 \end{pmatrix} \begin{pmatrix} w_1 \\ w_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

$$
\Rightarrow \begin{pmatrix} -1 & 1 \\ 2 & -2 \end{pmatrix} \begin{pmatrix} w_1 \\ w_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \Rightarrow \begin{pmatrix} -w_1+w_2 \\ 2w_1-2w_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

<!-- Page 042 -->
(why is this linear eqn) কোনো eqn এর ভেরিয়েবল এর degree 1 হলে তাকে linear eqn বলে।

Here,
$-w_1+w_2 = 0$
$2w_1-2w_2 = 0$

Gives, $-w_1+w_2 = 0 \Rightarrow w_1 = w_2$

eqn $= 1$, var $= 2$ $\rightarrow$ system has more than one / more solutions.

Set, $w_1 = 1$ then $w_2 = 1$.
then

$$
\begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

is an eigenvector corresponding to the eigenvalue $\lambda = 5$.

Then modal matrix is:

$$
P = \begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix}
$$

(Then the matrix obtained with the eigenvectors is $P$)

eigenvalue independent here.
why $\rightarrow$ echelon form এ row zero হলে dependent, না হলে independent.

$$
\begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix} \xrightarrow{R_2 \rightarrow R_2 + 2R_1} \begin{pmatrix} -1 & 1 \\ 0 & 3 \end{pmatrix}
$$

hence the eigenvectors are independent.

$$
P^{-1} = \frac{1}{-3}\begin{pmatrix} 1 & -1 \\ -2 & -1 \end{pmatrix} = \frac{1}{3}\begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix}
$$

Now,

$$
P^{-1} A P = \frac{1}{3} \begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix} \begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix}
$$

$$
= \frac{1}{3} \begin{pmatrix} -2 & 2 \\ 10 & 5 \end{pmatrix} \begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix}
$$

$$
= \frac{1}{3}\begin{pmatrix} 6 & 0 \\ 0 & 15 \end{pmatrix} = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}
$$

which is diagonalized matrix.

<!-- Page 043 -->
<b>Class 22 | sir</b>
<div align="right"><b>26-01-26</b></div>

**Eigen values and eigen vectors:**
**equal roots:**

**Consider the matrix

$$
A = \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix}
$$

**

Characteristics matrix of $A$ is $A-\lambda I$

$$
= \begin{pmatrix} 3 & 1 \\ -1 & 1 \end{pmatrix} - \lambda \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 3-\lambda & 1 \\ -1 & 1-\lambda \end{pmatrix}
$$

Characteristics polynomial of $A$ is $|A-\lambda I|$ and hence the ch polynomial is $|A-\lambda I| = 0$

$$
\Rightarrow \begin{vmatrix} 3-\lambda & 1 \\ -1 & 1-\lambda \end{vmatrix} = 0
$$

$\Rightarrow (3-\lambda)(1-\lambda) + 1 = 0$
$\Rightarrow \lambda^2 - 4\lambda + 3 + 1 = 0$
$\Rightarrow (\lambda-2)^2 = 0 \Rightarrow \lambda = 2, 2$

Let,

$$
V = \begin{pmatrix} v_1 \\ v_2 \end{pmatrix}
$$

be the eigenvector corresponding to the eigenvalue $\lambda = 2$.
we can't decide which one is effective.

$AV = \lambda V \Rightarrow (A-\lambda I)V = 0 \quad (\text{zero matrix})$

$$
\Rightarrow \begin{pmatrix} 3-2 & 1 \\ -1 & 1-2 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

$$
\Rightarrow \begin{pmatrix} 1 & 1 \\ -1 & -1 \end{pmatrix} \begin{pmatrix} v_1 \\ v_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \Rightarrow \begin{matrix} v_1-v_2=0 \\ v_1-v_2=0 \end{matrix} \Rightarrow v_1-v_2=0
$$

<!-- Page 044 -->
Set $v_2 = 1 \Rightarrow v_1 = 1$? *(Note: In notes: $v_1-v_2 = 0 \Rightarrow v_1=v_2$, so $v_2=1 \Rightarrow v_1=1$. The eigenvector is

$$
V = \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

)*

$$
V = \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

is an eigenvector corresponding to the eigenvalue $\lambda = 2$.

we can't find independent eigenvectors. So we can't generate/find inverse matrix, also can't diagonalize matrix.

**#

$$
\begin{pmatrix} 2 & 1 \\ -1 & 1 \end{pmatrix}
$$

HW eigen values and eigen vectors.**

*n x n matrix এ eigen vector matching এ সমসংখ্যক independent eigen vector বের করব*

**Cayley-Hamilton Theorem:**
$\rightarrow$ eigenvalues different হলেই inverse matrix থাকবে। ($|A| \neq 0$)

*zero means satisfy a polynomial ($x^2-9x+6$) and roots means satisfy a equation ($x^2-9x+6=0$)*

**Theorem: Every matrix is a zero of its characteristics polynomial.**

$A_{2\times2} = \lambda^2 + a\lambda + b$
Then $A^2 + aA + bI = 0$ (zero matrix)

**# Find inverse by Cayley-Hamilton.**
**Consider the matrix

$$
A = \begin{pmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{pmatrix}
$$

**
ch polynomial should be 3rd degree.

Ch polynomial of $A$ is $|A-\lambda I|$

$$
= \begin{vmatrix} 1-\lambda & 2 & 3 \\ -1 & 2-\lambda & 4 \\ 1 & 1 & 2-\lambda \end{vmatrix}
$$

<!-- Page 045 -->
$= (1-\lambda) \left\lbrace  (2-\lambda)(2-\lambda) - 4 \right\rbrace  - 2 \left\lbrace  -1(2-\lambda) - 4 \right\rbrace  + 3 \left\lbrace  -1 - (2-\lambda) \right\rbrace $
$= (1-\lambda) \left\lbrace  4 - 4\lambda + \lambda^2 - 4 \right\rbrace  - 2 \left\lbrace  -2 + \lambda - 4 \right\rbrace  + 3 \left\lbrace  -3 + \lambda \right\rbrace $
$= (1-\lambda) (\lambda^2 - 4\lambda) - 2 (\lambda - 6) + 3 (\lambda - 3)$
$= \lambda^2 - 4\lambda - \lambda^3 + 4\lambda^2 - 2\lambda + 12 + 3\lambda - 9$
$|A-\lambda I| = -\lambda^3 + 5\lambda^2 - 3\lambda + 3$

By Cayley-Hamilton theorem, we have, replacing $\lambda$ by $A$:
$-A^3 + 5A^2 - 3A + 3I = 0$
$\Rightarrow -A^{-1} A^3 + 5 A^{-1} A^2 - 3 A^{-1} A + 3 A^{-1} I = 0$ (multiplying by $A^{-1}$)
$\Rightarrow -A^2 + 5A - 3I + 3A^{-1} = 0$
$\Rightarrow 3A^{-1} = A^2 - 5A + 3I$

Therefore,

$$
A^2 = \begin{pmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{pmatrix} \begin{pmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{pmatrix} = \begin{pmatrix} 2 & 9 & 17 \\ 1 & 6 & 13 \\ 2 & 6 & 11 \end{pmatrix}
$$

$$
\Rightarrow 3A^{-1} = \begin{pmatrix} 2 & 9 & 17 \\ 1 & 6 & 13 \\ 2 & 6 & 11 \end{pmatrix} - 5 \begin{pmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{pmatrix} + 3 \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}
$$

$$
= \begin{pmatrix} 2 & 9 & 17 \\ 1 & 6 & 13 \\ 2 & 6 & 11 \end{pmatrix} + \begin{pmatrix} -5 & -10 & -15 \\ 5 & -10 & -20 \\ -5 & -5 & -10 \end{pmatrix} + \begin{pmatrix} 3 & 0 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 3 \end{pmatrix}
$$

$$
= \begin{pmatrix} 0 & -1 & 2 \\ 6 & -1 & -7 \\ -3 & 1 & 4 \end{pmatrix}
$$

So,

$$
A^{-1} = \frac{1}{3}\begin{pmatrix} 0 & -1 & 2 \\ 6 & -1 & -7 \\ -3 & 1 & 4 \end{pmatrix}
$$

(found)

<!-- Page 046 -->
**# $\nabla \cdot (A \times r)$ if $\nabla \times A = 0$**

$A = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}$
$r = x\hat{i} + y\hat{j} + z\hat{k}$

$A \times r = \hat{i}(zA_2 - yA_3) + \hat{j}(xA_3 - zA_1) + \hat{k}(yA_1 - xA_2)$

$\nabla \cdot (A \times r) = \frac{\partial}{\partial x}(zA_2 - yA_3) + \frac{\partial}{\partial y}(xA_3 - zA_1) + \frac{\partial}{\partial z}(yA_1 - xA_2)$
$= z \left(\frac{\partial A_2}{\partial x} - \frac{\partial A_1}{\partial y}\right) + x \left(\frac{\partial A_3}{\partial y} - \frac{\partial A_2}{\partial z}\right) + y \left(\frac{\partial A_1}{\partial z} - \frac{\partial A_3}{\partial x}\right)$
$= (x\hat{i} + y\hat{j} + z\hat{k}) \cdot (\nabla \times A)$
$= r \cdot (\nabla \times A) = 0$ since $\nabla \times A = 0$. (proved)

---

<b>Class 23 | sir</b>
<div align="right"><b>02-02-26</b></div>

**diagonalization (important)**

$$
A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}
$$

$\lambda = 2, 5$

$$
V = \begin{pmatrix} -1 \\ 2 \end{pmatrix},
$$

$$
W = \begin{pmatrix} 1 \\ 1 \end{pmatrix}
$$

$$
P = \begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix},
$$

$$
P^{-1} = \frac{1}{3}\begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix}
$$

$$
P^{-1} A P = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix} = M
$$

$A^5 = P M^5 P^{-1}$
$A^{100} = P M^{100} P^{-1}$

$$
A^5 = P M^5 P^{-1} = \frac{1}{3}\begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 32 & 0 \\ 0 & 3125 \end{pmatrix} \begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix}
$$

$$
A^3 = P M^3 P^{-1} = \frac{1}{3} \begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix} \begin{pmatrix} 8 & 0 \\ 0 & 125 \end{pmatrix} \begin{pmatrix} -1 & 1 \\ 2 & 1 \end{pmatrix}
$$

<!-- Page 047 -->
$\mathbb{R}^n \rightarrow n\text{ dimensional euclidean space}$

$\mathbb{R}^2 \rightarrow 2\text{ dimensional}$
$\mathbb{R}^2 = \lbrace(a, b) \mid a, b \in \mathbb{R}\rbrace$ such that vector $(1, 2)$ is a member of $\mathbb{R}^2$.
Represented as $i+2j$ on the cartesian plane.

$\mathbb{R}^3 = \lbrace(a, b, c) \mid a, b, c \in \mathbb{R}\rbrace$
$(2, 1, 1)$ is a member of $\mathbb{R}^3$ represented as $i+2j+k$ (or $2i+j+k$).

$\mathbb{R}^4 = \lbrace(a, b, c, d) \mid a, b, c, d \in \mathbb{R}\rbrace$
আর ভেক্টর আকারে প্রকাশ করা যাবে না।

$\mathbb{R}^n = \lbrace(a_1, a_2, \dots, a_n) \mid a_1, a_2, a_3, \dots, a_n \in \mathbb{R}\rbrace$
(Row vector)

**real number:** union of set of rational and non-rational numbers or numbers that can be placed on the $x$-axis.
$\mathbb{R} = \mathbb{Q} \cup \mathbb{Q}'$

Let in $\mathbb{R}^3$:
$V_1 = (1, 0, 0)$
$V_2 = (0, 1, 0)$
$V_3 = (0, 0, 1)$
(3D Geometry / User Basis)

$$
W = \begin{vmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{vmatrix}
$$

determinant বের করলে যদি not equal to zero হয় independent.
we can generate all vectors with these three independent vectors; they will form a basis.

$(2, 5, -6) = 2(1, 0, 0) + 5(0, 1, 0) - 6(0, 0, 1)$

<!-- Page 048 -->

$$
\mathbb{R}^2 \rightarrow \left. \begin{matrix} (1, 0) \\ (0, 1) \end{matrix} \right\rbrace  \text{independent vector (user basis)}
$$

এক ভেক্টর থেকে আরেকটা জেনারেট করা না গেলেই independent.
e.g. $(1, 2)$ and $(2, 1)$

$(5, 4) = 5(1, 0) + 4(0, 1)$

**#

$$
\begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}
$$

**
$(4, 5) = a(1, 2) + b(2, 1) = (a+2b, 2a+b)$
$a+2b = 4$
$2a+b = 5$
Solving gives: $a=2, b=1$.
*(Note: The handwritten note has a typo showing $a=1, b=3/2$ and $(4,5) = 1(1,2) + 3/2(2,1)$)*
$(4, 5) = 2(1, 2) + 1(2, 1)$

Now Column vector: row $n$ এ যাবে or column এ or vice versa.

$$
v_1 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix},
$$

$$
v_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix},
$$

$$
v_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
$$

두 ভেক্টরের মধ্যবর্তী কোনো vector space.

**Array Multiplication:**

$$
A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix},
$$

$$
B = \begin{pmatrix} 2 & 3 & 1 \\ 0 & 1 & 2 \\ 1 & 1 & -1 \end{pmatrix}
$$

In MATLAB:
- `A .* B` (element-wise multiplication)
- `A * B` (matrix multiplication)

$$
A.B = \begin{pmatrix} 2 & 6 & 3 \\ 0 & 5 & 12 \\ 7 & 8 & -9 \end{pmatrix}
$$

$V = (1, 2, 3)$
Norm $||V|| = \sqrt{1^2 + 2^2 + 3^2} = \sqrt{14}$ *(Note: notes write $9^2$ instead of $3^2$)*

<!-- Page 049 -->
**distance between two 3D vectors:**
$V_1 = (a_1, a_2, a_3)$
$V_2 = (b_1, b_2, b_3)$
$d(V_1, V_2) = \sqrt{(a_1-b_1)^2 + (a_2-b_2)^2 + (a_3-b_3)^2}$

**Generalized inner product:**
$V_1 = (a_1, a_2, \dots, a_n) \in \mathbb{R}^n$
$V_2 = (b_1, b_2, \dots, b_n) \in \mathbb{R}^n$
$V_1, V_2 \in \mathbb{R}^n$

If the angle between two vectors is $\theta$:
$\cos\theta = \frac{\langle V_1, V_2 \rangle}{||V_1|| \, ||V_2||} = \frac{V_1 \cdot V_2}{||V_1|| \, ||V_2||} = \frac{a_1b_1 + a_2b_2 + \dots + a_nb_n}{\sqrt{\sum a_i^2}\sqrt{\sum b_i^2}}$

For $V_1 = (1, 0)$, $V_2 = (0, 1)$:
$\cos\theta = \frac{0+0}{\sqrt{1}\sqrt{1}} = 0 \Rightarrow \theta = 90^\circ$

- $\theta = 0^\circ \Rightarrow$ dependent
- $\theta \neq 0^\circ \Rightarrow$ independent

For $V = (1, -1, 1)$, $||V|| = \sqrt{1+1+1} = \sqrt{3}$.

<!-- Page 050 -->
<b>Class 24 | sir</b>
<div align="right"><b>28-03-26</b></div>

**# fields**
note:
- addition and scalar multiplication আছে
- closed কিনা

**closure property:** দুইটা element যোগ করলে যোগফল ঐ সেট এ থাকলে।
- $\lbrace(1, 2), (2, 3)\rbrace$ it is not maintaining closure property.
- $\mathbb{R}^n = \lbrace(a_1, a_2, a_3 \dots a_n) \mid a_1, a_2 \dots \in \mathbb{N}\rbrace$
- $(a, b, c) = a\hat{i} + b\hat{j} + c\hat{k}$
- $\lbrace(0, 0)\rbrace$ satisfy the closure property.

**operations (mapping):**
- binary
- unary
- tertiary

**Binary operation:**
$f: A \otimes A \rightarrow A \quad (R = \lbrace \dots \rbrace)$
$+: \mathbb{R} \times \mathbb{R} \rightarrow \mathbb{R}$
$2+3 = 5 \in \mathbb{R}$

unary: $g: A \rightarrow A$

**Field হওয়ার শর্ত under addition:**
1. **Closure property:** $x, y \in K \Rightarrow x+y \in K$
2. **Commutative property (Abelian):** $x+y = y+x \quad (x, y \in F)$
3. **Associative property:** $x+(y+z) = (x+y)+z$
4. **Identity law:**
   - $0+1 = 1$
   - $0+x = x \quad (x \in F)$
   - $a \in K, e \in K \Rightarrow a+e = a$
   - $\mathbb{Z} = \lbrace\dots, -2, -1, 0, 1, 2, \dots \rbrace$ (identity for $\mathbb{Z}$)