# Topic 18: Matrix ODE and Diagonalization

This file contains the organized questions and answers for **Matrix ODE and Diagonalization**, priority ranked as **Priority 18** based on frequency and exam weight.

---

## Q1. Diagonalize the matrix $A = \begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}$. Hence evaluate $e^A$, and then solve $\frac{dx_1}{dt} = x_2$, $\frac{dx_2}{dt} = x_1$. (12)

| | |
|---|---|
| **ID** | PYQ-2017-8 |
| **Source** | 2017 Q8 [12 marks] |

**Answer:**

#### 1. Diagonalization check

Let $A = \begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}$. Its eigenvalues are the diagonal entries:

$$
\lambda_1 = 1, \quad \lambda_2 = 1
$$

To check if $A$ is diagonalizable, we find the eigenvectors by solving $(A - I)X = 0$:

$$
\begin{bmatrix}
0 & 1 \\
0 & 0
\end{bmatrix} \begin{bmatrix}
x \\
y
\end{bmatrix} = \begin{bmatrix}
0 \\
0
\end{bmatrix} \implies y = 0
$$

The eigenvectors are of the form $\begin{bmatrix}
x \\
0
\end{bmatrix}$. So there is only one linearly independent eigenvector:

$$
X_1 = \begin{bmatrix}
1 \\
0
\end{bmatrix}
$$

Since the geometric multiplicity (1) is less than the algebraic multiplicity (2), **the matrix $A$ is not diagonalizable**.

#### 2. Evaluation of $e^A$

Even though $A$ is not diagonalizable, we can evaluate $e^A$ using the power series definition. We decompose $A$ into:

$$
A = I + B, \quad \text{where } B = \begin{bmatrix}
0 & 1 \\
0 & 0
\end{bmatrix}
$$

Since the identity matrix $I$ commutes with any matrix ($IB = BI$), we can write:

$$
e^A = e^{I + B} = e^I \cdot e^B = e \cdot e^B
$$

Note that $B^2 = \begin{bmatrix}
0 & 1 \\
0 & 0
\end{bmatrix} \begin{bmatrix}
0 & 1 \\
0 & 0
\end{bmatrix} = \begin{bmatrix}
0 & 0 \\
0 & 0
\end{bmatrix}$. So $B^n = 0$ for all $n \geq 2$.

Using the series definition for $e^B$:

$$
e^B = I + B + \frac{B^2}{2!} + \dots = I + B = \begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix}
$$

Therefore:

$$
e^A = e \begin{bmatrix}
1 & 1 \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
e & e \\
0 & e
\end{bmatrix}
$$

#### 3. Solving the differential equations

We solve the systems in two different interpretations:

##### Interpretation 1: Solving the system as printed

The printed system is:

$$
\frac{dx_1}{dt} = x_2, \quad \frac{dx_2}{dt} = x_1
$$

We differentiate the first equation:

$$
\frac{d^2x_1}{dt^2} = \frac{dx_2}{dt} = x_1 \implies \frac{d^2x_1}{dt^2} - x_1 = 0
$$

The characteristic equation is $r^2 - 1 = 0$, which gives $r = \pm 1$. So the general solution for $x_1(t)$ is:

$$
x_1(t) = C_1 e^t + C_2 e^{-t}
$$

Then we find $x_2(t)$ using the first relation:

$$
x_2(t) = \frac{dx_1}{dt} = C_1 e^t - C_2 e^{-t}
$$

##### Interpretation 2: Solving the intended system $\frac{dX}{dt} = AX$

The intended system associated with matrix $A$ is:

$$
\frac{dx_1}{dt} = x_1 + x_2, \quad \frac{dx_2}{dt} = x_2
$$

The solution to a system of the form $\frac{dX}{dt} = AX$ is:

$$
X(t) = e^{At} X(0)
$$

We calculate the matrix exponential $e^{At}$ by decomposing $At = It + Bt$:

$$
e^{At} = e^t e^{Bt} = e^t (I + Bt) = e^t \begin{bmatrix}
1 & t \\
0 & 1
\end{bmatrix} = \begin{bmatrix}
e^t & t e^t \\
0 & e^t
\end{bmatrix}
$$

So the solution is:

$$
\begin{bmatrix}
x_1(t) \\
x_2(t)
\end{bmatrix} = \begin{bmatrix}
e^t & t e^t \\
0 & e^t
\end{bmatrix} \begin{bmatrix}
x_1(0) \\
x_2(0)
\end{bmatrix}
$$

This gives the general solution:

$$
x_1(t) = (C_1 + C_2 t) e^t
$$

$$
x_2(t) = C_2 e^t
$$

where $C_1 = x_1(0)$ and $C_2 = x_2(0)$.

---

*(start)* | [🏠 Index](00-index.md) | [2018 ➡](2018_answer.md)

---

## Q2. Solve the following system of differential equations by matrix method: (06)

| | |
|---|---|
| **ID** | PYQ-2020-7b | PYQ-2021-7b |
| **Appeared in** | 2020 Q7(b) [06 marks], 2021 Q7(b) [06 marks] |
| **Frequency** | ⭐⭐ (2 times) |

**Answer:**

$$\frac{dx}{dt} = 6x - 3y$$
$$\frac{dy}{dt} = 2x + y$$

**Answer:**

We write the system in matrix form:

$$
\frac{dX}{dt} = M X, \quad \text{where } M = \begin{bmatrix}
6 & -3 \\
2 & 1
\end{bmatrix}
$$

First we find the eigenvalues of $M$ by solving $|M - \lambda I| = 0$:

$$
\begin{vmatrix}
6-\lambda & -3 \\
2 & 1-\lambda
\end{vmatrix} = 0 \implies (6-\lambda)(1-\lambda) + 6 = \lambda^2 - 7\lambda + 12 = 0
$$

$$
(\lambda - 3)(\lambda - 4) = 0 \implies \lambda = 3 \quad \text{or} \quad \lambda = 4
$$

Now find the eigenvectors:
*   **For $\lambda = 3$:**

$$
M - 3I = \begin{bmatrix}
3 & -3 \\
2 & -2
\end{bmatrix} \implies 3x - 3y = 0 \implies x = y
$$

The eigenvector is:

$$
v_1 = \begin{bmatrix}
1 \\
1
\end{bmatrix}
$$

*   **For $\lambda = 4$:**

$$
M - 4I = \begin{bmatrix}
2 & -3 \\
2 & -3
\end{bmatrix} \implies 2x - 3y = 0 \implies x = \frac{3}{2}y
$$

The eigenvector (for $y=2$) is:

$$
v_2 = \begin{bmatrix}
3 \\
2
\end{bmatrix}
$$

The general solution is a linear combination of the fundamental solutions:

$$
\begin{bmatrix}
x(t) \\
y(t)
\end{bmatrix} = C_1 e^{3t} \begin{bmatrix}
1 \\
1
\end{bmatrix} + C_2 e^{4t} \begin{bmatrix}
3 \\
2
\end{bmatrix}
$$

So the system solution is:

$$
x(t) = C_1 e^{3t} + 3C_2 e^{4t}
$$

$$
y(t) = C_1 e^{3t} + 2C_2 e^{4t}
$$

---

