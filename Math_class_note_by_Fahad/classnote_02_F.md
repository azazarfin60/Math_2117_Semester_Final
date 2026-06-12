<!-- Page 011 -->
<div align="right"><b>19 Nov, 25</b></div>

<b>Math-2117</b>
<b>(PDF Maam)</b>

* Frenet - Serret formula $\rightarrow$ derivation (not needed)

- $T \rightarrow$ unit tangent vector
- $N \rightarrow$ principal normal
- $B \rightarrow$ Binormal

$$
T = \frac{\frac{d\vec{r}}{dt}}{\left| \frac{d\vec{r}}{dt} \right|} = \frac{\frac{d\vec{r}}{dt}}{\frac{ds}{dt}} = \frac{d\vec{r}}{dt} \frac{dt}{ds} = \frac{d\vec{r}}{ds}
$$

$$
\left| \frac{d\vec{r}}{dt} \right| = \frac{ds}{dt}
$$

$$
\frac{d\vec{T}}{ds} = \kappa \vec{N}
$$

- $\kappa \rightarrow$ kappa (curvature)
- $\rho = \frac{1}{\kappa} \rightarrow$ radius of curvature
- $\tau \rightarrow$ tau (Torsion)
- $\sigma = \frac{1}{\tau} \rightarrow$ radius of torsion

Box:

$$
\boxed{T \quad N \quad B \quad \kappa \quad \rho \quad \tau \quad \sigma}
$$

$\rightarrow$ terms to find of a curve.

---

<!-- Page 012 -->

$$
\boxed{\frac{d}{dt}(A \times B) = \frac{dA}{dt} \times B + A \times \frac{dB}{dt}}
$$

* $A = 5t^2\vec{i} + t\vec{j} - t^3\vec{k} ; \quad B = \sin t\,\vec{i} - \cos t\,\vec{j}$
  then $\frac{d}{dt}(A \times B) = ?$

Ans:-

$$
\frac{d}{dt}(A \times B) = \frac{d}{dt}A \times B + A \times \frac{d}{dt}B
$$

Here,

$$
\frac{d}{dt}A = 10t\,\vec{i} + \vec{j} - 3t^2\vec{k}
$$

$$
\frac{d}{dt}B = \cos t\,\vec{i} + \sin t\,\vec{j}
$$

Let $C_1 = \frac{dA}{dt} \times B$ and $C_2 = A \times \frac{dB}{dt}$.

$$
C_1 =
\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k} \\
10t & 1 & -3t^2 \\
\sin t & -\cos t & 0
\end{vmatrix}
$$

$$
= \vec{i}(3t^2\cos t) - \vec{j}(3t^2\sin t) + \vec{k}(-10t\cos t - \sin t)
$$

$$
= 3t^2\cos t\,\vec{i} - 3t^2\sin t\,\vec{j} - (10t\cos t + \sin t)\vec{k}
$$

$$
C_2 =
\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k} \\
5t^2 & t & -t^3 \\
\cos t & \sin t & 0
\end{vmatrix}
$$

$$
= \vec{i}(t^3\sin t) - \vec{j}(t^3\cos t) + \vec{k}(5t^2\sin t - t\cos t)
$$

$$
= t^3\sin t\,\vec{i} - t^3\cos t\,\vec{j} + (5t^2\sin t - t\cos t)\vec{k}
$$

---

<!-- Page 013 -->

$$
\therefore \frac{d}{dt}(A \times B) = C_1 + C_2
$$

$$
= 3t^2\cos t\,\vec{i} - 3t^2\sin t\,\vec{j} - 10t\cos t\,\vec{k} - \sin t\,\vec{k} + t^3\sin t\,\vec{i} - t^3\cos t\,\vec{j} + 5t^2\sin t\,\vec{k} - t\cos t\,\vec{k}
$$

$$
= (3t^2\cos t + t^3\sin t)\vec{i} - (3t^2\sin t + t^3\cos t)\vec{j} - (10t\cos t + \sin t + t\cos t - 5t^2\sin t)\vec{k} \quad (\text{Ans.})
$$

* $A = (2x^2y - x^4)\vec{i} + (e^{xy} - y\sin x)\vec{j} + (x^2\cos y)\vec{k}$
  find that $\frac{\partial^2 A}{\partial x\partial y} = \frac{\partial^2 A}{\partial y\partial x}$.

Ans:-

$$
\frac{\partial A}{\partial x} = (4xy - 4x^3)\vec{i} + (ye^{xy} - y\cos x)\vec{j} + (2x\cos y)\vec{k}
$$

$$
\therefore \frac{\partial^2 A}{\partial x\partial y} = \frac{\partial}{\partial y}\left(\frac{\partial A}{\partial x}\right) = 4x\vec{i} + (xy e^{xy} - \cos x)\vec{j} - (2x\sin y)\vec{k}
$$

Again,

$$
\frac{\partial A}{\partial y} = 2x^2\vec{i} + (x e^{xy} - \sin x)\vec{j} - (x^2\sin y)\vec{k}
$$

$$
\therefore \frac{\partial^2 A}{\partial y\partial x} = \frac{\partial}{\partial x}\left(\frac{\partial A}{\partial y}\right) = 4x\vec{i} + (xy e^{xy} - \cos x)\vec{j} - (2x\sin y)\vec{k}
$$

$$
\therefore \frac{\partial^2 A}{\partial x\partial y} = \frac{\partial^2 A}{\partial y\partial x} \quad (\text{proved})
$$

---

<!-- Page 014 -->

* $x = 3\cos t, \quad y = 3\sin t, \quad z = 4t$
  then unit tangent vector $\vec{T} = ?$

Ans:-

$$
\vec{r} = 3\cos t\,\vec{i} + 3\sin t\,\vec{j} + 4t\,\vec{k}
$$

$$
\frac{d\vec{r}}{dt} = -3\sin t\,\vec{i} + 3\cos t\,\vec{j} + 4\vec{k}
$$

$$
T = \frac{\frac{d\vec{r}}{dt}}{\left| \frac{d\vec{r}}{dt} \right|}
$$

$$
\frac{ds}{dt} = \left| \frac{d\vec{r}}{dt} \right| = \sqrt{9\sin^2 t + 9\cos^2 t + 16} = \sqrt{9 + 16} = 5
$$

$$
\therefore T = \frac{d\vec{r}}{ds} = \frac{d\vec{r}}{dt} \times \frac{dt}{ds} = -\frac{3}{5}\sin t\,\vec{i} + \frac{3}{5}\cos t\,\vec{j} + \frac{4}{5}\vec{k}
$$

$$
\frac{d\vec{T}}{dt} = -\frac{3}{5}\cos t\,\vec{i} - \frac{3}{5}\sin t\,\vec{j}
$$

$$
\therefore \frac{d\vec{T}}{ds} = -\frac{3}{25}\cos t\,\vec{i} - \frac{3}{25}\sin t\,\vec{j}
$$

We know,

$$
\frac{d\vec{T}}{ds} = \kappa \vec{N}, \quad |\vec{N}| = 1
$$

$$
\therefore \kappa = \left| \frac{d\vec{T}}{ds} \right| = \sqrt{\left(-\frac{3}{25}\cos t\right)^2 + \left(-\frac{3}{25}\sin t\right)^2} = \frac{3}{25}
$$

$$
\therefore \rho = \frac{25}{3} = \frac{1}{\kappa}
$$

$$
\therefore N = -\cos t\,\vec{i} - \sin t\,\vec{j}
$$

$$
B = T \times N =
\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k} \\
-\frac{3}{5}\sin t & \frac{3}{5}\cos t & \frac{4}{5} \\
-\cos t & -\sin t & 0
\end{vmatrix}
$$

---

<!-- Page 015 -->
<div align="right"><b>23 Nov, 25</b></div>

<b>Math-2117</b>
<b>(GCP Sir)</b>

### Difference between matrices and determinants:
- **Matrix:** $m \neq n$ হতে পারে। (No value)
- **Determinant:** $m = n$ must. (Value exists)

### System:-
A system of linear equations:

$$
a_{11}x_1 + a_{12}x_2 + a_{13}x_3 + \dots + a_{1n}x_n = b_1
$$

$$
a_{21}x_1 + a_{22}x_2 + a_{23}x_3 + \dots + a_{2n}x_n = b_2
$$

$$
\vdots
$$

$$
a_{n1}x_1 + a_{n2}x_2 + a_{n3}x_3 + \dots + a_{nn}x_n = b_n
$$

Unknowns are:-
- $x_1, x_2, x_3, \dots, x_n \rightarrow$ unknowns.
- $b_1, b_2, b_3, \dots, b_n =$ const.

* The degree of unknowns should be exactly 1.

* If one of $b_1, b_2, b_3, \dots, b_n$ is not zero then the system is non-homogeneous system.
* If all of them are $= 0$ then they are homogeneous system.

---

<!-- Page 016 -->

* $b_1, b_2, b_3, \dots, b_n \rightarrow 0$ হলে Solution সব সময় থাকবে। (Homogeneous system)
* কোন ১টি non-zero হলে থাকতেও পারে নাও পারে।
* non-homogeneous system $\rightarrow$ may have solution.

* Every system of linear equations can be written as

$$
\boxed{AX = B}
$$

where,

$$
A = \begin{bmatrix}
a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
\vdots & & & & \\
a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn}
\end{bmatrix}
$$

$$
X =
\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
\vdots \\
x_n
\end{bmatrix}, \quad B = \begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}
$$

---

<!-- Page 017 -->

* Example:

$$
2x + 3y - 5z = 2
$$

$$
x + y - z = 1
$$

$$
2x - 2y + z = 3
$$

In $AX = B$ form:

$$
A =
\begin{bmatrix}
2 & 3 & -5 \\
1 & 1 & -1 \\
2 & -2 & 1
\end{bmatrix}, \quad X = \begin{bmatrix} x \\ y \\ z \end{bmatrix}, \quad B = \begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix}
$$

$$
\therefore AX = B
$$

$$
\begin{bmatrix}
2 & 3 & -5 \\
1 & 1 & -1 \\
2 & -2 & 1
\end{bmatrix} \begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix}
$$

$$
\therefore
\begin{bmatrix}
2x + 3y - 5z \\
x + y - z \\
2x - 2y + z
\end{bmatrix} = \begin{bmatrix} 2 \\ 1 \\ 3 \end{bmatrix}
$$

---

<!-- Page 018 -->
<div align="left"><i>Philosophy $\rightarrow$ Physics $\rightarrow$ Math $\rightarrow$ application.</i></div>

$$
\therefore 2x + 3y - 5z = 2
$$

$$
x + y - z = 1
$$

$$
2x - 2y + z = 3
$$

$$
\therefore \text{Every linear system can be written as } AX = B. \quad (\text{proved})
$$

### steps:- (Matrix method)
1. $AX = B$
2. Augmented matrix $[A : B]$ (concatenation) $\rightarrow$ Horizontal cat
3. Convert the augmented matrix into echelon matrix
4. Find Rank of $A$ and Rank of $[A : B]$
5. Rank of $A$ = Rank of $[A : B]$ then solution exists
   - (I) Can be unique solution ($\text{Rank of } A = \text{Rank of } [A:B] = \text{number of unknowns}$)
   - (II) Can be more than 1 solution ($\text{Rank of } A = \text{Rank of } [A:B] < \text{number of unknowns}$)

<div align="left">
<i>Rank of A $\neq$ Rank of [A:B] $\rightarrow$ no solution</i><br>
<i>Rank of A = Rank of [A:B] < number of unknowns</i>
</div>

---

<!-- Page 019 -->

* If Rank of $A$ = Rank of $[A:B]$ then solution exists.
* If Rank of $A \neq$ Rank of $[A:B]$ then the system has no solution.

* **solve the system:-**

$$
x - 2y - 5z = 2
$$

$$
-x + y + 3z = -2
$$

$$
2x + y + z = 3
$$

Ans:-
The system can be set as $AX = B$
where,

$$
A =
\begin{bmatrix}
1 & -2 & -5 \\
-1 & 1 & 3 \\
2 & 1 & 1
\end{bmatrix}, \quad X = \begin{bmatrix} x \\ y \\ z \end{bmatrix} \quad \text{and} \quad B = \begin{bmatrix} 2 \\ -2 \\ 3 \end{bmatrix}
$$

Now, the augmented matrix

$$
[A:B] =
\begin{bmatrix}
1 & -2 & -5 & \bigm| & 2 \\
-1 & 1 & 3 & \bigm| & -2 \\
2 & 1 & 1 & \bigm| & 3
\end{bmatrix}
$$

$$
R_2 \rightarrow R_2 + R_1
$$

$$
R_3 \rightarrow R_3 - 2R_1
$$

$$
\sim
\begin{bmatrix}
1 & -2 & -5 & \bigm| & 2 \\
0 & -1 & -2 & \bigm| & 0 \\
0 & 5 & 11 & \bigm| & -1
\end{bmatrix}
$$

---

<!-- Page 020 -->

$$
\boxed{* \text{Rank} = \text{number of non-zero rows}}
$$

$$
R_3 \rightarrow 5R_2 + R_3
$$

$$
\sim
\begin{bmatrix}
1 & -2 & -5 & \bigm| & 2 \\
0 & -1 & -2 & \bigm| & 0 \\
0 & 0 & 1 & \bigm| & -1
\end{bmatrix}
$$

which is the echelon form of $[A:B]$

Here,
Rank of $A = 3$
& Rank of $[A:B] = 3$
and the number of unknowns (variables) $= 3$.

So, the system has a unique solution.

next class-এ করাবে।

* **Vector chap 2 (45) problem.**