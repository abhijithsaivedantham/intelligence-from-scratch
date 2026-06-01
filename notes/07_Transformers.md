# Chapter 13 - Transformer Architecture

## What is a Transformer?

A Transformer is a neural network architecture built using:

- Embeddings
- Self Attention
- Multi Head Attention
- Feed Forward Networks

It is the foundation of modern LLMs.

---

## Transformer Block

Input
 ↓
Multi Head Attention
 ↓
Feed Forward Network
 ↓
Output

---

## Multi Head Attention

Responsible for gathering contextual information.

Question:

"Which words are important?"

---

## Feed Forward Network

Processes the information collected by attention.

Question:

"What should be done with this information?"

---

## Stacking Layers

Transformers contain many layers.

Layer 1:
Basic patterns

Layer 2:
Relationships

Layer 3:
Higher-level meaning

...

Deeper layers learn increasingly abstract concepts.

---

## Mental Model

Attention = Gather Information

Feed Forward Network = Process Information

Transformer = Repeat This Process Many Times


Additional Notes

Different transformer layers learn different patterns.

Layer 1:
Simple patterns

Layer 2:
Relationships

Layer N:
Complex semantic meaning

Important Insight:

Layer 1 and Layer 12 do NOT learn the same thing.

Early layers focus on simple structures.

Later layers focus on abstract meaning.