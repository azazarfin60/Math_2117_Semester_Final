# Fahad's Class Note - Pages 51-60

## Page 51

$$
A^t = \begin{bmatrix} a_{11} & a_{21} & a_{31} \\ a_{12} & a_{22} & a_{32} \\ a_{13} & a_{23} & a_{33} \end{bmatrix} \quad \text{and} \quad B^t = \begin{bmatrix} b_{11} & b_{21} & b_{31} \\ b_{12} & b_{22} & b_{32} \\ b_{13} & b_{23} & b_{33} \end{bmatrix}
$$

$$
AB = \begin{bmatrix} a_{11}b_{11}+a_{12}b_{21}+a_{13}b_{31} & a_{11}b_{12}+a_{12}b_{22}+a_{13}b_{32} & a_{11}b_{13}+a_{12}b_{23}+a_{13}b_{33} \\ a_{21}b_{11}+a_{22}b_{21}+a_{23}b_{31} & a_{21}b_{12}+a_{22}b_{22}+a_{23}b_{32} & a_{21}b_{13}+a_{22}b_{23}+a_{23}b_{33} \\ a_{31}b_{11}+a_{32}b_{21}+a_{33}b_{31} & a_{31}b_{12}+a_{32}b_{22}+a_{33}b_{32} & a_{31}b_{13}+a_{32}b_{23}+a_{33}b_{33} \end{bmatrix}
$$

> [!NOTE]
> গুণ ভুল আছে (Referencing that the student wrote a note about a multiplication error in their handwritten calculations, though the above matrix representation is mathematically correct for $AB$).

$\star$ **As now $j$-th column element**
The element standing at the $i$-th row and $j$-th column of $AB$.

$$
\text{next cls.}
$$

---

## Page 52

**Math-2117**
**(13 Jan, 26) (Rupali Maam)**

### Vector integration.
* **Line integral $\rightarrow$ (done)**

#### Surface integral:-

**Problem - 17, 18, 19, 20, 23, 21, 22**

$$
\rightarrow \text{next cls surface integral.}
$$

---

$$
(AB)^t = \begin{bmatrix} a_{11}b_{11}+a_{12}b_{21}+a_{13}b_{31} & a_{21}b_{11}+a_{22}b_{21}+a_{23}b_{31} & a_{31}b_{11}+a_{32}b_{21}+a_{33}b_{31} \\ a_{11}b_{12}+a_{12}b_{22}+a_{13}b_{32} & a_{21}b_{12}+a_{22}b_{22}+a_{23}b_{32} & a_{31}b_{12}+a_{32}b_{22}+a_{33}b_{32} \\ a_{11}b_{13}+a_{12}b_{23}+a_{13}b_{33} & a_{21}b_{13}+a_{22}b_{23}+a_{23}b_{33} & a_{31}b_{13}+a_{32}b_{23}+a_{33}b_{33} \end{bmatrix}
$$

$$
\text{next cls.}
$$

---

## Page 53

**Math-2117**
**(19 Jan, 26) (GCP Sir)**

$\star$ **Rajshahi-র ১০টি District-এর bus fair-এর matrix code করতে হবে।**
* **Accurate**
* **Per kilo hisab করতে হবে।**

$\star$ **Prove that $(AB)^t = B^t A^t$**

From previous class,

$$
(AB)^t = \begin{bmatrix} a_{11}b_{11}+a_{21}b_{12}+a_{31}b_{13} & a_{12}b_{11}+a_{22}b_{12}+a_{32}b_{13} & a_{13}b_{11}+a_{23}b_{12}+a_{33}b_{13} \\ a_{11}b_{21}+a_{21}b_{22}+a_{31}b_{23} & a_{12}b_{21}+a_{22}b_{22}+a_{32}b_{23} & a_{13}b_{21}+a_{23}b_{22}+a_{33}b_{23} \\ a_{11}b_{31}+a_{21}b_{32}+a_{31}b_{33} & a_{12}b_{31}+a_{22}b_{32} & a_{13}b_{31}+a_{23}b_{32}+a_{33}b_{33} \end{bmatrix}
$$

> [!NOTE]
> গুণ ভুল আছে (Points to errors in the index elements of $(AB)^t$ as written by the student).

* **$(AB)^t$-এর $i$-th row $j$-th column-এর একটি specific element নিব। এবং $B^t A^t$-এর same element-এর সাথে compare করব।**

**(2nd row 3rd column)**

The element standing at the $i$-th row and $j$-th column of $AB$ is:

$$
\sum a_{in} b_{nj}
$$

which is the element standing at the $j$-th row and $i$-th column of $(AB)^t$.

The element standing at $j$-th row of $B^t$ is:

$$
b_{1j}, b_{2j}, b_{3j} \dots b_{nj}
$$

---

## Page 54

The elements of $i$-th column of $A^t$ are:-

$$
a_{i1}, a_{i2}, a_{i3} \dots a_{in}
$$

Thus the element standing at the $j$-th row and $i$-th column of $B^t A^t$ are:-

$$
\text{(2nd row 3rd column)}
$$

$$
\sum a_{in} b_{nj} \quad \Big| \quad a_{i1}b_{1j} + a_{i2}b_{2j} + a_{i3}b_{3j} + \dots a_{in}b_{nj}
$$

Thus,

$$
(AB)^t = B^t A^t \quad \text{(proved)}
$$

$$
\sum_{n=1}^{n} a_{in} b_{nj}
$$

---

## Page 55

### Linear Algebra:-

$$
AV = \lambda V
$$

$$
V \rightarrow \text{vector.}
$$

$\star$ **Vector space-এ যে সকল vector-কে operate করলে change হয় না তাদের eigen vector বলে।**

* **eigen value $\rightarrow$ কেন $\rightarrow$ কেন important.**
* **Characteristic matrix, ch. equation, Eigen values.**

#### Characteristic matrix:-
Let $A = (a_{ij})_{n \times n}$ be an n-square matrix. Then the characteristic matrix of $A$ is

$$
A - \lambda I
$$

#### Characteristic polynomial:-
The polynomial $|A - \lambda I|$ is called ch. polynomial.

$$
\rightarrow A^n + A^{n-1} + \dots + I \rightarrow \text{highest power finite.}
$$

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots \quad \rightarrow \text{(not polynomial)}
$$

---

## Page 56

#### Characteristic equation:-
The equation $|A - \lambda I| = 0$ is called ch. equation.

* **The solutions of $|A - \lambda I| = 0$ are called eigen values and the corresponding vectors associated with the eigen values are called eigen vectors.**
* **eigen vectors গুলো linearly independent.**

---

## Page 57

**Math-2117**
**(20 Jan, 26) (Rupali Maam)**

$$
\text{CT-3} \rightarrow \text{Grad, div, curl} \ (\text{chap}) \ , \ \text{integration (line, surface, volume)} \ (\text{chap})
$$

* **Volume integration:- $\checkmark$ (done)**

#### Problem $\rightarrow$ 26:-

$\star$ **Chapter 6:- The divergence theorem, Stokes theorem and related integral theorems.**

#### The divergence theorem:-
#### Stokes theorem:-

$$
\text{Converting surface integral to line.}
$$

#### Green's theorem:-

---

## Page 58

**Math-2117**
**(21 Jan, 26) (GCP Sir)**

$\star$ **$A_{n \times n}$**
* **ch. matrix $= A - \lambda I$**
* **ch. polynomial $= |A - \lambda I|$**
* **ch. equation $\rightarrow |A - \lambda I| = 0$**
* **values of $\lambda \rightarrow$ eigen values**

$\star$ **Consider the matrix

$$
A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}.
$$

Find its eigen values and eigen vectors.**

**Ans:-**

Characteristic (ch) matrix of $A$ is

$$
A - \lambda I = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix} - \lambda \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$

$$
= \begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix} \rightarrow \text{ch. matrix (Ans:)}
$$

Now, the characteristic equation is $|A - \lambda I| = 0$

$$
\Rightarrow \begin{vmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{vmatrix} = 0
$$

$$
\Rightarrow 12 - 7\lambda + \lambda^2 - 2 = 0
$$

$$
\Rightarrow \lambda^2 - 7\lambda + 10 = 0
$$

$$
\Rightarrow \lambda = 2, 5 \rightarrow \text{eigen values.}
$$

---

## Page 59

* **$\lambda (-)$ হলে asymptotically stable.**
* **eigen value $(+)$ হলে systemটি unstable.**

$\star$ **Thus the eigen values are 2, 5.**
$\star$ **we are operating in $2 \times 2$ Euclidean space $R^2 \rightarrow$ প্রতি vector-এর corresponding ২টা eigenvalues পাওয়া যাবে তার মধ্যে ১টি নিয়ে determine করতেছি।**

Let,

$$
V = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}
$$

be an eigen vector corresponding to the eigen value $\lambda = 2$.

Then,

$$
AV = \lambda V
$$

$$
\text{or, } AV - \lambda V = 0 \quad \text{, a zero matrix}
$$

$$
\text{or, } (A - \lambda I)V = 0
$$

$$
\text{or, } \begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \quad \text{; } \lambda = 2
$$

$$
\text{or, } \begin{bmatrix} 2 & 1 \\ 2 & 1 \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

$$
\text{or, } \begin{bmatrix} 2v_1 + v_2 \\ 2v_1 + v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

$$
\therefore 2v_1 + v_2 = 0 \quad \text{yielding } 2v_1 + v_2 = 0.
$$

Let, $v_2 = 2$, then $v_1 = -1$.

$$
\rightarrow \text{there are many solutions, we are just considering one.}
$$

Thus,

$$
V = \begin{bmatrix} -1 \\ 2 \end{bmatrix}
$$

is an eigen vector corresponding to the eigen value $\lambda = 2$.

---

## Page 60

**eigen value $\lambda = 5$.**

**Again,**
Let,

$$
W = \begin{bmatrix} w_1 \\ w_2 \end{bmatrix}
$$

be an eigen vector corresponding to the eigen value $\lambda = 5$.

Then eigen value equation will be,

$$
AW = \lambda W \quad \text{, giving yielding}
$$

$$
(A - \lambda I)W = 0 \quad \text{, a zero matrix}
$$

$$
\Rightarrow \begin{bmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

$$
\Rightarrow \begin{bmatrix} -1 & 1 \\ 2 & -2 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

$$
\Rightarrow \begin{bmatrix} -w_1 + w_2 \\ 2w_1 - 2w_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

This gives,

$$
-w_1 + w_2 = 0
$$

$$
2w_1 - 2w_2 = 0
$$

$$
\Rightarrow w_1 - w_2 = 0 \quad \text{, the system has more than one solution.}
$$
