[🏠 Index](00-index.md) | [CT-2 (Vector) Answer ➡](CT2_Vector_answer.md)

---

# CT 1 (Vector) Answers — Math 2117 (ECE'23)

---

### Q1. Explain the physical significance of dot and cross product. Show that $\vec{A} = \frac{1}{3}(2\hat{i} - 2\hat{j} + \hat{k})$, $\vec{B} = \frac{1}{3}(\hat{i} + 2\hat{j} + 2\hat{k})$ and $\vec{C} = \frac{1}{3}(2\hat{i} + \hat{j} - 2\hat{k})$ are mutually orthogonal unit vectors. (2+2+6)

**Answer:**

#### 1. Physical Significance of Dot Product
The dot product represents the projection of one vector onto another. It shows how much the two vectors point in the same direction. It results in a scalar quantity. In physics, we use it to calculate work done by a force:

$$
W = \vec{F} \cdot \vec{d}
$$

Here, $W$ is work. $\vec{F}$ is force. $\vec{d}$ is displacement.

#### 2. Physical Significance of Cross Product
The cross product represents a rotational effect. It results in a new vector. This vector is perpendicular to the plane of the two original vectors. The magnitude of the cross product equals the area of the parallelogram formed by the two vectors. In physics, we use it to calculate torque:

$$
\vec{\tau} = \vec{r} \times \vec{F}
$$

Here, $\vec{\tau}$ is torque. $\vec{r}$ is the position vector. $\vec{F}$ is force.

#### 3. Orthogonal Unit Vectors Verification
First, we check the magnitude of each vector.

For vector $\vec{A}$:

$$
|\vec{A}| = \sqrt{\left(\frac{2}{3}\right)^2 + \left(-\frac{2}{3}\right)^2 + \left(\frac{1}{3}\right)^2} = \sqrt{\frac{4}{9} + \frac{4}{9} + \frac{1}{9}} = \sqrt{\frac{9}{9}} = 1
$$

For vector $\vec{B}$:

$$
|\vec{B}| = \sqrt{\left(\frac{1}{3}\right)^2 + \left(\frac{2}{3}\right)^2 + \left(\frac{2}{3}\right)^2} = \sqrt{\frac{1}{9} + \frac{4}{9} + \frac{4}{9}} = \sqrt{\frac{9}{9}} = 1
$$

For vector $\vec{C}$:

$$
|\vec{C}| = \sqrt{\left(\frac{2}{3}\right)^2 + \left(\frac{1}{3}\right)^2 + \left(-\frac{2}{3}\right)^2} = \sqrt{\frac{4}{9} + \frac{1}{9} + \frac{4}{9}} = \sqrt{\frac{9}{9}} = 1
$$

So, all three vectors are unit vectors.

Next, we check if they are mutually orthogonal. We calculate their dot products.

Dot product of $\vec{A}$ and $\vec{B}$:

$$
\vec{A} \cdot \vec{B} = \left[\frac{1}{3}(2\hat{i} - 2\hat{j} + \hat{k})\right] \cdot \left[\frac{1}{3}(\hat{i} + 2\hat{j} + 2\hat{k})\right]
$$

$$
\vec{A} \cdot \vec{B} = \frac{1}{9} [2(1) + (-2)(2) + 1(2)] = \frac{1}{9} [2 - 4 + 2] = 0
$$

Dot product of $\vec{B}$ and $\vec{C}$:

$$
\vec{B} \cdot \vec{C} = \left[\frac{1}{3}(\hat{i} + 2\hat{j} + 2\hat{k})\right] \cdot \left[\frac{1}{3}(2\hat{i} + \hat{j} - 2\hat{k})\right]
$$

$$
\vec{B} \cdot \vec{C} = \frac{1}{9} [1(2) + 2(1) + 2(-2)] = \frac{1}{9} [2 + 2 - 4] = 0
$$

Dot product of $\vec{C}$ and $\vec{A}$:

$$
\vec{C} \cdot \vec{A} = \left[\frac{1}{3}(2\hat{i} + \hat{j} - 2\hat{k})\right] \cdot \left[\frac{1}{3}(2\hat{i} - 2\hat{j} + \hat{k})\right]
$$

$$
\vec{C} \cdot \vec{A} = \frac{1}{9} [2(2) + 1(-2) + (-2)(1)] = \frac{1}{9} [4 - 2 - 2] = 0
$$

The dot product of each pair is zero. So, the vectors are mutually orthogonal.

---

### Q2. State Frenet-Serret formulas. Show that $\vec{r} = e^{-t}(\vec{A} \cos 2t + \vec{B} \sin 2t)$, where $\vec{A}$ and $\vec{B}$ are constant vectors, is a solution of the differential equation $\frac{d^2\vec{r}}{dt^2} + 2\frac{d\vec{r}}{dt} + 5\vec{r} = 0$. (2+8)

**Answer:**

#### 1. Frenet-Serret Formulas
Let $s$ be the arc length along a space curve. Let $\vec{T}$ be the unit tangent vector. Let $\vec{N}$ be the unit principal normal vector. Let $\vec{B}_b$ be the unit binormal vector. Let $\kappa$ be curvature. Let $\tau$ be torsion.
The Frenet-Serret formulas are:
1. $\frac{d\vec{T}}{ds} = \kappa \vec{N}$
2. $\frac{d\vec{N}}{ds} = -\kappa \vec{T} + \tau \vec{B}_b$
3. $\frac{d\vec{B}_b}{ds} = -\tau \vec{N}$

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
