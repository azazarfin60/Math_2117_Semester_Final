# Section G: Basis and Dimension

## Q39 (04)
**Question:** **Define basis and dimension of a vector space.**

**Answer:**
*   **Basis:** A subset $B$ of a vector space $V$ is called a basis of $V$ if it satisfies two conditions:
    1.  $B$ is linearly independent (no vector in $B$ can be written as a linear combination of the others).
    2.  $B$ spans $V$ (every vector in $V$ can be expressed as a finite linear combination of vectors in $B$).
*   **Dimension:** The dimension of a vector space $V$, denoted as $\dim(V)$, is defined as the number of vectors in any basis for $V$. If $V$ has a basis with a finite number of vectors $n$, then $\dim(V) = n$. If $V$ is spanned by a finite set, it is called finite-dimensional; otherwise, it is infinite-dimensional.

## Q40 (05)
**Question:** **Prove that every finite-dimensional vector space has a basis.**

**Answer:**
Let $V$ be a finite-dimensional vector space. By definition, there exists a finite spanning set

$$
S = \lbrace v_1, v_2, \dots, v_n\rbrace
$$

such that $\text{span}(S) = V$.
We construct a basis by an iterative process of removing redundant vectors:

1. If $S$ is linearly independent, then $S$ is a basis, and we are done.
2. If $S$ is linearly dependent, there exists some vector $v_k \in S$ that can be written as a linear combination of the other vectors in $S$.
3. Remove $v_k$ from $S$ to form a new set

$$
S_1 = S \setminus \lbrace v_k\rbrace
$$

. Since $v_k$ was already a linear combination of the remaining vectors, its removal does not change the span. Thus,

$$
\text{span}(S_1) = \text{span}(S) = V.
$$

4. Check if $S_1$ is linearly independent. If it is, $S_1$ is a basis. If not, repeat the process.

Since $S$ is finite (contains $n$ elements), this removal process must terminate after at most $n$ steps. It cannot result in the empty set (unless $V = \lbrace 0\rbrace$, which trivially has an empty basis). When the process terminates, the resulting subset $S_k \subseteq S$ will be linearly independent and will still span $V$. Therefore, $S_k$ is a basis for $V$. Thus, every finite-dimensional vector space has a basis.

## Q41 (05)
**Question:** **Show that any two bases of a finite-dimensional vector space have the same number of elements.**

**Answer:**
Let $V$ be a finite-dimensional vector space. Let

$$
B_1 = \lbrace u_1, u_2, \dots, u_m\rbrace
$$

and

$$
B_2 = \lbrace v_1, v_2, \dots, v_n\rbrace
$$

be two bases for $V$. We want to show that $m = n$.

We will use the Steinitz Exchange Lemma. Since $B_1$ spans $V$ and $B_2$ is a linearly independent set in $V$, the lemma states that the number of vectors in the linearly independent set cannot exceed the number of vectors in the spanning set. Applying this:
*   Because $B_1$ is a spanning set and $B_2$ is linearly independent, we have $n \leq m$.
*   Because $B_2$ is a spanning set and $B_1$ is linearly independent, we have $m \leq n$.

Combining these two inequalities gives $m \leq n$ and $n \leq m$, which implies $m = n$. Therefore, any two bases of a finite-dimensional vector space must contain the exact same number of elements.

## Q42 (04)
**Question:** **Extend a linearly independent set to a basis.**

**Answer:**
Let $V$ be an $n$-dimensional vector space. Let

$$
S = \lbrace v_1, v_2, \dots, v_k\rbrace
$$

be a linearly independent set in $V$ with $k < n$. We want to extend $S$ to form a basis for $V$.

Let

$$
B = \lbrace e_1, e_2, \dots, e_n\rbrace
$$

be any known basis for $V$ (such as the standard basis if

$$
V = \mathbb{R}^n
$$

).
Consider the union of sets:

$$
S \cup B = \lbrace v_1, \dots, v_k, e_1, \dots, e_n\rbrace.
$$

This combined set clearly spans $V$ because it contains $B$, which already spans $V$.
To reduce this spanning set to a basis while keeping all elements of $S$:

1. Start with the set $S$. Since $S$ is linearly independent, we retain all $k$ vectors.
2. Consider $e_1$. Check if $e_1 \in \text{span}(S)$.
   *   If yes, discard $e_1$.
   *   If no, add $e_1$ to the set. The new set $S \cup \lbrace e_1\rbrace$ is still linearly independent.
3. Repeat this process for each $e_i$ in $B$, one by one. Check if $e_i$ is in the span of the previously accepted vectors. If not, append it; if it is, discard it.

Because $B$ spans $V$, this process guarantees that the span of the final accepted set will be $V$. Furthermore, we only add a vector if it is linearly independent from the existing set, ensuring the final set remains linearly independent. The process will stop when exactly $n - k$ vectors from $B$ have been added to $S$, resulting in a set of exactly $n$ linearly independent vectors that span $V$. This final set is the extended basis.