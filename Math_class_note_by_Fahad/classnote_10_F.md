# Fahad's Class Note - Pages 91-100

## Page 91

$$
(100,200) = 100(1,0) + 200(0,1)
$$

$$
\# \ v\_1 = (1,0) \ ; \ v\_2 = (2,0) \rightarrow \mathbb{R}^2
$$

$$
(3,2) = 1(1,0) + 1(2,0) + 1(0,2)
$$

$$
\therefore \mathbb{R}^2 \text{ এর span হবে } (1,0), (2,0), (0,2)
$$

$\#$ **independent হলে ২টি দিয়েই span হবে আর dependent হলে বেশি লাগবে। এখানে যেমন:- $(1,0), (2,0)$ dependent তাই $(0,2)$ বেশি লাগছে।**

$$
\# \ \mathbb{R}^3 \text{ এর span বের কর}
$$

$$
\lbrace (1,0,0) , (0,1,0) , (0,0,1) \rbrace
$$

$$
\begin{array}{c|c}
e\_1 = (1,0,0) & (2,0,0) \\
e\_2 = (0,1,0) & (0,2,0) \\
e\_3 = (0,0,1) & (0,0,2)
\end{array}
$$

$\rightarrow$ **echelon form এ convert করে check করা যায়।**
$\rightarrow$ **$\mathbb{R}^2$ হলে কমপক্ষে ২টি লাগবে span করতে।**
$\rightarrow$ **$\mathbb{R}^3$ হলে কমপক্ষে ৩টি লাগবে span করতে।**

> [!NOTE]
> linearly independent vector. dependent হলে বেশি লাগবে।

---

## Page 92

### Linear dependent and independent of vectors

$\star$ **Suppose you have 3 vectors you have to check whether they are dependent and independent.**

$$
v\_1 = (1, 2, 3) \ ; \ v\_2 = (4, 5, 6) \ ; \ v\_3 = (1, 1, 1)
$$

(i) At first we form the following matrix with the row vectors as:

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
1 & 1 & 1
\end{bmatrix}
$$

(ii) then reduce the matrix to its echelon form:

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
1 & 1 & 1
\end{bmatrix} \xrightarrow[R\_3 \rightarrow R\_1 - R\_3]{R\_2 \rightarrow 4R\_1 - R\_2} \begin{bmatrix} 1 & 2 & 3 \\ 0 & 3 & 6 \\ 0 & 1 & 2 \end{bmatrix} \xrightarrow{R\_3 \rightarrow R\_2 - 3R\_3} \begin{bmatrix} 1 & 2 & 3 \\ 0 & 3 & 6 \\ 0 & 0 & 0 \end{bmatrix}
$$

which is the echelon form of the matrix $A$.
It has two non-zero rows. So, rank of $A = 2$ and the vectors are 3.

---

## Page 93

So they are linearly dependent.

$$
\left[ \text{vector সংখ্যা} = \text{rank হলে linearly independent হত} \right]
$$

**তাই এই ৩টি vector দিয়ে $\mathbb{R}^3$ span করা যাবে না এই ৩টির বেশি vector লাগবে কারণ vectorগুলো linearly dependent. Linearly independent হলে এই ৩টি vector দিয়ে $\mathbb{R}^3$ span করা যেত।**

#### problem:-
$\star$ **4 vectors are taken from $\mathbb{R}^3$ check whether the vectors are dependent or independent [Do not form echelon form]**

**Ans:-**

$$
v\_1 = (2, 3, 4) \ ; \ v\_2 = (1, 2, 1) \ ; \ v\_3 = (1, 1, -1) \ ; \ v\_4 = (1, 1, 2)
$$

$\rightarrow$ Dependent হবে কারণ Rank তো 4 হবে না তাই dependent হবে Dependent vector লাগবে।
$\rightarrow$ $\mathbb{R}^3$ এর জন্য ৩টি থাকলে echelon দিয়ে check করে বলতে হবে but $\mathbb{R}^3$ এর জন্য ৩টির বেশি vector থাকলে তারা অবশ্যই linearly dependent হবে।

---

## Page 94

$$
\# \ v\_1, v\_2, v\_3 \dots v\_n \in V
$$

$$
v\_1 c\_1 + v\_2 c\_2 + v\_3 c\_3 + \dots + v\_n c\_n = 0 \text{ vector}
$$

- যদি $c\_1, c\_2 \dots c\_n = 0$ হয় তাহলে vector গুলো linearly independent.
- কোনো একটি non-zero হলে vector গুলো linearly dependent.

$\star$ **Problem:- what are the methodologies to find whether the given vectors are dependent or independent?**

**power cls:-**
**Math-2117**
**(GCP sir) (11 Apr, 26)**

### Linear Combination of vector

$$
v\_1, v\_2 \dots v\_n \in V \text{ defined on } \mathbb{R}
$$

$$
V = c\_1v\_1 + c\_2v\_2 + \dots + c\_nv\_n
$$

$$
\text{here, } c\_1, c\_2 \dots c\_n \in \mathbb{R}
$$

$$
e\_1 = (1,0) \ ; \ e\_2 = (0,1)
$$

---

## Page 95

### span of V
$c\_1v\_1 + c\_2v\_2$ দ্বারা যেকোনো vector তৈরি করা যাবে।

**what is vector span?**
$\rightarrow$ কতগুলো vector দিয়ে linear combination এর সাহায্যে vector তৈরি।

* set of all 3by3 matrix is a vector space over $\mathbb{R}$
* set of all straight line is a vector space over $\mathbb{R}$
* set of all polinomial is a vector space over $\mathbb{R}$

**vector field to vector field transformation**

### Linear mapping:-
$\rightarrow$ superposition (supper position)
$\rightarrow$ homogenous method.

$\mathbb{R}^3$ এর জন্য $\lbrace v\_1, v\_2, v\_3, v\_4 \rbrace \rightarrow$ minimum 3টি

$$
\lbrace v\_1 = (1,0,0) \ ; \ v\_2 = (0,1,0) \ ; \ v\_3 = (0,0,1) \rbrace \rightarrow \text{minimum spanning set.}
$$

---

## Page 96

**এই set Basis হতে হলে,**
**Condition $\rightarrow$ (i) 3টিই linearly independent হতে হবে।**

$$
\text{Standard basis } \lbrace u\_1 = (1,0,0) \ ; \ u\_2 = (0,1,0) \ ; \ u\_3 = (0,0,1) \rbrace
$$

4টি থাকলে basis হবে না।
যতগুলো independent vector থাকবে সেগুলো dimention.

### Sum and direct sum:-

$$
w, u
$$

$$
w+u = \lbrace v = u+w : u \in U, w \in W \rbrace
$$

$$
\text{dim}(w+u) = \text{dim}(W) + \text{dim}(U) - \text{dim}(U \cap W)
$$

$$
U \oplus W \rightarrow \text{dim}(U \cap W) = 0
$$

- $0$ হলে direct sum.
- $0$ না হলে sum.

### Linear mapping:-
এটি Relation.

**function হতে হলে**
- $A$ set এর প্রতিটি $B$ এর কোনোটার সাথে সম্পর্ক থাকতে হবে।
- $B$ এর ২টার সাথে সম্পর্ক থাকা যাবে না।

```
        Set A                          Set B
     +------------+                  +--------------+
     |     1      | --------------> |      5       |
     |     2      | --------------> |      6       |
     |     3      | --------------> |      7       |
     |     4      | --------------> |      8       |
     +------------+                  +--------------+
```

---

## Page 97

```
     Domain (U)                      Codomain (V)
   +-------------+                 +--------------+
   |   u, v      | --------------> |  T(u), T(v)  |
   |             |        T        |              |
   |   u + v     | --------------> | T(u) + T(v)  |
   +-------------+                 +--------------+
```

$$
\text{some vector space } U \text{ and } V
$$

$$
\frac{d}{dx} (x^2 + 2x) = \frac{d}{dx} x^2 + \frac{d}{dx} 2x \quad \rightarrow \text{ এটি linear mapping.}
$$

$$
T(u+v) = T(u) + T(v)
$$

$$
T(ku) = k T(u)
$$

$$
u \rightarrow T(u)
$$

$$
v \rightarrow T(v)
$$

$$
(u+v) \rightarrow T(u+v)
$$

$$
T(u+v) \text{ যদি } T(u)+T(v) \text{ হয় তাহলে Linear superposition principle মেনে চলে।}
$$

$$
T(u) = u\_1 \quad \dots \text{ (i)}
$$

$$
T(ku) = u\_2 \quad \dots \text{ (ii)}
$$

(i) $\rightarrow k$ দিয়ে গুণ করে $T(ku) = k T(u)$ তাহলে Linear homogeneity মেনে চলে।

#### এটি summary:-
* $T(u+v) = T(u) + T(v) \rightarrow$ super
* $T(ku) = k T(u) \rightarrow$ homo

---

## Page 98

$$
\text{Ex:- } \frac{d}{dx} (3x^2) = 3 \frac{d}{dx} (x^2) \quad \text{(homogeneity)}
$$

$$
\text{Ex:- } \frac{d}{dx} (x^2 + x^3) = \frac{d}{dx} (x^2) + \frac{d}{dx} (x^3) \quad \text{(super pos)}
$$

**এটাকে একসাথে বলে linearity condition.**

$$
\text{Ex:- } \frac{d}{dx} (3x^2+4x) \Rightarrow 3 \frac{d}{dx} (x^2) + 4 \frac{d}{dx} (x)
$$

---

## Page 99

**Math-2117**
**(GCP Sir) (18 Apr, 26)**

$$
\text{same vector space } T : V \rightarrow V \quad \text{(operator)}
$$

$$
\text{different } T : V \rightarrow W \quad \text{(mapping)}
$$

**to be linear mapping $\rightarrow$**
1. $T(u+v) = T(u) + T(v)$
2. $T(ku) = k T(u)$

* **what is linear mapping?**
* **what is linear operator?**

$\#$ **Same space এ mapping হলে operator.**

$$
T : V \rightarrow V
$$

$\#$ **ভিন্ন vector space-এ Linear mapping.**

$$
T : V \rightarrow W
$$

$\star$ **সকল operator, mapping কিন্তু সকল mapping, operator নয়।**

$\star$ **mapping $T(x,y) = (2x, 2y)$ এটি linear mapping কী না?**

**prove condition:-**
1. $T(u+v) = T(u) + T(v)$
2. $T(ku) = k T(u)$

---

## Page 100

$\star$ **span কী?**
$\rightarrow$ কোনো vector space এর সকল vector generate করতে যেকটি vector দরকার তাদের কে span বলে আর তাদের set কে span set বলে।

$\star$ **basis কী?** $\rightarrow$ vector space defined on $\mathbb{R}$.

$$
T : V(\mathbb{R}) \rightarrow V(\mathbb{R})
$$

$\star$ **very very much important.**

**$(2 \times 2)$ matrices:**

$$
\sigma\_1 =
\begin{bmatrix}
2 & 2 \\
2 & 2
\end{bmatrix} \ ; \ \sigma\_2 = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} \ ; \ \sigma\_3 = \begin{bmatrix} 2 & 2 \\ 0 & 0 \end{bmatrix}
$$

**check whether the vectors are linearly independent.**

**solve:-**
Linear combination করে।

$$
c\_1 v\_1 + c\_2 v\_2 + \dots + c\_n v\_n = 0 \text{ vector}
$$

if, $c\_1 = 0 \ \& \ c\_2 = 0 \ \& \ c\_3 = 0$ then they are linearly independent.

Now, let

$$
c\_1 \sigma\_1 + c\_2 \sigma\_2 + c\_3 \sigma\_3 =
\begin{bmatrix}
0 & 0 \\
0 & 0
\end{bmatrix}
$$

$$
\Rightarrow c\_1
\begin{bmatrix}
2 & 2 \\
2 & 2
\end{bmatrix} + c\_2 \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} + c\_3 \begin{bmatrix} 2 & 2 \\ 0 & 0 \end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}
$$

$$
\Rightarrow
\begin{bmatrix}
2c\_1 + 2c\_2 + 2c\_3 & 2c\_1 + 2c\_3 \\
2c\_1 & 2c\_1 + 2c\_2
\end{bmatrix} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}
$$

$$
\Rightarrow c\_1 + c\_2 + c\_3 = 0 \quad \dots \text{ (i)}
$$

$$
c\_1 + c\_3 = 0 \quad \dots \text{ (ii)}
$$

$$
c\_1 = 0 \quad \dots \text{ (iii)}
$$

$$
c\_1 + c\_2 = 0 \quad \dots \text{ (iv)}
$$
