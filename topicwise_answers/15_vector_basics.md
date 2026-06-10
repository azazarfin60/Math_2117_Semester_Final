# Topic 15: Vector Basics

This file contains the organized questions and answers for **Vector Basics**, priority ranked as **Priority 15** based on frequency and exam weight.

---

## Q1. Find an equation for the plane perpendicular to the vector $\bar{A} = 2\hat{i} + 3\hat{j} + 6\hat{k}$ and passing through the terminal point of the vector $\bar{B} = \hat{i} + 5\hat{j} + 3\hat{k}$. (04)

| | |
|---|---|
| **ID** | PYQ-2019-1a | PYQ-2024-2a |
| **Appeared in** | 2019 Q1(a) [04 marks], 2024 Q2(a) [04 marks] |
| **Frequency** | ⭐⭐ (2 times) |

**Answer:**

We assume the vector $\vec{B}$ starts at the origin. Its terminal point is $P(1, 5, 3)$.

The equation of a plane passing through a point $P(x_0, y_0, z_0)$ and perpendicular to a normal vector $\vec{A} = a\hat{i} + b\hat{j} + c\hat{k}$ is:

$$
a(x - x_0) + b(y - y_0) + c(z - z_0) = 0
$$

Substitute the point $(1, 5, 3)$ and the components of $\vec{A} = 2\hat{i} + 3\hat{j} + 6\hat{k}$:

$$
2(x - 1) + 3(y - 5) + 6(z - 3) = 0
$$

Expand the equation:

$$
2x - 2 + 3y - 15 + 6z - 18 = 0
$$

$$
2x + 3y + 6z - 35 = 0 \implies 2x + 3y + 6z = 35
$$

So the equation of the plane is $2x + 3y + 6z = 35$.

---

## Q2. Find the acute angles which the line joining the points $(1, -3, 2)$ and $(3, -5, 1)$ makes with the coordinate axes. (04)

| | |
|---|---|
| **ID** | PYQ-2019-1c |
| **Source** | 2019 Q1(c) [04 marks] |

**Answer:**

Let the points be $P(1, -3, 2)$ and $Q(3, -5, 1)$. The vector $\vec{PQ}$ representing the line segment is:

$$
\vec{PQ} = (3 - 1)\hat{i} + (-5 - (-3))\hat{j} + (1 - 2)\hat{k} = 2\hat{i} - 2\hat{j} - \hat{k}
$$

Find the magnitude of the vector $\vec{PQ}$:

$$
|\vec{PQ}| = \sqrt{2^2 + (-2)^2 + (-1)^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3
$$

The direction cosines of this vector are:

$$
\cos\alpha = \frac{2}{3}, \quad \cos\beta = -\frac{2}{3}, \quad \cos\gamma = -\frac{1}{3}
$$

where $\alpha, \beta, \gamma$ are the angles made with the positive directions of the $x$, $y$, and $z$ axes respectively.

For the acute angles, the cosines must be positive:

$$
\cos\alpha = \frac{2}{3} \implies \alpha = \cos^{-1}\left(\frac{2}{3}\right) \approx 48.19^\circ
$$

$$
\cos\beta = \frac{2}{3} \implies \beta = \cos^{-1}\left(\frac{2}{3}\right) \approx 48.19^\circ
$$

$$
\cos\gamma = \frac{1}{3} \implies \gamma = \cos^{-1}\left(\frac{1}{3}\right) \approx 70.53^\circ
$$

---

## Q3. What is the vector? Find a unit vector parallel to the resultant of vectors $\vec{r}_1 = 2\hat{i} + 4\hat{j} - 5\hat{k}$, $\vec{r}_2 = \hat{i} + 2\hat{j} + \hat{k}$. (04)

| | |
|---|---|
| **ID** | PYQ-2020-1a |
| **Source** | 2020 Q1(a) [04 marks] |

**Answer:**

#### 1. Definition of a Vector

A vector is a mathematical quantity that has both magnitude and direction. It also satisfies the parallelogram law of vector addition.

#### 2. Find the Unit Vector

We calculate the resultant vector $\vec{R}$ by adding the two given vectors:

$$
\vec{R} = \vec{r}_1 + \vec{r}_2 = (2\hat{i} + 4\hat{j} - 5\hat{k}) + (\hat{i} + 2\hat{j} + \hat{k}) = 3\hat{i} + 6\hat{j} - 4\hat{k}
$$

Find the magnitude of the resultant vector:

$$
|\vec{R}| = \sqrt{3^2 + 6^2 + (-4)^2} = \sqrt{9 + 36 + 16} = \sqrt{61}
$$

The unit vector parallel to $\vec{R}$ is:

$$
\hat{u} = \frac{\vec{R}}{|\vec{R}|} = \frac{3\hat{i} + 6\hat{j} - 4\hat{k}}{\sqrt{61}}
$$

---

## Q4. If $\bar{A} = 2\hat{i} + \hat{j} - 3\hat{k}$ and $\bar{B} = \hat{i} - 2\hat{j} + \hat{k}$, find a vector of magnitude 5 perpendicular to both $\bar{A}$ and $\bar{B}$. (04)

| | |
|---|---|
| **ID** | PYQ-2020-1c |
| **Source** | 2020 Q1(c) [04 marks] |

**Answer:**

We calculate the cross product of the two vectors to find a perpendicular direction:

$$
\bar{A} \times \bar{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & 1 & -3 \\ 1 & -2 & 1 \end{vmatrix} = \hat{i}(1 - 6) - \hat{j}(2 - (-3)) + \hat{k}(-4 - 1) = -5\hat{i} - 5\hat{j} - 5\hat{k}
$$

We simplify the perpendicular direction to:

$$
\vec{v} = \hat{i} + \hat{j} + \hat{k}
$$

The unit normal vector $\hat{n}$ is:

$$
\hat{n} = \pm \frac{\hat{i} + \hat{j} + \hat{k}}{\sqrt{1^2 + 1^2 + 1^2}} = \pm \frac{\hat{i} + \hat{j} + \hat{k}}{\sqrt{3}}
$$

The vector with a magnitude of 5 is:

$$
\vec{P} = \pm 5 \hat{n} = \pm \frac{5}{\sqrt{3}} (\hat{i} + \hat{j} + \hat{k})
$$

---

## Q5. What are the vector and scalar quantity? Give some examples. If $\vec{A} = 3\hat{i} - \hat{j} + 4\hat{k}$, $\vec{B} = -2\hat{i} + 4\hat{j} - 3\hat{k}$ and $\vec{C} = \hat{i} + 2\hat{j} - \hat{k}$, find the magnitude of $2\vec{A} - 3\vec{B} + 2\vec{C}$. (04)

| | |
|---|---|
| **ID** | PYQ-2021-1a |
| **Source** | 2021 Q1(a) [04 marks] |

**Answer:**

#### 1. Definitions and Examples

*   **Scalar Quantity:** A physical quantity that has only magnitude but no direction. Examples: Mass, Temperature, Time.
*   **Vector Quantity:** A physical quantity that has both magnitude and direction, and obeys vector addition rules. Examples: Velocity, Force, Acceleration.

#### 2. Find the Magnitude

We calculate the vector expression:

$$
\vec{V} = 2\vec{A} - 3\vec{B} + 2\vec{C}
$$

Substitute the given vectors:

$$
2\vec{A} = 6\hat{i} - 2\hat{j} + 8\hat{k}
$$

$$
-3\vec{B} = 6\hat{i} - 12\hat{j} + 9\hat{k}
$$

$$
2\vec{C} = 2\hat{i} + 4\hat{j} - 2\hat{k}
$$

Sum the components together:

$$
\vec{V} = (6 + 6 + 2)\hat{i} + (-2 - 12 + 4)\hat{j} + (8 + 9 - 2)\hat{k} = 14\hat{i} - 10\hat{j} + 15\hat{k}
$$

Find the magnitude:

$$
|\vec{V}| = \sqrt{14^2 + (-10)^2 + 15^2} = \sqrt{196 + 100 + 225} = \sqrt{521}
$$

So the magnitude is $\sqrt{521}$.

---

## Q6. What is meant by dot and cross product in vector analysis? Determine a unit vector perpendicular to the plane of $\vec{A} = 2\hat{i} - 6\hat{j} - 3\hat{k}$ and $\vec{B} = 4\hat{i} + 3\hat{j} - \hat{k}$. (04)

| | |
|---|---|
| **ID** | PYQ-2021-1b | PYQ-2023-1a |
| **Appeared in** | 2021 Q1(b) [04 marks], 2023 Q1(a) [03 marks] |
| **Frequency** | ⭐⭐ (2 times) |

**Answer:**

#### 1. Definitions

*   **Dot Product:** The scalar product of two vectors $\vec{A}$ and $\vec{B}$ is defined as $\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta$, where $\theta$ is the angle between them.
*   **Cross Product:** The vector product of two vectors $\vec{A}$ and $\vec{B}$ is defined as $\vec{A} \times \vec{B} = |\vec{A}||\vec{B}|\sin\theta \hat{n}$, where $\hat{n}$ is a unit vector perpendicular to the plane of the two vectors.

#### 2. Find the Perpendicular Unit Vector

We calculate the cross product of $\vec{A}$ and $\vec{B}$ to get a perpendicular vector:

$$
\vec{A} \times \vec{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \\ 2 & -6 & -3 \\ 4 & 3 & -1 \end{vmatrix} = \hat{i}(6 - (-9)) - \hat{j}(-2 - (-12)) + \hat{k}(6 - (-24)) = 15\hat{i} - 10\hat{j} + 30\hat{k}
$$

Find the magnitude of this cross product:

$$
|\vec{A} \times \vec{B}| = \sqrt{15^2 + (-10)^2 + 30^2} = \sqrt{225 + 100 + 900} = \sqrt{1225} = 35
$$

The unit vector perpendicular to the plane is:

$$
\hat{n} = \pm \frac{15\hat{i} - 10\hat{j} + 30\hat{k}}{35} = \pm \left( \frac{3}{7}\hat{i} - \frac{2}{7}\hat{j} + \frac{6}{7}\hat{k} \right)
$$

---

## Q7. Determine the angles $\alpha, \beta$, and $\gamma$ which the vector $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$ makes with the positive directions of the coordinate axes and show that $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$. (03)

| | |
|---|---|
| **ID** | PYQ-2023-2a |
| **Source** | 2023 Q2(a) [03 marks] |

**Answer:**

Let the magnitude of the position vector $\vec{r}$ be:

$$
r = |\vec{r}| = \sqrt{x^2 + y^2 + z^2}
$$

The cosine of the angles made with the coordinate axes are given by:

$$
\cos\alpha = \frac{\vec{r} \cdot \hat{i}}{r} = \frac{x}{r}
$$

$$
\cos\beta = \frac{\vec{r} \cdot \hat{j}}{r} = \frac{y}{r}
$$

$$
\cos\gamma = \frac{\vec{r} \cdot \hat{k}}{r} = \frac{z}{r}
$$

Sum the squares of these cosines:

$$
\cos^2\alpha + \cos^2\beta + \cos^2\gamma = \frac{x^2}{r^2} + \frac{y^2}{r^2} + \frac{z^2}{r^2} = \frac{x^2 + y^2 + z^2}{r^2} = \frac{r^2}{r^2} = 1
$$

This completes the proof.

---

## Q8. Find the constant 'a' such that the vectors $2\hat{i} - \hat{j} + \hat{k}$, $\hat{i} + 2\hat{j} - 3\hat{k}$ and $3\hat{i} + a\hat{j} + 5\hat{k}$ are coplanar. (03)

| | |
|---|---|
| **ID** | PYQ-2023-2b |
| **Source** | 2023 Q2(b) [03 marks] |

**Answer:**

Three vectors are coplanar if and only if their scalar triple product is zero. We set up the determinant:

$$
\begin{vmatrix} 2 & -1 & 1 \\ 1 & 2 & -3 \\ 3 & a & 5 \end{vmatrix} = 0
$$

Expand this determinant along the first row:

$$
2(10 - (-3a)) - (-1)(5 - (-9)) + 1(a - 6) = 0
$$

$$
2(10 + 3a) + 14 + a - 6 = 0
$$

$$
20 + 6a + 14 + a - 6 = 0
$$

$$
7a + 28 = 0 \implies 7a = -28 \implies a = -4
$$

So the constant is $a = -4$.

---

## Q9. What is vector field? Graph the vector fields defined by: (05)

| | |
|---|---|
| **ID** | PYQ-2024-1a |
| **Source** | 2024 Q1(a) [05 marks] |

**Answer:**

*   (i) $\vec{V}(x, y) = x\hat{i} + y\hat{j}$
*   (ii) $\vec{V}(x, y) = -x\hat{i} - y\hat{j}$

**Answer:**

#### 1. Definition of a Vector Field
A vector field is a function. It assigns a vector to every point in a given region. In a two-dimensional space, we write it as:

$$
\vec{V}(x, y) = P(x, y)\hat{i} + Q(x, y)\hat{j}
$$

Here, $P(x, y)$ and $Q(x, y)$ are scalar functions.

#### 2. Graphing the Vector Fields

##### (i) $\vec{V}(x, y) = x\hat{i} + y\hat{j}$
For any point $(x, y)$, the vector points directly away from the origin $(0, 0)$. The length of the vector equals the distance of the point from the origin, $r = \sqrt{x^2 + y^2}$.

We choose a few points to show the field:
*   At $(1, 0)$, the vector is $\hat{i}$. It points right with a length of 1.
*   At $(0, 1)$, the vector is $\hat{j}$. It points up with a length of 1.
*   At $(-1, 0)$, the vector is $-\hat{i}$. It points left with a length of 1.
*   At $(0, -1)$, the vector is $-\hat{j}$. It points down with a length of 1.
*   At $(2, 2)$, the vector is $2\hat{i} + 2\hat{j}$. It points diagonally outward with a length of $2\sqrt{2}$.

This field looks like a source. All vectors point radially outward from the center.

##### (ii) $\vec{V}(x, y) = -x\hat{i} - y\hat{j}$
For any point $(x, y)$, the vector points directly toward the origin $(0, 0)$. Its length equals the distance from the origin.

We choose a few points to show the field:
*   At $(1, 0)$, the vector is $-\hat{i}$. It points left with a length of 1.
*   At $(0, 1)$, the vector is $-\hat{j}$. It points down with a length of 1.
*   At $(-1, 0)$, the vector is $\hat{i}$. It points right with a length of 1.
*   At $(0, -1)$, the vector is $\hat{j}$. It points up with a length of 1.
*   At $(2, 2)$, the vector is $-2\hat{i} - 2\hat{j}$. It points diagonally inward with a length of $2\sqrt{2}$.

This field looks like a sink. All vectors point radially inward toward the center.

---

## Q10. Explain the physical significance of dot and cross product. Show that $\vec{A} = \frac{1}{3}(2\hat{i} - 2\hat{j} + \hat{k})$, $\vec{B} = \frac{1}{3}(\hat{i} + 2\hat{j} + 2\hat{k})$ and $\vec{C} = \frac{1}{3}(2\hat{i} + \hat{j} - 2\hat{k})$ are mutually orthogonal unit vectors. (2+2+6)

| | |
|---|---|
| **ID** | CT1V-1 |
| **Source** | CT1V Q1 [2+2+6 marks] |

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

