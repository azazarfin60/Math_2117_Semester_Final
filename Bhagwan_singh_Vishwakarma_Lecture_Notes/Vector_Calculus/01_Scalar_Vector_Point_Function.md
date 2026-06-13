# Lecture 01: Concept of Scalar and Vector Point Function

> **Series**: Vector Calculus
> **Lecture**: 01 of 14
> **Video**: https://www.youtube.com/watch?v=Y4ZFbx4OuAE

---

**Navigation**
[Index](README.md) | [Next Lecture >](02_Vector_Differentiation.md)

---

## Prerequisites
Before diving into vector calculus, let's recall basic vector algebra from high school. A **scalar** is a quantity with only magnitude (e.g., speed, number). A **vector** has both magnitude and direction (e.g., velocity). 

### Position Vectors
In a 3D Cartesian coordinate system ($X, Y, Z$) with unit vectors $\hat{i}, \hat{j}, \hat{k}$, we represent a point $A$ in 3D space with a **position vector** starting from the origin $O$ to point $A$. We denote this vector as $\vec{OA}$.

### Vector Multiplication
We have two ways to multiply vectors $\vec{a} = a_1\hat{i} + a_2\hat{j} + a_3\hat{k}$ and $\vec{b} = b_1\hat{i} + b_2\hat{j} + b_3\hat{k}$:
1.  **Scalar Product (Dot Product)**: The result is a scalar number.
    $$
    \vec{a} \cdot \vec{b} = a_1 b_1 + a_2 b_2 + a_3 b_3
    $$
2.  **Vector Product (Cross Product)**: The result is a new vector perpendicular to both original vectors.
    $$
    \vec{a} \times \vec{b} = |\vec{a}| |\vec{b}| \sin\theta \hat{n} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3 \end{vmatrix}
    $$

---

## 1. Scalar Point Functions

Imagine a region or domain $R$ in 3D space where we can pick any point $(x, y, z)$. 

A **scalar point function** maps a 3D point from this domain to a single real number (a scalar). The output is a 1D scalar value.

**Block Diagram Representation:**
`[Input (3D point)]` $\rightarrow$ `[Scalar Point Function]` $\rightarrow$ `[Scalar (Real Number)]`

### Example
Consider the scalar point function:
$$
f(x, y, z) = xy + x^2z
$$
Notice there are no unit vectors ($\hat{i}, \hat{j}, \hat{k}$) in the expression. Let us evaluate this function at the specific point $(1, 2, -1)$:
$$
f(1, 2, -1) = (1)(2) + (1)^2(-1) = 2 - 1 = 1
$$
The output is $1$, which is a pure scalar number. 

Other examples of scalar point functions:
*   $f(x, y, z) = x y z^2$
*   $f(x, y, z) = x y z + x^2 y^2$

---

## 2. Vector Point Functions

A **vector point function** maps a 3D point from the domain to a new vector in 3D space. 

Because the output is a vector, the function rule will always contain the unit vectors $\hat{i}$, $\hat{j}$, and $\hat{k}$.

**Block Diagram Representation:**
`[Input (3D point)]` $\rightarrow$ `[Vector Point Function]` $\rightarrow$ `[Vector]`

### Example
Consider the vector point function:
$$
\vec{F}(x, y, z) = xy\hat{i} + x^2z\hat{j} + y\hat{k}
$$
Let us evaluate this function at the same point $(1, 2, -1)$:
$$
\vec{F}(1, 2, -1) = (1)(2)\hat{i} + (1)^2(-1)\hat{j} + (2)\hat{k}
$$
Simplifying the expression gives:
$$
\vec{F}(1, 2, -1) = 2\hat{i} - \hat{j} + 2\hat{k}
$$
The output is a vector, possessing both magnitude and direction. 

Other examples of vector point functions:
*   $\vec{F}(x, y, z) = x^2\hat{i} + yz\hat{j} + z^2\hat{k}$
*   $\vec{F}(x, y, z) = x\hat{i} + y^2\hat{j} + xyz\hat{k}$

---

## What Comes Next
Now that we have defined scalar and vector point functions, the next lecture introduces vector differentiation, exploring how these functions change with respect to a single scalar variable.

---

**Navigation**
[Index](README.md) | [Next Lecture >](02_Vector_Differentiation.md)
