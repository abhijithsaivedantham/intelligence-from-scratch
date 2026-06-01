# Chapter 7 - Embeddings

## Problem

Computers cannot understand words directly.

Simple encodings:

Dog -> 1
Cat -> 2
Car -> 3

do not capture meaning.

The numbers are arbitrary.

---

## One-Hot Encoding

Dog -> [1,0,0]

Cat -> [0,1,0]

Car -> [0,0,1]

Problem:

Dog-Cat similarity = Dog-Car similarity

The model cannot understand semantic relationships.

---

## Embeddings

Embeddings are learned numerical representations of meaning.

Example:

Dog -> [0.8, 0.7]

Cat -> [0.75, 0.72]

Car -> [0.1, 0.9]

Dog and Cat are closer together because they have similar meanings.

---

## Key Idea

Words with similar meanings tend to have similar embeddings.

Closer vectors:
- Similar meaning

Farther vectors:
- Different meaning

---

## Applications

Embeddings are used in:

- Large Language Models
- Semantic Search
- RAG
- Recommendation Systems
- Vector Databases
- Agents