# Fahad's Class Note - Pages 41-50

## Page 41

Now prove the reverse,
* **ধরি closed path-এ work done = 0.**
* **Prove করতে হবে path-এর উপর depend করে না।**

$$
\oint \vec{F} \cdot d\vec{r} = 0
$$

$$
\int_{P_1 A B P_2} \vec{F} \cdot d\vec{r} = \int_{P_1 A P_2} \vec{F} \cdot d\vec{r} + \int_{P_2 B P_1} \vec{F} \cdot d\vec{r} = \int_{P_1 A P_2} \vec{F} \cdot d\vec{r} - \int_{P_1 B P_2} \vec{F} \cdot d\vec{r} = 0.
$$

> [!NOTE]
> vector-এর point alter করলে (-) হয়।

#### [Problem 16]

$$
\text{Next cls} \rightarrow \text{surface \& volume integration.}
$$

---

## Page 42

**Math-2117**
**(10 Jan, 26) (GCP Sir)**

$\star$ **Every square matrix can be written as the sum of symmetric and skew symmetric matrix.**

$\star$ **Let $A$ be a square matrix.**

Then,

$$
A = \frac{1}{2}(A + A^t) + \frac{1}{2}(A - A^t)
$$

$$
A = B + C
$$

where,

$$
B = \frac{1}{2}(A + A^t)
$$

$$
\text{and} \quad C = \frac{1}{2}(A - A^t)
$$

Now, we need to prove that $B$ is symmetric and $C$ is skew symmetric.

$\therefore$ **Now,**

$$
B^t = \left[ \frac{1}{2}(A + A^t) \right]^t
$$

$$
= \frac{1}{2}(A + A^t)^t
$$

$$
= \frac{1}{2} \left[ A^t + (A^t)^t \right]
$$

$$
B^t = \frac{1}{2}(A^t + A) = B
$$

Hence, $B$ is a symmetric matrix.

---

## Page 43

**Now,**

$$
C^t = \left[ \frac{1}{2}(A - A^t) \right]^t
$$

$$
C^t = \frac{1}{2}(A^t - A)
$$

$$
C^t = -\frac{1}{2}(A - A^t) = -C
$$

Hence, $C$ is a skew symmetric matrix.

Thus, Every square matrix can be written as the sum of symmetric matrix and a skew symmetric matrix.

$\rightarrow$ **This representation is unique. (Prove করতে হবে)**

$$
\text{↳ শুধুমাত্র একটি symmetric ও skew symmetric হবে।}
$$

#### Represent the matrix

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
1 & 2 & 1
\end{bmatrix}
$$

as the sum of a symmetric and a skew symmetric matrix.

---

## Page 44

**Ans:-**

$$
A = \frac{1}{2}(A + A^t) + \frac{1}{2}(A - A^t)
$$

$$
A = B + C
$$

$$
B = \frac{1}{2}(A + A^t) =
\begin{bmatrix}
1 & 3 & 2 \\
3 & 5 & 4 \\
2 & 4 & 1
\end{bmatrix}
$$

$$
C = \frac{1}{2}(A - A^t) =
\begin{bmatrix}
0 & -1 & 1 \\
1 & 0 & 2 \\
-1 & -2 & 0
\end{bmatrix} \quad \text{(Ans:)}
$$

Then,

$$
A =
\begin{bmatrix}
1 & 3 & 2 \\
3 & 5 & 4 \\
2 & 4 & 1
\end{bmatrix} + \begin{bmatrix} 0 & -1 & 1 \\ 1 & 0 & 2 \\ -1 & -2 & 0 \end{bmatrix}
$$

---

## Page 45

$\star$ **Hermitian - Matrix transpose-conjugate নিলে $= A$, skew-Hermitian-এর ক্ষেত্রে $= -A$.**

$\star$ **A Matrix will be called Hermitian $(A^\theta, A^H, A^*)$**

$$
A^\theta = (\overline{A})^t = (\overline{A^t}) \rightarrow \text{transpose-conjugate বলা হয়।}
$$

$$
A^\theta = A \quad \text{ (Hermitian)}
$$

$$
A^\theta = -A \quad \text{ (skew-Hermitian)}
$$

$\star$ **Let,**

$$
A =
\begin{bmatrix}
i & -2+i & 4-5i \\
0 & -i & 2i \\
0 & 3 & 4+5i
\end{bmatrix} = \frac{1}{2}(A^\theta + A) + \frac{1}{2}(A^\theta - A)
$$

$$
= B + C \quad \text{where } B = \frac{1}{2}(A^\theta + A) \quad \text{and} \quad C = \frac{1}{2}(A^\theta - A)
$$

> [!NOTE]
> Mathematically, to write $A$ as $B+C$ where $B$ is Hermitian and $C$ is skew-Hermitian, the expression is

$$
A = \frac{1}{2}(A + A^\theta) + \frac{1}{2}(A - A^\theta)
$$

. The notes define

$$
C = \frac{1}{2}(A^\theta - A)
$$

, which means $A = B - C$.

**Now,**

$$
B = \frac{1}{2}(A^\theta + A)
$$

$$
= \frac{1}{2} \left(
\begin{bmatrix}
-i & -2-i & 4+5i \\
0 & i & -2i \\
0 & 3 & 4-5i
\end{bmatrix}^t + \begin{bmatrix} i & -2+i & 4-5i \\ 0 & -i & 2i \\ 0 & 3 & 4+5i \end{bmatrix} \right)
$$

$$
= \frac{1}{2} \left(
\begin{bmatrix}
-i & 0 & 0 \\
-2-i & i & 3 \\
4+5i & -2i & 4-5i
\end{bmatrix} + \begin{bmatrix} i & -2+i & 4-5i \\ 0 & -i & 2i \\ 0 & 3 & 4+5i \end{bmatrix} \right)
$$

$$
B = \frac{1}{2}
\begin{bmatrix}
0 & -2+i & 4-5i \\
-2-i & 0 & 3-2i \\
4+5i & 3+2i & 8
\end{bmatrix} \rightarrow \text{Hermitian. [Diagonally Real numberগুলো থাকবে]}
$$

---

## Page 46

**Now,**

$$
C = \frac{1}{2}(A^H - A)
$$

$$
= \frac{1}{2} \left(
\begin{bmatrix}
-i & 0 & 0 \\
-2-i & i & 3 \\
4+5i & -2i & 4-5i
\end{bmatrix} - \begin{bmatrix} i & -2+i & 4-5i \\ 0 & -i & 2i \\ 0 & 3 & 4+5i \end{bmatrix} \right)
$$

$$
= \frac{1}{2}
\begin{bmatrix}
-2i & 2-i & -4+5i \\
-2-i & 2i & 3-2i \\
4+5i & -2i-3 & -10i
\end{bmatrix}
$$

* **Real part গুলো negative হবে।**
* **Skew-Hermitian**
* **Main diagonal $\rightarrow$ purely imaginary**

$$
\therefore A = B - C =
\begin{bmatrix}
i & -2+i & 4-5i \\
0 & -i & 2i \\
0 & 3 & 4+5i
\end{bmatrix}
$$

---

## Page 47

**Math-2117**
**(12 Jan, 26) (GCP Sir)**

#### Nilpotent:-
If

$$
A^n = 0
$$

, then it is called nilpotent matrix of index $n$.
* $A = \text{square matrix.}$

#### Involuntary:-
If

$$
A^n = I
$$

(Identity matrix), then $A$ is an involuntary matrix of index $n$.

$$
A^n = I
$$

#### Periodic matrix:-

$$
A^{n+1} = A
$$

Here, $n$ is period.

#### Idempotent matrix:-

$$
A^2 = A
$$

A square matrix can be idempotent matrix if

$$
A^2 = A
$$

---

## Page 48

**If থাকলে dual-টি প্রমাণ করতে হবে।**
**Iff " dual-টি " " " (if and only if)**

$\star$ **An n-square matrix A is involuntary iff $(I+A)(I-A) = \text{a zero-matrix}$.**

We know, an n-square matrix A is involuntary if

$$
A^2 = I.
$$

$$
\text{index} = 2
$$

First, we assume that $A$ is involuntary, we need to prove that

$$
(I-A)(I+A) = 0_{n \times n}.
$$

Now,

$$
(I-A)(I+A) = I^2 - A \cdot I + A \cdot I - A^2
$$

$$
= I - A^2
$$

$$
= I - I
$$

$$
= 0
$$

Conversely, assume that $(I-A)(I+A) = 0$.
we need to prove that $A$ is involuntary.

Here, we have

$$
(I-A)(I+A) = 0
$$

$$
I^2 - A^2 = 0
$$

$$
I - A^2 = 0
$$

$$
\Rightarrow A^2 = I
$$

which is yielding $A$ is involuntary.

Thus completes the prove.

---

## Page 49

$\star$ **Associative law of matrix addition:-**

$$
(A + B) + C = A + (B + C)
$$

$\star$ **Associative law of multiplication:-**

$$
(AB)C = A(BC)
$$

$\star$ **Commutative law of multiplication:-**

$$
AB \neq BA
$$

$\star$ **If $AB = BA = I$ then $B$ is inverse of $A$.**
$A$ and $B$ must be square matrices of the same size.

**Ans:- prove that,**

$$
(AB)^{-1} = B^{-1} A^{-1}
$$

If

$$
(AB)^{-1} \cdot AB = I
$$

then $(AB)^{-1}$ is inverse of $AB$.

Here,

$$
AB(B^{-1} A^{-1}) = A(B B^{-1}) A^{-1}
$$

$$
= A \cdot I \cdot A^{-1}
$$

$$
= A \cdot A^{-1}
$$

$$
= I
$$

$$
AB = I
$$

---

## Page 50

Again,

$$
(B^{-1} A^{-1}) AB = B^{-1}(A^{-1} A) B
$$

$$
= B^{-1} \cdot I \cdot B
$$

$$
= I
$$

$$
\because AB = BA = I
$$

$$
\therefore \text{inverse}
$$

Hence, $AB$ is the inverse of $B^{-1} A^{-1}$.
Therefore, $B^{-1} A^{-1}$ is the inverse of $AB$.

$\star$ **$\text{Adj}(AB) = \text{Adj}(B) \cdot \text{Adj}(A) \quad \text{prove} \rightarrow \text{H.W.}$**

$\star$ **Prove that,

$$
(AB)^t = B^t A^t
$$

**

**Ans:-**
Let,

$$
A =
\begin{bmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{bmatrix}
$$

and,

$$
B =
\begin{bmatrix}
b_{11} & b_{12} & b_{13} \\
b_{21} & b_{22} & b_{23} \\
b_{31} & b_{32} & b_{33}
\end{bmatrix}
$$

> [!NOTE]
> পরীক্ষায় লেখা যাইবে না। (Referencing that this 3x3 matrix example should not be used as a general proof in exams).