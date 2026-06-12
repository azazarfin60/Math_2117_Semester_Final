# Lecture 01: Vector Calculus - Concept of Scalar and Vector Point Function

> **Series**: Vector Calculus by Bhagwan Singh Vishwakarma
> **Lecture**: 01 of 14
> **Video**: https://www.youtube.com/watch?v=Y4ZFbx4OuAE

---

**Navigation**
[Index](README.md) | [Next Lecture >](02_Vector_Differentiation.md)

---

## Prerequisites
Before we dive into vector calculus, we must review basic vectors from high school. A scalar is a quantity with only magnitude, like speed or weight. A vector has both magnitude and direction, like velocity. 

We represent a point in 3D space with a position vector from the origin $O$ to a point $A$. We call this $\vec{OA}$. We define vectors using the unit vectors $\hat{i}$, $\hat{j}$, and $\hat{k}$ along the $X$, $Y$, and $Z$ axes.

We also have two ways to multiply vectors:
1.  **Scalar Product (Dot Product)**: The result is a scalar number.

$$
\vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2 + a_3 b_3
$$

2.  **Vector Product (Cross Product)**: The result is a new vector that is perpendicular to both original vectors.

$$
\vec{a} \times \vec{b} =
\begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
a_1 & a_2 & a_3 \\
b_1 & b_2 & b_3
\end{vmatrix}
$$

---

## Scalar Point Functions

Imagine a region $R$ in 3D space. This is our domain. We can pick any point $(x, y, z)$ from this space. 

A **scalar point function** acts like a magic box. You put a 3D point into the box, and it outputs a single real number (a scalar). It maps a point from 3D space to 1D space.

Here is an example of a scalar point function:

$$
f(x, y, z) = xy + x^2z
$$

Notice there are no $\hat{i}$, $\hat{j}$, or $\hat{k}$ unit vectors here. Let us evaluate this function at the point $(1, 2, -1)$:

$$
f(1, 2, -1) = (1)(2) + (1)^2(-1) = 2 - 1 = 1
$$

The output is $1$, which is a pure scalar number. 

Other examples of scalar point functions include:
- $f(x, y, z) = x y z^2$
- $f(x, y, z) = x y z + x^2 y^2$

Physical examples include temperature fields or density fields. At every point in a room, there is a specific temperature number, but no direction.

---

## Vector Point Functions

A **vector point function** is a different kind of magic box. You input a 3D point, and it outputs a vector. It maps a point from 3D space to a new vector in 3D space.

Because the output is a vector, the function rule will always contain the unit vectors $\hat{i}$, $\hat{j}$, and $\hat{k}$.

Here is an example of a vector point function:

$$
\vec{F}(x, y, z) = xy\hat{i} + x^2z\hat{j} + y\hat{k}
$$

Let us evaluate this function at the same point $(1, 2, -1)$:

$$
\vec{F}(1, 2, -1) = (1)(2)\hat{i} + (1)^2(-1)\hat{j} + (2)\hat{k}
$$

Simplify the math:

$$
\vec{F}(1, 2, -1) = 2\hat{i} - \hat{j} + 2\hat{k}
$$

The output is a vector. This vector has both a magnitude and a direction. 

Other examples of vector point functions include:
-

$$
\vec{F}(x, y, z) = x^2\hat{i} + yz\hat{j} + z^2\hat{k}
$$

-

$$
\vec{F}(x, y, z) = x\hat{i} + y^2\hat{j} + xyz\hat{k}
$$

Physical examples include velocity fields of fluid flow or gravitational force fields. At every point in space, gravity pulls with a specific strength (magnitude) in a specific direction.

---

## Key Takeaways

*   **Scalar Point Function**: Input is a 3D point. Output is a scalar number. The function formula has no unit vectors.
*   **Vector Point Function**: Input is a 3D point. Output is a vector. The function formula uses $\hat{i}$, $\hat{j}$, and $\hat{k}$.
*   Vector calculus lets us study these 3D functions just like we study standard 1D functions in normal calculus.

## What Comes Next
Now that we know what scalar and vector point functions are, we will learn how to differentiate them. The next lecture covers vector differentiation, limits, and continuity.

---

**Navigation**
[Index](README.md) | [Next Lecture >](02_Vector_Differentiation.md)
