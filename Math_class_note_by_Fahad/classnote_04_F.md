# Fahad's Class Note - Pages 31-40

## Page 31

**Math-2117**
**(08 Dec, 25) (Rupali Maam)**

### Vector integration:-

* Definite integral
* Indefinite integral

#### Line integrals, surface integrals, volume integrals.

$$
\int_{P_1}^{P_2} \vec{A} \cdot d\vec{r} = \int_C \vec{A} \cdot d\vec{r} = \int_C (A_1 dx + A_2 dy + A_3 dz)
$$

$$
\text{can be written as:- } \oint
$$

$$
d\vec{S} = \vec{n} ds
$$

* $\vec{n} \rightarrow$ outward unit normal vector.
* $d\vec{S} \rightarrow$ surface.

#### Surface integration:-

$$
\iint \rightarrow 2\text{ টি থাকবে।}
$$

#### Volume integration:-

$$
\iiint \rightarrow 3\text{ টি থাকবে।}
$$

---

## Page 32

$\star$ $\vec{R}(u) = (u-u^2)\hat{i} + 2u^3\hat{j} - 3\hat{k}$

**(a)**

$$
\int \vec{R}(u) du = \int \left[ (u-u^2)\hat{i} + 2u^3\hat{j} - 3\hat{k} \right] du
$$

$$
= \hat{i} \int (u-u^2) du + \hat{j} \int 2u^3 du + \hat{k} \int -3 du
$$

$$
= \left( \frac{u^2}{2} - \frac{u^3}{3} + C_1 \right)\hat{i} + \left( \frac{u^4}{2} + C_2 \right)\hat{j} + (-3u + C_3)\hat{k}
$$

---

#### Line integral. (Problem-6),

$\star$ **Problem-7.**

$$
\vec{F} = 3xy\,\hat{i} - 5z\,\hat{j} + 10x\,\hat{k} \quad , \quad x = t^2+1 \ , \ y = 2t^2 \ , \ z = t^3
$$

$$
\text{from } t=1 \text{ to } t=2 .
$$

> [!NOTE]
> $dt$ গুলো গুণ ছিল

$$
\vec{F} = 3(t^2+1)(2t^2)\hat{i} - 5t^3\hat{j} + 10(t^2+1)\hat{k}
$$

$$
\therefore W = 3\int_1^2 (2t^4 + 2t^2)\hat{i} - 5\int_1^2 t^3\hat{j} + 10\int_1^2 (t^2+1)\hat{k}
$$

$$
= \frac{442}{5}\hat{i} - \frac{75}{4}\hat{j} + \frac{100}{3}\hat{k}
$$

---

## Page 33

**Math-2117**
**(9 Dec, 25) (Rupali Maam)**

* **Math-10, 9 (Conservative force field)**

---

**Math-2117**
**(03 Jan, 26) (GCP Sir)**

#### How to find the inverse of a square matrix by matrix method.

$\star$ **If $AB = BA = I$ then the matrix $A$ is called the inverse of $B$.**

* **Inverse of a matrix is unique. There can not be more than 1 inverse matrix of a single matrix.**
* **With inverse matrices we can encode and decode a message.**
* **If a matrix has its inverse then the matrix is non-singular. $\rightarrow$ invertible.**

$$
\rightarrow |A| \neq 0
$$

* **The matrix is a square matrix and $|A| \neq 0 \rightarrow$ non-singular.**

---

## Page 34

$\star$ **Test if

$$
A = \begin{bmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{bmatrix}
$$

is singular or not.**

**Ans:-**

$$
|A| = 1(4-4) - 2(-2-4) + 3(-1-2) = 0 - 2(-6) + 3(-3) = 12 - 9 = 3 \neq 0
$$

$$
\therefore \text{The matrix is non-singular. Hence, invertible.}
$$

$$
\rightarrow \text{A matrix that can be inverted is called Invertible.}
$$

---

$\star$ **Using matrix method (only elementary) row operation. Find inverse of a matrix.**

* **We can write,**

$$
A = AI
$$

Here,

$$
A = \begin{bmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{bmatrix} \quad \text{and} \quad I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

**Steps $\rightarrow$ convert $A$ to its identity form then the changes in $I$ will be the inverse of $A$.**

$$
A = AI
$$

$$
\begin{bmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

---

## Page 35

$$
\begin{matrix} R_2 \rightarrow R_1 + R_2 \\ R_3 \rightarrow R_1 - R_3 \end{matrix}
$$

$$
\begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 7 \\ 0 & 1 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & -1 \end{bmatrix}
$$

$$
\begin{matrix} R_3 \rightarrow R_2 - 4R_3 \end{matrix}
$$

$$
\begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 7 \\ 0 & 0 & 3 \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ -3 & 1 & 4 \end{bmatrix}
$$

$$
\begin{matrix} R_1 \rightarrow 2R_1 - R_2 \end{matrix}
$$

$$
\begin{bmatrix} 2 & 0 & -1 \\ 0 & 4 & 7 \\ 0 & 0 & 3 \end{bmatrix} = \begin{bmatrix} 1 & -1 & 0 \\ 1 & 1 & 0 \\ -3 & 1 & 4 \end{bmatrix}
$$

$$
\begin{matrix} R_1 \rightarrow 3R_1 + R_3 \\ R_2 \rightarrow 3R_2 - 7R_3 \end{matrix}
$$

$$
\begin{bmatrix} 6 & 0 & 0 \\ 0 & 12 & 0 \\ 0 & 0 & 3 \end{bmatrix} = \begin{bmatrix} 0 & -2 & 4 \\ 24 & -4 & -28 \\ -3 & 1 & 4 \end{bmatrix}
$$

$$
\begin{matrix} R_1 \rightarrow \frac{R_1}{6} \\ R_2 \rightarrow \frac{R_2}{12} \\ R_3 \rightarrow \frac{R_3}{3} \end{matrix}
$$

$$
\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 0 & -\frac{1}{3} & \frac{2}{3} \\ 2 & -\frac{1}{3} & -\frac{7}{3} \\ -1 & \frac{1}{3} & \frac{4}{3} \end{bmatrix}
$$

$$
\text{Thus } A^{-1} = \begin{bmatrix} 0 & -\frac{1}{3} & \frac{2}{3} \\ 2 & -\frac{1}{3} & -\frac{7}{3} \\ -1 & \frac{1}{3} & \frac{4}{3} \end{bmatrix} \quad \text{(Ans)}
$$

---

## Page 36

$$
\frac{2}{3} - \frac{7}{3} + \frac{8}{3} = \frac{2-7+8}{3} = \frac{3}{3} = 1
$$

#### Justify if $A^{-1}$ is infact the inverse of $A$.

then,

$$
A \cdot A^{-1} = I
$$

$$
\text{L.H.S} = A \cdot A^{-1}
$$

$$
= \begin{bmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{bmatrix} \cdot \begin{bmatrix} 0 & -\frac{1}{3} & \frac{2}{3} \\ 2 & -\frac{1}{3} & -\frac{7}{3} \\ -1 & \frac{1}{3} & \frac{4}{3} \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}
$$

---

$\star$ **Encoding and decoding a text using the inverse of a matrix.**

**"KILL HIM"**

We use:
* K = 11
* I = 9
* L = 12
* H = 8
* M = 13

---

## Page 37

Now, we construct the matrix with the message as,

$$
B = \begin{bmatrix} K & I & L & L \\ H & I & M & \text{space} \end{bmatrix}
$$

$$
B = \begin{bmatrix} 11 & 9 & 12 & 12 \\ 8 & 9 & 13 & 0 \end{bmatrix}
$$

*as we can also organize them in columns.*
*We can also write them all in the same row or same column operating by considering 'space' as 0.*

We now take,
The $2 \times 2$ matrix as,

$$
A = \begin{bmatrix} 1 & 2 \\ -1 & 1 \end{bmatrix} \quad \rightarrow \text{randomly take a matrix which has an inverse.}
$$

$$
\therefore A^{-1} = \frac{1}{3} \begin{bmatrix} 1 & -2 \\ 1 & 1 \end{bmatrix}
$$

*(2x2) নিলাম যার দ্বারা আমরা B এর সাথে গুণ করব।*

$\star$ **The sender will have $A$ and the receiver will have $A^{-1}$.**

---

## Page 38

#### Encoding Matrix:-

$$
IC = \begin{bmatrix} 1 & 2 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 11 & 9 & 12 & 12 \\ 8 & 9 & 13 & 0 \end{bmatrix} = \begin{bmatrix} 27 & 27 & 38 & 12 \\ -3 & 0 & 1 & -12 \end{bmatrix}
$$

$$
\rightarrow \text{final message that will be sent.}
$$

#### Decoded Matrix:-

$$
A^{-1} \cdot IC = \frac{1}{3}\begin{bmatrix} 1 & -2 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 27 & 27 & 38 & 12 \\ -3 & 0 & 1 & -12 \end{bmatrix} = \begin{bmatrix} 11 & 9 & 12 & 12 \\ 8 & 9 & 13 & 0 \end{bmatrix}
$$

$$
\text{converting, } = \begin{bmatrix} K & I & L & L \\ H & I & M & \cdot \end{bmatrix}
$$

---

$\star$ **৩টি vector $\rightarrow$**

$$
\hat{i} + 2\hat{j} + 3\hat{k}
$$

$$
-\hat{i} + 2\hat{j} + \hat{k}
$$

$$
0\hat{i} + 2\hat{j} + 4\hat{k}
$$

$$
\rightarrow \text{matrix করে আমরা echelon form করে নিব}
$$

$$
\rightarrow \text{Rank বের করব}
$$

$$
\rightarrow \text{Rank = 3 হলে Independent.}
$$

$$
\text{Rank } \neq 3 \text{ হলে dependent.}
$$

---

## Page 39

**Math-2117**
**(6 Jan, 26) (Rupali Maam)**

### Vector integration. (Conservative force field)

#### Problem 12:-

$$
\nabla \times \vec{F} = 0 \quad \rightarrow \text{curl '0' মানে Force field টি conservative.}
$$

$\star$ **কোনো Force field conservative হলে $\vec{F} = \nabla \phi$ লিখতে পারি।**

$$
\rightarrow \text{scalar potential}
$$

$$
\nabla = \frac{\partial}{\partial x}\hat{i} + \frac{\partial}{\partial y}\hat{j} + \frac{\partial}{\partial z}\hat{k} \quad \rightarrow \text{nabla / del}
$$

$$
\nabla^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2} \quad \rightarrow \text{Laplacian operator.}
$$

*(Laplace equation এ আছে তাই Laplacian operator বলে).*

$$
\therefore \vec{F} = \nabla \phi
$$

$$
-\hat{i} + \hat{j} - \hat{k} = \frac{\partial \phi}{\partial x}\hat{i} + \frac{\partial \phi}{\partial y}\hat{j} + \frac{\partial \phi}{\partial z}\hat{k}
$$

$$
\text{given, } \dots
$$

$$
\therefore \dots = \frac{\partial \phi}{\partial x} \ ; \quad \dots = \frac{\partial \phi}{\partial y} \ ; \quad \dots = \frac{\partial \phi}{\partial z}
$$

যেকোনো একটিকে integration করে $\phi$ নির্ণয় করব।

Let,

$$
\frac{\partial \phi}{\partial x} = 2xy + z^3 \ ; \quad \frac{\partial \phi}{\partial y} = x^2 \ ; \quad \frac{\partial \phi}{\partial z} = 3xz^2
$$

$$
\therefore \phi = x^2y + xz^3 + f(y,z)
$$

$$
\therefore \phi = x^2y + g(x,z)
$$

$$
\therefore \phi = xz^3 + h(x,y)
$$

$$
\therefore \phi = \dots
$$

---

## Page 40

These agree if $f(y,z) = 0, \ g(x,z) = xz^3$ and $h(x,y) = x^2y$.

then,

$$
\phi = x^2y + xz^3 + \text{constant.}
$$

$$
\rightarrow \text{scalar potential}
$$

#### Problem 13:-
Work done between 2 points is independent of the path.

```
          Path A
       .----------.
      /            \
    (P_1)        (P_2)
      \            /
       `----------'
          Path B
```

$$
\int_{P_1}^{P_2} \vec{F} \cdot d\vec{r}
$$

$$
\int \vec{F} \cdot d\vec{r} = 0 \rightarrow \text{For all closed path.}
$$

$$
\therefore \oint \vec{F} \cdot d\vec{r} = \int_{P_1 A P_2 B P_1} \vec{F} \cdot d\vec{r} = \int_{P_1 A P_2} \vec{F} \cdot d\vec{r} + \int_{P_2 B P_1} \vec{F} \cdot d\vec{r}
$$

$$
= \int_{P_1 A P_2} \vec{F} \cdot d\vec{r} - \int_{P_1 B P_2} \vec{F} \cdot d\vec{r} = 0
$$

> [!NOTE]
> vector-এর point alter করলে (-) হয়।

ಧরি কাজ path-এর উপর dependent না।

$$
\rightarrow \text{Prove কাজ work done in a closed path = 0.}
$$
