# Topic 19: Vector Identities

This file contains the organized questions and answers for **Vector Identities**, priority ranked as **Priority 19** based on frequency and exam weight.

---

## Q1. If $\bar{A}$ is a constant vector, then prove that $\nabla(\bar{r} \cdot \bar{A}) = \bar{A}$. (03)

| | |
|---|---|
| **ID** | PYQ-2018-1c |
| **Source** | 2018 Q1(c) [03 marks] |

**Answer:**

Let the constant vector be:

$$
\bar{A} = A_1\hat{i} + A_2\hat{j} + A_3\hat{k}
$$

Let the position vector be:

$$
\bar{r} = x\hat{i} + y\hat{j} + z\hat{k}
$$

Calculate the dot product:

$$
\bar{r} \cdot \bar{A} = A_1x + A_2y + A_3z
$$

Now calculate the gradient:

$$
\nabla(\bar{r} \cdot \bar{A}) = \frac{\partial}{\partial x}(A_1x + A_2y + A_3z)\hat{i} + \frac{\partial}{\partial y}(A_1x + A_2y + A_3z)\hat{j} + \frac{\partial}{\partial z}(A_1x + A_2y + A_3z)\hat{k}
$$

$$
\nabla(\bar{r} \cdot \bar{A}) = A_1\hat{i} + A_2\hat{j} + A_3\hat{k} = \bar{A}
$$

This completes the proof.

---

## Q2. Show that $\nabla \times (\nabla \times \bar{A}) = -\nabla^2\bar{A} + \nabla(\nabla \cdot \bar{A})$. (05)

| | |
|---|---|
| **ID** | PYQ-2018-4a | PYQ-2021-2c |
| **Appeared in** | 2018 Q4(a) [05 marks], 2021 Q2(c) [04 marks] |
| **Frequency** | ⭐⭐ (2 times) |

**Answer:**

Let the vector be $\bar{A} = A_x\hat{i} + A_y\hat{j} + A_z\hat{k}$. We calculate the curl of $\bar{A}$:

$$
\nabla \times \bar{A} = \left( \frac{\partial A_z}{\partial y} - \frac{\partial A_y}{\partial z} \right)\hat{i} + \left( \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x} \right)\hat{j} + \left( \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y} \right)\hat{k}
$$

Let this vector be $\bar{V} = \nabla \times \bar{A}$. Now we find the curl of $\bar{V}$:

$$
\nabla \times (\nabla \times \bar{A}) = \nabla \times \bar{V} = \left( \frac{\partial V_z}{\partial y} - \frac{\partial V_y}{\partial z} \right)\hat{i} + \left( \frac{\partial V_x}{\partial z} - \frac{\partial V_z}{\partial x} \right)\hat{j} + \left( \frac{\partial V_y}{\partial x} - \frac{\partial V_x}{\partial y} \right)\hat{k}
$$

We evaluate the x-component:

$$
(\nabla \times \bar{V})_x = \frac{\partial}{\partial y}\left( \frac{\partial A_y}{\partial x} - \frac{\partial A_x}{\partial y} \right) - \frac{\partial}{\partial z}\left( \frac{\partial A_x}{\partial z} - \frac{\partial A_z}{\partial x} \right)
$$

$$
(\nabla \times \bar{V})_x = \frac{\partial^2 A_y}{\partial y \partial x} - \frac{\partial^2 A_x}{\partial y^2} - \frac{\partial^2 A_x}{\partial z^2} + \frac{\partial^2 A_z}{\partial z \partial x}
$$

We add and subtract $\frac{\partial^2 A_x}{\partial x^2}$ to the expression:

$$
(\nabla \times \bar{V})_x = \left( \frac{\partial^2 A_x}{\partial x^2} + \frac{\partial^2 A_y}{\partial y \partial x} + \frac{\partial^2 A_z}{\partial z \partial x} \right) - \left( \frac{\partial^2 A_x}{\partial x^2} + \frac{\partial^2 A_x}{\partial y^2} + \frac{\partial^2 A_x}{\partial z^2} \right)
$$

$$
(\nabla \times \bar{V})_x = \frac{\partial}{\partial x}\left( \frac{\partial A_x}{\partial x} + \frac{\partial A_y}{\partial y} + \frac{\partial A_z}{\partial z} \right) - \left( \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} + \frac{\partial^2}{\partial z^2} \right)A_x
$$

$$
(\nabla \times \bar{V})_x = \frac{\partial}{\partial x}(\nabla \cdot \bar{A}) - \nabla^2 A_x
$$

By using the same steps for the y and z-components, we get the vector identity:

$$
\nabla \times (\nabla \times \bar{A}) = \nabla(\nabla \cdot \bar{A}) - \nabla^2\bar{A}
$$

---

## Q3. Prove that $\nabla^2(1/r) = 0$. (04)

| | |
|---|---|
| **ID** | PYQ-2019-3b |
| **Source** | 2019 Q3(b) [04 marks] |

**Answer:**

Let $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$, then $r = \sqrt{x^2 + y^2 + z^2}$.

The partial derivatives of $r$ with respect to coordinates are:

$$
\frac{\partial r}{\partial x} = \frac{x}{r}, \quad \frac{\partial r}{\partial y} = \frac{y}{r}, \quad \frac{\partial r}{\partial z} = \frac{z}{r}
$$

We find the gradient of $\frac{1}{r}$:

$$
\vec{\nabla}\left(\frac{1}{r}\right) = \hat{i}\frac{\partial}{\partial x}(r^{-1}) + \hat{j}\frac{\partial}{\partial y}(r^{-1}) + \hat{k}\frac{\partial}{\partial z}(r^{-1})
$$

Using the chain rule:

$$
\frac{\partial}{\partial x}(r^{-1}) = -r^{-2}\frac{\partial r}{\partial x} = -r^{-2}\left(\frac{x}{r}\right) = -\frac{x}{r^3}
$$

So the gradient vector is:

$$
\vec{\nabla}\left(\frac{1}{r}\right) = -\frac{x\hat{i} + y\hat{j} + z\hat{k}}{r^3} = -\frac{\vec{r}}{r^3}
$$

The Laplacian $\nabla^2\left(\frac{1}{r}\right)$ is the divergence of the gradient:

$$
\nabla^2\left(\frac{1}{r}\right) = \vec{\nabla} \cdot \vec{\nabla}\left(\frac{1}{r}\right) = -\left[ \frac{\partial}{\partial x}\left(\frac{x}{r^3}\right) + \frac{\partial}{\partial y}\left(\frac{y}{r^3}\right) + \frac{\partial}{\partial z}\left(\frac{z}{r^3}\right) \right]
$$

Using the quotient rule:

$$
\frac{\partial}{\partial x}\left(\frac{x}{r^3}\right) = \frac{r^3(1) - x(3r^2\frac{\partial r}{\partial x})}{r^6} = \frac{r^3 - 3x^2r}{r^6} = \frac{1}{r^3} - \frac{3x^2}{r^5}
$$

Similarly:

$$
\frac{\partial}{\partial y}\left(\frac{y}{r^3}\right) = \frac{1}{r^3} - \frac{3y^2}{r^5}
$$

$$
\frac{\partial}{\partial z}\left(\frac{z}{r^3}\right) = \frac{1}{r^3} - \frac{3z^2}{r^5}
$$

Summing these three partial derivatives:

$$
\nabla^2\left(\frac{1}{r}\right) = -\left[ \frac{3}{r^3} - \frac{3(x^2 + y^2 + z^2)}{r^5} \right] = -\left[ \frac{3}{r^3} - \frac{3r^2}{r^5} \right] = -\left[ \frac{3}{r^3} - \frac{3}{r^3} \right] = 0
$$

This completes the proof.

---

## Q4. Evaluate $\nabla(\vec{A} \times \vec{r})$ if $\nabla \times \vec{A} = 0$. (03)

| | |
|---|---|
| **ID** | PYQ-2024-3a |
| **Source** | 2024 Q3(a) [03 marks] |

**Answer:**

We assume that the expression $\nabla(\vec{A} \times \vec{r})$ refers to the divergence:

$$
\nabla \cdot (\vec{A} \times \vec{r})
$$

Here, $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$ is the position vector.

We use the vector identity for the divergence of a cross product:

$$
\nabla \cdot (\vec{A} \times \vec{r}) = \vec{r} \cdot (\nabla \times \vec{A}) - \vec{A} \cdot (\nabla \times \vec{r})
$$

We are given that $\nabla \times \vec{A} = 0$. So, the first term is zero.

Next, we calculate the curl of the position vector $\vec{r}$:

$$
\nabla \times \vec{r} = \begin{vmatrix}
\hat{i} & \hat{j} & \hat{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
x & y & z
\end{vmatrix} = \hat{i}(0) - \hat{j}(0) + \hat{k}(0) = \vec{0}
$$

So, the second term is also zero:

$$
\vec{A} \cdot (\nabla \times \vec{r}) = \vec{A} \cdot \vec{0} = 0
$$

Thus, we find:

$$
\nabla \cdot (\vec{A} \times \vec{r}) = 0
$$

If the question meant the curl $\nabla \times (\vec{A} \times \vec{r})$, we use another identity:

$$
\nabla \times (\vec{A} \times \vec{r}) = (\vec{r} \cdot \nabla)\vec{A} - (\vec{A} \cdot \nabla)\vec{r} + \vec{A}(\nabla \cdot \vec{r}) - \vec{r}(\nabla \cdot \vec{A})
$$

We calculate the terms:
*   $\nabla \cdot \vec{r} = 1 + 1 + 1 = 3$. So, $\vec{A}(\nabla \cdot \vec{r}) = 3\vec{A}$.
*   $(\vec{A} \cdot \nabla)\vec{r} = \left( A_1 \frac{\partial}{\partial x} + A_2 \frac{\partial}{\partial y} + A_3 \frac{\partial}{\partial z} \right)(x\hat{i} + y\hat{j} + z\hat{k}) = \vec{A}$.

This gives:

$$
\nabla \times (\vec{A} \times \vec{r}) = 2\vec{A} + (\vec{r} \cdot \nabla)\vec{A} - \vec{r}(\nabla \cdot \vec{A})
$$

If $\vec{A}$ is a constant vector field, then its derivatives are zero. In that case, the curl is:

$$
\nabla \times (\vec{A} \times \vec{r}) = 2\vec{A}
$$

---

