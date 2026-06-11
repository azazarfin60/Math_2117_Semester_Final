# Fahad's Class Note - Pages 71-80

## Page 71

**GCP HW**

$\star$ **$A = \begin{bmatrix} 2 & 1 \\ -1 & 1 \end{bmatrix}$. Find eigen values and eigen vectors.**

**Ans:-**
Ch. matrix:
$$A - \lambda I = \begin{bmatrix} 2-\lambda & 1 \\ -1 & 1-\lambda \end{bmatrix}$$

$\therefore$ Ch. eq.
$$\lambda^2 - 3\lambda + 3 = 0$$
$$\therefore \lambda = \frac{3 \pm \sqrt{3}i}{2}$$

Let,
$$V = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$$
be an eigen vector corresponding to the eigen value $\lambda = \frac{3}{2} + \frac{\sqrt{3}}{2}i$.

$\therefore$ we know,
$$(A - \lambda I)v = 0 \quad \rightarrow \quad \begin{bmatrix} 2-\lambda & 1 \\ -1 & 1-\lambda \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
$$\Rightarrow (2-\lambda)v_1 + v_2 = 0 \quad \dots \text{ (i)}$$
$$-v_1 + (1-\lambda)v_2 = 0 \quad \dots \text{ (ii)}$$

Both equations give the same relation.
$\therefore$ From (i),
Let, $v_1 = 1$
$$\therefore v_2 = -(2-\lambda) = -\left( 2 - \left(\frac{3}{2} + \frac{\sqrt{3}}{2}i\right) \right) = -\frac{1}{2} + \frac{\sqrt{3}}{2}i$$

$$\therefore V = \begin{bmatrix} 1 \\ -\frac{1}{2} + \frac{\sqrt{3}}{2}i \end{bmatrix}$$
is an eigen vector corresponding to the eigen value $\lambda = \frac{3}{2} + \frac{\sqrt{3}}{2}i$.

---

## Page 72

Again, Let,
$$W = \begin{bmatrix} w_1 \\ w_2 \end{bmatrix}$$
be an eigen vector corresponding to the eigen value $\lambda = \frac{3}{2} - \frac{\sqrt{3}}{2}i$.

$$\therefore (2-\lambda)w_1 + w_2 = 0 \quad \dots \text{ (iii)}$$
$$-w_1 + (1-\lambda)w_2 = 0 \quad \dots \text{ (iv)}$$

both equations give the same relation.
$\therefore$ From (iii),
let, $w_1 = 1$
$$\therefore w_2 = -(2-\lambda) = -\left( 2 - \left(\frac{3}{2} - \frac{\sqrt{3}}{2}i\right) \right) = -\frac{1}{2} - \frac{\sqrt{3}}{2}i$$

$$\therefore W = \begin{bmatrix} 1 \\ -\frac{1}{2} - \frac{\sqrt{3}}{2}i \end{bmatrix}$$
is an eigen vector corresponding to the eigen values $\lambda = \frac{3 - \sqrt{3}i}{2}$.

$\star$ **Prove that $\operatorname{adj}(AB) = \operatorname{adj}(B) \cdot \operatorname{adj}(A)$**

**Ans:-**
For any n-square matrix $M$,
$$M \operatorname{adj}(M) = \det(M) I$$
$$\therefore (AB) \operatorname{adj}(AB) = \det(AB) \cdot I$$
$$\therefore (AB) \operatorname{adj}(AB) = \det(A) \det(B) I \quad \dots \text{ (i)}$$

> [!NOTE]
> We know using determinant property:
> $\det(AB) = \det(A) \det(B)$

---

## Page 73

Now, Let $X = \operatorname{adj}(B) \operatorname{adj}(A)$
$$\therefore AB X = A [ B \operatorname{adj}(B) ] \operatorname{adj}(A)$$
$$= A [ \det(B) \cdot I ] \operatorname{adj}(A)$$
$$= \det(B) \cdot A \operatorname{adj}(A)$$
$$= \det(B) \cdot \det(A) \cdot I$$
$$\therefore AB X = \det(A) \det(B) I \quad \dots \text{ (ii)}$$

From (i) and (ii) we have,
$$X = \operatorname{adj}(AB)$$
$$\therefore \operatorname{adj}(AB) = \operatorname{adj}(B) \operatorname{adj}(A) \quad \text{(proved)}$$

---

## Page 74

**Math-2117**
**(GCP Sir) (28 Mar, 26)**

### Fields:-
We taking into account 2 elements from a space.
A vector $\{ (1,2), (2,3) \}$ taken from $\mathbb{R}^2$
$$\mathbb{R}^2 = \{ (a, b) \mid a, b \in \mathbb{R} \}$$

$$\rightarrow \text{এই দুটি যোগ করলে } 3\hat{i} + 5\hat{j} \text{ - যা এই set এর মধ্যে নাই।}$$
$$\rightarrow \text{closure property মানে না।}$$

$$\{ (0,0) \} \rightarrow (0\hat{i} + 0\hat{j}) + (0\hat{i} + 0\hat{j}) = 0\hat{i} + 0\hat{j} \quad \text{যা same set-এর ভিতরে আছে :: closure property আছে।}$$

### Binary operation:-
Binary operation is a operation that:
$$f : A \times A \rightarrow A$$
$$g : A \rightarrow A \quad \rightarrow \text{Unary operation.}$$

$\star$ **To knows fields we need binary addition and multiplication.**

---

## Page 75

A non-empty set $F$ with plus and multiplication.

### Axioms for Addition:-
1. If $x \in F$ and $y \in F$, then their sum $x+y$ is in $F$. $\rightarrow$ **closure property.**
2. $x+y = y+x$ for all $x, y \in F$. $\rightarrow$ **Commutative property.**
3. $(x+y)+z = x+(y+z)$ for all $x, y, z \in F$. $\rightarrow$ **Associative**
4. $0+x = x$ for every $x \in F$. $\rightarrow$ **Identity law.**
5. For every $x \in F$, there exists $-x \in F$ such that $x + (-x) = 0$. $\rightarrow$ **Additive inverse.**

$$\mathbb{R}_+ \rightarrow \text{Does not contain 0 :: not valid.}$$
$$\mathbb{Z} \rightarrow \text{Contains 0 :: valid}$$
$$\therefore 0 \rightarrow \text{Identity element.}$$

> [!NOTE]
> এই 5টি Law মেনে চললে Field under addition হবে।

$$\star \ \{ 0, 1, 2, 3 \dots \} \rightarrow \text{Not a field under addition.}$$
$$\star \ \mathbb{R} \rightarrow \text{A field under addition.}$$

---

## Page 76

$$\text{Additive inverse} = -x$$
$$\text{Multiplicative inverse} = \frac{1}{x}$$

### Group under multiplication:-

#### Axioms of multiplication:-
1. $x \in F, y \in F$ হলে $xy \in F$ হতে হবে।
2. $xy = yx$ for all $x, y \in F$.
3. $(xy)z = x(yz)$ for all $x, y, z \in F$. $\rightarrow$ **Associative Law**
4. $F$ contains an element $1 \neq 0$ such that $1 \cdot x = x$, for every $x \in F$.
5. $x \in F$ and $x \neq 0$ then there exists an element $\frac{1}{x} \in F$ such that $x \cdot \frac{1}{x} = 1$.

$\star$ **Identity element = 1.**

$$\mathbb{Z} = \{ \dots -2, -1, 0, 1, 2 \dots \} \rightarrow \text{is a field under addition but not under multiplication.}$$
$$\{ \mathbb{R} - 0 \} \rightarrow \text{Field under multiplication} \quad \because \frac{1}{0} = \text{undefined.}$$

---

## Page 77

$$\rightarrow \text{Field under addition \& field under multiplication } \rightarrow \text{ Vector Space.}$$

$\star$ **Set of all rational number**
$$Q = \left\{ \frac{p}{q} \mid p, q \in \mathbb{Z}, \ q \neq 0 \right\}$$
$$\text{field under addition. not under multiplication cause 0 exists.}$$

### Vector space and sub-space
$$V = \{ \text{set of vectors defined on a field } k \}$$
$$= \left\{ \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix} \right\} \rightarrow \mathbb{R} \quad \text{(not closed under addition)}$$
$$= \{ x^2, x^2 + 1 \} \rightarrow \text{polynomials}$$
$$= \left\{ \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 2 \\ 1 \end{bmatrix}, \begin{bmatrix} 3 \\ 1 \end{bmatrix} \dots \right\} \rightarrow \text{column vectors}$$
$$= \{ (0, 1), (0, 2), (0, 3) \} \rightarrow \text{Row}$$

> [!NOTE]
> * none are vector space.
>
> If $v_1 \& v_2 \in V$, then $v_1 + v_2 \in V \rightarrow$ set is closed under addition.

$\star$ **must be closed under addition and scalar multiplication**

---

## Page 78

### First Law Condition of vector space:-
1. Must follow be closed under addition & scalar multiplication.

$$\text{(1 lec miss).}$$

**Math-2117**
**(GCP Sir) (6 Apr, 26)**

### Linear Combination of vectors:-
$$v_1, v_2 \dots v_n \in V \text{ defined on } \mathbb{R}, \ c_1, c_2 \dots c_n \in \mathbb{R}$$
$$v = c_1v_1 + c_2v_2 + \dots + c_nv_n \rightarrow \text{Linear combination of vectors.}$$

> [!NOTE]
> $c_1, c_2 \dots c_n \rightarrow$ span of $v$.

$$\mathbb{R}^3 \quad \{ (1,0,0), (0,1,0), (0,0,1) \}$$
$$e_1 = (1, 0, 0)$$
$$e_2 = (0, 1, 0)$$
$$e_3 = (0, 0, 1)$$

$\star$ **Linear dependent and independent of vectors**
$$v_1 = (1, 2, 3) \ ; \ v_2 = (4, 5, 6) \ ; \ v_3 = (1, 1, 1)$$

---

## Page 79

**Ans:-**
First we form the following matrix with the row vectors, as
$$A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 1 & 1 & 1 \end{bmatrix}$$

$$\text{eachalon } \rightarrow \begin{pmatrix} 1 & 2 & 3 \\ 0 & 3 & 6 \\ 0 & 0 & 0 \end{pmatrix}$$

Which is the echelon form of the matrix $A$.
It has 2 non-zero rows. $(\text{Rank} = 2)$.

Since the member of vectors is 3 and Rank = 2,
$\therefore$ The vectors are dependent.

---

## Page 80

**Math-2117**
**(Rupali Maam) (7 Apr)**

$\star$ **Green's theorem in the plane:- $1, 2, 6, 8, 9, 12 \quad \text{pg-112}$**
$\star$ **Stokes theorem, divergence theorem.**

$$\iint_S \vec{A} \cdot \hat{n} \, ds = \iiint_V \vec{\nabla} \cdot \vec{A} \, dv$$

> [!NOTE]
> (8 No) করে আনতে হবে

$$\vec{A} = (A_1\hat{i} + A_2\hat{j} + A_3\hat{k}) \quad \hat{n} = \vec{A} \cdot \hat{n}$$
$$\vec{\nabla} \cdot \vec{A} = \frac{\partial}{\partial x} A_1 + \frac{\partial}{\partial y} A_2 + \frac{\partial}{\partial z} A_3$$

$$\iint_S A_1\hat{i} \cdot \hat{n} \, ds + \iint_S A_2\hat{j} \cdot \hat{n} \, ds + \iint_S A_3\hat{k} \cdot \hat{n} \, ds = \iiint_V \frac{\partial}{\partial x} A_1 \, dv + \iiint_V \frac{\partial}{\partial y} A_2 \, dv + \iiint_V \frac{\partial}{\partial z} A_3 \, dv$$

$$\star \ ds_2 = \frac{dx dy}{\hat{k}_2 \cdot \hat{n}} \ ; \ ds_1 = \frac{dx dy}{-\hat{k}_1 \cdot \hat{n}}$$
$$\text{↳ } dx dy = \hat{k}_2 \cdot \hat{n} \, ds_2 \ ; \ dx dy = -\hat{k}_1 \cdot \hat{n} \, ds_1$$
