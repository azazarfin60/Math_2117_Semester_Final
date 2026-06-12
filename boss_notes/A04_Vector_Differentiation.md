[← Previous: A03 Triple Products](A03_Triple_Products_Area_Volume.md) | [Index](00_Index.md) | [Next: A05 Velocity and Acceleration →](A05_Velocity_Acceleration_Particle_Motion.md)

---

# A04: Vector Differentiation

> **Exam Weight**: Tier 3 | **Appeared in**: 2019, 2024 | **Typical Marks**: 3–4

Differentiating a vector function works exactly like scalar differentiation, component by component. The product rule still applies to both dot and cross products.

---

## The Basics

If a position vector is given as a function of time $t$:

$$
\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}
$$

The derivative with respect to $t$ is:

$$
\frac{d\vec{r}}{dt} = \frac{dx}{dt}\hat{i} + \frac{dy}{dt}\hat{j} + \frac{dz}{dt}\hat{k}
$$

### Product Rules
When differentiating the product of two vector functions $\vec{A}(t)$ and $\vec{B}(t)$:

**Dot Product Rule**:

$$
\frac{d}{dt} (\vec{A} \cdot \vec{B}) = \vec{A} \cdot \frac{d\vec{B}}{dt} + \frac{d\vec{A}}{dt} \cdot \vec{B}
$$

**Cross Product Rule** (Order matters!):

$$
\frac{d}{dt} (\vec{A} \times \vec{B}) = \vec{A} \times \frac{d\vec{B}}{dt} + \frac{d\vec{A}}{dt} \times \vec{B}
$$

---

## Must-Know Proof: Constant Magnitude (PYQ 2019)

**Problem**: If $\vec{A}$ has a constant magnitude, show that $\vec{A}$ and $\frac{d\vec{A}}{dt}$ are perpendicular, provided $\left\lvert \frac{d\vec{A}}{dt}\right\rvert  \neq 0$.

**Proof**:
Let the constant magnitude of $\vec{A}$ be $\lvert \vec{A} \rvert = c$ (where $c$ is a constant).
We know that the dot product of a vector with itself is its magnitude squared:

$$
\vec{A} \cdot \vec{A} = \lvert \vec{A} \rvert^2 = c^2
$$

Differentiate both sides with respect to $t$:

$$
\frac{d}{dt} (\vec{A} \cdot \vec{A}) = \frac{d}{dt} (c^2)
$$

Apply the dot product rule to the left side, and note that the derivative of a constant is 0:

$$
\vec{A} \cdot \frac{d\vec{A}}{dt} + \frac{d\vec{A}}{dt} \cdot \vec{A} = 0
$$

Since the dot product is commutative ($\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$):

$$
2 \left( \vec{A} \cdot \frac{d\vec{A}}{dt} \right) = 0 \implies \vec{A} \cdot \frac{d\vec{A}}{dt} = 0
$$

Because their dot product is zero and neither vector is the zero vector, $\vec{A}$ and $\frac{d\vec{A}}{dt}$ must be mutually perpendicular. $\blacksquare$

---

## Exam Patterns
- The "constant magnitude implies perpendicular derivative" proof is a classic theoretical question. Memorize the 4-step proof above.
- The fundamental concept of taking a derivative component-by-component is heavily used in the next topic: finding velocity and acceleration.

---

[← Previous: A03 Triple Products](A03_Triple_Products_Area_Volume.md) | [Index](00_Index.md) | [Next: A05 Velocity and Acceleration →](A05_Velocity_Acceleration_Particle_Motion.md)
