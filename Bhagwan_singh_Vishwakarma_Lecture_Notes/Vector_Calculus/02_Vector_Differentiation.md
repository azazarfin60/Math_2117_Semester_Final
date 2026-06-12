# Lecture 02: Vector Calculus - Vector Differentiation

> **Series**: Vector Calculus by Bhagwan Singh Vishwakarma
> **Lecture**: 02 of 14
> **Video**: https://www.youtube.com/watch?v=t-xP272h8Xc

---

**Navigation**
[< Previous Lecture](01_Scalar_Vector_Point_Function.md) | [Index](README.md) | [Next Lecture >](03_Gradient.md)

---

## Prerequisites
In the previous lecture, we learned that a vector point function outputs a vector for any given point in space. Since these outputs are vectors that change depending on the input variables, we can study how fast they change using differentiation.

---

## Vector Differential Coefficients

When a vector point function $\vec{F}$ depends on multiple variables like $x, y$, and $z$, we use partial differentiation. The derivatives we find are called **Vector Differential Coefficients**.

Let us take an example:

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

## Ordinary Vector Differentiation

Often, a vector function depends on a single scalar parameter, like time $t$. For example, the position vector $\vec{r}$ of a moving particle. In this case, we use ordinary differentiation notation: $\frac{d\vec{r}}{dt}$.

*   **Velocity**: The first derivative of a position vector with respect to time gives the velocity vector $\vec{v}$.

$$
    \vec{v} = \frac{d\vec{r}}{dt}
$$

*   **Acceleration**: The second derivative of the position vector gives the acceleration vector $\vec{a}$.

$$
    \vec{a} = \frac{d^2\vec{r}}{dt^2}
$$

## Solved Problems

### Problem 1: Velocity and Acceleration
**Question:** If a position vector is given by

$$
\vec{r} = a \cos t\hat{i} + a \sin t\hat{j} + t\hat{k},
$$

Find the velocity, the acceleration, and the magnitude of the acceleration.

**Solution:**
First, find velocity by differentiating once:

$$
\vec{v} = \frac{d\vec{r}}{dt} = -a \sin t\hat{i} + a \cos t\hat{j} + \hat{k}
$$

Next, find acceleration by differentiating again:

$$
\vec{a} = \frac{d^2\vec{r}}{dt^2} = -a \cos t\hat{i} - a \sin t\hat{j}
$$

Finally, find the magnitude of the acceleration:

$$
\left| \frac{d^2\vec{r}}{dt^2} \right| = \sqrt{(-a\cos t)^2 + (-a\sin t)^2 + 0^2} = \sqrt{a^2(\cos^2 t + \sin^2 t)} = a
$$

### Problem 2: Dot Product Differentiation
**Question:** If

$$
\vec{u} = t^2\hat{i} - t\hat{j} + (2t+1)\hat{k}
$$

 and

$$
\vec{v} = (2t-3)\hat{i} + \hat{j} - t\hat{k},
$$

Find $\frac{d}{dt}(\vec{u} \cdot \vec{v})$ at $t=1$.

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

Finally, evaluate at $t=1$:

$$
\left. \frac{d}{dt}(\vec{u} \cdot \vec{v}) \right|_{t=1} = 6(1)^2 - 10(1) - 2 = 6 - 10 - 2 = -6
$$

### Problem 3: Exponential Derivative Identity
**Question:** If $\vec{r} = \vec{a} e^{nt} + \vec{b} e^{-nt}$, where $\vec{a}$ and $\vec{b}$ are constant vectors, prove that $\frac{d^2\vec{r}}{dt^2} - n^2\vec{r} = 0$.

**Solution:**
Compute the first derivative. Since $\vec{a}$ and $\vec{b}$ are constant, only the exponential terms change:

$$
\frac{d\vec{r}}{dt} = n\vec{a}e^{nt} - n\vec{b}e^{-nt}
$$

Compute the second derivative:

$$
\frac{d^2\vec{r}}{dt^2} = n^2\vec{a}e^{nt} + (-n)^2\vec{b}e^{-nt}
$$

$$
\frac{d^2\vec{r}}{dt^2} = n^2(\vec{a}e^{nt} + \vec{b}e^{-nt})
$$

Notice that the term inside the brackets is our original vector $\vec{r}$:

$$
\frac{d^2\vec{r}}{dt^2} = n^2\vec{r}
$$

Rearranging gives the final proof:

$$
\frac{d^2\vec{r}}{dt^2} - n^2\vec{r} = 0
$$

### Problem 4: Position Vector and Kinematics
**Question:** A particle moves so that its position vector is given by

$$
\vec{r} = \cos \omega t\hat{i} + \sin \omega t\hat{j},
$$

Where $\omega$ is a constant. Show that the velocity $\vec{v}$ is perpendicular to $\vec{r}$, and that the acceleration $\vec{a}$ is directed towards the origin.

**Solution:**
First, compute velocity:

$$
\vec{v} = \frac{d\vec{r}}{dt} = -\omega \sin \omega t\hat{i} + \omega \cos \omega t\hat{j}
$$

To check if they are perpendicular, compute the dot product:

$$
\vec{v} \cdot \vec{r} = (-\omega \sin \omega t)(\cos \omega t) + (\omega \cos \omega t)(\sin \omega t) = 0
$$

Since the dot product is $0$, the velocity is perpendicular to the position vector.

Next, compute acceleration:

$$
\vec{a} = \frac{d^2\vec{r}}{dt^2} = -\omega^2 \cos \omega t\hat{i} - \omega^2 \sin \omega t\hat{j}
$$

$$
\vec{a} = -\omega^2(\cos \omega t\hat{i} + \sin \omega t\hat{j}) = -\omega^2 \vec{r}
$$

The negative sign indicates that the acceleration vector points exactly opposite to the position vector. Because the position vector points away from the origin, the acceleration is directed straight towards the origin.

---

## Key Takeaways

*   Differentiating a vector point function yields a new vector representing the rate of change.
*   If a vector function depends on time $t$, its first derivative gives velocity, and its second derivative gives acceleration.
*   The standard derivative rules (like product rules and chain rules) apply directly to vector components.

## What Comes Next
With the foundation of vector differentiation set, we are ready to introduce the powerful del operator ($\nabla$). In the next lecture, we will explore the **gradient** of a scalar field and its geometric meaning.

---

**Navigation**
[< Previous Lecture](01_Scalar_Vector_Point_Function.md) | [Index](README.md) | [Next Lecture >](03_Gradient.md)
