---
layout: default
title: Triángulo de Pascal
parent: Programación dinámica
grandparent: 3. Matemáticas y algoritmos
nav_order: 1
---

## Binomial expansion: expanding (a+b)ⁿ step by step

**Base cases**
- (a+b)⁰ = 1
- (a+b)¹ = a + b

**Rule:** to get the next power, multiply every term by **a** and by **b**, then combine like terms.

### From (a+b)¹ to (a+b)²

```
        a                 b
       / \               / \
     ×a   ×b           ×a   ×b
     /     \           /     \
   a²       ab       ab       b²
            └────┬────┘
           ab + ab = 2ab

(a+b)² = a² + 2ab + b²
```

### From (a+b)² to (a+b)³

```
         a²                 2ab                 b²
        /  \               /   \               /  \
      ×a    ×b           ×a     ×b           ×a    ×b
      /      \           /       \           /      \
     a³      a²b       2a²b      2ab²      ab²      b³
              └────┬────┘         └────┬────┘
                 3a²b                3ab²

(a+b)³ = a³ + 3a²b + 3ab² + b³
```

### From (a+b)³ to (a+b)⁴

```
         a³               3a²b              3ab²               b³
        /  \              /  \              /  \              /  \
      ×a    ×b          ×a    ×b          ×a    ×b          ×a    ×b
      /      \          /      \          /      \          /      \
     a⁴      a³b     3a³b      3a²b²  3a²b²      3ab³     ab³      b⁴
              └───┬───┘          └───┬───┘        └───┬───┘
                4a³b               6a²b²            4ab³

(a+b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴
```

### The coefficients form Pascal's triangle

Each number is the sum of the two above it (e.g. 3 + 3 = 6).

```
n=0:            1
n=1:          1   1
n=2:        1   2   1
n=3:      1   3   3   1
n=4:    1   4   6   4   1
n=5:  1   5  10   10  5   1
```

### Binomial theorem

$$
(a+b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^{k}
$$

OR

(a+b)ⁿ = Σₖ₌₀ⁿ C(n,k) · aⁿ⁻ᵏ · bᵏ

#### What it says

It packs the whole tree and Pascal's triangle into one line. Piece by piece:

- **Σ (sigma)** means "add up". The k=0 underneath and the n on top mean: work out the expression for k = 0, 1, 2, … up to n, then add all the results.
- **(n over k)**, or C(n,k), read "n choose k", is the **number from Pascal's triangle**: row n, position k (counting from 0). You can also calculate it directly:
  C(n,k) = n! / (k! · (n−k)!)
- **aⁿ⁻ᵏ** makes the power of a count down from n.
- **bᵏ** makes the power of b count up from 0.

## Example: n = 4

| k | C(4,k) | aⁿ⁻ᵏ | bᵏ | Term |
|---|---|---|---|---|
| 0 | 1 | a⁴ | b⁰ = 1 | a⁴ |
| 1 | 4 | a³ | b | 4a³b |
| 2 | 6 | a² | b² | 6a²b² |
| 3 | 4 | a | b³ | 4ab³ |
| 4 | 1 | 1 | b⁴ | b⁴ |

Add them up and you get **a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴**, the same answer you got from the tree.

Here's a check with the factorial formula for the middle term: C(4,2) = 4! / (2! · 2!) = 24 / 4 = **6** ✓

**Why it's useful:** with this formula you can find any single term without building the tree or the triangle. For example, the a⁷b³ term in (a+b)¹⁰ is C(10,3) = 120, so the term is 120a⁷b³.

## Pascal's rule

That's **Pascal's rule**. It's the "each number is the sum of the two above it" rule from Pascal's triangle, written as a formula.

**LaTeX version:**

```markdown
$$
\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}
$$
```

**Plain text version:**

```markdown
C(n,k) = C(n−1, k−1) + C(n−1, k)
```

## What it says

To get the number at **row n, position k**, add the two numbers in the **row above** (n−1):
- the one at position **k−1** (up and to the left)
- the one at position **k** (up and to the right)

## Example

C(4,2) = C(3,1) + C(3,2) = 3 + 3 = **6**

```
row 3:    1   3   3   1
               \ /
row 4:  1   4   6   4   1
```

## Why it's true (connecting to the board)

This is the tree step written as a formula. On the board, every term in row n came from two terms in row n−1:
- one **multiplied by a**
- one **multiplied by b**

Like terms were then added. For example, **3a²b = a²b + 2a²b**: the a²b came from a² × b, and the 2a²b came from 2ab × a. In numbers, that's 1 + 2 = 3, which is exactly C(3,1) = C(2,0) + C(2,1).

You can also see it as counting. Say you're choosing k people out of n. Point at one particular person:
- If you **pick them**, you need k−1 more from the other n−1 people: C(n−1, k−1) ways.
- If you **don't pick them**, you need all k from the other n−1 people: C(n−1, k) ways.

Add the two cases together and you get every possible choice.

If your class is programming-related, this is also the standard formula for building Pascal's triangle in code. Each row is calculated from the previous one, starting from the 1 at the top. The image cuts off on the right, so I can't tell what he wrote after the "a".