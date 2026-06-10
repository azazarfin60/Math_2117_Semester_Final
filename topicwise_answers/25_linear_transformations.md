# Topic 25: Linear Transformations

This file contains the organized questions and answers for **Linear Transformations**, priority ranked as **Priority 25** based on frequency and exam weight.

---

## Q1. Define Kernel and image of a linear mapping. Let $F : V \rightarrow U$ be a linear mapping. Show that the Kernel of $F$ is a subspace of $V$ and the image of $F$ is a subspace of $U$. (06)

| | |
|---|---|
| **ID** | PYQ-2019-8b |
| **Source** | 2019 Q8(b) [06 marks] |

**Answer:**

#### 1. Definitions

*   **Kernel of $F$:** The set of all vectors in $V$ that map to the zero vector in $U$. It is denoted by $\text{Ker}(F)$:

$$
\text{Ker}(F) = \{ v \in V \mid F(v) = 0_U \}
$$

*   **Image of $F$:** The set of all vectors in $U$ that are mapped to by at least one vector in $V$. It is denoted by $\text{Im}(F)$:

$$
\text{Im}(F) = \{ u \in U \mid \exists v \in V \text{ such that } F(v) = u \}
$$

#### 2. Prove $\text{Ker}(F)$ is a subspace of $V$

To show that $\text{Ker}(F)$ is a subspace of $V$, we must verify three properties:

1.  **Non-emptiness / Zero Vector:** Since $F$ is linear:

$$
F(0_V) = 0_U \implies 0_V \in \text{Ker}(F)
$$

2.  **Closure under Addition:** Let $v_1, v_2 \in \text{Ker}(F)$. Then $F(v_1) = 0_U$ and $F(v_2) = 0_U$.

$$
F(v_1 + v_2) = F(v_1) + F(v_2) = 0_U + 0_U = 0_U \implies v_1 + v_2 \in \text{Ker}(F)
$$

3.  **Closure under Scalar Multiplication:** Let $v \in \text{Ker}(F)$ and let $k$ be a scalar in the field. Then $F(v) = 0_U$.

$$
F(k v) = k F(v) = k (0_U) = 0_U \implies k v \in \text{Ker}(F)
$$

Since all three properties are satisfied, $\text{Ker}(F)$ is a subspace of $V$.

#### 3. Prove $\text{Im}(F)$ is a subspace of $U$

To show that $\text{Im}(F)$ is a subspace of $U$, we verify the three properties:

1.  **Non-emptiness / Zero Vector:** Since $F(0_V) = 0_U$, the zero vector $0_U$ has a pre-image in $V$:

$$
0_U \in \text{Im}(F)
$$

2.  **Closure under Addition:** Let $u_1, u_2 \in \text{Im}(F)$. Then there exist $v_1, v_2 \in V$ such that $F(v_1) = u_1$ and $F(v_2) = u_2$.

$$
u_1 + u_2 = F(v_1) + F(v_2) = F(v_1 + v_2)
$$

Since $v_1 + v_2 \in V$ (as $V$ is a vector space), $u_1 + u_2$ is the image of $v_1 + v_2$, so:

$$
u_1 + u_2 \in \text{Im}(F)
$$

3.  **Closure under Scalar Multiplication:** Let $u \in \text{Im}(F)$ and let $k$ be a scalar. Then there exists $v \in V$ such that $F(v) = u$.

$$
k u = k F(v) = F(k v)
$$

Since $k v \in V$, $k u$ is the image of $k v$, so:

$$
k u \in \text{Im}(F)
$$

Since all three properties are satisfied, $\text{Im}(F)$ is a subspace of $U$.

---

## Q2. Identify that the following mappings $F$ are linear or not linear: (04)

| | |
|---|---|
| **ID** | PYQ-2023-8c |
| **Source** | 2023 Q8(c) [04 marks] |

**Answer:**

*   **(i)** $F : \mathbb{R}^3 \rightarrow \mathbb{R}$ defined by $F(x, y, z) = 2x - 3y + 4z$
*   **(ii)** $F : \mathbb{R}^2 \rightarrow \mathbb{R}^3$ defined by $F(x, y) = (x+1, 2y, x+y)$

**Answer:**

#### (i) Mapping $F(x, y, z) = 2x - 3y + 4z$

Let $u = (x_1, y_1, z_1)$ and $v = (x_2, y_2, z_2)$ be vectors in $\mathbb{R}^3$.
*   **Check Addition:**

$$
F(u + v) = F(x_1 + x_2, y_1 + y_2, z_1 + z_2) = 2(x_1 + x_2) - 3(y_1 + y_2) + 4(z_1 + z_2)
$$

$$
F(u + v) = (2x_1 - 3y_1 + 4z_1) + (2x_2 - 3y_2 + 4z_2) = F(u) + F(v)
$$

*   **Check Scalar Multiplication:**

$$
F(ku) = F(kx_1, ky_1, kz_1) = 2(kx_1) - 3(ky_1) + 4(kz_1) = k(2x_1 - 3y_1 + 4z_1) = kF(u)
$$

So the mapping is **linear**.

#### (ii) Mapping $F(x, y) = (x+1, 2y, x+y)$

A linear mapping must map the zero vector to the zero vector. We check the image of $(0, 0)$:

$$
F(0, 0) = (0 + 1, 2(0), 0 + 0) = (1, 0, 0) \neq (0, 0, 0)
$$

Since the image of the zero vector is not the zero vector, this mapping is **not linear**.

---

[⬅ 2021](2021_answer.md) | [🏠 Index](00-index.md) | [2024 ➡](2024_answer.md)

---

