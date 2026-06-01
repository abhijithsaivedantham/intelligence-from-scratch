# Chapter 9 - Attention

## Problem

Words can have different meanings depending on context.

Example:

Abhijith deposited money into the bank.

Bank = Financial Institution

The fisherman sat on the bank.

Bank = River Side

---

## Key Idea

A word should not be interpreted alone.

It should consider surrounding words.

---

## Attention

Attention allows a model to focus on the most relevant words.

Example:

Sentence:

Abhijith deposited money into the bank.

Word:

bank

Attention may focus on:

- money
- deposited

These words help determine the meaning.

---

## Mental Model

Attention = Selective Focus

A word asks:

"Which other words are important for understanding me?"

---

## Why Attention Matters

Attention enables:

- Context Understanding
- Better Language Processing
- Long-Range Relationships
- Modern LLMs

Transformers are built on Attention.


# Chapter 10 - Query, Key, Value (QKV)

Attention is implemented using:

- Query (Q)
- Key (K)
- Value (V)

---

## Query

Represents what the current word is looking for.

Example:

Bank asks:

"What words help explain my meaning?"

---

## Key

Represents what information another word contains.

Examples:

money
deposited
river
fisherman

---

## Value

Represents the actual information carried by a word.

---

## Attention Process

Query
 ↓
Compare with Keys
 ↓
Find Relevant Words
 ↓
Retrieve Values
 ↓
Build Context-Aware Meaning

---

## Mental Model

Query = Search Request

Key = Label

Value = Information


# Chapter 11 - Self Attention

## What is Self Attention?

Self-Attention allows words in a sentence to look at other words in the same sentence and determine which are most relevant.

Example:

The dog chased the cat because it was scared.

The word "it" may attend strongly to:

- dog
- cat
- scared

to determine its meaning.

---

## Why Self Attention?

Traditional NLP processed words sequentially.

This made long-range relationships difficult.

Self-Attention allows every word to interact with every other word.

---

## Mental Model

Self-Attention = Group Discussion

Every word asks:

"Which other words are important for me?"

---

## Benefits

- Better context understanding
- Long-range relationships
- Parallel processing
- Foundation of Transformers


# Chapter 12 - Multi Head Attention

## Problem

A single attention mechanism may miss important relationships.

Different relationships exist in language:

- Grammar
- Meaning
- Context
- References

---

## Multi Head Attention

Instead of one attention mechanism, Transformers use multiple attention heads.

Each head learns different patterns and relationships.

Example:

Head 1 -> Pronouns

Head 2 -> Grammar

Head 3 -> Meaning

Head 4 -> Long-range Context

These roles are learned automatically.

---

## Mental Model

Multi-Head Attention = Multiple Experts

Each expert looks at the sentence differently.

Their outputs are combined to form a richer understanding.

---

## Benefits

- Better context understanding
- Multiple perspectives
- Improved language comprehension
- Core component of Transformers