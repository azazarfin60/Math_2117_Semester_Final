[← Previous: A04 Vector Differentiation](A04_Vector_Differentiation.md) | [Index](00_Index.md) | [Next: A06 Curvature and Torsion →](A06_Curvature_Torsion_Frenet_Serret.md)

---

# A05: Velocity, Acceleration, and Particle Motion

> **Exam Weight**: Tier 2 | **Appeared in**: 2019, 2020, 2023, 2024 | **Typical Marks**: 4

A particle's motion in space is described by its position vector $\vec{r}(t)$. Taking derivatives with respect to time $t$ gives its velocity and acceleration.

---

## The Core Formulas

Given a position vector $\vec{r}(t)$:
1. **Velocity**: $\vec{v}(t) = \frac{d\vec{r}}{dt}$
2. **Acceleration**: $\vec{a}(t) = \frac{d\vec{v}}{dt} = \frac{d^2\vec{r}}{dt^2}$

If asked for a component of velocity or acceleration in a specific direction, take the dot product of your result with the **unit vector** $\hat{u}$ of that direction.

---

## Worked Example 1: Directional Components (PYQ 2019, 2023)

**Problem**: A particle moves along $x = 2t^2, y = t^2 - 4t, z = 3t - 5$. Find the components of velocity and acceleration at $t=1$ in the direction of

$$
\vec{d} = \hat{i} - 3\hat{j} + 2\hat{k}.
$$

**Solution**:
**Step 1: Setup**
Position:

$$
\vec{r}(t) = 2t^2\hat{i} + (t^2 - 4t)\hat{j} + (3t - 5)\hat{k}
$$

Direction Unit Vector:

$$
\hat{u} = \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{1^2 + (-3)^2 + 2^2}} = \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{14}}
$$

**Step 2: Velocity**

$$
\vec{v}(t) = \frac{d\vec{r}}{dt} = 4t\hat{i} + (2t - 4)\hat{j} + 3\hat{k}
$$

At $t=1$:

$$
\vec{v}(1) = 4\hat{i} - 2\hat{j} + 3\hat{k}
$$

Component in direction $\hat{u}$:

$$
v_d = \vec{v}(1) \cdot \hat{u} = (4\hat{i} - 2\hat{j} + 3\hat{k}) \cdot \left( \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{14}} \right) = \frac{4(1) - 2(-3) + 3(2)}{\sqrt{14}} = \frac{4 + 6 + 6}{\sqrt{14}} = \frac{16}{\sqrt{14}}
$$

**Step 3: Acceleration**

$$
\vec{a}(t) = \frac{d\vec{v}}{dt} = 4\hat{i} + 2\hat{j}
$$

At $t=1$:

$$
\vec{a}(1) = 4\hat{i} + 2\hat{j}
$$

(Acceleration is constant)
Component in direction $\hat{u}$:

$$
a_d = \vec{a}(1) \cdot \hat{u} = (4\hat{i} + 2\hat{j}) \cdot \left( \frac{\hat{i} - 3\hat{j} + 2\hat{k}}{\sqrt{14}} \right) = \frac{4(1) + 2(-3) + 0}{\sqrt{14}} = \frac{4 - 6}{\sqrt{14}} = -\frac{2}{\sqrt{14}}
$$

---

## Worked Example 2: Trigonometric Motion (PYQ 2024)

**Problem**: A particle moves so that its position vector is

$$
\vec{r} = \cos \omega t \hat{i} + \sin \omega t \hat{j}
$$

where $\omega$ is constant. Show that velocity $\vec{v}$ is perpendicular to $\vec{r}$, and that $\vec{r} \times \vec{v}$ is a constant vector.

**Solution**:
**Step 1: Velocity**

$$
\vec{v} = \frac{d\vec{r}}{dt} = -\omega \sin \omega t \hat{i} + \omega \cos \omega t \hat{j}
$$

**Step 2: Show Perpendicular**

$$
\vec{r} \cdot \vec{v} = (\cos \omega t)(-\omega \sin \omega t) + (\sin \omega t)(\omega \cos \omega t) = -\omega \sin \omega t \cos \omega t + \omega \sin \omega t \cos \omega t = 0
$$

Since the dot product is zero, $\vec{v}$ is perpendicular to $\vec{r}$.

**Step 3: Show Constant Cross Product**

$$
\vec{r} \times \vec{v} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \cos \omega t & \sin \omega t & 0 \\ -\omega \sin \omega t & \omega \cos \omega t & 0 \end{vmatrix}
$$

$$
= \hat{k} \left[ (\cos \omega t)(\omega \cos \omega t) - (\sin \omega t)(-\omega \sin \omega t) \right] = \hat{k}(\omega \cos^2 \omega t + \omega \sin^2 \omega t)
$$

$$
= \omega(\cos^2 \omega t + \sin^2 \omega t)\hat{k} = \omega\hat{k}
$$

Since $\omega$ is a constant, $\omega\hat{k}$ is a constant vector.

---

## Exam Patterns
- When asked for a "component in the direction of", do not forget to divide the direction vector by its magnitude to make it a unit vector before dotting.
- Simple derivatives involving $e^t$, $\sin$, and $\cos$ are common. Remember the chain rule for arguments like $\omega t$ or $3t$.

---

[← Previous: A04 Vector Differentiation](A04_Vector_Differentiation.md) | [Index](00_Index.md) | [Next: A06 Curvature and Torsion →](A06_Curvature_Torsion_Frenet_Serret.md)
