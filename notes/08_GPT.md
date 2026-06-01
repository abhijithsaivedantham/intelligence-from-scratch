# Chapter 14 - GPT

GPT stands for:

G - Generative
P - Pretrained
T - Transformer

---

## Generative

GPT generates text one token at a time.

Example:

Input:
"The capital of France is"

Prediction:
"Paris"

---

## Pretrained

Before deployment, GPT is trained on massive amounts of text.

Training data includes:

- Books
- Websites
- Articles
- Documentation
- Code

---

## Transformer

GPT is built using the Transformer architecture.

Components:

- Tokenization
- Embeddings
- Multi Head Attention
- Feed Forward Networks
- Multiple Layers

---

## Training Objective

GPT learns by predicting the next token.

Example:

"The sky is ____"

Target:

"blue"

The model repeats this process billions of times.

---

## Key Insight

A surprisingly simple objective:

Predict Next Token

leads to complex abilities such as:

- Language Understanding
- Reasoning
- Coding
- Question Answering


# Final Pipeline

Text
↓
Tokenization
↓
Tokens
↓
Token IDs
↓
Embeddings
↓
Transformer Layers
    ↓
    Multi-Head Attention
    ↓
    Feed Forward Network
↓
Next Token Prediction