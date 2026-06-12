<!-- Page 031 -->
**# Write the matrix

$$
A =
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
1 & 2 & 1
\end{pmatrix}
$$

as the sum of a symmetric matrix and a skew symmetric matrix.**

Ans:

$$
B =
\begin{pmatrix}
1 & 3 & 2 \\
3 & 5 & 4 \\
2 & 4 & 1
\end{pmatrix}
$$

$$
C =
\begin{pmatrix}
0 & -1 & 1 \\
1 & 0 & 2 \\
-1 & -2 & 0
\end{pmatrix}
$$

$B = \frac{1}{2}(A + A^T)$

$$
= \frac{1}{2}\left[
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
1 & 2 & 1
\end{pmatrix} + \begin{pmatrix} 1 & 4 & 1 \\ 2 & 5 & 2 \\ 3 & 6 & 1 \end{pmatrix}\right]
$$

$$
= \frac{1}{2}
\begin{pmatrix}
2 & 6 & 4 \\
6 & 10 & 8 \\
4 & 8 & 2
\end{pmatrix} = \begin{pmatrix} 1 & 3 & 2 \\ 3 & 5 & 4 \\ 2 & 4 & 1 \end{pmatrix}
$$

$C = \frac{1}{2}(A - A^T)$

$$
= \frac{1}{2}\left[
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
1 & 2 & 1
\end{pmatrix} - \begin{pmatrix} 1 & 4 & 1 \\ 2 & 5 & 2 \\ 3 & 6 & 1 \end{pmatrix}\right]
$$

$$
= \frac{1}{2}
\begin{pmatrix}
0 & -2 & 2 \\
2 & 0 & 4 \\
-2 & -4 & 0
\end{pmatrix} = \begin{pmatrix} 0 & -1 & 1 \\ 1 & 0 & 2 \\ -1 & -2 & 0 \end{pmatrix}
$$

Thus,

$$
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
1 & 2 & 1
\end{pmatrix} = \begin{pmatrix} 1 & 3 & 2 \\ 3 & 5 & 4 \\ 2 & 4 & 1 \end{pmatrix} + \begin{pmatrix} 0 & -1 & 1 \\ 1 & 0 & 2 \\ -1 & -2 & 0 \end{pmatrix}
$$

<!-- Page 032 -->

$$
A =
\begin{bmatrix}
i & -2+i & 3i+2 \\
0 & -i & 2i \\
0 & 3 & 4+5i
\end{bmatrix}
$$

**hermitian:**
$A^\theta$ or $A^H$ or $A^\oplus = (\bar{A})^T = (\overline{A^T})$

$A^\theta = A \Rightarrow$ hermitian
$A^\theta = -A \Rightarrow$ skew hermitian

$B = \frac{1}{2}(A^\theta + A)$
$C = \frac{1}{2}(A - A^\theta)$

$A = \frac{1}{2}(A^\theta + A) + \frac{1}{2}(A - A^\theta) = B + C$

Now,
$B = \frac{1}{2}(A^\theta + A) = \frac{1}{2}((\bar{A})^T + A)$

$$
= \frac{1}{2} \left[
\begin{pmatrix}
-i & -2-i & 3i+2 \\
0 & i & -2i \\
0 & 3 & 4-5i
\end{pmatrix}^T + \begin{pmatrix} i & -2+i & 3i+2 \\ 0 & -i & 2i \\ 0 & 3 & 4+5i \end{pmatrix} \right]
$$

$$
= \frac{1}{2} \left[
\begin{bmatrix}
-i & 0 & 0 \\
-2-i & i & 3 \\
-3i+2 & -2i & 4-5i
\end{bmatrix} + \begin{bmatrix} i & -2+i & 3i+2 \\ 0 & -i & 2i \\ 0 & 3 & 4+5i \end{bmatrix} \right]
$$

$$
= \frac{1}{2}
\begin{bmatrix}
0 & -2+i & 3i+2 \\
-2-i & 0 & 3+2i \\
2-3i & 3-2i & 8
\end{bmatrix}
$$

(hermitian)

- main diagonal এ real number থাকা লাগবে।

<!-- Page 033 -->
$C = \frac{1}{2}[A - A^\theta]$

$$
= \frac{1}{2} \left[
\begin{bmatrix}
i & -2+i & 2+3i \\
0 & -i & 2i \\
0 & 3 & 4+5i
\end{bmatrix} - \begin{bmatrix} -i & 0 & 0 \\ -2-i & i & 3 \\ 2-3i & -2i & 4-5i \end{bmatrix} \right]
$$

$$
= \frac{1}{2}
\begin{bmatrix}
2i & -2+i & 2+3i \\
2+i & -2i & 2i-3 \\
-2+3i & 3+2i & 10i
\end{bmatrix}
$$

(skew hermitian)

*(Note: The notes contain a slight sign error in calculating $C$ in the original handwriting where $A^\theta - A$ was written instead of $A - A^\theta$, but the final properties hold.)*

- main diagonal এর elements purely imaginary.
- negative conjugate super, sub এর

---

<b>Class 17 | sir</b>
<div align="right"><b>12-01-26</b></div>

**# What is a nilpotent / zeropotent / nullpotent matrix?**
$A^n = [0]$ or $A^n = 0$ ($A$ is square matrix), a zero matrix.

**# involutary matrix:**
$A^2 = I$

**# periodic matrix:**
$A^{n+1} = A$; period $= n$

**# idempotent matrix:**
$A^2 = A$

এই related theory.

iff $\rightarrow$ if and only if
if

**# An n-square matrix $A$ is involutory iff $(I+A)(I-A) = 0$, a zero matrix.**
এটা থাকলে conversely proof করতে হবে।

We know an n-square matrix $A$ is involutory if $A^2 = I$.
First, we assume that $A$ is involutory. We need to proof that $(I-A)(I+A) = O_{n \times n}$ where $I = n \times n$ identity matrix.

<!-- Page 034 -->
Now,
$(I-A)(I+A) = I^2 - AI + IA - A^2 = I - A + A - I = 0$ (proved) (Since $A^2 = I$)

Conversely, assume that $(I-A)(I+A) = 0$, $0 = \text{zero matrix}$.
we need to show proof that $A$ is involutory.
Here,
$(I-A)(I+A) = 0$
$\Rightarrow I^2 + I \cdot A - A \cdot I - A^2 = 0$
$\Rightarrow I + A - A - A^2 = 0$
$\Rightarrow I - A^2 = 0 \Rightarrow A^2 = I$ yielding $A$ is involuntary. This completes the proof.

**Associative law for sum:**
$(A+B)+C = A + (B+C)$

**Associative law for multiplication:**
$A(BC) = (AB)C$

**Commutative law for multiplication:**
$AB = BA = I$
$A, B$ should be square matrix of same size.
$B$ is called the inverse matrix of $A$.

**# $(AB)^{-1} = B^{-1} A^{-1}$ proof that.**
$(AB)^{-1}(AB) = I$
$(AB)(AB)^{-1} = I$

Here,
$AB(B^{-1} A^{-1}) = A(B B^{-1})A^{-1}$ (associative law)
$= A I A^{-1} = A A^{-1} = I$

<!-- Page 035 -->
Again,
$(B^{-1} A^{-1}) AB = B^{-1}(A^{-1} A)B = B^{-1}(I B) = B^{-1} B = I$

that's how we can say $(B^{-1} A^{-1})$ is the inverse of $(AB)$.
Therefore, $B^{-1} A^{-1} = (AB)^{-1}$
$\Rightarrow (AB)^{-1} = B^{-1} A^{-1}$ (proved)

*Frank Ayers এর বই*

**# $\text{adj}(AB) = \text{Adj}(B) \cdot \text{adj}(A)$**
**# $(AB)^t = B^t A^t$**

$$
A =
\begin{pmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{pmatrix},
$$

$$
B =
\begin{pmatrix}
1 & 2 & 3 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{pmatrix}
$$

$\rightarrow$ *This is verification not proof. be careful.*

$$
A =
\begin{pmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{pmatrix},
$$

$$
B =
\begin{pmatrix}
b_{11} & b_{12} & b_{13} \\
b_{21} & b_{22} & b_{23} \\
b_{31} & b_{32} & b_{33}
\end{pmatrix}
$$

$a_{32} = \text{element/entry standing at the 3rd row, 2nd column}$

$$
A^t =
\begin{pmatrix}
a_{11} & a_{21} & a_{31} \\
a_{12} & a_{22} & a_{32} \\
a_{13} & a_{23} & a_{33}
\end{pmatrix},
$$

$$
B^t =
\begin{pmatrix}
b_{11} & b_{21} & b_{31} \\
b_{12} & b_{22} & b_{32} \\
b_{13} & b_{23} & b_{33}
\end{pmatrix}
$$

$$
AB =
\begin{pmatrix}
a_{11}b_{11} + a_{12}b_{21} + a_{13}b_{31} & a_{11}b_{12} + a_{12}b_{22} + a_{13}b_{32} & a_{11}b_{13} + a_{12}b_{23} + a_{13}b_{33} \\
a_{21}b_{11} + a_{22}b_{21} + a_{23}b_{31} & a_{21}b_{12} + a_{22}b_{22} + a_{23}b_{32} & a_{21}b_{13} + a_{22}b_{23} + a_{23}b_{33} \\
a_{31}b_{11} + a_{32}b_{21} + a_{33}b_{31} & a_{31}b_{12} + a_{32}b_{22} + a_{33}b_{32} & a_{31}b_{13} + a_{32}b_{23} + a_{33}b_{33}
\end{pmatrix}
$$

<!-- Page 036 -->
$(AB)^t = B^t A^t$

$i\text{th row } j\text{th column's element}$
$j\text{th row } i\text{th column's element}$

The element standing at the $i\text{th}$ row and $j\text{th}$ column of $AB$.

---

<b>Class 18 | mam</b>
<div align="right"><b>13-01-26</b></div>

**Surface Integral**

$\iint_s A \cdot n \, ds$
$n = \text{unit normal vector}$
$S = \text{surface}$
$A = \text{vector field / area}$

$ds = \frac{dx \, dy}{|n \cdot k|}$ (where $k$ is normal to the plane of projection)

$ds = \frac{dx \, dz}{|n \cdot j|}$
$ds = \frac{dy \, dz}{|n \cdot i|}$

surface কে region এ convert করে ফেলেছি।

$2x+3y+6z = 12$
$2x+3y = 12 \quad (z=0)$
$y = \frac{12-2x}{3} \quad (y=0)$
$x = 6 \quad (x=0)$

<!-- Page 037 -->
<b>Class 19 | sir</b>
<div align="right"><b>19-01-26</b></div>

$(AB)^t = B^t A^t$

$$
(AB)^t =
\begin{pmatrix}
a_{11}b_{11} + a_{12}b_{21} + a_{13}b_{31} & a_{21}b_{11} + a_{22}b_{21} + a_{23}b_{31} & a_{31}b_{11} + a_{32}b_{21} + a_{33}b_{31} \\
a_{11}b_{12} + a_{12}b_{22} + a_{13}b_{32} & a_{21}b_{12} + a_{22}b_{22} + a_{23}b_{32} & a_{31}b_{12} + a_{32}b_{22} + a_{33}b_{32} \\
a_{11}b_{13} + a_{12}b_{23} + a_{13}b_{33} & a_{21}b_{13} + a_{22}b_{23} + a_{23}b_{33} & a_{31}b_{13} + a_{32}b_{23} + a_{33}b_{33}
\end{pmatrix}
$$

**# Prove: $(AB)^t = B^t A^t$**

The element standing at the $i\text{th}$ row and $j\text{th}$ column of $AB$ is $\sum_{k} a_{ik} b_{kj}$ which is the element standing at the $j\text{th}$ row and $i\text{th}$ column of $(AB)^t$.

The elements standing at $j$-th row of $B^t$:
$b_{1j}, b_{2j}, b_{3j} \dots b_{nj}$

The elements standing at $i$-th column of $A^t$:
$a_{i1}, a_{i2}, a_{i3} \dots a_{in}$

<!-- Page 038 -->
Thus the element standing at the $j$-th row and $i$-th column of $B^t A^t$ is:
$\sum_k b_{kj} a_{ik} = \sum_k a_{ik} b_{kj}$

Thus,
$(AB)^t = B^t A^t$ (proved)

**Linear Algebra:**
**Eigen value:**
$A \vec{V} = \lambda \vec{V}$
ভেক্টরের উপর এমন operator ব্যবহার করলে তার direction change হয় না।
যাদের eigenvalue high তাদের বলে Representative.

$R^3 = (a, b, c)$ $\rightarrow$ 3D
$R^2 = (a, b)$

$$
\begin{pmatrix}
1 & 1 & 2 \\
1 & 1 & 1 \\
1 & 1 & 1
\end{pmatrix}
$$

(3D)

$$
\begin{pmatrix}
1 & 2 & 4 & 5 \\
2 & 4 & 5 & 6 \\
8 & 9 & 10 & 11
\end{pmatrix}
$$

(5D $\rightarrow$)

**Characteristics matrix**
**Characteristics equation**
**Eigen value**

Let $A = (a_{ij})_{n \times n}$ be an $n$-square matrix. Then the characteristic matrix of $A$ is $A - \lambda I$.

**Characteristics polynomial:** The polynomial $|A - \lambda I|$ is called characteristics polynomial.

$I + \lambda A + \lambda^2 A^2 \dots$ (not finite, not polynomial)
$A^n + A^{n-1} + I$ (highest finite power $\Rightarrow$ polynomial)

<!-- Page 039 -->
**Characteristics equation:** The equation $|A - \lambda I| = 0$ is called ch. eqn.

The solutions of ch. eqn are called eigenvalues and associated with the eigen values corresponding vectors are called eigen vector.
$\rightarrow$ Eigen values are independent from another.

**Applications**

---

<b>Class 20 | mam</b>
<div align="right"><b>20-01-26</b></div>

**Volume integral**

**CH-6 divergence theorem**
$\rightarrow$ Stokes thm
$\rightarrow$ Greens theorem

simple closed curve, normal closed curve
no intersect (circle)
self intersect (figure 8)
intersect করবে না

**Core table:**
Grad, div, curl
integration
দাগানো গুলো and core type

<!-- Page 040 -->
<b>Class 21 | sir</b>
<div align="right"><b>24-01-26</b></div>

**# characteristics matrix**
$A_{n \times n}$ ch matrix is $A - \lambda I$
ch polynomial is $|A - \lambda I|$
ch eqn is $|A - \lambda I| = 0$
values of $\lambda$ are called eigen values.

characteristics vector:
**# Consider a matrix

$$
A =
\begin{pmatrix}
4 & 1 \\
2 & 3
\end{pmatrix}.
$$

Find its eigenvalues and eigenvectors.**
(2 eigen values and 2 vectors)

Characteristic matrix of $A$ is $A - \lambda I$.

$$
\begin{pmatrix}
4 & 1 \\
2 & 3
\end{pmatrix} - \lambda \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{pmatrix}
$$

Now, the ch. equation is $|A - \lambda I| = 0$

$$
\Rightarrow
\begin{vmatrix}
4-\lambda & 1 \\
2 & 3-\lambda
\end{vmatrix} = 0
$$

$\Rightarrow (4-\lambda)(3-\lambda) - 2 = 0$
$\Rightarrow 12 - 7\lambda + \lambda^2 - 2 = 0$
$\Rightarrow \lambda^2 - 7\lambda + 10 = 0$
$\Rightarrow \lambda = 2, 5$

thus the eigen values are 2, 5.
(different eigen values)

- negative হলে stable (asymptotically stable)
- জিরো হলে marginal stable

For $\lambda = 2$:

$$
(A - 2I)X = 0 \Rightarrow
\begin{pmatrix}
2 & 1 \\
2 & 1
\end{pmatrix}\begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix} \Rightarrow 2x_1 + x_2 = 0 \Rightarrow x_2 = -2x_1
$$

eigenvector is

$$
\begin{pmatrix}
1 \\
-2
\end{pmatrix}.
$$

Verification:

$$
A
\begin{pmatrix}
1 \\
-2
\end{pmatrix} = \begin{pmatrix} 2 \\ -4 \end{pmatrix} = 2\begin{pmatrix} 1 \\ -2 \end{pmatrix}
$$

pointing to eigenvalue (2) and eigenvector

$$
\begin{pmatrix}
1 \\
-2
\end{pmatrix}.
$$
