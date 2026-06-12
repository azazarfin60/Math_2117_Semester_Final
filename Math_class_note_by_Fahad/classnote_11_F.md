# Fahad's Class Note - Pages 101-110

## Page 101

So, $c\_1 = c\_2 = c\_3 = 0$
So, the vectors are linearly independent.

$\star$ **check whether $v\_1 = (2, 3, 3) \ ; \ v\_2 = (4, 5, -1) \ ; \ v\_3 = (4, 4, 1)$ are linearly dependent/independent.**

### Image and kernel of a linear mapping

$$
T : V(\mathbb{R}) \rightarrow W(\mathbb{R})
$$

```
          Domain V                        Codomain W
     +-----------------+              +-----------------+
     |       v_1       | -----------> |       w_1       |
     |       v_2       | -----------> |       w_2       |
     |       v_3       | -----------> |       w_3       |
     |       v_4       | -----------> |       w_4       |
     +-----------------+              +-----------------+
```
- $\lbrace w\_1, w\_2, w\_3, w\_4 \rbrace \rightarrow \text{Im}(T) \rightarrow \text{image of the mapping.}$

**যেগুলোর map '0' vector হবে তাদের kernel বলা হবে।**

$$
T(x,y,z) = (x,y,0)
$$

$$
\text{then } (0,0,1), (0,0,2), (0,0,3) \dots \text{ এগুলো kernel}
$$

$\star$ **what is meant by image of a mapping what is kernel.**
$\star$ **define kernel of T.**

$$
\text{ker}(T) = \lbrace u \mid u \rightarrow 0 \rbrace
$$

---

## Page 102

**Math-2117**
**(GCP Sir) (20 Apr, 26)**

$\star$ **Let: $T : \mathbb{R}^3 \rightarrow \mathbb{R}^3$ be a linear mapping defined by $T(x,y,z) = (x+2y, y-z, x+2z)$. Find a basis and dimension of (i) Image of T and (ii) Kernel of T.**

**Ans:-**
The usual basis or standard basis of $\mathbb{R}^3$ is:

$$
\lbrace (1,0,0) , (0,1,0) , (0,0,1) \rbrace \text{ that generates } \mathbb{R}^3.
$$

Then the basis $\lbrace T(1,0,0) , T(0,1,0) , T(0,0,1) \rbrace$ will generate the Im $T$.

Now,

$$
\lbrace T(1,0,0) , T(0,1,0) , T(0,0,1) \rbrace
$$

$$
= \lbrace (1,0,1) , (2,1,0) , (0,-1,2) \rbrace
$$

> [!NOTE]
> $v \in \mathbb{R}^3 \rightarrow$ Domain
> $T(v) \in \mathbb{R}^3 \rightarrow$ Codomain / Image

Now, we will check how many of them are independent.

---

## Page 103

Now, we will generate the following matrix and will reduce it to its echelon form. Matrix as follows:-

$$
\begin{pmatrix}
1 & 0 & 1 \\
2 & 1 & 0 \\
0 & -1 & 2
\end{pmatrix}
$$

$$
R\_2 \rightarrow 2R\_1 - R\_2
$$

$$
\sim
\begin{pmatrix}
1 & 0 & 1 \\
0 & -1 & 2 \\
0 & -1 & 2
\end{pmatrix}
$$

$$
R\_3 \rightarrow R\_2 - R\_3
$$

$$
\sim
\begin{pmatrix}
1 & 0 & 1 \\
0 & -1 & 2 \\
0 & 0 & 0
\end{pmatrix}
$$

We see there are 2 independent vectors $(1,0,1)$ and $(0,-1,2)$ and hence $\lbrace (1,0,1) , (0,-1,2) \rbrace$ is a basis of Im $T$.

$$
\therefore \text{Dimension of Im } T \ ; \ \text{dim}T = 2.
$$

---

## Page 104

$\star$ **Kernel of T is a set of vectors যাদের উপর img নিলে 0 vector পাওয়া যাবে।**

Such that,

$$
\text{ker } T = \lbrace (x,y,z) \in \mathbb{R}^3 \mid T(x,y,z) = (0,0,0) \rbrace
$$

i.e.,

$$
\begin{aligned}
x+2y &= 0 \\
y-z &= 0 \\
x+2z &= 0
\end{aligned}
$$

Using $L\_3 = L\_1 - L\_3$:

$$
\begin{aligned}
x+2y &= 0 \\
y-z &= 0 \\
2y-2z &= 0
\end{aligned}
$$

$$
\sim \begin{aligned}
x+2y &= 0 \\
y-z &= 0
\end{aligned}
$$

The system has 2 equations with 3 unknowns.

$$
\therefore \text{Free variable} = 3 - 2 = 1
$$

Say, $z$ is a free variable. Set $z=1, y=1, x=-2$.
Thus,

$$
\lbrace (-2,1,1) \rbrace \text{ is a basis of ker } T.
$$

$$
\text{dim ker } T = 1.
$$

---

$\star$ **Let, $T : \mathbb{R}^2 \rightarrow \mathbb{R}^2$ defined by $T(x,y) = (x+2y, y)$ and $T' : \mathbb{R}^2 \rightarrow \mathbb{R}^2$ defined by $T'(x,y) = (y,x)$**
1. Find $(3T - 2T')(0,1)$
2. $(TT')(2,3)$
3. $(T^2 T')(4,5)$

---

## Page 105

### Composition check

$$
TT'(x,y) = T(T'(x,y))
$$

$$
= T(y,x) = (y+2x, x)
$$

### Linearity check of $T'$

Let, $u \in \mathbb{R}^2, v \in \mathbb{R}^2$ and $u = (a,b), v = (a',b')$.

$$
u+v = [ (a+a') , (b+b') ]
$$

$$
T'(u+v) = [ (b+b') , (a+a') ]
$$

Again,

$$
T'(u) = (b,a) \ ; \ T'(v) = (b',a')
$$

$$
T'(u) + T'(v) = (b,a) + (b',a') = [ (b+b') , (a+a') ]
$$

---

### Matrix Representation for a linear mapping:-

Let, $T : \mathbb{R}^2 \rightarrow \mathbb{R}^2$ is defined by:

$$
T(x,y) = (5x+y , -4x+3y).
$$

Find the matrix representation of $T$ with respect to the basis $\lbrace u\_1 = (3,1) \ ; \ v\_2 = (5,2) \rbrace$.

```
                 T : A -> B  (Codomain)
                     |
                  (Domain)

Domain Basis = { v_1, v_2 ... v_n }
Codomain Basis = { w_1, w_2 ... w_n }
T(v_1), T(v_2) ... T(v_n) : images of T
T(v_1) = a_11 w_1 + a_12 w_2 + a_13 w_3 + ...
```

---

## Page 106

$$
T(v\_2) = a\_21 w\_1 + a\_22 w\_2 + a\_23 w\_3 + \dots + a\_2n w\_n
$$

$$
T(v\_n) = a\_n1 w\_1 + a\_n2 w\_2 + \dots + a\_nm w\_m
$$

$$
A = \begin{bmatrix}
a\_11 & a\_12 & \dots & a\_1n \\
a\_21 & a\_22 & \dots & a\_2n \\
\vdots & \vdots & \ddots & \vdots \\
a\_m1 & a\_m2 & \dots & a\_mn
\end{bmatrix} = [T]\_w \quad \rightarrow \text{mapping এর matrix}
$$

**Ans:-**

$$
T(u\_1) = T(3,1) = (16, -9)
$$

$$
T(v\_2) = T(5,2) = (27, -14)
$$

Let,

$$
T(u\_1) = a u\_1 + b v\_2
$$

$$
\text{or, } (16, -9) = a(3,1) + b(5,2)
$$

$$
\Rightarrow (3a+5b, a+2b) = (16, -9)
$$

$$
\begin{aligned}
3a + 5b &= 16 \\
a + 2b &= -9
\end{aligned}
$$

$$
\therefore a = 77 \ ; \ b = -43
$$

$$
\therefore (16,-9) = 77(3,1) - 43(5,2) \quad \dots \text{ (i)}
$$

---

## Page 107

Again let,

$$
(27, -14) = c(3,1) + d(5,2)
$$

$$
= (3c+5d, c+2d)
$$

$$
\begin{aligned}
3c+5d &= 27 \\
c+2d &= -14
\end{aligned}
$$

$$
\therefore c = 124 \ ; \ d = -69
$$

$$
\therefore (27,-14) = 124(3,1) - 69(5,2) \quad \dots \text{ (ii)}
$$

$\therefore$ The required matrix representation is:-

$$
T =
\begin{bmatrix}
77 & -43 \\
124 & -69
\end{bmatrix}^t = \begin{bmatrix} 77 & 124 \\ -43 & -69 \end{bmatrix}
$$

---

## Page 108

**Math-2117**
**(Rupali Madam) (21 Apr, 26)**

### Stokes theorem:-
* Prove.
* statement

### Green's theorem ***.

#### Suggestions:-
$\rightarrow$ **সহজগুলো থেকে বেশি।**

---

**Math-2117**
**(GCP Sir) (21 Apr, 26)**

### Inner product space/pre inverse space:-

#### Inner product of two vectors $\langle u,v \rangle$

$$
\langle u,v \rangle : V \times V \rightarrow \mathbb{R} / \mathbb{C}
$$

$$
\text{(2 vectors) (Complex or Real numbers)}
$$

#### Properties:-
1. $\langle au+v, w \rangle = a \langle u,w \rangle + \langle v,w \rangle \quad \text{linearity prop.}$
2. $\langle u,v \rangle = \overline{\langle v,u \rangle} \quad \text{symmetry prop.}$
3. $\langle u,v \rangle \geq 0$
4. $\langle u,u \rangle = 0 \Leftrightarrow u = 0 \quad \text{positive prop.}$

---

## Page 109

### Norm:-

$$
\|v\| = \sqrt{\langle v,v \rangle}
$$

### Angle between 2 vectors:-

$$
\cos \theta = \frac{\langle u,v \rangle}{\|u\| \cdot \|v\|}
$$

$\star$ **Find the angle between the vector $u\_1 = (1,2,3) \ ; \ u\_2 = (1,1,1)$**

$$
\cos \theta = \frac{1+2+3}{\sqrt{14}\sqrt{3}} = \frac{6}{\sqrt{42}}
$$

- **Orthogonal vector** $\rightarrow$ if $\theta = 90^\circ$
- **Orthonormal vector** $\rightarrow$ if $\theta = 90^\circ$ && $\|u\| = 1, \|v\| = 1$

$\star$ **Find the angle between the matrices.**

$$
u =
\begin{bmatrix}
1 & 0 \\
0 & 1
\end{bmatrix} \quad \text{and} \quad v = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix}
$$

$$
\Rightarrow \cos \theta = \frac{\langle u,v \rangle}{\|u\| \cdot \|v\|}
$$

$$
\Rightarrow \frac{1+0+0+1}{\sqrt{2}\sqrt{4}} = \frac{2}{2\sqrt{2}} = \frac{1}{\sqrt{2}}
$$

$$
\text{angle } \theta = 45^\circ \text{ হলে similar}
$$

---

## Page 110

$\star$ **A rule between two functions inner product of two functions:**

$$
\langle f,g \rangle = \int\_a^b f g \, dx \quad \text{where } f \text{ and } g \text{ are defined over } [a,b]
$$

$$
\langle \sin x, \cos x \rangle = \int\_{-\pi/2}^{\pi/2} \cos x \cdot \sin x \, dx = 0
$$

Fourier basis $\lbrace 1, \sin x, \cos x, \sin 2x, \cos 2x \dots \rbrace$
**এগুলো orthogonal vector.**
**এই সবগুলোর মধ্যবর্তী Angle $90^\circ$.**

$$
\langle 1, \sin x \rangle = 0
$$

$\star$ **Show that $\lbrace (1,0,0), (0,1,0), (0,0,1) \rbrace$ forms an orthogonal basis of $\mathbb{R}^3$.**

**Ans:-**
Here,
Let, $e\_1 = (1,0,0) \ ; \ e\_2 = (0,1,0) \ ; \ e\_3 = (0,0,1)$

Here,

$$
\|e\_1\| = 1
$$

$$
\|e\_2\| = 1
$$

$$
\|e\_3\| = \sqrt{0^2 + 0^2 + 1^2} = 1
$$
