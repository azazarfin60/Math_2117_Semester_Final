# Topic 10: Matrix Types and Properties

This file contains the organized questions and answers for **Matrix Types and Properties**, priority ranked as **Priority 10** based on frequency and exam weight.

---

## Q1. If $A_\alpha = \begin{pmatrix} \cos\alpha & \sin\alpha \\ -\sin\alpha & \cos\alpha \end{pmatrix}$, then show that $A_\alpha \cdot A_\beta = A_{\alpha+\beta} = A_\beta \cdot A_\alpha$. (03)

| | |
|---|---|
| **ID** | PYQ-2017-5a |
| **Source** | 2017 Q5(a) [03 marks] |

**Answer:**

Let us multiply the two matrices $A_\alpha$ and $A_\beta$:

$$
A_\alpha \cdot A_\beta = \begin{pmatrix} \cos\alpha & \sin\alpha \\ -\sin\alpha & \cos\alpha \end{pmatrix} \begin{pmatrix} \cos\beta & \sin\beta \\ -\sin\beta & \cos\beta \end{pmatrix}
$$

Multiply rows by columns:

$$
A_\alpha \cdot A_\beta = \begin{pmatrix} \cos\alpha\cos\beta - \sin\alpha\sin\beta & \cos\alpha\sin\beta + \sin\alpha\cos\beta \\ -\sin\alpha\cos\beta - \cos\alpha\sin\beta & -\sin\alpha\sin\beta + \cos\alpha\cos\beta \end{pmatrix}
$$

We apply standard trigonometric addition formulas:

$$
\cos(\alpha+\beta) = \cos\alpha\cos\beta - \sin\alpha\sin\beta
$$

$$
\sin(\alpha+\beta) = \sin\alpha\cos\beta + \cos\alpha\sin\beta
$$

Substitute these identities back into the product matrix:

$$
A_\alpha \cdot A_\beta = \begin{pmatrix} \cos(\alpha+\beta) & \sin(\alpha+\beta) \\ -\sin(\alpha+\beta) & \cos(\alpha+\beta) \end{pmatrix} = A_{\alpha+\beta}
$$

Since addition of angles is commutative ($\alpha + \beta = \beta + \alpha$), we also have:

$$
A_{\alpha+\beta} = A_{\beta+\alpha} = A_\beta \cdot A_\alpha
$$

So we have shown that $A_\alpha \cdot A_\beta = A_{\alpha+\beta} = A_\beta \cdot A_\alpha$.

---

## Q2. Define symmetric, skew-symmetric, and Hermitian matrices with examples. (03)

| | |
|---|---|
| **ID** | PYQ-2018-5a |
| **Source** | 2018 Q5(a) [03 marks] |

**Answer:**

#### Symmetric Matrix

A square matrix $A$ is symmetric if it equals its transpose:

$$
A^T = A
$$

*Example:*

$$
\begin{pmatrix} 1 & 2 \\ 2 & 5 \end{pmatrix}
$$

#### Skew-Symmetric Matrix

A square matrix $A$ is skew-symmetric if its transpose equals its negative:

$$
A^T = -A
$$

The diagonal elements of a skew-symmetric matrix are always zero.

*Example:*

$$
\begin{pmatrix} 0 & -3 \\ 3 & 0 \end{pmatrix}
$$

#### Hermitian Matrix

A square matrix $A$ with complex entries is Hermitian if it equals its conjugate transpose:

$$
A^\dagger = (\bar{A})^T = A
$$

*Example:*

$$
\begin{pmatrix} 2 & 1+i \\ 1-i & 3 \end{pmatrix}
$$

---

## Q3. Define singular matrix. If $A$ and $B$ are non-singular matrices of the same order, then show that $(AB)^{-1} = B^{-1}A^{-1}$. Hence prove that $(A^{-1})^n = (A^n)^{-1}$ for any positive integer. (05)

| | |
|---|---|
| **ID** | PYQ-2018-5b | PYQ-2023-4b |
| **Appeared in** | 2018 Q5(b) [05 marks], 2023 Q4(b) [02 marks] |
| **Frequency** | ⭐⭐ (2 times) |

**Answer:**

#### 1. Singular Matrix

A square matrix is singular if its determinant is zero. It has no inverse.

#### 2. Prove $(AB)^{-1} = B^{-1}A^{-1}$

We multiply $AB$ by $B^{-1}A^{-1}$:

$$
(AB)(B^{-1}A^{-1}) = A(B B^{-1})A^{-1} = A I A^{-1} = A A^{-1} = I
$$

$$
(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1} I B = B^{-1} B = I
$$

Since the product in both directions is the identity matrix, we get:

$$
(AB)^{-1} = B^{-1}A^{-1}
$$

#### 3. Prove $(A^{-1})^n = (A^n)^{-1}$

We use mathematical induction on $n$:

*   **Base Case ($n=1$):** $(A^{-1})^1 = (A^1)^{-1}$, which is true.
*   **Inductive Step:** Assume the statement is true for $n=k$:

$$
(A^{-1})^k = (A^k)^{-1}
$$

We test for $n = k+1$:

$$
(A^{k+1})^{-1} = (A^k \cdot A)^{-1}
$$

Using the product inverse property shown above:

$$
(A^k \cdot A)^{-1} = A^{-1} \cdot (A^k)^{-1}
$$

Substitute the induction assumption:

$$
A^{-1} \cdot (A^k)^{-1} = A^{-1} \cdot (A^{-1})^k = (A^{-1})^{k+1}
$$

So the statement is true for $n=k+1$. The proof is complete.

---

## Q4. For two matrices $A$ and $B$, prove that $(AB)' = B'A'$. (03)

| | |
|---|---|
| **ID** | PYQ-2020-5a |
| **Source** | 2020 Q5(a) [03 marks] |

**Answer:**

Let $A$ be an $m \times n$ matrix and $B$ be an $n \times p$ matrix. Let the product matrix be $C = AB$.

The $(i, j)$-th element of $C$ is:

$$
c_{ij} = \sum_{k=1}^n a_{ik} b_{kj}
$$

The transpose element $(C')_{ij}$ is defined as the $(j, i)$-th element of $C$:

$$
(C')_{ij} = c_{ji} = \sum_{k=1}^n a_{jk} b_{ki}
$$

Now look at the product of the transposes $B' A'$. The $(i, j)$-th element of this product is:

$$
(B'A')_{ij} = \sum_{k=1}^n (B')_{ik} (A')_{kj}
$$

Using the transpose definitions $(B')_{ik} = b_{ki}$ and $(A')_{kj} = a_{jk}$, we substitute:

$$
(B'A')_{ij} = \sum_{k=1}^n b_{ki} a_{jk} = \sum_{k=1}^n a_{jk} b_{ki}
$$

Since $(AB)'_{ij} = (B'A')_{ij}$ for all indices, we get:

$$
(AB)' = B'A'
$$

The proof is complete.

---

## Q5. Show that every square matrix can be uniquely expressed as the sum of a symmetric and a skew symmetric matrices. (04)

| | |
|---|---|
| **ID** | PYQ-2020-5b | PYQ-2021-5a |
| **Appeared in** | 2020 Q5(b) [04 marks], 2021 Q5(a) [06 marks] |
| **Frequency** | ⭐⭐ (2 times) |

**Answer:**

Let $A$ be a square matrix. We can decompose $A$ as:

$$
A = \frac{1}{2}(A + A^T) + \frac{1}{2}(A - A^T)
$$

Let $P = \frac{1}{2}(A + A^T)$ and $Q = \frac{1}{2}(A - A^T)$.

#### 1. Show $P$ is symmetric

Calculate the transpose of $P$:

$$
P^T = \left[ \frac{1}{2}(A + A^T) \right]^T = \frac{1}{2}(A^T + (A^T)^T) = \frac{1}{2}(A^T + A) = P
$$

So $P$ is symmetric.

#### 2. Show $Q$ is skew-symmetric

Calculate the transpose of $Q$:

$$
Q^T = \left[ \frac{1}{2}(A - A^T) \right]^T = \frac{1}{2}(A^T - (A^T)^T) = \frac{1}{2}(A^T - A) = -Q
$$

So $Q$ is skew-symmetric.

#### 3. Prove Uniqueness

Suppose there is another decomposition:

$$
A = P' + Q'
$$

where $P'$ is symmetric and $Q'$ is skew-symmetric. Taking the transpose:

$$
A^T = (P' + Q')^T = P'^T + Q'^T = P' - Q'
$$

We solve the equations:
1.  $P' + Q' = A$
2.  $P' - Q' = A^T$

Adding them gives:

$$
2P' = A + A^T \implies P' = \frac{1}{2}(A + A^T) = P
$$

Subtracting them gives:

$$
2Q' = A - A^T \implies Q' = \frac{1}{2}(A - A^T) = Q
$$

The decomposition is unique.

---

## Q6. Define commutative, idempotent and involutory matrix. (02)

| | |
|---|---|
| **ID** | PYQ-2023-4a |
| **Source** | 2023 Q4(a) [02 marks] |

**Answer:**

*   **Commutative Matrices:** Two square matrices $A$ and $B$ are commutative if $AB = BA$.
*   **Idempotent Matrix:** A square matrix $A$ is idempotent if its square equals itself: $A^2 = A$.
*   **Involutory Matrix:** A square matrix $A$ is involutory if its square equals the identity matrix: $A^2 = I$.

---

## Q7. Show that every square matrix can be expressed as the sum of a Hermitian matrix and a Skew-Hermitian matrix. (05)

| | |
|---|---|
| **ID** | PYQ-2023-5a |
| **Source** | 2023 Q5(a) [05 marks] |

**Answer:**

Let $A$ be a square matrix. We write $A$ as:

$$
A = \frac{1}{2}(A + A^\dagger) + \frac{1}{2}(A - A^\dagger)
$$

where $A^\dagger = (\bar{A})^T$ is the conjugate transpose of $A$. Let:

$$
P = \frac{1}{2}(A + A^\dagger) \quad \text{and} \quad Q = \frac{1}{2}(A - A^\dagger)
$$

#### 1. Show $P$ is Hermitian

$$
P^\dagger = \left[ \frac{1}{2}(A + A^\dagger) \right]^\dagger = \frac{1}{2}(A^\dagger + (A^\dagger)^\dagger) = \frac{1}{2}(A^\dagger + A) = P
$$

So $P$ is a Hermitian matrix.

#### 2. Show $Q$ is Skew-Hermitian

$$
Q^\dagger = \left[ \frac{1}{2}(A - A^\dagger) \right]^\dagger = \frac{1}{2}(A^\dagger - (A^\dagger)^\dagger) = \frac{1}{2}(A^\dagger - A) = -Q
$$

So $Q$ is a Skew-Hermitian matrix.

So $A = P + Q$ is the sum of a Hermitian matrix and a Skew-Hermitian matrix.

---

