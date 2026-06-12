# Lecture 25: Vector Space - Numerical Problem on Eigen Value & Vectors

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 25 of 27
> **Video**: https://www.youtube.com/watch?v=CDKS5Se6r3Q

---

**Navigation**
[< Previous Lecture](24_Eigenvalue_Eigenvector_Theory.md) | [Index](README.md) | [Next Lecture >](26_Matrix_Eigenvalue_Problems.md)


---

## Prerequisites
Before moving to numerical problems and diagonalization, we must finish the theoretical foundation of eigenvalues. Today we will prove that distinct eigenvalues produce fundamentally unique (linearly independent) eigenvectors, and we will establish the characteristic equation used to calculate eigenvalues.

---

## Theorem 4: Independence of Distinct Eigenvectors

**Statement:** Distinct non-zero eigenvectors of a linear operator $T$ corresponding to distinct eigenvalues of $T$ are linearly independent.

**Proof (by Mathematical Induction):**
Let $T : V \to V$ be a linear operator. Let $\alpha_1, \alpha_2, \dots, \alpha_n$ be eigenvectors corresponding to distinct eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$.
This means: $T(\alpha_i) = \lambda_i \alpha_i$ for all $i = 1, \dots, n$.
We want to prove that the set $S_n = \lbrace \alpha_1, \alpha_2, \dots, \alpha_n \rbrace$ is linearly independent. We proceed by induction on $n$.

**Base Case ($n = 1$):**
For $n = 1$, the set is $S_1 = \lbrace \alpha_1 \rbrace$.
Because $\alpha_1$ is an eigenvector, it is a non-zero vector ($\alpha_1 \neq \bar{0}$). Any set containing a single non-zero vector is linearly independent. The base case holds.

**Induction Hypothesis ($n = k$):**
Assume the theorem holds for $k$ eigenvectors. Thus, the set $S_k = \lbrace \alpha_1, \alpha_2, \dots, \alpha_k \rbrace$ is linearly independent.

**Inductive Step ($n = k + 1$):**
We must prove that $S_{k+1} = \lbrace \alpha_1, \dots, \alpha_k, \alpha_{k+1} \rbrace$ is linearly independent. Let's set up a linear combination equal to the zero vector:

$$
a_1 \alpha_1 + a_2 \alpha_2 + \dots + a_k \alpha_k + a_{k+1} \alpha_{k+1} = \bar{0} \quad \text{--- (1)}
$$

Apply the linear operator $T$ to both sides. Since $T(\bar{0}) = \bar{0}$:

$$
a_1 T(\alpha_1) + a_2 T(\alpha_2) + \dots + a_k T(\alpha_k) + a_{k+1} T(\alpha_{k+1}) = \bar{0}
$$

Substitute $T(\alpha_i) = \lambda_i \alpha_i$:

$$
a_1 \lambda_1 \alpha_1 + a_2 \lambda_2 \alpha_2 + \dots + a_k \lambda_k \alpha_k + a_{k+1} \lambda_{k+1} \alpha_{k+1} = \bar{0} \quad \text{--- (2)}
$$

Now, multiply the original equation (1) by the scalar $\lambda_{k+1}$:

$$
a_1 \lambda_{k+1} \alpha_1 + a_2 \lambda_{k+1} \alpha_2 + \dots + a_k \lambda_{k+1} \alpha_k + a_{k+1} \lambda_{k+1} \alpha_{k+1} = \bar{0} \quad \text{--- (3)}
$$

Subtract equation (3) from equation (2). The last term ($a_{k+1}$) perfectly cancels out:

$$
a_1 (\lambda_1 - \lambda_{k+1}) \alpha_1 + a_2 (\lambda_2 - \lambda_{k+1}) \alpha_2 + \dots + a_k (\lambda_k - \lambda_{k+1}) \alpha_k = \bar{0} \quad \text{--- (4)}
$$

Look at equation (4). It is a linear combination of the first $k$ eigenvectors equal to zero. By our induction hypothesis, the first $k$ eigenvectors are linearly independent. Therefore, every single scalar coefficient in this equation must be exactly zero:

$$
a_i (\lambda_i - \lambda_{k+1}) = 0 \quad \text{for all } i = 1, \dots, k
$$

Because the eigenvalues are distinct, $\lambda_i \neq \lambda_{k+1}$, meaning $(\lambda_i - \lambda_{k+1}) \neq 0$. The only way the product can be zero is if:

$$
a_1 = 0, \quad a_2 = 0, \quad \dots, \quad a_k = 0
$$

Substitute these zero coefficients back into equation (1):

$$
0 \cdot \alpha_1 + \dots + 0 \cdot \alpha_k + a_{k+1} \alpha_{k+1} = \bar{0} \implies a_{k+1} \alpha_{k+1} = \bar{0}
$$

Because $\alpha_{k+1}$ is an eigenvector, it is not zero ($\alpha_{k+1} \neq \bar{0}$). Thus, $a_{k+1} = 0$.
Since $a_1 = a_2 = \dots = a_{k+1} = 0$, the set $S_{k+1}$ is linearly independent. By mathematical induction, the theorem holds for any number $n$.

---

### Corollary: Maximum Number of Distinct Eigenvalues
**Statement:** A linear operator $T$ on an $n$-dimensional vector space $V$ can have at most $n$ distinct eigenvalues.

**Proof:**
Assume, for contradiction, that $T$ has $n+1$ distinct eigenvalues. By Theorem 4, their corresponding $n+1$ eigenvectors must form a linearly independent set in $V$. However, it is a fundamental property of vector spaces that an $n$-dimensional space can contain a maximum of $n$ linearly independent vectors. The existence of $n+1$ linearly independent vectors is a contradiction. Thus, $T$ cannot have more than $n$ distinct eigenvalues.

---

## Theorem 5: The Characteristic Equation

**Statement:** Let $T$ be a linear operator on a finite-dimensional vector space $V$. The following three statements are mathematically equivalent:
1.  $\lambda$ is an eigenvalue of $T$.
2.  The operator $(T - \lambda I)$ is singular.
3.  $\det(T - \lambda I) = 0$.

**Proof (Circular Implication):**

**Part 1: (1) $\implies$ (2)**
Assume $\lambda$ is an eigenvalue of $T$. By definition, there is a non-zero vector $\alpha \in V$ such that $T(\alpha) = \lambda \alpha$.
Rewrite this:

$$
T(\alpha) - \lambda \alpha = \bar{0}
$$

$$
T(\alpha) - \lambda I(\alpha) = \bar{0} \implies (T - \lambda I)(\alpha) = \bar{0}
$$

Since the operator $(T - \lambda I)$ maps a non-zero vector $\alpha$ to the zero vector, its null space is not trivial. Therefore, $(T - \lambda I)$ is a singular operator.

**Part 2: (2) $\implies$ (3)**
Assume $(T - \lambda I)$ is singular. In a finite-dimensional space, a singular operator maps multiple vectors to zero, meaning its rank is less than the dimension of the space. Because it does not have full rank, the determinant of its matrix representation must be zero:

$$
\det(T - \lambda I) = 0
$$

**Part 3: (3) $\implies$ (1)**
Assume $\det(T - \lambda I) = 0$. Because the determinant is zero, the matrix is not invertible, which means the operator $(T - \lambda I)$ is singular.
Because it is singular, its null space contains at least one non-zero vector. Let this non-zero vector be $\alpha$.

$$
(T - \lambda I)(\alpha) = \bar{0}
$$

Expand this:

$$
T(\alpha) - \lambda I(\alpha) = \bar{0} \implies T(\alpha) = \lambda \alpha
$$

Because $\alpha$ is a non-zero vector that satisfies this relation, $\lambda$ is, by definition, an eigenvalue of $T$.
The equivalence of all three statements is proven.

## Key Takeaways
*   **Distinct Eigenvalues $\implies$ Independence**: Eigenvectors from different eigenvalues point in fundamentally different, non-overlapping directions in the vector space.
*   **The Characteristic Equation**: Theorem 5 provides the computational method to find eigenvalues. To find the eigenvalues of a transformation (or matrix), you set $\det(T - \lambda I) = 0$ and solve for $\lambda$. This is called the characteristic equation.

## What Comes Next
We will use the characteristic equation $\det(A - \lambda I) = 0$ to calculate the eigenvalues of matrices and determine if those matrices can be diagonalized.

---

**Navigation**
[< Previous Lecture](24_Eigenvalue_Eigenvector_Theory.md) | [Index](README.md) | [Next Lecture >](26_Matrix_Eigenvalue_Problems.md)
