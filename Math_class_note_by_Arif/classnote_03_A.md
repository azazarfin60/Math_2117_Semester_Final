<!-- Page 021 -->
**# It moves along curve $x = 2t^2$, $y = t^2-4t$, $z = 3t-5$. Find components of its velocity and acceleration at $t = 1$ in direction $\hat{i}-3\hat{j}+2\hat{k}$**

$r = 2t^2\hat{i} + (t^2-4t)\hat{j} + (3t-5)\hat{k}$

$v = \frac{dr}{dt} = 4t\hat{i} + (2t-4)\hat{j} + 3\hat{k}$
$a = \frac{dv}{dt} = 4\hat{i} + 2\hat{j}$

at $t = 1$:
$v = 4\hat{i} - 2\hat{j} + 3\hat{k}$
$a = 4\hat{i} + 2\hat{j}$

Unit vector in direction $\hat{i}-3\hat{j}+2\hat{k}$ is:
$\frac{\hat{i}-3\hat{j}+2\hat{k}}{\sqrt{1^2 + (-3)^2 + 2^2}} = \frac{\hat{i}-3\hat{j}+2\hat{k}}{\sqrt{14}}$

components of velocity:
$\frac{(4\hat{i}-2\hat{j}+3\hat{k}) \cdot (\hat{i}-3\hat{j}+2\hat{k})}{\sqrt{14}} = \frac{4+6+6}{\sqrt{14}} = \frac{16}{\sqrt{14}}$

components of acceleration:
$\frac{(4\hat{i}+2\hat{j}) \cdot (\hat{i}-3\hat{j}+2\hat{k})}{\sqrt{14}} = \frac{4-6}{\sqrt{14}} = -\frac{2}{\sqrt{14}}$

**# unit tangent vector $x = t^2+1, y = 4t-3, z = 2t^2-6t$, and at $t = 2$**

$R = (t^2+1)\hat{i} + (4t-3)\hat{j} + (2t^2-6t)\hat{k}$

$\frac{dr}{dt} = 2t\hat{i} + 4\hat{j} + (4t-6)\hat{k}$

$T = \frac{dr/dt}{|dr/dt|} = \frac{2t\hat{i} + 4\hat{j} + (4t-6)\hat{k}}{\sqrt{(2t)^2 + 4^2 + (4t-6)^2}}$

at $t = 2$:
$T = \frac{4\hat{i} + 4\hat{j} + 2\hat{k}}{\sqrt{4^2 + 4^2 + 2^2}} = \frac{4\hat{i} + 4\hat{j} + 2\hat{k}}{6} = \frac{2}{3}\hat{i} + \frac{2}{3}\hat{j} + \frac{1}{3}\hat{k}$

**# IF A has a constant magnitude show that A and dA/dt are perpendicular provided $|dA/dt| \neq 0$**

$A$ has a constant magnitude, $A \cdot A = \text{constant}$

$\frac{d}{dt}(A \cdot A) = A \cdot \frac{dA}{dt} + \frac{dA}{dt} \cdot A = 0$
$\Rightarrow 2 A \cdot \frac{dA}{dt} = 0 \Rightarrow A \cdot \frac{dA}{dt} = 0$

Thus, $A \cdot \frac{dA}{dt} = 0$ and $A$ is perpendicular to $\frac{dA}{dt}$ provided $\left|\frac{dA}{dt}\right| \neq 0$.

<!-- Page 022 -->
**# show $\vec{A} \cdot \frac{d\vec{A}}{dt} = A \frac{dA}{dt}$**

$\vec{A} = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}$
$A = \sqrt{A_1^2 + A_2^2 + A_3^2}$

$\frac{dA}{dt} = \frac{1}{2}(A_1^2 + A_2^2 + A_3^2)^{-1/2} \left(2A_1\frac{dA_1}{dt} + 2A_2\frac{dA_2}{dt} + 2A_3\frac{dA_3}{dt}\right)$
$\frac{dA}{dt} = \frac{A_1\frac{dA_1}{dt} + A_2\frac{dA_2}{dt} + A_3\frac{dA_3}{dt}}{(A_1^2 + A_2^2 + A_3^2)^{1/2}} = \frac{\vec{A} \cdot \frac{d\vec{A}}{dt}}{A}$
$\Rightarrow A \frac{dA}{dt} = \vec{A} \cdot \frac{d\vec{A}}{dt}$

**# $\phi(x,y,z) = xy^2z$, $A = xz\hat{i} - xy^2\hat{j} + yz^2\hat{k}$, find $\frac{\partial^3}{\partial x^2 \partial z}(\phi A)$ at $(2, -1, 1)$**

$\phi A = x^2 y^2 z^2 \hat{i} - x^2 y^4 z \hat{j} + x y^3 z^3 \hat{k}$

$\frac{\partial}{\partial z}(\phi A) = 2x^2 y^2 z \hat{i} - x^2 y^4 \hat{j} + 3x y^3 z^2 \hat{k}$

$\frac{\partial^2}{\partial x \partial z}(\phi A) = 4x y^2 z \hat{i} - 2x y^4 \hat{j} + 3 y^3 z^2 \hat{k}$

$\frac{\partial^3}{\partial x^2 \partial z}(\phi A) = 4 y^2 z \hat{i} - 2 y^4 \hat{j}$

at $(2, -1, 1)$:
$\frac{\partial^3}{\partial x^2 \partial z}(\phi A) = 4(-1)^2(1)\hat{i} - 2(-1)^4\hat{j} = 4\hat{i} - 2\hat{j}$

~~**# prove Frenet-Serret formulas**~~
since $T \cdot T = 1$, $T \cdot \frac{dT}{ds} = 0$, $\frac{dT}{ds}$ perpendicular to $T$
$N$ unit
$\frac{dT}{ds} = kN$
$\frac{dB}{ds} = -\tau N$
$\frac{dN}{ds} = \tau B - kT$

**# $x = 3\cos t$, $y = 3\sin t$, $z = 4t$**
(a) unit tangent $T$
(b) principal normal $N$, curvature $K$, radius of curvature $\rho = 1/k$
(c) binormal $B$, torsion $\tau$, radius of torsion $\sigma = 1/\tau$

(a)
$R = 3\cos t \hat{i} + 3\sin t \hat{j} + 4t\hat{k}$
$\frac{dR}{dt} = -3\sin t \hat{i} + 3\cos t \hat{j} + 4\hat{k}$
$\left|\frac{dR}{dt}\right| = 5$
$T = \frac{dr/dt}{|dr/dt|} = -\frac{3}{5}\sin t \hat{i} + \frac{3}{5}\cos t \hat{j} + \frac{4}{5}\hat{k}$

<!-- Page 023 -->
(b)
$\frac{dT}{dt} = \frac{d}{dt}\left(-\frac{3}{5}\sin t\right)\hat{i} + \frac{d}{dt}\left(\frac{3}{5}\cos t\right)\hat{j} + 0 = -\frac{3}{5}\cos t \hat{i} - \frac{3}{5}\sin t \hat{j}$

$\frac{dT}{ds} = \frac{dT}{dt} / \frac{ds}{dt} = \frac{dT}{dt} / \left|\frac{dr}{dt}\right| = \frac{dT/dt}{5} = -\frac{3}{25}\cos t \hat{i} - \frac{3}{25}\sin t \hat{j}$

$\frac{dT}{ds} = kN$
$\left|\frac{dT}{ds}\right| = |k||N| = k \quad (k \geq 0)$

$k = \left|\frac{dT}{ds}\right| = \sqrt{\left(-\frac{3}{25}\cos t\right)^2 + \left(-\frac{3}{25}\sin t\right)^2} = \frac{3}{25}$
$\rho = \frac{1}{k} = \frac{25}{3}$

$\frac{dT}{ds} = kN \Rightarrow N = \frac{1}{k}\frac{dT}{ds} = \frac{25}{3}\left(-\frac{3}{25}\cos t \hat{i} - \frac{3}{25}\sin t \hat{j}\right) = -\cos t \hat{i} - \sin t \hat{j}$

(c)
$B = T \times N = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ -\frac{3}{5}\sin t & \frac{3}{5}\cos t & \frac{4}{5} \\ -\cos t & -\sin t & 0 \end{vmatrix} = \frac{4}{5}\sin t \hat{i} - \frac{4}{5}\cos t \hat{j} + \frac{3}{5}\hat{k}$

$\frac{dB}{dt} = \frac{4}{5}\cos t \hat{i} + \frac{4}{5}\sin t \hat{j}$
$\frac{dB}{ds} = \frac{dB/dt}{|dr/dt|} = \frac{4}{25}\cos t \hat{i} + \frac{4}{25}\sin t \hat{j}$

$-\tau N = -\tau (-\cos t \hat{i} - \sin t \hat{j}) = \frac{4}{25}\cos t \hat{i} + \frac{4}{25}\sin t \hat{j}$
$\Rightarrow \tau = \frac{4}{25}$
$\sigma = \frac{1}{\tau} = \frac{25}{4}$

<!-- Page 024 -->
**# $x = t$, $y = t^2$, $z = \frac{2}{3}t^3$**
(a) curvature
(b) torsion

$r = t\hat{i} + t^2\hat{j} + \frac{2}{3}t^3\hat{k}$
$\frac{dr}{dt} = \hat{i} + 2t\hat{j} + 2t^2\hat{k}$

(a)
$\frac{ds}{dt} = \left|\frac{dr}{dt}\right| = \sqrt{1^2 + (2t)^2 + (2t^2)^2} = \sqrt{1+4t^2+4t^4} = 1+2t^2$

$T = \frac{dr/dt}{ds/dt} = \frac{\hat{i} + 2t\hat{j} + 2t^2\hat{k}}{1+2t^2}$

$\frac{dT}{dt} = \frac{(1+2t^2)(2\hat{j} + 4t\hat{k}) - (\hat{i} + 2t\hat{j} + 2t^2\hat{k})(4t)}{(1+2t^2)^2} = \frac{-4t\hat{i} + (2-4t^2)\hat{j} + 4t\hat{k}}{(1+2t^2)^2}$

$\frac{dT}{ds} = \frac{dT/dt}{ds/dt} = \frac{-4t\hat{i} + (2-4t^2)\hat{j} + 4t\hat{k}}{(1+2t^2)^3}$

$\left|\frac{dT}{ds}\right| = |k||N| = k = \sqrt{\frac{(-4t)^2 + (2-4t^2)^2 + (4t)^2}{(1+2t^2)^6}} = \frac{2}{(1+2t^2)^2}$
$\rho = \frac{1}{k} = \frac{(1+2t^2)^2}{2}$

(b)
$N = \frac{1}{k}\frac{dT}{ds} = \frac{-2t\hat{i} + (1-2t^2)\hat{j} + 2t\hat{k}}{1+2t^2}$

$B = T \times N = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \frac{1}{1+2t^2} & \frac{2t}{1+2t^2} & \frac{2t^2}{1+2t^2} \\ \frac{-2t}{1+2t^2} & \frac{1-2t^2}{1+2t^2} & \frac{2t}{1+2t^2} \end{vmatrix} = \frac{2t^2\hat{i} - 2t\hat{j} + \hat{k}}{1+2t^2}$

$\frac{dB}{ds} = \frac{dB/dt}{ds/dt} = \frac{4t\hat{i} + (4t^2-2)\hat{j} - 4t\hat{k}}{(1+2t^2)^3}$
$-\tau N = \frac{4t\hat{i} + (4t^2-2)\hat{j} - 4t\hat{k}}{(1+2t^2)^3}$
$\Rightarrow \tau = \frac{2}{(1+2t^2)^2} = k \text{ for this curve}$

<!-- Page 025 -->
<div align="right"><b>03-01-2026</b></div>

<b>Class 14 | sir</b>

**Inverse of a square matrix** (by matrix method)
said to be inverse matrix, $AB = BA = I$
inverse matrix is unique.
$A, B$ must be Non-Singular ($|A| \neq 0$) or Invertible matrix.
$I = \text{identity matrix}$
$A, B$ একে অপরের inverse

$A = \begin{bmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{bmatrix}$

$|A| = 3 \neq 0 \text{ [non-singular]}$
thus the matrix is non-singular, hence inverse exist.

Using only elementary row operation:
$A = AI$
$= \begin{bmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$
এটিকে identity matrix বানালে এটা inverse হবে
convert to echelon form

$R_2 \rightarrow R_1 + R_2$
$R_3 \rightarrow R_1 - R_3$
$\begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 7 \\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ 1 & 0 & -1 \end{bmatrix}$

$R_3 \rightarrow R_2 - 4R_3$
$\begin{bmatrix} 1 & 2 & 3 \\ 0 & 4 & 7 \\ 0 & 0 & 3 \end{bmatrix} \begin{bmatrix} 1 & 0 & 0 \\ 1 & 1 & 0 \\ -3 & 1 & 4 \end{bmatrix}$

$R_1 \rightarrow 2R_1 - R_2$
$\begin{bmatrix} 2 & 0 & -1 \\ 0 & 4 & 7 \\ 0 & 0 & 3 \end{bmatrix} \begin{bmatrix} 1 & -1 & 0 \\ 1 & 1 & 0 \\ -3 & 1 & 4 \end{bmatrix}$

$R_1 \rightarrow 3R_1 + R_3$
$R_2 \rightarrow 3R_2 - 7R_3$
$\begin{bmatrix} 6 & 0 & 0 \\ 0 & 12 & 0 \\ 0 & 0 & 3 \end{bmatrix} \begin{bmatrix} 0 & -2 & 4 \\ 24 & -4 & -28 \\ -3 & 1 & 4 \end{bmatrix}$

<!-- Page 026 -->
$R_1 \rightarrow \frac{1}{6}R_1$
$R_2 \rightarrow \frac{1}{12}R_2$
$R_3 \rightarrow \frac{1}{3}R_3$
$\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 0 & -\frac{1}{3} & \frac{2}{3} \\ 2 & -\frac{1}{3} & -\frac{7}{3} \\ -1 & \frac{1}{3} & \frac{4}{3} \end{bmatrix}$

Thus the inverse of matrix $A$, $A^{-1} = \begin{bmatrix} 0 & -\frac{1}{3} & \frac{2}{3} \\ 2 & -\frac{1}{3} & -\frac{7}{3} \\ -1 & \frac{1}{3} & \frac{4}{3} \end{bmatrix}$

**Justification:**
$A A^{-1} = I$
$= \begin{bmatrix} 1 & 2 & 3 \\ -1 & 2 & 4 \\ 1 & 1 & 2 \end{bmatrix} \begin{bmatrix} 0 & -\frac{1}{3} & \frac{2}{3} \\ 2 & -\frac{1}{3} & -\frac{7}{3} \\ -1 & \frac{1}{3} & \frac{4}{3} \end{bmatrix} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$

* আসতে পারে
- কোড থাকলে সেইভাবে করা লাগবে
message decode / encode
-> Ascii value pattern / sequence দিয়ে করা যাবে

KILL HIM
K for 11
I for 9
L for 12
H for 8
M for 13

Now we construct the matrix with the message as,
$B = \begin{bmatrix} 11 & 9 & 12 & 12 \\ 8 & 9 & 13 & 0 \end{bmatrix}$
or, $B = \begin{bmatrix} 11 & 9 & 12 & 12 & 0 & 8 & 9 & 13 \end{bmatrix}$

we now take the preferable $2 \times 2$ matrix as $A = \begin{bmatrix} 1 & 2 \\ -1 & 1 \end{bmatrix}$ (always square)
with inverse $A^{-1} = \frac{1}{3}\begin{bmatrix} 1 & -2 \\ 1 & 1 \end{bmatrix}$ (inverse exist না করলে নেওয়া যাবে না)

**Encoded matrix:**
$I_C = \begin{bmatrix} 1 & 2 \\ -1 & 1 \end{bmatrix} \begin{bmatrix} 11 & 9 & 12 & 12 \\ 8 & 9 & 13 & 0 \end{bmatrix} = \begin{bmatrix} 27 & 27 & 38 & 12 \\ -3 & 0 & 1 & -12 \end{bmatrix}$

<!-- Page 027 -->
**Decoded matrix:**
$A^{-1} (I_C) = \frac{1}{3}\begin{bmatrix} 1 & -2 \\ 1 & 1 \end{bmatrix} \begin{bmatrix} 27 & 27 & 38 & 12 \\ -3 & 0 & 1 & -12 \end{bmatrix} = \begin{bmatrix} 11 & 9 & 12 & 12 \\ 8 & 9 & 13 & 0 \end{bmatrix}$

**# Dependent নাকি independent**
rank-3 হলে independent কম হলে dependent

$\hat{i} + 2\hat{j} + 3\hat{k}$
$\hat{i} + 2\hat{j} + \hat{k}$
$\hat{i} + \hat{j} + \hat{k}$

$\begin{pmatrix} 1 & 2 & 3 \\ 1 & 2 & 1 \\ 1 & 1 & 1 \end{pmatrix} - \text{rank-3 = independent}$
$\begin{pmatrix} 1 & 2 & 3 \\ 1 & 2 & 1 \\ 0 & 0 & 0 \end{pmatrix} - \text{dependent}$

<!-- Page 028 -->
**Practice**

**Matrix:** is a rectangular array of elements arranged in rows and columns used to represent linear relations and linear transformations.

**# Use of matrix**
- Solving systems of linear equations
- study vector spaces
- Eigenvalue problems
- Canonical forms
- data encrypt decrypt

**Augmented matrix:** is a matrix formed by appending the column/row of constants of a linear equations to the coefficient matrix.

**# Why we need to study symmetric matrices?**
1. represents self-adjoint linear operators, which have special and well behaved properties.
2. Every symmetric matrix has only real eigenvalues, which simplifies both theory and analysis.
3. can always be diagonalized by an orthogonal matrix, making computation and proof cleaner.
4. Symmetric matrix correspond to linear transformations that preserve angles under suitable bases.
5. many optimization problems depend on symmetric matrix.

**Symmetric matrix:** a square matrix that satisfies $A^T = A$
**Skew Symmetric matrix:** a square matrix that satisfies $A^T = -A$
- main diagonal must be zero.

<!-- Page 029 -->
**Trisis/Tridiagonal matrix:** is a square matrix in which non-zero elements occur only on the main, super, sub diagonals.

**# use of Trisis matrix:**
1. Solving linear systems efficiently
2. Modeling difference equations
3. Numerical solutions of differential equations
4. Eigenvalue computations
5. sparse system computation

**# Importance:**
1. Computational efficiency
2. Stability analysis
3. Simplifies matrix factorization

**Echelon matrix:** If in a matrix the number of zeroes preceding the first non zero entry increases row by row then it is called Echelon matrix.

**Purpose:**
1. simplifies solving linear equations
2. Reveals rank of a matrix
3. Determines the checking of solution

**Rank of the matrix:** number of non-zero rows/column in echelon form.

**Trivial solutions:** In the context of homogenous system of linear eqn $Ax = 0$, the trivial solution is the solution where all the variables are zero, $x = 0$.

<!-- Page 030 -->
<div align="right"><b>06-01-26</b></div>

<b>Class 15 | mam</b>
Page - Pdf - 100, book - 93
(15) Proof আসতে পারে।
(14) (16)

---

<div align="right"><b>10-01-26</b></div>

<b>Class 16 | sir</b>

**# Every square matrix can be written as the sum of a symmetric matrix and a skew symmetric matrix.**

Let, $A$ be a square matrix.
Then, $A = \frac{1}{2}(A+A^T) + \frac{1}{2}(A-A^T)$
$A = B + C$ where $B = \frac{1}{2}(A+A^T)$ and $C = \frac{1}{2}(A-A^T)$

$B^T = \left[\frac{1}{2}(A+A^T)\right]^T$
$= \frac{1}{2}(A+A^T)^T$
$= \frac{1}{2}(A^T + (A^T)^T)$
$= \frac{1}{2}(A^T + A)$
$B^T = \frac{1}{2}(A+A^T)$
$\boxed{B^T = B}$
Hence, $B$ is a symmetric matrix.

$C^T = \left[\frac{1}{2}(A-A^T)\right]^T$
$= \frac{1}{2}(A-A^T)^T$
$= \frac{1}{2}(A^T - A)$
$= -\frac{1}{2}(A-A^T)$
$\boxed{C^T = -C}$
Hence, $C$ is a skew symmetric matrix.

This representation is unique.
Thus every square matrix can be written as the sum of a symmetric and a skew symmetric matrix. (proved)