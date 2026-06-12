# Section H: Matrix Representation, Change of Basis, Similarity

## Q43 (04)
**Question:** **Find the matrix representation of a linear transformation with respect to a given basis.**

**Answer:**
Let $T: V \to W$ be a linear transformation. Let

$$
B = \lbrace v_1, v_2, \dots, v_n\rbrace
$$

be a basis for $V$ and

$$
C = \lbrace w_1, w_2, \dots, w_m\rbrace
$$

be a basis for $W$. To find the matrix representation $[T]_B^C$, we perform the following steps:

1.  **Apply Transformation:** Apply the linear transformation $T$ to each basis vector in the domain basis $B$. This yields the image vectors $T(v_1), T(v_2), \dots, T(v_n)$ in $W$.
2.  **Express as Linear Combinations:** Express each of these image vectors as a linear combination of the basis vectors in the codomain basis $C$. For the $j$-th vector $T(v_j)$:

$$
T(v_j) = a_{1j}w_1 + a_{2j}w_2 + \dots + a_{mj}w_m
$$

3.  **Extract Coordinate Vectors:** Extract the coefficients

$$
(a_{1j}, a_{2j}, \dots, a_{mj})
$$

to form the coordinate vector $[T(v_j)]_C$.
4.  **Construct Matrix:** Construct the $m \times n$ matrix $[T]_B^C$ by using these coordinate vectors as its columns:

$$
[T]_B^C = \begin{pmatrix}
[T(v_1)]_C & [T(v_2)]_C & \dots & [T(v_n)]_C
\end{pmatrix} =
\begin{pmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
a_{21} & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{pmatrix}
$$

This matrix satisfies the fundamental property

$$
[T(x)]_C = [T]_B^C [x]_B
$$

for any vector $x \in V$.

## Q44 (05)
**Question:** **Define singular and non-singular transformations and relate them to matrices.**

**Answer:**
Let $T: V \to V$ be a linear transformation on a finite-dimensional vector space $V$.

*   **Non-Singular Transformation:** A linear transformation $T$ is non-singular if its kernel contains only the zero vector, i.e., $\text{ker}(T) = \lbrace 0\rbrace$. Equivalently, $T$ is non-singular if it is a bijective (invertible) mapping. If $T(v) = 0$, then $v$ must be $0$.
*   **Singular Transformation:** A linear transformation $T$ is singular if its kernel contains non-zero vectors, i.e., $\text{ker}(T) \neq \lbrace 0\rbrace$. This means there exists some $v \neq 0$ such that $T(v) = 0$. A singular transformation is not invertible.

**Relation to Matrices:**
Let $A$ be the $n \times n$ matrix representation of the transformation $T$ with respect to some basis.
1.  **Non-Singular:** The transformation $T$ is non-singular if and only if the matrix $A$ is invertible. This occurs when the determinant of $A$ is non-zero ($\det(A) \neq 0$), meaning its columns are linearly independent and its rank is equal to $n$.
2.  **Singular:** The transformation $T$ is singular if and only if the matrix $A$ is not invertible. This occurs when the determinant of $A$ is exactly zero ($\det(A) = 0$), meaning its columns are linearly dependent and its rank is strictly less than $n$.