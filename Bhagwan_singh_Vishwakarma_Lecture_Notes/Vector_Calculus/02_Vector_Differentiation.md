# Lecture 02: Vector Differentiation

> **Series**: Vector Calculus
> **Lecture**: 02 of 14
> **Video**: https://www.youtube.com/watch?v=t-xP272h8Xc

---

**Navigation**
[< Previous Lecture](01_Scalar_Vector_Point_Function.md) | [Index](README.md) | [Next Lecture >](03_Gradient.md)

---

## Prerequisites
In the previous lecture, we learned that a vector point function outputs a vector for any given point in space. Since these outputs are vectors that change depending on the input variables, we can study how fast they change using differentiation.

---

## 1. Vector Differential Coefficients

When a vector point function $\vec{F}$ depends on multiple variables like $x, y$, and $z$, we use partial differentiation. The derivatives we find are called **Vector Differential Coefficients**.

Let us take an example vector field function:
$$
\vec{F}(x,y,z) = x^2\hat{i} + y^2z\hat{j} + z\hat{k}
$$

We can differentiate this partially with respect to $x$:
$$
\frac{\partial \vec{F}}{\partial x} = 2x\hat{i} + 0\hat{j} + 0\hat{k} = 2x\hat{i}
$$

Similarly, with respect to $y$ and $z$:
$$
\frac{\partial \vec{F}}{\partial y} = 2yz\hat{j}
$$
$$
\frac{\partial \vec{F}}{\partial z} = y^2\hat{j} + \hat{k}
$$
Notice that the result of differentiating a vector point function is always another vector point function.

---

## 2. Ordinary Vector Differentiation

If a vector function depends on a single scalar parameter, like time $t$, we use ordinary differentiation notation: $\frac{d\vec{r}}{dt}$.
Example: $\vec{F}(t) = t^2\hat{i} + (t^2+3)\hat{j} + t^3\hat{k}$

*   **Velocity**: The first derivative gives the velocity vector $\vec{v}$.
    $$
    \vec{v} = \frac{d\vec{F}}{dt} = 2t\hat{i} + 2t\hat{j} + 3t^2\hat{k}
    $$
*   **Acceleration**: The second derivative gives the acceleration vector $\vec{a}$.
    $$
    \vec{a} = \frac{d^2\vec{F}}{dt^2} = 2\hat{i} + 2\hat{j} + 6t\hat{k}
    $$

---

## 3. Solved Problems

### Problem 1: Derivative of a Vector
**Question:** If $\vec{r} = a \cos t\hat{i} + a \sin t\hat{j} + t\hat{k}$, find $\frac{d\vec{r}}{dt}$, $\frac{d^2\vec{r}}{dt^2}$ and $\left|\frac{d^2\vec{r}}{dt^2}\right|$.

**Solution:**
First, find velocity by differentiating once:
$$
\frac{d\vec{r}}{dt} = -a \sin t\hat{i} + a \cos t\hat{j} + \hat{k}
$$

Next, find acceleration by differentiating again:
$$
\frac{d^2\vec{r}}{dt^2} = -a \cos t\hat{i} - a \sin t\hat{j}
$$

Finally, find the magnitude of the acceleration:
$$
\left| \frac{d^2\vec{r}}{dt^2} \right| = \sqrt{(-a\cos t)^2 + (-a\sin t)^2 + 0^2} = \sqrt{a^2(\cos^2 t + \sin^2 t)} = a
$$

### Problem 2: Dot Product Differentiation
**Question:** If $\vec{u} = t^2\hat{i} - t\hat{j} + (2t+1)\hat{k}$ and $\vec{v} = (2t-3)\hat{i} + \hat{j} - t\hat{k}$, find $\frac{d}{dt}(\vec{u} \cdot \vec{v})$ at $t=1$.

**Solution:**
First, compute the dot product algebraically:
$$
\vec{u} \cdot \vec{v} = (t^2)(2t-3) + (-t)(1) + (2t+1)(-t)
$$
$$
\vec{u} \cdot \vec{v} = 2t^3 - 3t^2 - t - 2t^2 - t = 2t^3 - 5t^2 - 2t
$$

Now, differentiate the result with respect to $t$:
$$
\frac{d}{dt}(\vec{u} \cdot \vec{v}) = \frac{d}{dt}(2t^3 - 5t^2 - 2t) = 6t^2 - 10t - 2
$$

Evaluate at $t=1$:
$$
\left. \frac{d}{dt}(\vec{u} \cdot \vec{v}) \right|_{t=1} = 6(1)^2 - 10(1) - 2 = 6 - 10 - 2 = -6
$$

### Problem 3: Exponential Derivative Identity
**Question:** If $\vec{r} = \vec{a} e^{nt} + \vec{b} e^{-nt}$, where $\vec{a}$ and $\vec{b}$ are constant vectors, prove that $\frac{d^2\vec{r}}{dt^2} - n^2\vec{r} = 0$.

**Solution:**
Compute the first derivative:
$$
\frac{d\vec{r}}{dt} = n\vec{a}e^{nt} - n\vec{b}e^{-nt}
$$

Compute the second derivative:
$$
\frac{d^2\vec{r}}{dt^2} = n^2\vec{a}e^{nt} + (-n)^2\vec{b}e^{-nt} = n^2(\vec{a}e^{nt} + \vec{b}e^{-nt})
$$

Notice the term inside the brackets is $\vec{r}$:
$$
\frac{d^2\vec{r}}{dt^2} = n^2\vec{r} \implies \frac{d^2\vec{r}}{dt^2} - n^2\vec{r} = 0 \quad \text{(Proved)}
$$

### Problem 4: Trigonometric Derivative Identity
**Question:** If $\vec{r} = (\cos nt)\hat{i} + (\sin nt)\hat{j}$, prove that $\frac{d^2\vec{r}}{dt^2} = -n^2\vec{r}$.

**Solution:**
First derivative:
$$
\frac{d\vec{r}}{dt} = -n\sin nt\hat{i} + n\cos nt\hat{j}
$$
Second derivative:
$$
\frac{d^2\vec{r}}{dt^2} = -n^2\cos nt\hat{i} - n^2\sin nt\hat{j} = -n^2(\cos nt\hat{i} + \sin nt\hat{j}) = -n^2\vec{r} \quad \text{(Proved)}
$$

### Problem 5: Cross Product Differentiation
**Question:** If $\vec{r} = (5t^2)\hat{i} + t\hat{j} - t^3\hat{k}$ and $\vec{s} = (\sin t)\hat{i} - (\cos t)\hat{j}$, find the value of $\frac{d}{dt}(\vec{r} \times \vec{s})$.

**Solution:**
First, compute the cross product determinant:
$$
\vec{r} \times \vec{s} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 5t^2 & t & -t^3 \\ \sin t & -\cos t & 0 \end{vmatrix}
$$
$$
\vec{r} \times \vec{s} = (-t^3 \cos t)\hat{i} - (t^3\sin t)\hat{j} + (-5t^2\cos t - t\sin t)\hat{k}
$$

Take the derivative using product rule on each component:
$$
\frac{d}{dt}(\vec{r} \times \vec{s}) = \left(-3t^2 \cos t + t^3 \sin t\right)\hat{i} - \left(3t^2 \sin t + t^3 \cos t\right)\hat{j} - \left(10t \cos t - 5t^2 \sin t + \sin t + t \cos t\right)\hat{k}
$$
Simplify:
$$
\frac{d}{dt}(\vec{r} \times \vec{s}) = \left(t^3 \sin t - 3t^2 \cos t\right)\hat{i} - \left(3t^2 \sin t + t^3 \cos t\right)\hat{j} - \left(11t\cos t - 5t^2 \sin t + \sin t\right)\hat{k}
$$

### Problem 6: Unit Vector Identity
**Question:** Show that $\vec{R} \times d\vec{R} = \frac{\vec{r} \times d\vec{r}}{r^2}$, where $\vec{R} = \frac{\vec{r}}{r}$ (unit vector).

**Solution:**
Differentiate $\vec{R}$:
$$
d\vec{R} = d\left(\frac{\vec{r}}{r}\right) = d\left(\frac{1}{r} \vec{r}\right) = \frac{1}{r} d\vec{r} + d\left(\frac{1}{r}\right)\vec{r} = \frac{1}{r} d\vec{r} - \frac{1}{r^2} dr \vec{r}
$$

Now compute the cross product $\vec{R} \times d\vec{R}$:
$$
\vec{R} \times d\vec{R} = \left(\frac{\vec{r}}{r}\right) \times \left( \frac{1}{r} d\vec{r} - \frac{dr}{r^2} \vec{r} \right) = \frac{\vec{r} \times d\vec{r}}{r^2} - \frac{dr}{r^3} (\vec{r} \times \vec{r})
$$

Since the cross product of any vector with itself is zero ($\vec{r} \times \vec{r} = 0$), we have:
$$
\vec{R} \times d\vec{R} = \frac{\vec{r} \times d\vec{r}}{r^2} \quad \text{(Proved)}
$$

### Problem 7: Vector Cross Derivative Identity
**Question:** If $\frac{d\vec{a}}{dt} = \vec{r} \times \vec{a}$ and $\frac{d\vec{b}}{dt} = \vec{r} \times \vec{b}$, show that $\frac{d}{dt}(\vec{a} \times \vec{b}) = \vec{r} \times (\vec{a} \times \vec{b})$.

**Solution:**
Apply the derivative product rule for cross products:
$$
\frac{d}{dt}(\vec{a} \times \vec{b}) = \frac{d\vec{a}}{dt} \times \vec{b} + \vec{a} \times \frac{d\vec{b}}{dt}
$$
Substitute the given relationships:
$$
\frac{d}{dt}(\vec{a} \times \vec{b}) = (\vec{r} \times \vec{a}) \times \vec{b} + \vec{a} \times (\vec{r} \times \vec{b})
$$

Using the vector triple product identity $\vec{x} \times (\vec{y} \times \vec{z}) = (\vec{x} \cdot \vec{z})\vec{y} - (\vec{x} \cdot \vec{y})\vec{z}$:
*   First term: $(\vec{r} \times \vec{a}) \times \vec{b} = -\vec{b} \times (\vec{r} \times \vec{a}) = -[(\vec{b} \cdot \vec{a})\vec{r} - (\vec{b} \cdot \vec{r})\vec{a}] = (\vec{r} \cdot \vec{b})\vec{a} - (\vec{a} \cdot \vec{b})\vec{r}$
*   Second term: $\vec{a} \times (\vec{r} \times \vec{b}) = (\vec{a} \cdot \vec{b})\vec{r} - (\vec{a} \cdot \vec{r})\vec{b}$

Add the two terms:
$$
\frac{d}{dt}(\vec{a} \times \vec{b}) = (\vec{r} \cdot \vec{b})\vec{a} - (\vec{a} \cdot \vec{b})\vec{r} + (\vec{a} \cdot \vec{b})\vec{r} - (\vec{a} \cdot \vec{r})\vec{b} = (\vec{r} \cdot \vec{b})\vec{a} - (\vec{r} \cdot \vec{a})\vec{b}
$$

By the vector triple product definition, this expands exactly to:
$$
\vec{r} \times (\vec{a} \times \vec{b}) = (\vec{r} \cdot \vec{b})\vec{a} - (\vec{r} \cdot \vec{a})\vec{b}
$$

Hence:
$$
\frac{d}{dt}(\vec{a} \times \vec{b}) = \vec{r} \times (\vec{a} \times \vec{b}) \quad \text{(Proved)}
$$

### Problem 8: Position Vector and Kinematics
**Question:** A particle moves so that its position vector is given by $\vec{r} = \cos \omega t\hat{i} + \sin \omega t\hat{j}$, where $\omega$ is a constant. Show that:
1.  The velocity $\vec{v}$ of the particle is perpendicular to $\vec{r}$.
2.  The acceleration $\vec{a}$ is directed towards the origin and has magnitude proportional to the distance from the origin.
3.  $\vec{r} \times \vec{v} = \text{a constant vector}$.

**Solution:**
**(1) Perpendicular Velocity**
Compute velocity:
$$
\vec{v} = \frac{d\vec{r}}{dt} = -\omega \sin \omega t\hat{i} + \omega \cos \omega t\hat{j}
$$
Compute the dot product to check for perpendicularity:
$$
\vec{v} \cdot \vec{r} = (-\omega \sin \omega t)(\cos \omega t) + (\omega \cos \omega t)(\sin \omega t) = 0
$$
Since $\vec{v} \cdot \vec{r} = 0$, the velocity is perpendicular to the position vector ($\vec{v} \perp \vec{r}$).

**(2) Acceleration Directed to Origin**
Compute acceleration:
$$
\vec{a} = \frac{d^2\vec{r}}{dt^2} = -\omega^2 \cos \omega t\hat{i} - \omega^2 \sin \omega t\hat{j} = -\omega^2(\cos \omega t\hat{i} + \sin \omega t\hat{j}) = -\omega^2 \vec{r}
$$
The negative sign indicates the direction of acceleration is opposite to the position vector (directed towards the origin).
Magnitude: $|\vec{a}| = |-\omega^2 \vec{r}| = \omega^2 |\vec{r}|$, which is proportional to the distance from the origin.

**(3) Constant Cross Product**
Compute $\vec{r} \times \vec{v}$:
$$
\vec{r} \times \vec{v} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ \cos \omega t & \sin \omega t & 0 \\ -\omega\sin\omega t & \omega\cos\omega t & 0 \end{vmatrix} = \hat{k} (\omega\cos^2\omega t - (-\omega\sin^2\omega t))
$$
$$
\vec{r} \times \vec{v} = \omega(\cos^2\omega t + \sin^2\omega t)\hat{k} = \omega\hat{k}
$$
Since $\omega$ is constant and $\hat{k}$ is a fixed unit vector, $\vec{r} \times \vec{v} = \omega\hat{k}$ is a constant vector. (Proved)

---

## 4. Practice Problems
1. If $\vec{r} = t^2\hat{i} - t\hat{j} + (2t+1)\hat{k}$, find at $t = 0$, the values of:
   - $\frac{d\vec{r}}{dt}$
   - $\frac{d^2\vec{r}}{dt^2}$
   - $\left|\frac{d\vec{r}}{dt}\right|$
   - $\left|\frac{d^2\vec{r}}{dt^2}\right|$

---

## What Comes Next
With the foundation of vector differentiation set, we are ready to introduce the powerful del operator ($\nabla$). In the next lecture, we will explore the **gradient** of a scalar field and its geometric meaning.

---

**Navigation**
[< Previous Lecture](01_Scalar_Vector_Point_Function.md) | [Index](README.md) | [Next Lecture >](03_Gradient.md)
