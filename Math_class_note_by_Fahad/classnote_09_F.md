# Fahad's Class Note - Pages 81-90

## Page 81

**(Previous cls-1)**
**Math-2117**
**(GCP Sir) (11-Apr, 26)**

### Vector Space

#### Scaler feild:-
* Set of all integers is a scalar field under multiplication? $\rightarrow$ NO
  $\rightarrow$ A field under addition.
* Set of all real numbers is a scaler field under multiplication? $\rightarrow$ No
  $\rightarrow$ A field under addition.
* Lets consider a set of vectors


$$
V = \text{set of vectors over a field } A .
$$

$$
= \lbrace (0,1,1), (0,2,1) \dots \rbrace
$$

> [!NOTE]
> The elements of the vectors come from the field $A$.

---

## Page 82

**pdf pg-15:-**

### Abstract Concept:-
1. Vector addition: $u, v \in V$ a sum $u+v$ in $V$
2. Scalar multiplication: $u \in V, K \in F$ a product $ku \in V$

* closed under associative law


$$
(u+v) + w = u + (v+w)
$$

* $u$ vector এর সাথে কোন vector add করলে $u$ vector পাওয়া যাবে।


$$
u+0 = 0+u = u \quad \rightarrow \text{ Identity law}
$$

* $(-u+u) = u+(-u) = 0 \quad \rightarrow \text{ Inverse law}$
* $u+v = v+u \quad \rightarrow \text{ Commutative law}$

$$
\begin{array}{l|r}
\text{c(u+v) = cv + cu} & \lbrace (0,0) \rbrace \rightarrow \text{Vector space over a field } \mathbb{R}. \\
\text{(c+k) u = cu + ku} & \lbrace (2,1) \rbrace \rightarrow \text{Not vector space} \\
\text{(ck) u = c (ku)} & \lbrace (2,1), (4,2) \rbrace \rightarrow \text{Not vector space} \\
\text{1u = u} &
\end{array}
$$

---

## Page 83

$\star$ **Set of all straight lines defined on $\mathbb{R}$ is vector space.**

$\star$ **$\lbrace (x,y) : y = mx \rbrace$ is a vector space?**

Let,

$$
y = x
$$

$$
y = 2x
$$

$$
y = \frac{3}{2}x
$$

1. $\lbrace (2,2), (2,4), (4,6) \dots \rbrace$
2. $\lbrace (0,0), (1,1), (2,2) \rbrace$

$$
(0,0) + \lbrace (1,1) + (2,2) \rbrace = (3,3)
$$

$$
\lbrace (0,0) + (1,1) \rbrace + (2,2) = (3,3)
$$

$$
\begin{array}{l}
\text{(ii) } (1,1) + (0,0) = (1,1) \\
\text{(iii) } (1,1) + (-1,-1) = (0,0) \\
\text{(iv) } (1,1) + (0,0) = (0,0) + (1,1) \\
\text{Additive law satisfy করে।}
\end{array}
$$

**Again:-**
1. $3 \lbrace (1,1) + (2,4) \rbrace$


$$
= (3,3) + (6,12) = (9,15) \quad \left[ y = \frac{5x}{3} \right]
$$

---

## Page 84

2. $(3+2) (1,1)$


$$
= 3 (1,1) + 2 (1,1) = (3,3) + (2,2) = (5,5)
$$

3. $2 \times 3 (1,1) = 6 (1,1) = (6,6)$


$$
2 (3) (1,1) = 2 (3,3) = (6,6)
$$

4. $1u = 1(1,1) = (1,1)$

Satisfied all the properties. So the straight line is a vector space.

$\star$ **$\mathbb{R}^3$ over $\mathbb{R}$ is a vector space or not?**

$$
\mathbb{R}^3 = \lbrace (a,b,c) \mid a,b,c \in \mathbb{R} \rbrace
$$

$\rightarrow$ Yes, $\mathbb{R}^3$ is a vector space.
$\rightarrow$ $xy / yz / zx$ plane.

$\star$ **$\mathbb{R}^2$ over $\mathbb{R}$ is a vector space.**
$\star$ **$\mathbb{R}^2, \mathbb{R}^3, \mathbb{R}^4 \dots \mathbb{R}^n$ all are vector space.**
$\rightarrow$ সবগুলো প্রমাণ করতে হবে।

---

## Page 85

$\star$ **Set of all $n \times n$ matrices is a vector space.**

$\star$ **$\mathbb{R}^n = \lbrace (a\_1, a\_2 \dots a\_n) : a\_i \in \mathbb{R} \rbrace$ and $F=\mathbb{R}$**
- $a\_i \in \mathbb{R} \rightarrow$ Real number
- $F=\mathbb{R} \rightarrow$ জটিল (complex) ও হতে পারে।

### Subspaces (pg-18)
It is also a vector space and a subset of the vector space.
$\rightarrow$ over a field হতে হবে।

#### Conditions:-
1. $0 \in W \rightarrow$ '0' element থাকতে হবে।
2. $u+v \in W$
3. $ku \in W$
- (2) and (3) mean closed under addition and scalar multiplication.

#### Example:-
1. All straight lines passing through origin.
2. Set of all $2 \times 2$ matrices.

**What is polynomial?**

$$
y = a\_0 + a\_1x + a\_2x^2 + \dots a\_nx^n
$$

$\rightarrow$ polynomial is also a vector space and $y^2, y^3 \dots$ are subspaces.

---

## Page 86

*(Reconstruction of Faint Page)*

### Linear Mapping

Let $U$ and $V$ be two vector spaces. A mapping $f : U \rightarrow V$ is called a linear mapping if:
1. **Superposition:** $f(u+v) = f(u) + f(v)$ for all $u, v \in U$.
2. **Homogeneity:** $f(ku) = k f(u)$ for all $u \in U$ and scalar $k$.

```
       Domain (U)                      Codomain (V)
     +------------+                  +--------------+
     |     u      | ---------------> |     f(u)     |
     |     v      | ---------------> |     f(v)     |
     |    u + v   | ---------------> |  f(u) + f(v) |
     |    ku      | ---------------> |    k f(u)    |
     +------------+                  +--------------+
```

---

## Page 87

**Math-2117**
**(GCP Sir) (13 Apr, 26)**

$\star$ **A mapping $f : \mathbb{R}^2 \rightarrow \mathbb{R}^2$ is defined as $f(x,y) = (2x, 2y)$ show that it is a linear mapping.**

**Ans:-**
Let, $u = (a, b) \in \mathbb{R}^2 \ ; \ v = (a', b') \in \mathbb{R}^2$

Now,

$$
u+v = (a, b) + (a', b') = [ (a+a') , (b+b') ]
$$

$$
\therefore f(u+v) = f[ (a+a'), (b+b') ] = [ 2(a+a'), 2(b+b') ]
$$

Again,

$$
f(u) = (2a, 2b) \ ; \ f(v) = (2a', 2b')
$$

$$
f(u) + f(v) = (2a, 2b) + (2a', 2b') = [ 2(a+a') , 2(b+b') ]
$$

Thus, $f(u+v) = f(u) + f(v) \rightarrow$ first condition satisfied.

(ii) $f(ku) = k \cdot f(u)$ (Homogeneity property)/(proportionality)
Now,

$$
f(ku) = f(ka, kb) = (2ka, 2kb)
$$

$$
k \cdot f(u) = k \cdot f(a,b) = k(2a, 2b) = (2ka, 2kb)
$$

---

## Page 88

Thus, the mapping is a linear mapping.

$\star$ **The projection mapping $f : \mathbb{R}^3 \rightarrow \mathbb{R}^3$ is defined as $f(x,y,z) = (x,y,0)$. Show that it is a linear mapping.**

**Ans:-**
Let, $u = (a,b,c) \ ; \ v = (a',b',c')$

$$
\therefore u+v = (a+a', b+b', c+c')
$$

$$
\therefore f(u+v) = (a+a', b+b', 0)
$$

$$
f(u) = (a,b,0) \ ; \ f(v) = (a',b',0)
$$

$$
\therefore f(u) + f(v) = (a+a', b+b', 0)
$$

Thus, $f(u+v) = f(u) + f(v)$

Again,

$$
k \cdot f(u) = k(a,b,0) = (ka, kb, 0)
$$

$$
f(ku) = (ka, kb, 0)
$$

Thus the mapping is linear.

---

## Page 89

$\star$ **A mapping $f : \mathbb{R}^2 \rightarrow \mathbb{R}^2$ defined as $f(x,y) = (xy, x)$ show that it is not a linear mapping.**

**Ans:-**
Let, $u = (a,b) \ ; \ v = (a', b')$

$$
u+v = [ (a+a'), (b+b') ]
$$

$$
f(u+v) = ( (a+a')(b+b') , a+a' )
$$

$$
= [ (ab + a'b + ab' + a'b') , (a+a') ]
$$

$$
f(u) = (ab, a) \ ; \ f(v) = (a'b', a')
$$

$$
\therefore f(u) + f(v) = (ab + a'b', a+a')
$$

$\therefore$ Not a linear mapping.

$$
\# \ \lbrace (1,2) \rbrace = V \rightarrow \text{not a vector space.}
$$

$$
\# \ \lbrace (1,2), (0,0), (-1,-2) \rbrace \rightarrow \text{Not a vector space because satisfies all the properties of addition but does not satisfy the multiplication properties.}
$$

---

## Page 90

**(prev cls)**
**Math-2117**
**(06.04.26) (GCP Sir)**

### Linear Combination of vectors
$v\_1, v\_2 \dots v\_n \in V$ are defined on $\mathbb{R}$.

$$
V = c\_1v\_1 + c\_2v\_2 + \dots + c\_nv\_n
$$

$$
e\_1 = (1,0) \ ; \ e\_2 = (0,1)
$$

$$
\therefore v = 2e\_1 + 3e\_2 = 2(1,0) + 3(0,1) = (2,3)
$$

$c\_1v\_1 + c\_2v\_2 + \dots + c\_nv\_n$ are called linear combination of vectors where $v\_1, v\_2 \dots v\_n$ are from $V$ and $c\_1, c\_2 \dots c\_n$ are from $\mathbb{R}$.

#### Span of V:-
Linear combination এর মাধ্যমে vector তৈরি করে যদি ঐ vector গুলো $V$ এর মধ্যে থাকে তাহলে span of $V$.
Here $e\_1, e\_2$ are span of vector.

$$
\mathbb{R}^2 \rightarrow e\_2 = (0,1) \ ; \ e\_1 = (1,0)
$$
