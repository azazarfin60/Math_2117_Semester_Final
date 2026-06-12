<!-- Page 001 -->
<div align="right"><b>08-11-23</b></div>

<b>Class 1 | Sir</b>
<b>Dr. Gourav Chandra Das</b>
Prof. of math
RU
`gcpaul@ru.ac.bd`

<b>necessary of linear algebra</b>
- linear eqns
- scanning images (image processing)
- matrices

Eigen values and eigen vectors
- use of matrix / matrix presentation.

### Matrix & linear algebra

**Matrix definition**
- square/rectangular form
- either real/complex
- information should be collected from field

**real number:** number that can be placed on real axis.
**complex:** $2 + 3i \rightarrow (2,3)$

$m \times n$ matrix
$m = \text{row}$
$n = \text{column}$

**square matrix:** equal number of rows and columns. very easy to use.
$A+B, A-B$ if both are same.

$$
A =
\begin{bmatrix}
2 & 3 \\
4 & 5
\end{bmatrix}_{2 \times 2}
$$

$$
B =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6
\end{bmatrix}_{2 \times 3}
$$

$$
[A : B] =
\begin{bmatrix}
2 & 3 & 1 & 2 & 3 \\
4 & 5 & 4 & 5 & 6
\end{bmatrix}
$$

(horizontal concatenation)

$$
A =
\begin{bmatrix}
1 & 2 \\
4 & 5
\end{bmatrix}_{2 \times 2}
$$

$$
B =
\begin{bmatrix}
1 & 2 \\
3 & 4 \\
5 & 6
\end{bmatrix}_{3 \times 2}
$$

$$
\begin{bmatrix}
A \\
B
\end{bmatrix} = \begin{bmatrix} 1 & 2 \\ 4 & 5 \\ 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix}
$$

(vertical concat)

$$
A^T = A
$$

<!-- Page 002 -->
<div align="right"><b>[Upside Down Text Transcribed]</b></div>

**in general**
$A + B = B + A$
commutative law doesn't satisfy $AB \neq BA$
$A - B \neq B - A$

$A \times B \quad m \times n \quad n \times p$

**n-square matrix:**

$$
A^2 = A \times A
$$

, $A^3 \neq A^n$

**Why do we need to study symmetric matrix?**

**skew symmetric:**

$$
A^T = -A
$$

, main diagonal must zero
**antisymmetric:** $A^T \neq A$

$$
A =
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
$$

$$
A^T =
\begin{bmatrix}
a & d & g \\
b & e & h \\
c & f & i
\end{bmatrix}
$$

**Trisis matrix / Tridiagonal matrix**

$$
A =
\begin{bmatrix}
a & b & 0 \\
c & d & e \\
0 & f & g
\end{bmatrix}
$$

$\rightarrow$ super diagonal
$\rightarrow$ main diagonal
$\rightarrow$ sub diagonal

use of trisis matrix : importance?

$$
a_{22} = \text{main}
$$

$$
A =
\begin{bmatrix}
0 & h & g \\
-h & 0 & f \\
-g & -f & 0
\end{bmatrix}
$$

$$
A^T =
\begin{bmatrix}
0 & -h & -g \\
h & 0 & -f \\
g & f & 0
\end{bmatrix} = -A
$$

$$
A^T = -A
$$

<!-- Page 003 -->
<div align="right"><b>10-11-23</b></div>

<b>Class 2 | Mam Rupali</b>

$P(1,2,3)$
Position vector,

$$
\vec{r} = x\hat{i} + y\hat{j} + z\hat{k} = 1\hat{i} + 2\hat{j} + 3\hat{k}
$$

init point $\rightarrow$ terminal point

vector analysis
SCHAUM'S outline
Murray R. Spiegel

---

<div align="right"><b>11-11-23</b></div>

<b>Class 3 | Rupali mam</b>

**Dot:**

$$
\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta
$$

$$
\vec{A} \cdot \vec{B} = 0 \text{ (perpendicular each other, } \theta = 90^\circ \text{)}
$$

$$
\vec{A} \cdot \vec{B} = AB \text{ (} \theta = 0^\circ \text{)}
$$

$\rightarrow$ mean: একটা ভেক্টর আরেকটার সাথে কেমন, প্যারালাল না লম্ব।
$\rightarrow$ একটার সাপেক্ষে অন্যটা কতটুকু similar।

**Cross:**

$$
\vec{A} \times \vec{B} = AB\sin\theta\hat{n}
$$

**Triple product**

$$
\vec{A} \cdot (\vec{B} \times \vec{C})
$$

$$
\vec{A} \times \vec{B} \cdot (\vec{C} - \vec{D})
$$

<!-- Page 004 -->
<div align="right"><b>15-11-23</b></div>

<b>Class 4 | Sir</b>

**Echelon Matrix:**
- find inverse
- Row cannonical form

What, Why,
**def:** If in a matrix the number of zeroes preceeding the first non zero entry increases row by row.
first nonzero $\rightarrow$ pivot

$$
\begin{pmatrix}
\textcircled{1} & 2 & 3 & 4 \\
0 & \textcircled{1} & 2 & 3 \\
0 & 0 & \textcircled{1} & 2 \\
0 & 0 & 0 & \textcircled{1}
\end{pmatrix}
$$

number of zeros $\rightarrow$ increases

$$
\begin{pmatrix}
1 & 0 & 1 & 1 \\
0 & 1 & 1 & 1 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$

more rank = 2

$$
\begin{pmatrix}
1 & 0 & 1 & 1 \\
0 & 1 & 1 & 1 \\
0 & 2 & 0 & 0
\end{pmatrix}
$$

not in echelon form
1 more than before pivot

**# rank of the matrix? by echelon**
$\rightarrow$ number of non zero row in echelon form
pivot না থাকলে কলাম এর সাপেক্ষে ডান্টিক বাদ

**# Reduce the matrix**

$$
\begin{pmatrix}
1 & 2 & 4 & 5 \\
6 & 7 & 1 & 1 \\
4 & 3 & 4 & 5
\end{pmatrix}
$$

**to its echelon form**

Perform elementary row operation transformation
$R_2 \rightarrow 6R_1 - R_2$
$R_3 \rightarrow R_1 + R_3$

$$
\begin{pmatrix}
1 & 2 & 4 & 5 \\
0 & 5 & 23 & 29 \\
0 & 5 & 8 & 10
\end{pmatrix}
$$

$\rightarrow$ number of zero = 1
$\rightarrow$ number of zero = 1
so not echelon still

equivalent sign $\rightarrow$ same inform gather করবে but they are not equal just equivalent.

$3D \rightarrow 2D$
Elementary transformation

<!-- Page 005 -->
$R_3 \rightarrow R_2 - R_3$

$$
\begin{pmatrix}
1 & 2 & 4 & 5 \\
0 & 5 & 23 & 29 \\
0 & 0 & 15 & 19
\end{pmatrix}
$$

$$
n_o = 1
$$

$$
n_o = 2
$$

$\text{rank} = 3 \rightarrow \text{so echelon}$

**Row cannonical form**
**Row reduced echelon form**
1. pivot should be 1
2. should be echelon form
3. only non zero entry of that corresponding column

$$
\begin{pmatrix}
1 & 2^0 & 4^0 & 5^0 \\
0 & \textcircled{1} & 4^0 & 5 \\
0 & 0 & \textcircled{1} & 6
\end{pmatrix}
$$

important in image processing also.

$$
\frac{d}{dx}(x^2) = 2x
$$

$$
\frac{d}{dx} : \text{conti} \rightarrow \text{conti}
$$

$f: R \rightarrow R$

**# write down the workflow of conversion to cannonical form.**
4- dimention eucledion axis

$$
\begin{pmatrix}
1 & 2 & 3 & 5 \\
-1 & 1 & 2 & 1 \\
1 & 1 & 2 & 3
\end{pmatrix}
$$

$R_2 \rightarrow R_1 + R_2$
$R_3 \rightarrow R_1 - R_3$

$$
\begin{pmatrix}
1 & 2 & 3 & 5 \\
0 & 3 & 5 & 6 \\
0 & 1 & 1 & 2
\end{pmatrix}
$$

$R_3 \rightarrow R_2 - 3R_3$

$$
\begin{pmatrix}
1 & 2 & 3 & 5 \\
0 & 3 & 5 & 6 \\
0 & 0 & 2 & 0
\end{pmatrix}
$$

which is an echelon matrix

$R_1 \rightarrow 3R_1 - 2R_2$

$$
\begin{pmatrix}
3 & 0 & -1 & 3 \\
0 & 3 & 5 & 6 \\
0 & 0 & 2 & 0
\end{pmatrix}
$$

$R_1 \rightarrow 2R_1 + R_3$

$$
\begin{pmatrix}
6 & 0 & 0 & 6 \\
0 & 3 & 5 & 6 \\
0 & 0 & 2 & 0
\end{pmatrix}
$$

<!-- Page 006 -->
$R_2 \rightarrow 2R_2 - 5R_3$

$$
\begin{pmatrix}
6 & 0 & 0 & 6 \\
0 & 6 & 0 & 12 \\
0 & 0 & 2 & 0
\end{pmatrix}
$$

$$
R_1 \rightarrow \frac{1}{6} R_1
$$

$$
R_2 \rightarrow \frac{1}{6} R_2
$$

$$
R_3 \rightarrow \frac{1}{2} R_3
$$

$$
\begin{pmatrix}
1 & 0 & 0 & 1 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & 0
\end{pmatrix}
$$

which is row reduced echelon matrix

<div align="right"><b>17-11-23</b></div>

<b>Class 5 | Mam</b>

**Vector differenciation**

$$
f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
$$

(average $\rightarrow$ limit $\rightarrow$ তাৎক্ষনিক)

**parametric equation**

$$
x^2 + y^2 = r^2 \rightarrow \text{Cartesian}
$$

$x = r\cos\theta$
$y = r\sin\theta$

$\rightarrow$ space curve $\rightarrow$ একটা parameter এর মাধ্যমে প্রকাশ
$\rightarrow$ differentiable form আনব / derivative

distance - straight line
arc length - curve

<!-- Page 007 -->
<div align="right"><b>18-11-23</b></div>

<b>Class 6</b>

$$
\vec{r} = 3\cos t \hat{i} + 3\sin t \hat{j} + 4t\hat{k}
$$

$$
\frac{d\vec{r}}{dt} = -3\sin t \hat{i} + 3\cos t \hat{j} + 4\hat{k}
$$

$$
T = \frac{\frac{d\vec{r}}{dt}}{\left| \frac{d\vec{r}}{dt} \right|} = \frac{-3\sin t \hat{i} + 3\cos t \hat{j} + 4\hat{k}}{\dots}
$$

<div align="right"><b>22-11-23</b></div>

<b>Class 7 | Sir</b>

**# matrix vs determinant**
Matrix
- row column
- no restrictions
- no value

Determinant
- equal number of row & column
- value

**A system of linear equations:**
what is system?

$$
a_{11}x_1 + a_{12}x_2 + a_{13}x_3 + \dots + a_{1n}x_n = b_1
$$

$$
a_{21}x_1 + a_{22}x_2 + a_{23}x_3 + \dots + a_{2n}x_n = b_2
$$

$\dots$

$$
a_{n1}x_1 + a_{n2}x_2 + a_{n3}x_3 + \dots + a_{nn}x_n = b_n
$$

- Unknown are $x_1, x_2 \dots x_n$
- degree of unkown are 1
-

$$
b_1, b_2 \dots b_n = \text{constant}
$$

**non-homogeneous**
$b_1, b_2 \dots b_n$ if one of them are not zero.
solution পাওয়া যেতেও পারে নাও পারে
$b_1, b_2 \dots b_n$ affected by outer environment

**homogeneous**
$b_1, b_2 \dots b_n$ all are zero
সবসময় পাওয়া যাবে।

<!-- Page 008 -->
একে অপরের উপর depend করলে কোনো unique solution নাই।
homogenous এর unique এর সল্যুশন নাই।

$AX = B$

$$
A = egin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \ a_{21} & a_{22} & \dots & a_{2n} \ a_{n1} & a_{n2} & \dots & a_{nn} \end{pmatrix} \leftarrow 	ext{coefficient of the unknowns}
$$

$X = egin{pmatrix} x_1 \ x_2 \
dots \ x_n \end{pmatrix}$
$B = egin{pmatrix} b_1 \ b_2 \
dots \ b_n \end{pmatrix}$

$[A:B]$
solution থাকলে consistent
না থাকলে non-consistent

$\# 2x + 3y - 5z = 2$
$x + y - z = 1$
$2x - 2y + z = 3$

$AX = B$
$A = egin{pmatrix} 2 & 3 & -5 \ 1 & 1 & -1 \ 2 & -2 & 1 \end{pmatrix}$
$X = egin{pmatrix} x \ y \ z \end{pmatrix}$
$B = egin{pmatrix} 2 \ 1 \ 3 \end{pmatrix}$

$egin{pmatrix} 2 & 3 & -5 \ 1 & 1 & -1 \ 2 & -2 & 1 \end{pmatrix} egin{pmatrix} x \ y \ z \end{pmatrix} = egin{pmatrix} 2 \ 1 \ 3 \end{pmatrix}$
$\Rightarrow egin{pmatrix} 2x + 3y - 5y \ x + y - z \ 2x - 2y + z \end{pmatrix} = egin{pmatrix} 2 \ 1 \ 3 \end{pmatrix}$

**Matrix method**
$
ightarrow$ system should be written into $AX=B$ form
$
ightarrow$ Augmented matrix বৃদ্ধি করা (concatenated)
$[A:B]
ightarrow$ horizontal cat

$\Rightarrow$ convert augmented $
ightarrow$ echelon matrix
$
ightarrow$ decision
find rank of $A$ and rank of $[A:B]$

$
ightarrow$ if both rank are same then solution exist
$	ext{Rank of } A = 	ext{Rank of } [A:B]$

<!-- Page 009 -->
solution can be
- unique solution (rank of augmented matrix = rank of A and equal to number of unkowns or variables)
- more than one solution (rank same but rank of $[A:B] = 	ext{rank of } A < 	ext{number of unknown}$)

if $	ext{rank}(A)
eq 	ext{rank}[A:B]$
then the system has no solution.

how can we solve the linear eqn?

**# solve the system:**
$x - 2y - 5z = 2$
$-x + y + 3z = -2$
$2x + y + z = 3$

The system can be set as $AX = B$
$A = egin{bmatrix} 1 & -2 & -5 \ -1 & 1 & 3 \ 2 & 1 & 1 \end{bmatrix}$
$X = egin{bmatrix} x \ y \ z \end{bmatrix}$
$B = egin{bmatrix} 2 \ -2 \ 3 \end{bmatrix}$
matrix form of the system

Now, the augmented matrix is
$[A:B] = egin{bmatrix} 1 & -2 & -5 &
dots & 2 \ -1 & 1 & 3 &
dots & -2 \ 2 & 1 & 1 &
dots & 3 \end{bmatrix}$
matrix গুলো vertical cat করা হয়েছে
horizontal cat

convert this to echelon form
$egin{bmatrix} 1 & -2 & -5 & 2 \ -1 & 1 & 3 & -2 \ 2 & 1 & 1 & 3 \end{bmatrix}$

$R_2
ightarrow R_1 + R_2$
$R_3
ightarrow R_3 - 2R_1$
$egin{bmatrix} 1 & -2 & -5 & 2 \ 0 & -1 & -2 & 0 \ 0 & 5 & 11 & -1 \end{bmatrix}$

$R_3
ightarrow 5R_2 + R_3$
$egin{bmatrix} 1 & -2 & -5 & 2 \ 0 & -1 & -2 & 0 \ 0 & 0 & 1 & -1 \end{bmatrix}$

<!-- Page 010 -->
which is the echelon form of augmented matrix
$egin{bmatrix} 1 & -2 & -5 & 2 \ 0 & -1 & -2 & 0 \ 0 & 0 & 1 & -1 \end{bmatrix}$

$	ext{rank } A = 3$
$	ext{rank of } [A:B] = 3$
number of unknowns = $3$
so the system has a unique solution.

---

<div align="right"><b>24-11-23</b></div>

<b>Class 8 | Mam</b>

$\# x = 3\cos t$, $y = 3\sin t$, $z = 4t$
$
ec{r} = 3\cos t \hat{i} + 3\sin t \hat{j} + 4t\hat{k}$
$
rac{d
ec{r}}{dt} = -3\sin t \hat{i} + 3\cos t \hat{j} + 4\hat{k}$

$\left|
rac{d
ec{r}}{dt}
ight| = 5$

$T =
rac{
rac{d
ec{r}}{dt}}{\left|
rac{d
ec{r}}{dt}
ight|} =
rac{-3\sin t \hat{i} + 3\cos t \hat{j} + 4\hat{k}}{5} = -
rac{3}{5}\sin t \hat{i} +
rac{3}{5}\cos t \hat{j} +
rac{4}{5}\hat{k}$

$
rac{dT}{ds} = kN$
$
rac{dT}{dt} 	imes
rac{dt}{ds} = kN$
$
rac{dT}{dt} 	imes
rac{1}{\left|
rac{d
ec{r}}{dt}
ight|} = kN$

$
rac{1}{5} \left(-
rac{3}{5}\cos t \hat{i} -
rac{3}{5}\sin t \hat{j}
ight) = kN$
$
rac{1}{25} (-3\cos t \hat{i} - 3\sin t \hat{j}) = kN$

$|N| = 1$
$\left|
rac{1}{25} (-3\cos t \hat{i} - 3\sin t \hat{j})
ight| = |k||N|$
$
rac{1}{25} \sqrt{9\cos^2 t + 9\sin^2 t} = |k|$
$|k| =
rac{3}{25}$
$k =
rac{3}{25}$