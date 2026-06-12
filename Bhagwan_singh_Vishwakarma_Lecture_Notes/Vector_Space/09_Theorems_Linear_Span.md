# Lecture 09: Vector Space - Theorems on Linear Span

> **Series**: Vector Space by Bhagwan Singh Vishwakarma
> **Lecture**: 09 of 27
> **Video**: https://www.youtube.com/watch?v=iF7ya80h1Rs

---

**Navigation**
[< Previous Lecture](08_Dimension_Sum_Subspace.md) | [Index](README.md) | [Next Lecture >](10_Theorems_Independence_Dependence.md)

---

## Prerequisites
We know that the linear span $L(S)$ of a set $S$ is the collection of all possible linear combinations of the vectors in $S$. We also proved earlier that the linear span of any set is always a vector subspace of $V(F)$. 

Today, we will prove five critical theorems related to the behavior of the linear span. These theorems test your understanding of how sets, spans, and subspaces interact.

---

## The Five Theorems of Linear Span

Let $S$ and $T$ be two subsets of a vector space $V(F)$. The following five properties always hold true:

1.  If $S \subseteq L(T)$, then $L(S) \subseteq L(T)$.
2.  If $S \subseteq T$, then $L(S) \subseteq L(T)$.
3.  $S$ is a subspace of $V(F)$ if and only if $L(S) = S$.
4.  $L(S \cup T) = L(S) + L(T)$.
5.  $L(L(S)) = L(S)$.

We will prove each of these step by step. The key to proving these is to rely on two facts:
*   Any set is a subset of its own linear span ($S \subseteq L(S)$).
*   A linear span is always a subspace, meaning it is closed under linear combinations.

---

### Proof 1: If, then

We are given that every element of $S$ is already in the linear span of $T$. We want to show that any linear combination built from $S$ will also belong to the linear span of $T$.

Let $S = \lbrace \alpha_1, \alpha_2, \dots, \alpha_n \rbrace$.
Since $S \subseteq L(T)$, we know that all these vectors belong to $L(T)$:

$$
\alpha_1, \alpha_2, \dots, \alpha_n \in L(T)
$$

Now, let $x$ be an arbitrary element of $L(S)$. By definition, $x$ is a linear combination of elements of $S$:

$$
x = a_1\alpha_1 + a_2\alpha_2 + \dots + a_n\alpha_n \quad (\text{where } a_i \in F)
$$

We already know that $\alpha_1, \dots, \alpha_n$ belong to $L(T)$. We also know that $L(T)$ is a subspace. Because it is a subspace, it is closed under vector addition and scalar multiplication. Therefore, any linear combination of elements inside $L(T)$ must also stay inside $L(T)$.

$$
a_1\alpha_1 + a_2\alpha_2 + \dots + a_n\alpha_n \in L(T)
$$

Because this combination is equal to $x$, we have:

$$
x \in L(T)
$$

We picked $x$ from $L(S)$ and showed it belongs to $L(T)$. Thus:

$$
L(S) \subseteq L(T)
$$

---

### Proof 2: If, then

This proof is almost identical to the first one.

Let $S = \lbrace \alpha_1, \alpha_2, \dots, \alpha_n \rbrace$.
Since $S \subseteq T$, we know:

$$
\alpha_1, \alpha_2, \dots, \alpha_n \in T
$$

Any set is automatically a subset of its own linear span ($T \subseteq L(T)$). Because these vectors are in $T$, they must also be in $L(T)$:

$$
\alpha_1, \alpha_2, \dots, \alpha_n \in L(T)
$$

Let $x$ be an arbitrary element of $L(S)$. By definition:

$$
x = a_1\alpha_1 + a_2\alpha_2 + \dots + a_n\alpha_n
$$

Because all the $\alpha_i$ vectors belong to the subspace $L(T)$, their linear combination must also belong to $L(T)$.

$$
x \in L(T)
$$

Thus, $L(S) \subseteq L(T)$.

---

### Proof 3: is a subspace if and only if

This is an "if and only if" proof, so we must prove both directions.

**Part A: Assume $L(S) = S$**
We know that the linear span $L(S)$ of any set is always a vector subspace. Since $S$ is equal to $L(S)$, $S$ must also be a vector subspace.

**Part B: Assume $S$ is a subspace**
We want to show $L(S) = S$. To show two sets are equal, we prove they contain each other.

1.  **Show $S \subseteq L(S)$:**
    Any vector $\alpha \in S$ can be written as $1 \cdot \alpha$. This is a linear combination of elements in $S$. Thus, $\alpha \in L(S)$. So, $S \subseteq L(S)$.
2.  **Show $L(S) \subseteq S$:**
    Let $x \in L(S)$. Then $x$ is a linear combination:

$$
    x = a_1\alpha_1 + a_2\alpha_2 + \dots + a_n\alpha_n \quad (\text{where } \alpha_i \in S)
$$

    Because $S$ is given as a subspace, it is closed under linear combinations. Therefore, this sum must belong to $S$.

$$
    x \in S
$$

    Thus, $L(S) \subseteq S$.

Since they contain each other, $L(S) = S$.

---

### Proof 4

We want to show that the span of the union of two sets is the same as the linear sum of their individual spans. We prove mutual containment.

**Part A: Show $L(S \cup T) \subseteq L(S) + L(T)$**
Let $x \in L(S \cup T)$. This means $x$ is a linear combination of elements from both $S$ and $T$.

$$
x = \sum_{i=1}^n a_i\alpha_i + \sum_{j=1}^m b_j\beta_j \quad (\text{where } \alpha_i \in S, \beta_j \in T)
$$

The first sum is built entirely from elements of $S$, so it belongs to $L(S)$. Let's call it $y$.
The second sum is built entirely from elements of $T$, so it belongs to $L(T)$. Let's call it $z$.

$$
x = y + z \quad (\text{where } y \in L(S), z \in L(T))
$$

By the definition of the linear sum of subspaces, $x$ belongs to $L(S) + L(T)$. Thus:

$$
L(S \cup T) \subseteq L(S) + L(T)
$$

**Part B: Show $L(S) + L(T) \subseteq L(S \cup T)$**
Let $x \in L(S) + L(T)$. This means $x$ is the sum of an element from $L(S)$ and an element from $L(T)$:

$$
x = y + z
$$

Since $y \in L(S)$, $y$ is a linear combination of elements of $S$: $y = \sum a_i\alpha_i$.
Since $z \in L(T)$, $z$ is a linear combination of elements of $T$: $z = \sum b_j\beta_j$.

Therefore, $x = \sum a_i\alpha_i + \sum b_j\beta_j$.
Since both $S$ and $T$ are subsets of $S \cup T$, all $\alpha_i$ and $\beta_j$ vectors belong to $S \cup T$. Thus, $x$ is a linear combination of elements in $S \cup T$.

$$
x \in L(S \cup T)
$$

Thus, $L(S) + L(T) \subseteq L(S \cup T)$. Both directions are proven.

---

### Proof 5

This looks complicated, but it is the easiest one to prove if we use Theorem 3.

From Theorem 3, we proved that for any subspace $W$, $L(W) = W$.
We already know that the linear span $L(S)$ is always a subspace of $V(F)$.
So, substitute $W = L(S)$ into the rule:

$$
L(L(S)) = L(S)
$$

The theorem is instantly proven.

---

## Key Takeaways
*   The linear span is always a subspace, so any linear combination of its elements stays inside it.
*   If $S$ is already a subspace, its span is just itself: $L(S) = S$.
*   The span of a union is the linear sum of the spans: $L(S \cup T) = L(S) + L(T)$.
*   Taking the span of a span does nothing new: $L(L(S)) = L(S)$.

## What Comes Next
We have covered the fundamentals of span, independence, and basis. In the next lectures, we will look at more advanced theorems involving linear independence and how to extend a linearly independent set to form a complete basis for a vector space.

---

**Navigation**
[< Previous Lecture](08_Dimension_Sum_Subspace.md) | [Index](README.md) | [Next Lecture >](10_Theorems_Independence_Dependence.md)
