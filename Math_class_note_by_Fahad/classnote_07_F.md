# Fahad's Class Note - Pages 61-70

## Page 61

Set

$$
w_1 = 1
$$

, then

$$
w_2 = 1
$$

, then

then

$$
\begin{bmatrix}
1 \\
1
\end{bmatrix}
$$

is an eigen vector associated with the eigen value $\lambda = 5$.

> [!NOTE]
> ↳ 2টি independent eigen value পাব।
>
> $\therefore$ Then model matrix is $\rightarrow$ extended.

$$
P =
\begin{bmatrix}
-1 & 1 \\
2 & 1
\end{bmatrix} \quad \rightarrow \text{Linearly dependent না!}
$$

$$
\text{:: একটি দেখে কখনোই আরেকটি পাওয়া যাবে না।}
$$

$$
P \xrightarrow{R_2 \rightarrow 2R_1 + R_2}
\begin{bmatrix}
-1 & 1 \\
0 & 3
\end{bmatrix} \quad \text{Not 0} \quad \therefore \text{the eigen vectors are independent.}
$$

$$
P^{-1} = -\frac{1}{3}
\begin{bmatrix}
1 & -1 \\
-2 & -1
\end{bmatrix} = \frac{1}{3} \begin{bmatrix} -1 & 1 \\ 2 & 1 \end{bmatrix}
$$

Now,

$$
P^{-1}AP = \frac{1}{3}
\begin{bmatrix}
-1 & 1 \\
2 & 1
\end{bmatrix} \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix} \begin{bmatrix} -1 & 1 \\ 2 & 1 \end{bmatrix}
$$

$$
= \frac{1}{3}
\begin{bmatrix}
-2 & 2 \\
10 & 5
\end{bmatrix} \begin{bmatrix} -1 & 1 \\ 2 & 1 \end{bmatrix}
$$

$$
= \frac{1}{3}
\begin{bmatrix}
6 & 0 \\
0 & 15
\end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & 5 \end{bmatrix} \quad \rightarrow \text{diagonalized matrix.}
$$

---

## Page 62

**Math-2117**
**(26 Jan, 26) (GCP Sir)**

### Eigen values and eigen vectors:- (with equal eigen values)
$\rightarrow$ We need to find out equal effective eigen values.

$\star$ **Consider the matrix**

$$
A =
\begin{bmatrix}
3 & -1 \\
1 & 1
\end{bmatrix}
$$

characteristic matrix of $A$ is

$$
A - \lambda I =
\begin{bmatrix}
3 & -1 \\
1 & 1
\end{bmatrix} - \lambda \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 3-\lambda & -1 \\ 1 & 1-\lambda \end{bmatrix}
$$

$\therefore$ ch. polynomial of $A$ is $|A - \lambda I|$ and hence the ch. polynomial equation is $|A - \lambda I| = 0$.

$$
\Rightarrow
\begin{vmatrix}
3-\lambda & -1 \\
1 & 1-\lambda
\end{vmatrix} = 0
$$

$$
\Rightarrow 3 - 3\lambda - \lambda + \lambda^2 + 1 = 0
$$

$$
\Rightarrow \lambda^2 - 4\lambda + 4 = 0
$$

$$
\Rightarrow (\lambda - 2)^2 = 0
$$

$$
\therefore \lambda = 2, 2
$$

---

## Page 63

Let,

$$
V =
\begin{bmatrix}
v_1 \\
v_2
\end{bmatrix}
$$

be the eigen vector corresponding to the eigen value $\lambda = 2$.

$$
AV - \lambda V = (A - \lambda I)V = 0 \text{ , a zero vector}
$$

$$
\Rightarrow
\begin{bmatrix}
3-\lambda & -1 \\
1 & 1-\lambda
\end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

$$
\Rightarrow
\begin{bmatrix}
3-2 & -1 \\
1 & 1-2
\end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

$$
\Rightarrow
\begin{bmatrix}
1 & -1 \\
1 & -1
\end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

$$
\text{or, } \left.
\begin{matrix}
v_1 - v_2 = 0 \\
v_1 - v_2 = 0
\end{matrix} \right\rbrace  \sim v_1 - v_2 = 0
$$

Set,

$$
v_2 = 1.
$$

$$
v_1 = 1
$$

$$
\therefore V =
\begin{bmatrix}
1 \\
1
\end{bmatrix}
$$

is an eigen vector corresponding to the eigen value $\lambda = 2$.

$$
\star \text{ H.W. }
\begin{bmatrix}
2 & 1 \\
-1 & 1
\end{bmatrix} \text{ find eigen values and eigen vectors.}
$$

---

## Page 64

$\star$ **Cayley-Hamilton theorem:-**
We can find the inverse of a matrix if the inverse exists. (if eigen values are different)

#### Theorem:-
Every matrix is a zero in its ch. polynomial.

$$
A_{2 \times 2} = \lambda^2 + a\lambda + b = 0
$$

$$
\therefore A^2 + aA + bI = 0 \text{ , a zero matrix.}
$$

> [!NOTE]
> Margin notes:
> $|A - \lambda I| = 0$
> $A' = |A| \neq 0$
> $|A| = |A'|$

$\star$ **Consider the matrix**

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
-1 & 2 & 4 \\
1 & 1 & 2
\end{bmatrix}_{3 \times 3}
$$

**Ans:-**
ch. polynomial of $A$ is

$$
|A - \lambda I| =
\begin{vmatrix}
1 & 2 & 3 \\
-1 & 2 & 4 \\
1 & 1 & 2
\end{vmatrix} - \lambda \begin{vmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{vmatrix}
$$

$$
\Rightarrow |A - \lambda I| =
\begin{vmatrix}
1-\lambda & 2 & 3 \\
-1 & 2-\lambda & 4 \\
1 & 1 & 2-\lambda
\end{vmatrix}
$$

$$
\Rightarrow |A - \lambda I| = (1-\lambda) \lbrace (2-\lambda)^2 - 4 \rbrace - 2 \lbrace -1(2-\lambda) - 4 \rbrace + 3 \lbrace -1 - 1(2-\lambda) \rbrace
$$

$$
= (1-\lambda)(4 - 4\lambda + \lambda^2 - 4) - 2 \lbrace \lambda - 2 - 4 \rbrace + 3 \lbrace -1 - 2 + \lambda \rbrace
$$

$$
= -4\lambda + \lambda^2 + 4\lambda^2 - \lambda^3 + 12 - 2\lambda - 9 + 3\lambda
$$

---

## Page 65

$$
= -\lambda^3 + 5\lambda^2 - 3\lambda + 3 = 0
$$

$$
\rightarrow \text{যেহেতু Determinent Not (0) } \therefore \text{ Inverse বের করা যাবে!}
$$

By Cayley-Hamilton theorem, we have,

$$
-A^3 + 5A^2 - 3A + 3I = 0 \text{ , a zero matrix.}
$$

$$
\Rightarrow -A^{-1}A^3 + 5A^{-1}A^2 - 3A^{-1}A + 3A^{-1}I = A^{-1} \cdot 0
$$

$$
\Rightarrow -A^2 + 5A - 3I + 3A^{-1} = 0
$$

$$
\Rightarrow 3A^{-1} = 0 + A^2 - 5A + 3I
$$

$$
\Rightarrow 3A^{-1} = A^2 - 5A + 3I
$$

$$
\Rightarrow 3A^{-1} =
\begin{bmatrix}
1 & 2 & 3 \\
-1 & 2 & 4 \\
1 & 1 & 2
\end{bmatrix} \begin{bmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{bmatrix} - 5 \begin{bmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{bmatrix} + 3 \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

$$
\Rightarrow 3A^{-1} =
\begin{bmatrix}
0 & -1 & 2 \\
6 & -1 & -7 \\
-3 & 1 & 4
\end{bmatrix}
$$

$$
\star \text{ PCA, CCA, ICA}
$$

$$
\text{↳ Principle Component Analysis}
$$

---

## Page 66

**Math-2117**
**(03 Feb, 26) (GCP Sir)**

$$
A =
\begin{bmatrix}
4 & 1 \\
2 & 3
\end{bmatrix}, \ \lambda = 2, 5, \ V = \begin{bmatrix} -1 \\ 2 \end{bmatrix}, \ W = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \ P = \begin{bmatrix} -1 & 1 \\ 2 & 1 \end{bmatrix}
$$

$$
P^{-1} = \frac{1}{3}
\begin{bmatrix}
-1 & 1 \\
2 & 1
\end{bmatrix} \quad \therefore P^{-1}AP = \begin{bmatrix} 2 & 0 \\ 0 & 5 \end{bmatrix}
$$

$$
P^{-1}AP = M
$$

$$
M^5 =
\begin{bmatrix}
32 & 0 \\
0 & 3125
\end{bmatrix} \quad P^{-1}AP = \begin{bmatrix} 2 & 0 \\ 0 & 5 \end{bmatrix}
$$

$\star$ **Find $A^5$.**

**Ans:-**

$$
A^5 = P M^5 P^{-1} = \frac{1}{3}
\begin{bmatrix}
-1 & 1 \\
2 & 1
\end{bmatrix} \begin{bmatrix} 32 & 0 \\ 0 & 3125 \end{bmatrix} \begin{bmatrix} -1 & 1 \\ 2 & 1 \end{bmatrix}
$$

$$
\rightarrow \text{Thus you can get any power of A.}
$$

$$
\rightarrow \text{You can also calculate } A^{100} \text{ using this method.}
$$

$\star$ **$\mathbb{R}^n \rightarrow$ n dimensional Euclidean space**

$$
\mathbb{R}^2 = \lbrace (a, b) \mid a, b \in \mathbb{R} \rbrace
$$

$$
\mathbb{R}^3 = \lbrace (a, b, c) \mid a, b, c \in \mathbb{R} \rbrace
$$

$$
\mathbb{R}^4 = \lbrace (a, b, c, d) \mid a, b, c, d \in \mathbb{R} \rbrace
$$

> [!NOTE]
> Coordinate system drawings:
> - For $\mathbb{R}^2$, showing point $(1,2)$ with vector representing $(i + 2j)$.
> - For $\mathbb{R}^3$, showing point $(1,2,3)$ with vector representing $(i + 2j + 3\hat{k})$.
>
> Bengali text:
> $\rightarrow$ ৩ টির বেশি vector-এ লিখতে পারি না। আমরা transform করে 4D থেকে 3D করতে পারব।

---

## Page 67

$$
\mathbb{R}^n = \lbrace (a_1, a_2, a_3 \dots a_n) \mid a_1, a_2, a_3 \dots a_n \in \mathbb{R} \rbrace
$$

$\star$ **

$$
\mathbb{R}^3 \rightarrow v_1 = (1, 0, 0), v_2 = (0, 1, 0), v_3 = (0, 0, 1)
$$

**

$$
\text{row vector / column vector. We can also use vectors,}
$$

$$
\begin{vmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{vmatrix} \neq 0 \rightarrow \text{হলে independent}
$$

$$
\rightarrow \text{usual basis of } \mathbb{R}^3
$$

$$
\star \text{ Independent হলে } \rightarrow \text{ you can generate all vectors in } \mathbb{R}^3 \text{ from these 3 vectors.}
$$

$\star$ **

$$
\begin{bmatrix}
1 & 2 \\
2 & 1
\end{bmatrix}
$$

vectors থেকে $(4, 5)$ নির্ণয়।**

$$
(4, 5) = a(1, 2) + b(2, 1)
$$

$$
= (a + 2b, 2a + b)
$$

$$
\therefore a + 2b = 4
$$

$$
2a + b = 5 \quad \therefore a = 2, \ b = 1
$$

$$
\therefore (4, 5) = 2(1, 2) + 1(2, 1)
$$

$\star$ **We need to define a generalized linear product to find the angle between any 2 vectors.**

$$
\vec{A} \cdot \vec{B} = AB \cos \theta \quad \rightarrow \text{valid for } \mathbb{R}^3 \text{ not more than } \mathbb{R}^3 .
$$

---

## Page 68

$$
\text{PCB Design Session}
$$

$$
\text{PCB } \rightarrow \text{ Printed Circuit Board}
$$

### Simple IPS design:-
```
          E_on (Bulb)    E_off (Bulb)
             \             /
              \___________/
                    |
                 [System] ------ [Battery]
```

#### Input:-
1. DC Jack (12V)
2. AC Line
   - $\rightarrow$ transformer
   - $\rightarrow$ Diode

#### Output:-
1. 3 terminals.

#### System:-
1. Electrical switch (Relay) $\rightarrow$ to switch between bulbs.

---

## Page 69

$$
\rightarrow \text{Preliminaries of vector Space.}
$$

$\star$ **Finding the angle between 2 vectors.**

### Array Multiplication:-

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix} \quad B = \begin{bmatrix} 2 & 3 & 1 \\ 0 & 1 & 2 \\ 1 & 1 & -1 \end{bmatrix}
$$

$$
A \cdot B =
\begin{bmatrix}
2 & 6 & 3 \\
0 & 5 & 12 \\
7 & 8 & -9
\end{bmatrix}
$$

$$
\rightarrow \text{যখন Array Multiplication হবে তখন just element গুলো গুণ করব।}
$$

$\star$ **Let $v = (1, 2, 3)$**

$$
\therefore \|v\| = \sqrt{1^2 + 2^2 + 3^2} \rightarrow \text{Norm of v.}
$$

$$
= \sqrt{14}
$$

$\star$ **Distance between 2 vectors:-**

$$
v_1 = (a_1, a_2, a_3)
$$

$$
v_2 = (b_1, b_2, b_3)
$$

$$
\therefore d(v_1, v_2) = \sqrt{(a_1-b_1)^2 + (a_2-b_2)^2 + (a_3-b_3)^2}
$$

---

## Page 70

$\star$ **Generalized inner product:-**

$$
v_1 = (a_1, a_2, a_3 \dots a_n)
$$

$$
v_2 = (b_1, b_2, b_3 \dots b_n)
$$

If angle between them is $\theta$, then

$$
\cos \theta = \frac{\langle v_1, v_2 \rangle}{\|v_1\| \cdot \|v_2\|} \quad \rightarrow \text{product}
$$

$$
\text{cos} \theta = \frac{v_1 \cdot v_2}{\|v_1\| \cdot \|v_2\|} \quad \text{(Array Multiplication in numerator)}
$$

$$
= \frac{a_1b_1 + a_2b_2 + a_3b_3 + \dots + a_nb_n}{\sqrt{\sum a_n^2} \cdot \sqrt{\sum b_n^2}}
$$

$$
\star \text{ মধ্যবর্তী কোণ 0 হলে vector গুলো independent.}
$$
