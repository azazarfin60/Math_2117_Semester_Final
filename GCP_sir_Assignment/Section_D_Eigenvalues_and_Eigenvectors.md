# Section D: Eigenvalues and Eigenvectors

## Q21 (04)
**Question:** **Prove that eigenvalues of a triangular matrix are its diagonal entries.**

**Answer:**
Let $A$ be an $n \times n$ triangular matrix. Without loss of generality, assume $A$ is an upper triangular matrix:

$$
A = \begin{pmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
0 & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & a_{nn}
\end{pmatrix}
$$

The eigenvalues of $A$ are the roots of the characteristic equation $\det(A - \lambda I) = 0$.
The matrix $A - \lambda I$ is:

$$
A - \lambda I = \begin{pmatrix}
a_{11} - \lambda & a_{12} & \dots & a_{1n} \\
0 & a_{22} - \lambda & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & a_{nn} - \lambda
\end{pmatrix}
$$

Since $A - \lambda I$ is also an upper triangular matrix, its determinant is simply the product of its main diagonal entries:

$$
\det(A - \lambda I) = (a_{11} - \lambda)(a_{22} - \lambda) \dots (a_{nn} - \lambda)
$$

Setting the determinant to zero gives:

$$
(a_{11} - \lambda)(a_{22} - \lambda) \dots (a_{nn} - \lambda) = 0
$$

The roots of this equation are $\lambda_1 = a_{11}, \lambda_2 = a_{22}, \dots, \lambda_n = a_{nn}$.
Thus, the eigenvalues of a triangular matrix are exactly its diagonal entries.

## Q22 (05)
**Question:** **Show that eigenvectors corresponding to distinct eigenvalues are linearly independent.**

**Answer:**
Let $v_1, v_2, \dots, v_k$ be eigenvectors of a matrix $A$ corresponding to distinct eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_k$. We proceed by mathematical induction on $k$.

For $k = 1$, a single eigenvector $v_1$ is non-zero by definition, so $\lbrace v_1\rbrace$ is linearly independent.
Assume that any set of $k-1$ eigenvectors corresponding to distinct eigenvalues is linearly independent.
Consider a linear combination of the $k$ eigenvectors set to zero:

$$
c_1v_1 + c_2v_2 + \dots + c_kv_k = 0 \quad \text{--- (1)}
$$

Multiply equation (1) by the matrix $A$:

$$
A(c_1v_1 + c_2v_2 + \dots + c_kv_k) = A(0) = 0
$$

Since $Av_i = \lambda_i v_i$, this becomes:

$$
c_1\lambda_1v_1 + c_2\lambda_2v_2 + \dots + c_k\lambda_kv_k = 0 \quad \text{--- (2)}
$$

Now, multiply equation (1) by $\lambda_k$ and subtract it from equation (2):

$$
c_1(\lambda_1 - \lambda_k)v_1 + c_2(\lambda_2 - \lambda_k)v_2 + \dots + c_{k-1}(\lambda_{k-1} - \lambda_k)v_{k-1} + c_k(\lambda_k - \lambda_k)v_k = 0
$$

This leaves:

$$
c_1(\lambda_1 - \lambda_k)v_1 + \dots + c_{k-1}(\lambda_{k-1} - \lambda_k)v_{k-1} = 0
$$

By the inductive hypothesis, $\lbrace v_1, \dots, v_{k-1}\rbrace$ is a linearly independent set. Therefore, all coefficients in the linear combination must be zero:

$$
c_i(\lambda_i - \lambda_k) = 0 \quad \text{for } i = 1, \dots, k-1
$$

Since the eigenvalues are distinct, $\lambda_i - \lambda_k \neq 0$. Thus, $c_i = 0$ for all $i = 1, \dots, k-1$.
Substituting these zeros back into equation (1) gives $c_kv_k = 0$. Since $v_k \neq 0$, we must have $c_k = 0$.
Since all $c_i = 0$, the set of vectors $\lbrace v_1, \dots, v_k\rbrace$ is linearly independent.

## Q23 (05)
**Question:** **Find eigenvalues and eigenvectors of

$$
A =
\begin{pmatrix}
2 & 1 \\
1 & 2
\end{pmatrix}.
$$

**

**Answer:**
**1. Find Eigenvalues:**
The characteristic equation is $\det(A - \lambda I) = 0$.

$$
\det
\begin{pmatrix}
2 - \lambda & 1 \\
1 & 2 - \lambda
\end{pmatrix} = (2 - \lambda)(2 - \lambda) - 1 = \lambda^2 - 4\lambda + 4 - 1 = \lambda^2 - 4\lambda + 3 = 0
$$

Factoring the characteristic polynomial:

$$
(\lambda - 3)(\lambda - 1) = 0
$$

The eigenvalues are $\lambda_1 = 3$ and $\lambda_2 = 1$.

**2. Find Eigenvectors:**
**For $\lambda_1 = 3$:**
Solve $(A - 3I)v = 0$.

$$
\begin{pmatrix}
2 - 3 & 1 \\
1 & 2 - 3
\end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

This gives the equation $-x + y = 0 \implies x = y$.
The eigenvector for $\lambda_1 = 3$ is

$$
v_1 =
\begin{pmatrix}
1 \\
1
\end{pmatrix}.
$$

**For $\lambda_2 = 1$:**
Solve $(A - 1I)v = 0$.

$$
\begin{pmatrix}
2 - 1 & 1 \\
1 & 2 - 1
\end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

This gives the equation $x + y = 0 \implies x = -y$.
The eigenvector for $\lambda_2 = 1$ is

$$
v_2 =
\begin{pmatrix}
1 \\
-1
\end{pmatrix}.
$$

## Q24 (04)
**Question:** **Prove that the sum of eigenvalues equals the trace of the matrix.**

**Answer:**
Let $A$ be an $n \times n$ matrix. The characteristic polynomial is defined as $P(\lambda) = \det(A - \lambda I)$.
The roots of this polynomial are the eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$.
We can express the polynomial in its factored form based on its roots:

$$
P(\lambda) = (-1)^n (\lambda - \lambda_1)(\lambda - \lambda_2) \dots (\lambda - \lambda_n)
$$

Expanding this product, the coefficient of $\lambda^{n-1}$ is given by:

$$
(-1)^n \left( -(\lambda_1 + \lambda_2 + \dots + \lambda_n) \right) = (-1)^{n-1} \sum_{i=1}^n \lambda_i
$$

Alternatively, computing the determinant $\det(A - \lambda I)$ from the definition using permutations, the only term that contributes to $\lambda^n$ and $\lambda^{n-1}$ comes from the product of the diagonal elements:

$$
(a_{11} - \lambda)(a_{22} - \lambda) \dots (a_{nn} - \lambda)
$$

Expanding this product, the term with $\lambda^{n-1}$ is:

$$
(-1)^{n-1} \lambda^{n-1} (a_{11} + a_{22} + \dots + a_{nn}) = (-1)^{n-1} \lambda^{n-1} \text{tr}(A)
$$

Since both expressions must be equal, the coefficients of $\lambda^{n-1}$ are identical:

$$
(-1)^{n-1} \sum_{i=1}^n \lambda_i = (-1)^{n-1} \text{tr}(A)
$$

Dividing by $(-1)^{n-1}$ yields:

$$
\sum_{i=1}^n \lambda_i = \text{tr}(A)
$$

Thus, the sum of the eigenvalues equals the trace of the matrix.

## Q25 (05)
**Question:** **Let $A$ be invertible. Prove that eigenvalues of $A^{-1}$ are reciprocals of eigenvalues of $A$.**

**Answer:**
Let $\lambda$ be an eigenvalue of the invertible matrix $A$, and let $v$ be its corresponding non-zero eigenvector.
By definition, we have:

$$
Av = \lambda v
$$

Since $A$ is invertible, we can multiply both sides on the left by $A^{-1}$:

$$
A^{-1}(Av) = A^{-1}(\lambda v)
$$

This simplifies to:

$$
I v = \lambda (A^{-1}v)
$$

$$
v = \lambda (A^{-1}v)
$$

Since $A$ is invertible, $0$ cannot be an eigenvalue (because $\det(A) \neq 0$). Thus $\lambda \neq 0$.
We can divide both sides by $\lambda$:

$$
\frac{1}{\lambda} v = A^{-1}v
$$

This equation shows that $\frac{1}{\lambda}$ is an eigenvalue of $A^{-1}$ with the same corresponding eigenvector $v$.
Therefore, the eigenvalues of $A^{-1}$ are exactly the reciprocals of the eigenvalues of $A$.

## Q26 (04)
**Question:** **State and prove the necessary and sufficient condition for a matrix to be diagonalizable.**

**Answer:**
**Statement:**
An $n \times n$ matrix $A$ is diagonalizable if and only if it possesses $n$ linearly independent eigenvectors.

**Proof:**
$(\Rightarrow)$ **Necessary condition:** Suppose $A$ is diagonalizable.
Then there exists an invertible matrix $P$ and a diagonal matrix $D$ such that $A = PDP^{-1}$.
Multiplying by $P$ on the right, we get $AP = PD$.
Let $P$ consist of column vectors $v_1, v_2, \dots, v_n$, and let $D$ have diagonal entries $\lambda_1, \lambda_2, \dots, \lambda_n$.
The $i$-th column of the product $AP$ is $Av_i$.
The $i$-th column of the product $PD$ is $\lambda_i v_i$.
Since $AP = PD$, it follows that $Av_i = \lambda_i v_i$ for all $i = 1, \dots, n$.
This means that the column vectors $v_1, \dots, v_n$ of $P$ are eigenvectors of $A$.
Since $P$ is invertible, its columns must be linearly independent.
Thus, $A$ has $n$ linearly independent eigenvectors.

$(\Leftarrow)$ **Sufficient condition:** Suppose $A$ has $n$ linearly independent eigenvectors $v_1, v_2, \dots, v_n$ corresponding to eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_n$.
Construct a matrix $P$ using these eigenvectors as its columns:

$$
P = \begin{pmatrix} v_1 & v_2 & \dots & v_n \end{pmatrix}.
$$

Since the columns are linearly independent, $P$ is invertible.
Construct a diagonal matrix $D$ with the corresponding eigenvalues on the diagonal: $D = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$.
Then

$$
AP = A \begin{pmatrix} v_1 & v_2 & \dots & v_n \end{pmatrix} = \begin{pmatrix} Av_1 & Av_2 & \dots & Av_n \end{pmatrix} = \begin{pmatrix} \lambda_1 v_1 & \lambda_2 v_2 & \dots & \lambda_n v_n \end{pmatrix}.
$$

Similarly,

$$
PD = \begin{pmatrix} v_1 & v_2 & \dots & v_n \end{pmatrix} \text{diag}(\lambda_1, \dots, \lambda_n) = \begin{pmatrix} \lambda_1 v_1 & \lambda_2 v_2 & \dots & \lambda_n v_n \end{pmatrix}.
$$

Since $AP = PD$ and $P$ is invertible, we can multiply on the right by $P^{-1}$ to obtain $A = PDP^{-1}$.
Thus, $A$ is diagonalizable.

## Q27 (05)
**Question:** **Diagonalize the matrix:

$$
\begin{pmatrix}
4 & 1 \\
0 & 4
\end{pmatrix}
$$

(if possible).**

**Answer:**
To determine if the matrix is diagonalizable, we must check if it has 2 linearly independent eigenvectors.
Let

$$
A =
\begin{pmatrix}
4 & 1 \\
0 & 4
\end{pmatrix}.
$$

**1. Find Eigenvalues:**
The characteristic equation is $\det(A - \lambda I) = 0$.

$$
\det
\begin{pmatrix}
4 - \lambda & 1 \\
0 & 4 - \lambda
\end{pmatrix} = (4 - \lambda)^2 = 0
$$

The only eigenvalue is $\lambda = 4$ (with algebraic multiplicity 2).

**2. Find Eigenvectors:**
Solve $(A - 4I)v = 0$.

$$
\begin{pmatrix}
4 - 4 & 1 \\
0 & 4 - 4
\end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}
$$

This gives the equation $y = 0$. The variable $x$ is a free variable.
So the eigenvectors are of the form

$$
\begin{pmatrix}
x \\
0
\end{pmatrix} = x \begin{pmatrix} 1 \\ 0 \end{pmatrix}.
$$

There is only one linearly independent eigenvector:

$$
v_1 =
\begin{pmatrix}
1 \\
0
\end{pmatrix}.
$$

Since the $2 \times 2$ matrix $A$ has only 1 linearly independent eigenvector (its geometric multiplicity is 1), it does not have enough eigenvectors to form an invertible matrix $P$.
Therefore, the matrix

$$
\begin{pmatrix}
4 & 1 \\
0 & 4
\end{pmatrix}
$$

is **not diagonalizable**.