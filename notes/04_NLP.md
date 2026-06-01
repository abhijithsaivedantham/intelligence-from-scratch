# Chapter 8 - Tokenization

## What is a Token?

A token is the smallest unit processed by an LLM.

Important:

Token != Word

A word may consist of multiple tokens.

---

## Example

Word:

unhappiness

Possible Tokens:

un
happy
ness

---

## Why Tokenization?

1. Reduce vocabulary size
2. Handle unseen words
3. Reuse learned meaning

Examples:

play
playing
player
played

share the root token:

play

---

## GPT Processing Pipeline

Text
 ↓
Tokens
 ↓
Token IDs
 ↓
Embeddings
 ↓
Neural Network
 ↓
Prediction

GPT never sees raw text directly.

It sees tokenized numerical representations.