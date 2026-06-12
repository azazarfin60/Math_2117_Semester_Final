# Lecture 04: Vector Calculus - Concept of Directional Derivative

> **Series**: Vector Calculus by Bhagwan Singh Vishwakarma
> **Lecture**: 04 of 14
> **Video**: https://www.youtube.com/watch?v=UcEozy_ig_U

---

**Navigation**
[< Previous Lecture](03_Gradient.md) | [Index](README.md) | [Next Lecture >](05_Curl_and_Divergence.md)

---

## Prerequisites
We previously learned that the gradient of a scalar point function $\phi$, denoted by $\nabla\phi$, gives a vector that is perfectly normal (perpendicular) to the surface. But what if we want to know how the surface changes in an arbitrary direction, not just the normal direction? 

---

## Directional Derivative

The **Directional Derivative (D.D.)** is the rate of change of a scalar surface $\phi(x,y,z)$ at a specific point $P(x_1, y_1, z_1)$ along the direction of a given vector $\vec{a}$. 

To calculate it, we evaluate the gradient of $\phi$ at the given point, and then project it onto the desired direction by taking the dot product with the unit vector $\hat{a}$.

$$
\text{D.D.} = \frac{d\phi}{ds} = \hat{a} \cdot \nabla\phi
$$

Where:
- $\nabla\phi$ is the gradient vector evaluated at point $P$.
- $\hat{a} = \frac{\vec{a}}{\lvert \vec{a} \rvert}$ is the unit vector in the direction of vector $\vec{a}$.

Because the dot product yields a scalar, the directional derivative is a scalar magnitude.

### Maximum Directional Derivative
The dot product $\hat{a} \cdot \nabla\phi$ equals $\lvert \nabla\phi \rvert \cos\theta$. This value is maximized when $\cos\theta = 1$, which occurs when $\theta = 0$. 

This means the directional derivative is **maximum in the exact direction of the normal vector** ($\nabla\phi$). 
The maximum possible magnitude of the directional derivative is simply the magnitude of the gradient:

$$
\text{Max D.D.} = |\nabla\phi|
$$

### Unit Normal Vector
Since the gradient $\nabla\phi$ provides a vector normal to the surface, we can easily find the **unit normal vector** $\hat{n}$ by dividing the gradient by its own magnitude:

$$
\hat{n} = \frac{\nabla\phi}{|\nabla\phi|}
$$

---

## Solved Problems

### Problem 1: Basic Directional Derivative
**Question:** Find the directional derivative of $\phi = (x^2 + y^2 + z^2)^{-1/2}$ at the point $P(3, 1, 2)$ in the direction of the vector

$$
\vec{a} = yz\hat{i} + zx\hat{j} + xy\hat{k}.
$$


**Solution:**
First, compute the gradient $\nabla\phi$:

$$
\frac{\partial\phi}{\partial x} = -\frac{1}{2}(x^2 + y^2 + z^2)^{-3/2}(2x) = -x(x^2 + y^2 + z^2)^{-3/2}
$$

By symmetry, we get similar terms for $y$ and $z$.

$$
\nabla\phi = -(x^2 + y^2 + z^2)^{-3/2}(x\hat{i} + y\hat{j} + z\hat{k})
$$

Evaluate the gradient at $P(3, 1, 2)$:

$$
x^2 + y^2 + z^2 = 3^2 + 1^2 + 2^2 = 14
$$

$$
\nabla\phi|_{(3,1,2)} = \frac{-(3\hat{i} + \hat{j} + 2\hat{k})}{14\sqrt{14}}
$$

Next, find the unit vector $\hat{a}$ along $\vec{a}$ at the point $P(3,1,2)$:

$$
\vec{a}|_{(3,1,2)} = (1)(2)\hat{i} + (2)(3)\hat{j} + (3)(1)\hat{k} = 2\hat{i} + 6\hat{j} + 3\hat{k}
$$

$$
|\vec{a}| = \sqrt{2^2 + 6^2 + 3^2} = \sqrt{49} = 7 \implies \hat{a} = \frac{2\hat{i} + 6\hat{j} + 3\hat{k}}{7}
$$

Finally, take the dot product $\hat{a} \cdot \nabla\phi$:

$$
\text{D.D.} = \left(\frac{2\hat{i} + 6\hat{j} + 3\hat{k}}{7}\right) \cdot \left(\frac{-(3\hat{i} + \hat{j} + 2\hat{k})}{14\sqrt{14}}\right)
$$

$$
\text{D.D.} = \frac{-[2(3) + 6(1) + 3(2)]}{98\sqrt{14}} = \frac{-18}{98\sqrt{14}} = -\frac{9}{49\sqrt{14}}
$$

### Problem 2: Direction Defined by Points
**Question:** Find the directional derivative of $\phi = x^2 - y^2 + 2z^2$ at the point $P(1, 2, 3)$ in the direction of the line $PQ$, where $Q$ is the point $(5, 0, 4)$.

**Solution:**
First, compute the gradient and evaluate it at $P(1, 2, 3)$:

$$
\nabla\phi = 2x\hat{i} - 2y\hat{j} + 4z\hat{k}
$$

$$
\nabla\phi|_{(1,2,3)} = 2(1)\hat{i} - 2(2)\hat{j} + 4(3)\hat{k} = 2\hat{i} - 4\hat{j} + 12\hat{k}
$$

Next, construct the direction vector $\vec{PQ}$:

$$
\vec{PQ} = \vec{OQ} - \vec{OP} = (5\hat{i} + 0\hat{j} + 4\hat{k}) - (\hat{i} + 2\hat{j} + 3\hat{k}) = 4\hat{i} - 2\hat{j} + \hat{k}
$$

Find the unit vector $\hat{a}$:

$$
|\vec{PQ}| = \sqrt{16 + 4 + 1} = \sqrt{21} \implies \hat{a} = \frac{4\hat{i} - 2\hat{j} + \hat{k}}{\sqrt{21}}
$$

Compute the directional derivative $\hat{a} \cdot \nabla\phi$:

$$
\text{D.D.} = \left(\frac{4\hat{i} - 2\hat{j} + \hat{k}}{\sqrt{21}}\right) \cdot (2\hat{i} - 4\hat{j} + 12\hat{k}) = \frac{8 + 8 + 12}{\sqrt{21}} = \frac{28}{\sqrt{21}}
$$

### Problem 3: Finding Unknown Constants
**Question:** Find the constants $a, b, c$ so that the directional derivative of $\phi = axy^2 + byz + cz^2x^3$ at the point $(1, 2, -1)$ has a maximum magnitude of $64$ in the direction parallel to the $Z$-axis.

**Solution:**
First, compute the gradient and evaluate at $(1, 2, -1)$:

$$
\nabla\phi = (ay^2 + 3cz^2x^2)\hat{i} + (2axy + bz)\hat{j} + (by + 2czx^3)\hat{k}
$$

$$
\nabla\phi|_{(1,2,-1)} = (4a + 3c)\hat{i} + (4a - b)\hat{j} + (2b - 2c)\hat{k}
$$

The directional derivative is maximum in the direction of the gradient. For this maximum to occur parallel to the $Z$-axis (the $\hat{k}$ direction), the $\hat{i}$ and $\hat{j}$ components must be zero:
1.  $4a + 3c = 0 \implies c = -\frac{4}{3}a$
2.  $4a - b = 0 \implies b = 4a$

Also, the magnitude of the gradient must equal the maximum magnitude of $64$. Since only the $\hat{k}$ component survives, it must be positive and equal to $64$:

$$
2b - 2c = 64 \implies b - c = 32
$$

Substitute $b$ and $c$ in terms of $a$:

$$
4a - \left(-\frac{4}{3}a\right) = 32 \implies \frac{16}{3}a = 32 \implies a = 6
$$

Now, substitute $a = 6$ back to find $b$ and $c$:

$$
b = 4(6) = 24
$$

$$
c = -\frac{4}{3}(6) = -8
$$

Final Answer: $a = 6, b = 24, c = -8$.

### Problem 4: Angle Between Surfaces
**Question:** Find the angle between the surfaces $x^2 + y^2 + z^2 = 9$ and $z = x^2 + y^2 - 3$ at the point $(2, -1, 2)$.

**Solution:**
The angle between two surfaces is the angle between their normal vectors. Let's find the gradient of both surfaces.

$$
\phi_1 = x^2 + y^2 + z^2 - 9 \implies \nabla\phi_1 = 2x\hat{i} + 2y\hat{j} + 2z\hat{k}
$$

$$
\phi_2 = x^2 + y^2 - z - 3 \implies \nabla\phi_2 = 2x\hat{i} + 2y\hat{j} - \hat{k}
$$

Evaluate both gradients at $(2, -1, 2)$ to find the normal vectors $\vec{n}_1$ and $\vec{n}_2$:

$$
\vec{n}_1 = 4\hat{i} - 2\hat{j} + 4\hat{k}
$$

$$
\vec{n}_2 = 4\hat{i} - 2\hat{j} - \hat{k}
$$

Use the dot product formula $\cos\theta = \frac{\vec{n}_1 \cdot \vec{n}_2}{\lvert \vec{n}_1 \rvert\lvert \vec{n}_2 \rvert}$ to find the angle:

$$
|\vec{n}_1| = \sqrt{16+4+16} = 6
$$

$$
|\vec{n}_2| = \sqrt{16+4+1} = \sqrt{21}
$$

$$
\vec{n}_1 \cdot \vec{n}_2 = (4)(4) + (-2)(-2) + (4)(-1) = 16 + 4 - 4 = 16
$$

$$
\theta = \cos^{-1}\left(\frac{16}{6\sqrt{21}}\right) = \cos^{-1}\left(\frac{8}{3\sqrt{21}}\right)
$$

### Problem 5: Combined Concepts
**Question:** For the surface $\phi = x^2 yz + 4xz^2$ at the point $(1, -2, -1)$:
1. Find the directional derivative in the direction

$$
2\hat{i} - \hat{j} - 2\hat{k}.
$$

2. In what direction is the directional derivative maximum, and what is its magnitude?
3. Find the unit normal vector to the surface.

**Solution:**
First, evaluate the gradient at $(1, -2, -1)$:

$$
\nabla\phi = (2xyz + 4z^2)\hat{i} + (x^2 z)\hat{j} + (x^2 y + 8xz)\hat{k}
$$

$$
\nabla\phi|_{(1,-2,-1)} = 8\hat{i} - \hat{j} - 10\hat{k}
$$

**Part 1: Directional Derivative**
Find unit vector $\hat{a}$ for

$$
2\hat{i} - \hat{j} - 2\hat{k}:
$$

:

$$
\hat{a} = \frac{2\hat{i} - \hat{j} - 2\hat{k}}{3}
$$

$$
\text{D.D.} = \hat{a} \cdot \nabla\phi = \left(\frac{2\hat{i} - \hat{j} - 2\hat{k}}{3}\right) \cdot (8\hat{i} - \hat{j} - 10\hat{k}) = \frac{16 + 1 + 20}{3} = \frac{37}{3}
$$

**Part 2: Maximum Directional Derivative**
The maximum directional derivative is in the direction of the gradient itself:

$$
8\hat{i} - \hat{j} - 10\hat{k}.
$$

Its magnitude is $\lvert \nabla\phi \rvert$:

$$
\text{Max D.D.} = \sqrt{8^2 + (-1)^2 + (-10)^2} = \sqrt{64 + 1 + 100} = \sqrt{165}
$$

**Part 3: Unit Normal Vector**
Divide the gradient by its magnitude to find the unit normal vector:

$$
\hat{n} = \frac{\nabla\phi}{|\nabla\phi|} = \frac{8\hat{i} - \hat{j} - 10\hat{k}}{\sqrt{165}}
$$

---

## Key Takeaways
*   The directional derivative measures the rate of change of a surface along a chosen vector direction.
*   It is calculated by taking the dot product of the surface's gradient and the unit vector of the desired direction ($\hat{a} \cdot \nabla\phi$).
*   The directional derivative is maximum in the direction of the normal vector (the gradient), and its maximum value is exactly the magnitude of the gradient ($\lvert \nabla\phi \rvert$).

## What Comes Next
We have seen how the del operator $\nabla$ applies to a scalar point function to produce a gradient vector. Next, we will see what happens when we apply the del operator to a vector point function. This introduces the concepts of **Divergence** (dot product) and **Curl** (cross product).

---

**Navigation**
[< Previous Lecture](03_Gradient.md) | [Index](README.md) | [Next Lecture >](05_Curl_and_Divergence.md)
