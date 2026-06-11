<!-- Page 011 -->
$\# A = xz^3 \hat{i} - 2x^2 yz \hat{j} + 2yz^4 \hat{k}$

$\nabla \times A \quad (1, -1, 1)$

$\nabla \times A = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ xz^3 & -2x^2 yz & 2yz^4 \end{vmatrix} = \hat{i}(2z^4 + 2x^2y) - \hat{j}(0 - 3xz^2) + \hat{k}(-4xyz - 0)$
$= (2x^2y + 2z^4)\hat{i} + 3xz^2\hat{j} - 4xyz\hat{k}$

$\nabla \cdot (\nabla \times A) = 4xy - 4xy = 0$

<div align="right"><b>30-11-23</b></div>

<b>Class 10 | Sir</b>

**# inconsistent system vs consistent system**
**# linear eq - highest power of x is only 1** $\rightarrow$ system that has a solution
**# Trivial solution** $x+y=0$, $x$ এবং $y$ যেকোনো মানের জন্য valid

$x+y=2$
$x+2y=3$
unique solution $x=1, y=1$

$x+y=2$
$2x+2y=3$
no solution (parallel lines)

$x+y=2$
$2x+2y=4$
infinite solution (overlapping lines)

$x+y=0$
intersect one solution $\rightarrow$ trivial, zero solution
homo - geneous linear eqn always have solution, degree = 1

<!-- Page 012 -->
**# solve the system**
$x - 2y - 5z = 2$
$-x + y + 3z = -2$
$2x + y + z = 3$

$\begin{bmatrix} 1 & -2 & -5 & 2 \\ 0 & 1 & -2 & 0 \\ 0 & 0 & 1 & -1 \end{bmatrix} = [A:B]$

from eq 3 we get
$z = -1$

$-y - 2z = 0 \rightarrow y = 2$
$x - 2y - 5z = 2 \rightarrow x = 1$

The unique solution of system is $(x,y,z) = (1, 2, -1)$

$AX = B$
$X = A^{-1}B$
একমাত্র unique solution এর ক্ষেত্রে বের হবে Multiple solution অন্য ক্ষেত্রে এটা অকেজো

**# Find the condition of $\lambda$ so that the system**
$x + y + 3z = 5$
$2x + y - z = 7$
$x + 2y + \lambda z = \mu$

has (i) unique solution (consistent)
(ii) no solution (inconsistent)
(iii) more than one solution (consistent)

**Matrix representations**
$A = \begin{bmatrix} 1 & 1 & 3 \\ 2 & 1 & -1 \\ 1 & 2 & \lambda \end{bmatrix}$, $X = \begin{bmatrix} x \\ y \\ z \end{bmatrix}$, $B = \begin{bmatrix} 5 \\ 7 \\ \mu \end{bmatrix}$
$AX = B$

<!-- Page 013 -->
**augmented matrix / concatenated matrix**
$[A:B] = \begin{bmatrix} 1 & 1 & 3 & 5 \\ 2 & 1 & -1 & 7 \\ 1 & 2 & \lambda & \mu \end{bmatrix}$

$R_2 \rightarrow 2R_1 - R_2$
$R_3 \rightarrow R_1 - R_3$
$\begin{bmatrix} 1 & 1 & 3 & 5 \\ 0 & 1 & 7 & 3 \\ 0 & -1 & 3-\lambda & 5-\mu \end{bmatrix}$

$R_3 \rightarrow R_2 + R_3$
$\begin{bmatrix} 1 & 1 & 3 & 5 \\ 0 & 1 & 7 & 3 \\ 0 & 0 & 10-\lambda & 8-\mu \end{bmatrix}$
which is echelon matrix of $[A:B]$

**Case I**
(i) unique solution
$\text{Rank of } (A) = \text{Rank } [A:B] = \text{number of variables} = 3$
$\therefore 10-\lambda \neq 0 \Rightarrow \lambda \neq 10$

(ii) no solution
$10-\lambda = 0$, This is possible if $8-\mu \neq 0$
$\text{Rank}(A) = 2$
$\text{Rank}[A:B] = 3$

(iii) many solutions
$\text{Rank}(A) = \text{Rank}[A:B] < \text{No of variables}$
~~This is not possible.~~
~~This system has no many solution.~~

<!-- Page 014 -->
**Vector:** A vector is a quantity having both magnitude and direction
such as, displacement, velocity, force, acceleration

**Scalar:** is a quantity having only magnitude but no direction.
such as, mass, length, time, temperature.

**Laws of vector algebra** If $A, B, C$ are vectors and $m, n$ are scalars.
1. commutative law for addition: $A+B = B+A$
2. Associative law for addition: $A+(B+C) = (A+B)+C$
3. commutative law for multiplication: $mA = Am$
4. Associative law for multiplication: $m(nA) = (mn)A$
5. Distributive law
$(m+n)A = mA + nA$
$m(A+B) = mA + mB$

**Unit vector:** vector having unit magnitude. If $A$ is a vector with magnitude $A \neq 0$ then $\vec{A}/A$ is a unit vector having the same direction with $A$.
$a = \frac{\vec{A}}{|\vec{A}|}$

**# Proof that magnitude $A$ of vector $\vec{A} = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}$ is $A = \sqrt{A_1^2 + A_2^2 + A_3^2}$**
By pythagoras theorem, $(\overline{OP})^2 = (\overline{OQ})^2 + (\overline{QP})^2$
$\overline{OP}$ denotes the magnitude of vector $OP$
Similarly, $(\overline{OQ})^2 = (\overline{OR})^2 + (\overline{RQ})^2$
Then, $(\overline{OP})^2 = (\overline{OR})^2 + (\overline{RQ})^2 + (\overline{QP})^2$
$\Rightarrow A^2 = A_1^2 + A_2^2 + A_3^2$
$A = \sqrt{A_1^2 + A_2^2 + A_3^2}$ (proved)

<!-- Page 015 -->
**#** $\vec{r_1} = 2\hat{i} - \hat{j} + \hat{k}$
$\vec{r_2} = \hat{i} + 3\hat{j} - 2\hat{k}$
$\vec{r_3} = -2\hat{i} + \hat{j} - 3\hat{k}$
$\vec{r_4} = 3\hat{i} + 2\hat{j} + 5\hat{k}$
find $a, b, c$, $\vec{r_4} = a\vec{r_1} + b\vec{r_2} + c\vec{r_3}$
$\vec{r_4} = a(2\hat{i} - \hat{j} + \hat{k}) + b(\hat{i} + 3\hat{j} - 2\hat{k}) + c(-2\hat{i} + \hat{j} - 3\hat{k})$
$\Rightarrow 3\hat{i} + 2\hat{j} + 5\hat{k} = \hat{i}(2a+b-2c) + \hat{j}(-a+3b+c) + \hat{k}(a-2b-3c)$

$2a+b-2c = 3$
$-a+3b+c = 2$
$a-2b-3c = 5$
$a = -2$
$b = 1$
$c = -3$

**Dot or scalar product**
$\vec{A} \cdot \vec{B} = AB\cos\theta$
1. $\vec{A} \cdot \vec{B} = \vec{B} \cdot \vec{A}$ (commutative law)
2. $\vec{A} \cdot (\vec{B} + \vec{C}) = \vec{A} \cdot \vec{B} + \vec{A} \cdot \vec{C}$ (distributive law)
3. $m(\vec{A} \cdot \vec{B}) = (m\vec{A}) \cdot \vec{B} = \vec{A} \cdot (m\vec{B}) = (\vec{A} \cdot \vec{B})m$ ($m$ scalar)
4. $\hat{i} \cdot \hat{i} = \hat{j} \cdot \hat{j} = \hat{k} \cdot \hat{k} = 1$
$\hat{i} \cdot \hat{j} = \hat{j} \cdot \hat{k} = \hat{k} \cdot \hat{i} = 0$
5. $\vec{A} = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}$
$\vec{B} = B_1\hat{i} + B_2\hat{j} + B_3\hat{k}$
$\vec{A} \cdot \vec{B} = A_1 B_1 + A_2 B_2 + A_3 B_3$
$\vec{A} \cdot \vec{A} = A^2 = A_1^2 + A_2^2 + A_3^2$
$\vec{B} \cdot \vec{B} = B^2 = B_1^2 + B_2^2 + B_3^2$
6. $\vec{A} \cdot \vec{B} = 0$ and $\vec{A}, \vec{B}$ are not NULL vectors, then $A$ and $B$ are perpendicular

**Cross or vector product**
$\vec{A} \times \vec{B} = AB\sin\theta \hat{u}$ ($\hat{u}$ = unit vector indicating direction of $\vec{A} \times \vec{B}$)
1. $\vec{A} \times \vec{B} = -\vec{B} \times \vec{A}$ (commutative law)
2. $\vec{A} \times (\vec{B} + \vec{C}) = \vec{A} \times \vec{B} + \vec{A} \times \vec{C}$ (Distributive law)
3. $m(\vec{A} \times \vec{B}) = (m\vec{A}) \times \vec{B} = \vec{A} \times (m\vec{B}) = (\vec{A} \times \vec{B})m$ ($m$ scalar)
4. $\hat{i} \times \hat{i} = \hat{j} \times \hat{j} = \hat{k} \times \hat{k} = 0$
$\hat{i} \times \hat{j} = \hat{k}, \hat{j} \times \hat{k} = \hat{i}, \hat{k} \times \hat{i} = \hat{j}$
5. $\vec{A} \times \vec{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ A_1 & A_2 & A_3 \\ B_1 & B_2 & B_3 \end{vmatrix}$
6. $\vec{A} \times \vec{B} = 0$, $A$ and $B$ are not NULL, then $A$ and $B$ are parallel.
7. The magnitude of $\vec{A} \times \vec{B}$ is the same area of parallelogram with sides $A$ and $B$.

<!-- Page 016 -->
**Triple product:**
1. $(\vec{A} \cdot \vec{B})\vec{C} \neq \vec{A}(\vec{B} \cdot \vec{C})$
2. $\vec{A} \cdot (\vec{B} \times \vec{C}) = \vec{B} \cdot (\vec{C} \times \vec{A}) = \vec{C} \cdot (\vec{A} \times \vec{B})$
$\vec{A} \cdot (\vec{B} \times \vec{C}) = \begin{vmatrix} A_1 & A_2 & A_3 \\ B_1 & B_2 & B_3 \\ C_1 & C_2 & C_3 \end{vmatrix}$
3. $\vec{A} \times (\vec{B} \times \vec{C}) \neq (\vec{A} \times \vec{B}) \times \vec{C}$
4. $\vec{A} \times (\vec{B} \times \vec{C}) = (\vec{A} \cdot \vec{C})\vec{B} - (\vec{A} \cdot \vec{B})\vec{C}$
$(\vec{A} \times \vec{B}) \times \vec{C} = (\vec{A} \cdot \vec{C})\vec{B} - (\vec{B} \cdot \vec{C})\vec{A}$

$\vec{A} \cdot (\vec{B} \times \vec{C}) = \text{scalar triple product / box product } [ABC]$
$\vec{A} \times (\vec{B} \times \vec{C}) = \text{vector triple product}$

**# prove $\vec{A} = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}$, $A = \sqrt{\vec{A} \cdot \vec{A}} = \sqrt{A_1^2 + A_2^2 + A_3^2}$**
$\vec{A} \cdot \vec{A} = AA\cos 0^\circ = A^2 \Rightarrow A = \sqrt{\vec{A} \cdot \vec{A}}$
$\vec{A} \cdot \vec{A} = (A_1\hat{i} + A_2\hat{j} + A_3\hat{k}) \cdot (A_1\hat{i} + A_2\hat{j} + A_3\hat{k}) = A_1^2 + A_2^2 + A_3^2$
$A = \sqrt{\vec{A} \cdot \vec{A}} = \sqrt{A_1^2 + A_2^2 + A_3^2}$

**# $\vec{A} = 2\hat{i} + 2\hat{j} - \hat{k}$**
$\vec{B} = 6\hat{i} - 3\hat{j} + 2\hat{k}$
find angle
$A = \sqrt{2^2 + 2^2 + (-1)^2} = 3$
$B = \sqrt{6^2 + (-3)^2 + 2^2} = 7$
$AB = 21$
$\vec{A} \cdot \vec{B} = AB\cos\theta \Rightarrow \theta = \cos^{-1}\left(\frac{\vec{A} \cdot \vec{B}}{AB}\right) = \cos^{-1}\left(\frac{12 - 6 - 2}{21}\right) = 79.01^\circ$

**# $\vec{A} = 3\hat{i} - 6\hat{j} + 2\hat{k}$ angles of axis.**
let $\alpha, \beta, \gamma$ are the angles $A$ makes with the $x, y, z$ axis.
$\vec{A} \cdot \hat{i} = (A)(1)\cos\alpha = \sqrt{3^2 + (-6)^2 + 2^2}\cos\alpha = 7\cos\alpha$
$\vec{A} \cdot \hat{i} = (3\hat{i} - 6\hat{j} + 2\hat{k}) \cdot \hat{i} = 3 - 0 - 0 = 3$
$\alpha = \cos^{-1}\frac{\vec{A} \cdot \hat{i}}{|A||\hat{i}|} = \cos^{-1}\left(\frac{3}{7}\right) = 64.6^\circ$
$\beta = \cos^{-1}\left(\frac{-6}{7}\right) = 149^\circ$
$\gamma = \cos^{-1}\left(\frac{2}{7}\right) = 73.4^\circ$

$\cos^{-1}\left(\frac{\text{যার সাথে angle তার সহগ}}{|A|}\right)$


<!-- Page 017 -->
**# Find projection of $\vec{A} = \hat{i} - 2\hat{j} + \hat{k}$ on vector $\vec{B} = 4\hat{i} - 4\hat{j} + 7\hat{k}$**
$\frac{\vec{A} \cdot \vec{B}}{|\vec{B}|} = \frac{4 + 8 + 7}{\sqrt{4^2 + (-4)^2 + 7^2}} = \frac{19}{9}$

**# Find a unit vector perpendicular to the plane of $A = 2\hat{i} - 6\hat{j} - 3\hat{k}$ and $B = 4\hat{i} + 3\hat{j} - \hat{k}$**
let $\vec{c} = x\hat{i} + y\hat{j} + z\hat{k}$
then, it is perpendicular to $A$ and $B$
$C \cdot A = 2x - 6y - 3z = 0 \Rightarrow 2x - 6y = 3z$
$C \cdot B = 4x + 3y - z = 0 \Rightarrow 4x + 3y = z$

$x = \frac{1}{2}z$
$y = -\frac{1}{3}z$
$\vec{c} = z\left(\frac{1}{2}\hat{i} - \frac{1}{3}\hat{j} + \hat{k}\right)$
$\frac{\vec{c}}{c} = \frac{z\left(\frac{1}{2}\hat{i} - \frac{1}{3}\hat{j} + \hat{k}\right)}{\sqrt{z^2\left(\left(\frac{1}{2}\right)^2 + \left(-\frac{1}{3}\right)^2 + 1^2\right)}} = \pm \left(\frac{3}{7}\hat{i} - \frac{2}{7}\hat{j} + \frac{6}{7}\hat{k}\right)$

**Ordinary derivatives of vectors**
$\frac{\Delta R}{\Delta u} = \frac{R(u + \Delta u) - R(u)}{\Delta u}$
$\frac{dR}{du} = \lim_{\Delta u \to 0} \frac{\Delta R}{\Delta u} = \lim_{\Delta u \to 0} \frac{R(u + \Delta u) - R(u)}{\Delta u}$

space curve:
$R(u) = x(u)\hat{i} + y(u)\hat{j} + z(u)\hat{k}$
$\frac{dR}{du} = \frac{dx}{du}\hat{i} + \frac{dy}{du}\hat{j} + \frac{dz}{du}\hat{k}$

<!-- Page 018 -->
**differentiation formulas:**
1. $\frac{d}{du}(A+B) = \frac{dA}{du} + \frac{dB}{du}$
2. $\frac{d}{du}(A \cdot B) = A \cdot \frac{dB}{du} + \frac{dA}{du} \cdot B$
3. $\frac{d}{du}(A \times B) = A \times \frac{dB}{du} + \frac{dA}{du} \times B$
4. $\frac{d}{du}(\phi A) = \phi \frac{dA}{du} + \frac{d\phi}{du} A$
5. $\frac{d}{du}(A \cdot B \times C) = A \cdot B \times \frac{dC}{du} + A \cdot \frac{dB}{du} \times C + \frac{dA}{du} \cdot B \times C$
6. $\frac{d}{du}(A \times (B \times C)) = A \times (B \times \frac{dC}{du}) + A \times (\frac{dB}{du} \times C) + \frac{dA}{du} \times (B \times C)$

$A, B, C$ are differentiable vector functions of a scalar $u$, and $\phi$ is a differentiable scalar function of $u$.

**Partial derivatives of vectors:**
1. $\frac{\partial A}{\partial x} = \lim_{\Delta x \to 0} \frac{A(x+\Delta x, y, z) - A(x, y, z)}{\Delta x}$
2. $\frac{\partial A}{\partial y} = \lim_{\Delta y \to 0} \frac{A(x, y+\Delta y, z) - A(x, y, z)}{\Delta y}$
3. $\frac{\partial A}{\partial z} = \lim_{\Delta z \to 0} \frac{A(x, y, z+\Delta z) - A(x, y, z)}{\Delta z}$
4. $\frac{\partial}{\partial x}(A \cdot B) = A \cdot \frac{\partial B}{\partial x} + \frac{\partial A}{\partial x} \cdot B$
5. $\frac{\partial}{\partial x}(A \times B) = A \times \frac{\partial B}{\partial x} + \frac{\partial A}{\partial x} \times B$
6. $\frac{\partial^2}{\partial y \partial x}(A \cdot B) = \frac{\partial}{\partial y}\left(\frac{\partial}{\partial x}(A \cdot B)\right) = \dots$

<!-- Page 019 -->
**Differentials of vectors:**
1. $A = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}$ then $dA = dA_1\hat{i} + dA_2\hat{j} + dA_3\hat{k}$
2. $d(A \cdot B) = A \cdot dB + dA \cdot B$
3. $d(A \times B) = A \times dB + dA \times B$
4. $A = A(x,y,z)$ then $dA = \frac{\partial A}{\partial x}dx + \frac{\partial A}{\partial y}dy + \frac{\partial A}{\partial z}dz$

**Differential geometry:**
$\frac{dr}{du}$ is a vector in direction of the tangent
$\frac{dr}{ds}$ is a unit tangent vector $T$
$N$ is a principal normal
$B$ is called the binormal $B = T \times N$

Frenet-Serret formula:
$\frac{dT}{ds} = kN$
$\frac{dN}{ds} = \tau B - kT$
$\frac{dB}{ds} = -\tau N$

$k = \text{curvature}$
$\tau = \text{torsion}$
$\sigma = \frac{1}{\tau}$

$T = \frac{\frac{dr}{dt}}{\left|\frac{dr}{dt}\right|} = \frac{dr}{dt} / \frac{ds}{dt} = \frac{dr}{ds}$

**# $R(u) = x(u)\hat{i} + y(u)\hat{j} + z(u)\hat{k}$ prove $\frac{dR}{du} = \frac{dx}{du}\hat{i} + \frac{dy}{du}\hat{j} + \frac{dz}{du}\hat{k}$**
$\frac{dR}{du} = \lim_{\Delta u \to 0} \frac{R(u+\Delta u) - R(u)}{\Delta u}$

<!-- Page 020 -->
$= \lim_{\Delta u \to 0} \frac{[x(u+\Delta u)\hat{i} + y(u+\Delta u)\hat{j} + z(u+\Delta u)\hat{k}] - [x(u)\hat{i} + y(u)\hat{j} + z(u)\hat{k}]}{\Delta u}$
$= \lim_{\Delta u \to 0} \frac{x(u+\Delta u) - x(u)}{\Delta u}\hat{i} + \frac{y(u+\Delta u) - y(u)}{\Delta u}\hat{j} + \frac{z(u+\Delta u) - z(u)}{\Delta u}\hat{k}$
$= \frac{dx}{du}\hat{i} + \frac{dy}{du}\hat{j} + \frac{dz}{du}\hat{k}$

**# $R = \sin t \hat{i} + \cos t \hat{j} + t \hat{k}$**
find (a) $\frac{dR}{dt}$ (b) $\frac{d^2R}{dt^2}$ (c) $\left|\frac{dR}{dt}\right|$ (d) $\left|\frac{d^2R}{dt^2}\right|$
(a) $\frac{dR}{dt} = \frac{d}{dt}(\sin t)\hat{i} + \frac{d}{dt}(\cos t)\hat{j} + \frac{d}{dt}(t)\hat{k} = \cos t \hat{i} - \sin t \hat{j} + \hat{k}$
(b) $\frac{d^2R}{dt^2} = \frac{d}{dt}\left(\frac{dR}{dt}\right) = \frac{d}{dt}(\cos t)\hat{i} - \frac{d}{dt}(\sin t)\hat{j} + \frac{d}{dt}(1)\hat{k} = -\sin t \hat{i} - \cos t \hat{j}$
(c) $\left|\frac{dR}{dt}\right| = \sqrt{\cos^2 t + (-\sin t)^2 + 1^2} = \sqrt{2}$
(d) $\left|\frac{d^2R}{dt^2}\right| = \sqrt{(-\sin t)^2 + (-\cos t)^2} = 1$

**# $x = e^{-t}, y = 2\cos 3t, z = 2\sin 3t$**
velocity and acceleration magnitudes at $t=0$
$R = e^{-t}\hat{i} + 2\cos 3t \hat{j} + 2\sin 3t \hat{k}$
$V = \frac{dR}{dt} = -e^{-t}\hat{i} - 6\sin 3t \hat{j} + 6\cos 3t \hat{k}$
$a = \frac{dV}{dt} = e^{-t}\hat{i} - 18\cos 3t \hat{j} - 18\sin 3t \hat{k}$

at $t=0$:
$V = -\hat{i} + 6\hat{k}$, $|V| = \sqrt{1^2 + 6^2} = \sqrt{37}$
$a = \hat{i} - 18\hat{j}$, $|a| = \sqrt{1^2 + (-18)^2} = \sqrt{325}$
