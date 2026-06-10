# Topic 17: Velocity, Acceleration, and Particle Motion

This file contains the organized questions and answers for **Velocity, Acceleration, and Particle Motion**, priority ranked as **Priority 17** based on frequency and exam weight.

---

## Q1 (04)

A particle moves along the curve $x = 2t^2, y = t^2 - 4t, z = 3t - 5$, where $t$ is the time. Find the components of its velocity and acceleration at time $t=1$ in the direction $\hat{i} - 3\hat{j} + 2\hat{k}$.

| | |
|---|---|
| **ID** | PYQ-2019-2a | PYQ-2023-2c |
| **Appeared in** | 2019 Q2(a) [04 marks], 2023 Q2(c) [04 marks] |
| **Frequency** | ⭐⭐ (2 times) |

**Answer:**

Let the direction vector be $\vec{d} = \hat{i} - 3\hat{j} + 2\hat{k}$. The unit direction vector $\hat{u}$ is:

$$
\hat{u} = \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{1^2 + (-3)^2 + 2^2}} = \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{14}}
$$

The position vector of the particle is:

$$
\vec{r}(t) = 2t^2\hat{i} + (t^2 - 4t)\hat{j} + (3t - 5)\hat{k}
$$

#### 1. Velocity Component

Differentiate the position vector to get the velocity vector:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt} = 4t\hat{i} + (2t - 4)\hat{j} + 3\hat{k}
$$

Evaluate velocity at $t=1$:

$$
\vec{v}(1) = 4\hat{i} - 2\hat{j} + 3\hat{k}
$$

The component of velocity in the direction of $\hat{u}$ is:

$$
v_d = \vec{v}(1) \cdot \hat{u} = (4\hat{i} - 2\hat{j} + 3\hat{k}) \cdot \left( \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{14}} \right) = \frac{4 + 6 + 6}{\sqrt{14}} = \frac{16}{\sqrt{14}}
$$

#### 2. Acceleration Component

Differentiate the velocity vector to get the acceleration vector:

$$
\vec{a}(t) = \frac{d\vec{v}}{dt} = 4\hat{i} + 2\hat{j}
$$

Evaluate acceleration at $t=1$:

$$
\vec{a}(1) = 4\hat{i} + 2\hat{j}
$$

The component of acceleration in the direction of $\hat{u}$ is:

$$
a_d = \vec{a}(1) \cdot \hat{u} = (4\hat{i} + 2\hat{j}) \cdot \left( \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{14}} \right) = \frac{4 - 6 + 0}{\sqrt{14}} = -\frac{2}{\sqrt{14}}
$$

---

## Q2 (04)

If $\bar{A}$ has a constant magnitude show that $\bar{A}$ and $\frac{d\bar{A}}{dt}$ are perpendicular provided $\left|\frac{d\bar{A}}{dt}\right| \neq 0$.

| | |
|---|---|
| **ID** | PYQ-2019-2b |
| **Source** | 2019 Q2(b) [04 marks] |

**Answer:**

Let the constant magnitude of $\vec{A}$ be $|\vec{A}| = c$ (where $c$ is a constant).

Then we can write:

$$
\vec{A} \cdot \vec{A} = |\vec{A}|^2 = c^2
$$

Differentiate both sides with respect to $t$:

$$
\frac{d}{dt} (\vec{A} \cdot \vec{A}) = \frac{d}{dt} (c^2)
$$

Using the product rule for vector dot products:

$$
\vec{A} \cdot \frac{d\vec{A}}{dt} + \frac{d\vec{A}}{dt} \cdot \vec{A} = 0
$$

Since the dot product is commutative ($\vec{a} \cdot \vec{b} = \vec{b} \cdot \vec{a}$):

$$
2 \left( \vec{A} \cdot \frac{d\vec{A}}{dt} \right) = 0 \implies \vec{A} \cdot \frac{d\vec{A}}{dt} = 0
$$

Since the dot product of $\vec{A}$ and $\frac{d\vec{A}}{dt}$ is zero, and neither vector is zero (given $\left|\frac{d\vec{A}}{dt}\right| \neq 0$ and magnitude of $\vec{A}$ is a non-zero constant), the vectors must be perpendicular.

---

## Q3 (04)

A particle moves along a curve whose parametric equations are $x = e^{-t}, y = 2\cos 3t, z = 2\sin 3t$, where $t$ is the time. Find the magnitudes of the velocity and acceleration at $t=0$.

| | |
|---|---|
| **ID** | PYQ-2020-2a |
| **Source** | 2020 Q2(a) [04 marks] |

**Answer:**

The position vector of the particle is:

$$
\vec{r}(t) = e^{-t}\hat{i} + 2\cos 3t\hat{j} + 2\sin 3t\hat{k}
$$

#### 1. Magnitude of Velocity

Differentiate the position vector to find the velocity vector:

$$
\vec{v}(t) = \frac{d\vec{r}}{dt} = -e^{-t}\hat{i} - 6\sin 3t\hat{j} + 6\cos 3t\hat{k}
$$

At $t=0$:

$$
\vec{v}(0) = -\hat{i} - 0\hat{j} + 6\hat{k} = -\hat{i} + 6\hat{k}
$$

The magnitude is:

$$
|\vec{v}(0)| = \sqrt{(-1)^2 + 6^2} = \sqrt{1 + 36} = \sqrt{37}
$$

#### 2. Magnitude of Acceleration

Differentiate the velocity vector to find the acceleration vector:

$$
\vec{a}(t) = \frac{d\vec{v}}{dt} = e^{-t}\hat{i} - 18\cos 3t\hat{j} - 18\sin 3t\hat{k}
$$

At $t=0$:

$$
\vec{a}(0) = \hat{i} - 18\hat{j} - 0\hat{k} = \hat{i} - 18\hat{j}
$$

The magnitude is:

$$
|\vec{a}(0)| = \sqrt{1^2 + (-18)^2} = \sqrt{1 + 324} = \sqrt{325} = 5\sqrt{13}
$$

---

## Q4 (04)

A particle moves so that its position vector is given by $\vec{r} = \cos \omega t \hat{i} + \sin \omega t \hat{j}$ where $\omega$ is constant. Show that the velocity $\vec{v}$ of the particle is perpendicular to $\vec{r}$, also show that $\vec{r} \times \vec{v} = \vec{a}$ constant vector.

| | |
|---|---|
| **ID** | PYQ-2024-2b |
| **Source** | 2024 Q2(b) [04 marks] |

**Answer:**

#### 1. Show that Velocity is Perpendicular to Position
We find the velocity vector $\vec{v}$ by taking the derivative of $\vec{r}$ with respect to $t$:

$$
\vec{v} = \frac{d\vec{r}}{dt} = -\omega \sin \omega t \hat{i} + \omega \cos \omega t \hat{j}
$$

We calculate the dot product of $\vec{r}$ and $\vec{v}$:

$$
\vec{r} \cdot \vec{v} = (\cos \omega t)(-\omega \sin \omega t) + (\sin \omega t)(\omega \cos \omega t) = -\omega \sin \omega t \cos \omega t + \omega \sin \omega t \cos \omega t = 0
$$

The dot product is zero. So, the velocity vector $\vec{v}$ is perpendicular to $\vec{r}$.

#### 2. Show that $\vec{r} \times \vec{v}$ is a Constant Vector
We calculate the cross product:

$$
\vec{r} \times \vec{v} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\cos \omega t & \sin \omega t & 0 \\
-\omega \sin \omega t & \omega \cos \omega t & 0
\end{vmatrix}
$$

$$
\vec{r} \times \vec{v} = \hat{i}(0) - \hat{j}(0) + \hat{k} \left[ (\cos \omega t)(\omega \cos \omega t) - (\sin \omega t)(-\omega \sin \omega t) \right]
$$

$$
\vec{r} \times \vec{v} = \hat{k} \left( \omega \cos^2 \omega t + \omega \sin^2 \omega t \right) = \omega (\cos^2 \omega t + \sin^2 \omega t)\hat{k} = \omega\hat{k}
$$

The term $\omega$ is a constant. So, the vector $\omega\hat{k}$ is constant. Let $\vec{a} = \omega\hat{k}$. We get:

$$
\vec{r} \times \vec{v} = \vec{a}
$$

This is a constant vector.

---

## Q5 (2+8)

State Frenet-Serret formulas. Show that $\vec{r} = e^{-t}(\vec{A} \cos 2t + \vec{B} \sin 2t)$, where $\vec{A}$ and $\vec{B}$ are constant vectors, is a solution of the differential equation $\frac{d^2\vec{r}}{dt^2} + 2\frac{d\vec{r}}{dt} + 5\vec{r} = 0$.

| | |
|---|---|
| **ID** | CT1V-2 |
| **Source** | CT1V Q2 [2+8 marks] |

**Answer:**

#### 1. Frenet-Serret Formulas
Let $s$ be the arc length along a space curve. Let $\vec{T}$ be the unit tangent vector. Let $\vec{N}$ be the unit principal normal vector. Let $\vec{B}\_b$ be the unit binormal vector. Let $\kappa$ be curvature. Let $\tau$ be torsion.
The Frenet-Serret formulas are:
1. $\frac{d\vec{T}}{ds} = \kappa \vec{N}$
2. $\frac{d\vec{N}}{ds} = -\kappa \vec{T} + \tau \vec{B}\_b$
3. $\frac{d\vec{B}\_b}{ds} = -\tau \vec{N}$

#### 2. Verification of Differential Equation
We are given:

$$
\vec{r} = e^{-t}(\vec{A} \cos 2t + \vec{B} \sin 2t)
$$

We find the first derivative of $\vec{r}$ with respect to $t$:

$$
\frac{d\vec{r}}{dt} = -e^{-t}(\vec{A} \cos 2t + \vec{B} \sin 2t) + e^{-t}(-2\vec{A} \sin 2t + 2\vec{B} \cos 2t)
$$

$$
\frac{d\vec{r}}{dt} = e^{-t} [(-\vec{A} + 2\vec{B})\cos 2t + (-2\vec{A} - \vec{B})\sin 2t]
$$

Now we find the second derivative:

$$
\frac{d^2\vec{r}}{dt^2} = -e^{-t} [(-\vec{A} + 2\vec{B})\cos 2t + (-2\vec{A} - \vec{B})\sin 2t] + e^{-t} [-2(-\vec{A} + 2\vec{B})\sin 2t + 2(-2\vec{A} - \vec{B})\cos 2t]
$$

$$
\frac{d^2\vec{r}}{dt^2} = e^{-t} [(\vec{A} - 2\vec{B} - 4\vec{A} - 2\vec{B})\cos 2t + (2\vec{A} + \vec{B} + 2\vec{A} - 4\vec{B})\sin 2t]
$$

$$
\frac{d^2\vec{r}}{dt^2} = e^{-t} [(-3\vec{A} - 4\vec{B})\cos 2t + (4\vec{A} - 3\vec{B})\sin 2t]
$$

We substitute these derivatives into the left-hand side of the differential equation:

$$
\text{LHS} = \frac{d^2\vec{r}}{dt^2} + 2\frac{d\vec{r}}{dt} + 5\vec{r}
$$

$$
\text{LHS} = e^{-t} [(-3\vec{A} - 4\vec{B})\cos 2t + (4\vec{A} - 3\vec{B})\sin 2t] + 2e^{-t} [(-\vec{A} + 2\vec{B})\cos 2t + (-2\vec{A} - \vec{B})\sin 2t] + 5e^{-t} [\vec{A} \cos 2t + \vec{B} \sin 2t]
$$

Combine the coefficient terms for $\cos 2t$:

$$
(-3\vec{A} - 4\vec{B}) + 2(-\vec{A} + 2\vec{B}) + 5\vec{A} = -3\vec{A} - 4\vec{B} - 2\vec{A} + 4\vec{B} + 5\vec{A} = 0
$$

Combine the coefficient terms for $\sin 2t$:

$$
(4\vec{A} - 3\vec{B}) + 2(-2\vec{A} - \vec{B}) + 5\vec{B} = 4\vec{A} - 3\vec{B} - 4\vec{A} - 2\vec{B} + 5\vec{B} = 0
$$

So, the equation becomes:

$$
\text{LHS} = e^{-t} [0 \cos 2t + 0 \sin 2t] = 0 = \text{RHS}
$$

This confirms that $\vec{r}$ is a solution.

---

*(start)* | [🏠 Index](00-index.md) | [CT-2 (Vector) Answer ➡](CT2_Vector_answer.md)

---

