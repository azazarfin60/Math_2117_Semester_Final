# Fahad's Class Note - Pages 21-30

## Page 21

**Math-2117**
**(24 nov, 25) (Rupali Maam)**

### Space Curve

#### Frenet-serret formula

#### Chap-3 (Problem-19)

$$
x = 3\cos t, \quad y = 3\sin t, \quad z = 4t
$$

Unit tangent $\vec{T} = ?$

$$
\vec{r} = 3\cos t\,\hat{i} + 3\sin t\,\hat{j} + 4t\hat{k}
$$

$$
\frac{d\vec{r}}{dt} = -3\sin t\,\hat{i} + 3\cos t\,\hat{j} + 4\hat{k}
$$

$$
\frac{ds}{dt} = \left|\frac{d\vec{r}}{dt}\right| = \sqrt{(-3\sin t)^2 + (3\cos t)^2 + 4^2} = \sqrt{9(\sin^2 t + \cos^2 t) + 16} = \sqrt{9 + 16} = 5
$$

$$
\therefore \vec{T} = \frac{d\vec{r}}{ds} = \frac{d\vec{r}}{dt} \cdot \frac{dt}{ds} = \left( -3\sin t\,\hat{i} + 3\cos t\,\hat{j} + 4\hat{k} \right) \cdot \frac{1}{5}
$$

$$
= -\frac{3}{5}\sin t\,\hat{i} + \frac{3}{5}\cos t\,\hat{j} + \frac{4}{5}\hat{k}
$$

---

*Prove that* $\frac{d\vec{T}}{ds} = \kappa \vec{N}$

**Ans:-**

$$
\frac{d\vec{T}}{ds} = \frac{d\vec{T}}{dt} \cdot \frac{dt}{ds}
$$

> [!NOTE]
> $\vec{N}$ is the unit normal vector, so $|\vec{N}| = 1$.

$$
\frac{d\vec{T}}{dt} = -\frac{3}{5}\cos t\,\hat{i} - \frac{3}{5}\sin t\,\hat{j}
$$

---

## Page 22

$$
\therefore \frac{d\vec{T}}{ds} = \frac{d\vec{T}}{dt} \cdot \frac{dt}{ds} = \left( -\frac{3}{5}\cos t\,\hat{i} - \frac{3}{5}\sin t\,\hat{j} \right) \cdot \frac{1}{5}
$$

$$
= -\frac{3}{25}\cos t\,\hat{i} - \frac{3}{25}\sin t\,\hat{j}
$$

$$
\therefore \frac{d\vec{T}}{ds} = \kappa \vec{N} \quad \text{[Frenet-serret]}
$$

$$
\therefore \left|\frac{d\vec{T}}{ds}\right| = |\kappa| |\vec{N}| = \kappa \quad \text{[since } |\vec{N}| = 1\text{]}
$$

$$
\therefore \sqrt{\left(-\frac{3}{25}\cos t\right)^2 + \left(-\frac{3}{25}\sin t\right)^2} = \frac{3}{25} = \kappa
$$

$$
\therefore \rho = \frac{1}{\kappa} = \frac{25}{3}
$$

Again,

$$
\vec{B} = \vec{T} \times \vec{N} =
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
-\frac{3}{5}\sin t & \frac{3}{5}\cos t & \frac{4}{5} \\
-\cos t & -\sin t & 0
\end{vmatrix}
$$

$$
= \hat{i}\left( 0 - \left(-\frac{4}{5}\sin t\right) \right) - \hat{j}\left( 0 - \left(-\frac{4}{5}\cos t\right) \right) + \hat{k}\left( \frac{3}{5}\sin^2 t - \left(-\frac{3}{5}\cos^2 t\right) \right)
$$

$$
= \frac{4}{5}\sin t\,\hat{i} - \frac{4}{5}\cos t\,\hat{j} + \frac{3}{5}\hat{k}
$$

$$
\frac{d\vec{B}}{dt} = \frac{4}{5}\cos t\,\hat{i} + \frac{4}{5}\sin t\,\hat{j}
$$

$$
\therefore \frac{d\vec{B}}{ds} = \frac{d\vec{B}}{dt} \cdot \frac{dt}{ds} = \frac{4}{25}\cos t\,\hat{i} + \frac{4}{25}\sin t\,\hat{j}
$$

---

## Page 23

$$
-\tau\vec{N} = -\tau(-\cos t\,\hat{i} - \sin t\,\hat{j}) = \frac{4}{25}\cos t\,\hat{i} + \frac{4}{25}\sin t\,\hat{j} = \frac{d\vec{B}}{ds}
$$

$$
\therefore \tau = \frac{4}{25}
$$

$$
\sigma = \frac{1}{\tau} = \frac{25}{4}
$$

---

### Chap-4 (Gradient, Divergence, Curl)

**Math-2117**
**(25 nov, 25) (Rupali Maam)**

The vector differentiation operator,

$$
\text{nabla } \nabla \text{ (del)}
$$

$$
\nabla = \frac{\partial}{\partial x}\hat{i} + \frac{\partial}{\partial y}\hat{j} + \frac{\partial}{\partial z}\hat{k}
$$

#### Physical meaning of gradient

$$
\phi(x,y,z) \rightarrow \text{scalar}
$$

$$
\nabla \phi \rightarrow \text{gradient indicates the direction of maximum change.}
$$

---

## Page 24

$$
\vec{v}(x,y,z) = v_1\hat{i} + v_2\hat{j} + v_3\hat{k}
$$

$$
\nabla \cdot \vec{v} \rightarrow \text{divergence}
$$

```
   (Source)
চারিদিকে ছড়িয়ে পড়ে (+)

     sink -> negative divergence (-)

  Solenoidal -> 0
```

$$
\nabla \times \vec{v} \rightarrow \text{Curl}
$$

$$
\nabla(\nabla \cdot \phi) \rightarrow \text{divergence of grad phi.}
$$

$$
\nabla^2 \rightarrow \text{Laplace operator.}
$$

**Prove,**
10. $\nabla \times \nabla(\phi) = 0$
11. $\nabla \cdot (\nabla \times \vec{A}) = 0$
*(general form দিয়ে করতে হবে।)*

---

$\star$ $\phi = 3x^2y - y^3z^2$, find $\nabla \phi$ (grad of $\phi$) at point $(1,-2,1)$

$$
\nabla \phi = \frac{\partial \phi}{\partial x}\hat{i} + \frac{\partial \phi}{\partial y}\hat{j} + \frac{\partial \phi}{\partial z}\hat{k}
$$

$$
= 6xy\,\hat{i} + (3x^2 - 3y^2z^2)\hat{j} + (-2y^3z)\hat{k}
$$

$$
\therefore \nabla \phi \text{ at } (1,-2,1) = 6(1)(-2)\hat{i} + \left(3(1)^2 - 3(-2)^2(1)^2\right)\hat{j} + \left(-2(-2)^3(1)\right)\hat{k}
$$

$$
= -12\hat{i} - 9\hat{j} + 16\hat{k}
$$

---

## Page 25

$\star$ **CT-1 (chap 1, 2, 3)**

$\star\star\star$ **Normally আসে।**

$$
\phi = \ln |r| ; \quad \phi = \frac{1}{r}
$$

$$
(4), (6), (7)
$$

#### Directional Derivative

---

$\star$ $\phi = 2x^3y^2z^4$, find $\nabla \cdot \nabla \phi$ :

**Ans:-**

$$
\nabla \cdot \nabla \phi = \nabla^2 \phi = 12xy^2z^4\,\hat{i} + 4x^3z^4\hat{j} + 24x^3y^2z^2\,\hat{k}
$$

#### Curl of gradient

$$
\nabla \times (\nabla \phi) =
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
6x^2y^2z^4 & 4x^3yz^4 & 8x^3y^2z^3
\end{vmatrix}
$$

$$
= \hat{i}\left(16x^3yz^3 - 16x^3yz^3\right) + \hat{j}\left(24x^2y^2z^3 - 24x^2y^2z^3\right) + \hat{k}\left(12x^2yz^4 - 12x^2yz^4\right)
$$

$$
= 0
$$

---

## Page 26

$\star$

$$
\vec{A} = xz^3\,\hat{i} - 2x^2yz\,\hat{j} + 2xz^4\hat{k},
$$

$\nabla \times \vec{A} = ?$

$$
\nabla \times \vec{A} =
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
xz^3 & -2x^2yz & 2xz^4
\end{vmatrix}
$$

$$
= \hat{i}\left( 0 + 2x^2y \right) + \hat{j}\left( 2z^4 - 3xz^2 \right) + \hat{k}\left( -4xyz + 0 \right)
$$

---

## Page 27

**Math-2117**
**(29 nov, 25) (GCP Sir)**

$\star$ **'0' Solution means trivial solution of a system.**

$$
\downarrow
$$

$$
\text{where all are considered '0'.}
$$

$$
x+y=0
$$

---

$\star$

$$
\begin{matrix}
x+y=2 \\
x+2y=3
\end{matrix} \quad ; \quad x=1, y=1 \rightarrow \text{unique solutions.}
$$

---

$\star$

$$
\begin{matrix}
x+y=2 & \text{--- (I)} \\
2x+2y=3 & \text{--- (II)}
\end{matrix}
$$

```
   \           \ (II)
    \           \
     \           \ (I)
      \           \
```

$$
\text{the 2 lines are parallel to each other, so they have no solutions.}
$$

যদি উভয় equ. একই line প্রকাশ করে তাহলে $\infty$ solutions as they কারণ অসংখ্য point-এ ছেদ করে।

---

**previous solution.**

$$
\begin{bmatrix}
1 & -2 & -5 & \bigm| & 2 \\
0 & -1 & -2 & \bigm| & 0 \\
0 & 0 & 1 & \bigm| & -1
\end{bmatrix}
$$

Then the equivalent system will be:-

$$
\begin{matrix}
x - 2y - 5z = 2 & \text{--- (I)} \\
-y - 2z = 0 & \text{--- (II)} \\
z = -1 & \text{--- (III)}
\end{matrix}
$$

$$
\because z = -1
$$

$$
\therefore y = 2
$$

$$
\therefore x = 1
$$

(Ans)

---

## Page 28

$$
\text{consistent } \rightarrow \text{ solution আছে}
$$

$$
\text{inconsistent } \rightarrow \text{ solution নাই}
$$

$$
\therefore \text{The unique solution of the system is, } (x,y,z) = (1,2,-1)
$$

#### Method-2

$$
AX = B
$$

$$
X = A^{-1}B
$$

$$
\therefore
\begin{bmatrix}
x \\
y \\
z
\end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}
$$

> [!NOTE]
>

$$
A^{-1} = \frac{\text{adj}(A)^T}{|A|} \quad \text{কাজ করবে না in case of many solution}
$$

---

$\star$ **find the condition of $\lambda$ so that the system**

$$
x+y+3z=5
$$

$$
2x+y-2z=7
$$

$$
x+2y+\lambda z=3 \quad \text{--- (1)}
$$

**has**
1. Unique solution
2. No solution
3. More than one solution.

**Ans:-**

$AX$ Eqn. (1) can be put in matrix form as,

$$
AX = B
$$

$$
\begin{bmatrix}
1 & 1 & 3 \\
2 & 1 & -2 \\
1 & 2 & \lambda
\end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 5 \\ 7 \\ 3 \end{bmatrix}
$$

---

## Page 29

Now, augmented matrix

$$
[A : B] =
\begin{bmatrix}
1 & 1 & 3 & \bigm| & 5 \\
2 & 1 & -2 & \bigm| & 7 \\
1 & 2 & \lambda & \bigm| & 3
\end{bmatrix}
$$

$$
[A : B] \quad
\begin{matrix}
R_2 \rightarrow 2R_1 - R_2 \\
R_3 \rightarrow R_1 - R_3
\end{matrix}
$$

$$
\sim
\begin{bmatrix}
1 & 1 & 3 & \bigm| & 5 \\
0 & 1 & 7 & \bigm| & 3 \\
0 & -1 & 3-\lambda & \bigm| & 2
\end{bmatrix}
$$

$$
[A : B] \quad R_3 \rightarrow R_3 + R_2
$$

$$
\sim
\begin{bmatrix}
1 & 1 & 3 & \bigm| & 5 \\
0 & 1 & 7 & \bigm| & 3 \\
0 & 0 & 10-\lambda & \bigm| & 5
\end{bmatrix} \quad \text{which is the echelon matrix of } [A:B]
$$

### (I) Case 1:-
#### Unique solution

$$
\text{Rank}(A) = \text{Rank}(A:b) = \text{No. of variables} = 3
$$

$$
\therefore 10-\lambda \neq 0
$$

$$
\Rightarrow \lambda \neq 10
$$

### (II) Case 2:-
#### No solution

$$
\text{Rank}(A) \neq \text{Rank}(A:b) \text{; this is possible if,}
$$

$$
\therefore 10-\lambda = 0
$$

$$
\lambda = 10
$$

---

## Page 30

### (III) Case 3:-
#### More than one solution

$$
\text{Rank}(A) = \text{Rank}(A:B) < \text{No. of variables}
$$

$$
\text{It is not possible.}
$$

$$
\therefore \text{which means the system has no more than 1 solution.}
$$

---

**Math-2117**
**(2 Dec, 25) (Rupali Maam)**

#### Gradient, Divergence, Curl

#### Curl (28 & 29)