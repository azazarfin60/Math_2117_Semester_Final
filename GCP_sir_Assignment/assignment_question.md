# GCP Sir's Assignment Questions

---

### Section A: Vector Spaces and Subspaces

1. Prove that $\mathbb{R}^n$ with usual operations is a vector space over $\mathbb{R}$.
2. Construct a non-trivial subspace of $\mathbb{R}^5$ that is not spanned by standard basis vectors.
3. Test whether the set $V = \lbrace(x, y) \in \mathbb{R}^2 : xy = 0\rbrace$ is a vector space.
4. Let $V = \mathbb{R}^4$. Prove that the set $W = \lbrace(x, y, z, w) : x + y + z + w = 0\rbrace$ is a subspace and find its dimension.
5. Let $W = \lbrace(x, y, z) \in \mathbb{R}^3 : x + 2y + 3z = 0\rbrace$. Show that $W$ is a subspace and find its dimension.
6. Give an example of a subset of a vector space that is closed under addition but not scalar multiplication.
7. Prove that the intersection of any collection of subspaces is a subspace.
8. Let $U, W \subseteq V$. Prove that $U + W$ is a subspace and

$$
\dim(U + W) = \dim U + \dim W - \dim(U \cap W)
$$

9. Prove that every subspace of a vector space is itself a vector space.
10. Show that the union of two subspaces is not necessarily a subspace.

---

### Section B: Sum and Direct Sum

11. Define the sum of two subspaces and give an example.
12. Prove that the sum of two subspaces is a subspace.
13. Show that $V = U \oplus W$ if and only if $V = U + W$ and $U \cap W = \lbrace 0\rbrace$.
14. Let $U = \text{span}\lbrace(1, 0, 0), (0, 1, 0)\rbrace$, $W = \text{span}\lbrace(0, 0, 1)\rbrace$. Show that $\mathbb{R}^3 = U \oplus W$.
15. Give an example where $U + W \neq U \oplus W$.

---

### Section C: Linear Transformations

16. Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ be defined by $T(x, y) = (x^2, y)$. Check whether $T$ is a linear transformation. Justify your answer.
17. Define kernel, range, rank, and nullity of a linear transformation.
18. Let $T: \mathbb{R}^3 \to \mathbb{R}^2$ be given by $T(x, y, z) = (x + y, y + z)$. Is it a linear transformation?
    Find: (i) Kernel of $T$, (ii) Range of $T$, (iii) Rank and Nullity.
19. Let $T: \mathbb{R}^3 \to \mathbb{R}^3$ be defined by $T(x, y, z) = (x + y, y + z, z + x)$.
    Find the matrix of $T$, its rank, nullity, and verify the rank-nullity theorem.
20. Find the matrix of the linear transformation $T: \mathbb{R}^2 \to \mathbb{R}^2$, defined by $T(x, y) = (2x + y, x - y)$, with respect to the standard basis.
21. Prove that a linear transformation $T: V \to W$ is injective if and only if $\text{ker}(T) = \lbrace 0\rbrace$.
22. Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ be given by $T(x, y) = (3x + 2y, x + y)$. Determine whether $T$ is invertible. If yes, find $T^{-1}$.
23. Let $T: \mathbb{R}^2 \to \mathbb{R}^2$ be defined by $T(x, y) = (x + y, x - y)$. Let $B = \lbrace(1, 1), (1, -1)\rbrace$. Find the matrix of $T$ with respect to the basis $B$.
24. Show that a linear transformation is injective if and only if its nullity is zero.
25. Prove that a linear transformation is invertible if and only if it is both one-to-one and onto.

---

### Section D: Eigenvalues and Eigenvectors

21. Prove that eigenvalues of a triangular matrix are its diagonal entries.
22. Show that eigenvectors corresponding to distinct eigenvalues are linearly independent.
23. Find eigenvalues and eigenvectors of

$$
A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}.
$$

24. Prove that the sum of eigenvalues equals the trace of the matrix.
25. Let $A$ be invertible. Prove that eigenvalues of $A^{-1}$ are reciprocals of eigenvalues of $A$.
26. State and prove the necessary and sufficient condition for a matrix to be diagonalizable.
27. Diagonalize the matrix:

$$
\begin{pmatrix} 4 & 1 \\ 0 & 4 \end{pmatrix}
$$

(if possible).

---

### Section E: Normed Linear Space & Hilbert Space

28. Define a normed linear space and give two examples.
29. Verify whether $\|x\| = |x_1| + |x_2|$ defines a norm on $\mathbb{R}^2$.
30. Prove that every inner product space is a normed space.
31. Show that the space $\ell^2$ is a Hilbert space.
32. Prove the parallelogram law in an inner product space.

---

### Section F: Banach Space (Branch Space)

33. Define a Banach space and give an example.
34. Prove that every finite-dimensional normed linear space is complete.
35. Show that $\ell^\infty$ is a Banach space.
36. Give an example of a normed space that is not complete.
37. Prove that every Hilbert space is a Banach space.

---

### Section G: Basis and Dimension

39. Define basis and dimension of a vector space.
40. Prove that every finite-dimensional vector space has a basis.
41. Show that any two bases of a finite-dimensional vector space have the same number of elements.
42. Extend a linearly independent set to a basis.

---

### Section H: Matrix Representation, Change of Basis, Similarity

43. Find the matrix representation of a linear transformation with respect to a given basis.
44. Define singular and non-singular transformations and relate them to matrices.