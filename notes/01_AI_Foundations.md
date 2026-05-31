## Chapter 1 -  Intelligence

Intelligence is the ability to use knowledge and experience
to make useful decisions in new situations.

Calculator:
Input -> Rule -> Output

GPS:
Location -> Algorithm -> Route

Human:
Knowledge
+ Experience
+ Goals
+ Predictions
+ Context
-> Decision

A key characteristic of intelligence is adaptation to new situations.


# What Are We Building?

Goal:
Build an intelligent assistant capable of reasoning, remembering, using tools, and interacting through voice.

JARVIS =
Brain (LLM)
+ Memory
+ Tools
+ Voice
+ Planning

Learning Path:

AI
→ Machine Learning
→ Deep Learning
→ NLP
→ Transformers
→ GPT
→ LLM Engineering
→ RAG
→ Tool Calling
→ Agents
→ LangGraph
→ Voice AI
→ JARVIS


## Generalization

Generalization is the ability of a model to make useful predictions on new data it has never seen before.

Example:

Training:
2 hrs -> Fail
4 hrs -> Fail
6 hrs -> Pass
8 hrs -> Pass

Prediction:
7 hrs -> Pass

The model is not memorizing.
It is learning patterns from data.


## Generalization vs Extrapolation

Generalization:
Making predictions on new examples similar to training data.

Extrapolation:
Making predictions far outside the range of training data.

Models are generally better at interpolation than extrapolation.

The quality, diversity, and coverage of training data strongly affect model performance.


## Why Deep Learning Works

Humans learn concepts through examples.

A child learns what a dog is by seeing many dogs.

Deep learning follows a similar idea:
instead of manually defining rules,
the neural network learns patterns directly from data.

Traditional ML:
Data -> Human Features -> Model -> Prediction

Deep Learning:
Data -> Neural Network -> Prediction


# Chapter 2 - How Does a Neural Network Learn?

## The Problem

Suppose we want to predict whether a student will pass or fail based on study hours.

Training Data:

2 hours -> Fail
4 hours -> Fail
6 hours -> Pass
8 hours -> Pass

Instead of manually writing rules, we want the computer to learn the pattern from data.

---

## The Idea of a Neuron

The simplest neuron takes an input and produces an output.

Example:

Study Hours
    ↓
 Neuron
    ↓
Prediction

Mathematically:

Prediction = Input × Weight

Example:

Input = 5
Weight = 4

Prediction = 20

---

## What is a Weight?

A weight represents the importance of an input.

Example:

To predict exam success:

- Study Hours
- Sleep Hours
- Attendance

Not all factors contribute equally.

Possible weights:

Study Hours = 0.7
Sleep Hours = 0.2
Attendance = 0.1

Higher weight means greater influence on the prediction.

---

## Learning

The goal of training is to find the best weights.

Example:

Input = 5
Weight = 4

Prediction = 20

Actual Score = 80

The prediction is incorrect.

The model must adjust its weight to improve future predictions.

Learning is the process of adjusting weights to reduce mistakes.

---

## Loss

Loss measures how wrong a prediction is.

Example:

Actual = 80
Prediction = 20

Loss = 80 - 20 = 60

Large Loss:
- Poor prediction

Small Loss:
- Better prediction

Example:

Actual = 80
Prediction = 78

Loss = 2

This is much better.

---

## Weight Adjustment

If predictions are too low:

Prediction = 20
Actual = 80

The weight should increase.

If predictions are too high:

Prediction = 100
Actual = 80

The weight should decrease.

General Rule:

Prediction too low  -> Increase Weight

Prediction too high -> Decrease Weight

---

## Learning Loop

Every neural network follows the same process:

1. Make Prediction
2. Calculate Loss
3. Update Weights
4. Repeat

Visualized:

Input
  ↓
Weight
  ↓
Prediction
  ↓
Loss
  ↓
Weight Update
  ↓
Repeat

---

## Learning Rate

Learning Rate determines how much the model changes its weights after an error.

Small Learning Rate:
- Learns slowly
- More stable

Large Learning Rate:
- Learns quickly
- Can overshoot the correct solution

Example:

Weight = 4

Small update:
Weight = 5

Large update:
Weight = 104

Usually, small controlled updates work better.

---

## Convergence

As training continues:

Loss:
60
30
10
3
1
0.8
0.79

Improvements become smaller over time.

Convergence is the point where additional training provides very little improvement.

---

## Key Concepts Learned

- Neuron
- Input
- Weight
- Prediction
- Loss
- Learning Rate
- Weight Update
- Convergence

---

## Important Mental Model

A neural network learns by continuously adjusting its weights.

Training is NOT:

Memorize Answers

Training IS:

Adjust Weights Until Loss Becomes Small

This same principle powers:

- Neural Networks
- Deep Learning
- Computer Vision Models
- Speech Models
- Large Language Models (GPT)

The only difference is scale.

GPT uses billions of weights, but learns using the same fundamental idea.


# Chapter 3 - Real Neurons and Multiple Inputs

## Features

A feature is a piece of information used for prediction.

Example:

- Study Hours
- Sleep Hours
- Attendance
- Previous Marks

These are features.

---

## Multiple Inputs

Real-world predictions require multiple inputs.

Instead of:

Prediction = Input × Weight

We use:

Prediction =
(Input1 × Weight1)
+
(Input2 × Weight2)
+
(Input3 × Weight3)

Each feature has its own weight.

---

## Weights

Weights represent the importance of a feature.

Example:

Study Hours = 0.8
Sleep Hours = 0.2

The model considers study hours more important.

Higher weight = greater influence on output.

---

## Bias

Bias is an additional value added to the neuron.

Formula:

Output =
Σ(Input × Weight)
+
Bias

Bias acts like a starting point or baseline prediction.

Think:

Weights -> Importance

Bias -> Starting Point

---

## Neuron Workflow

Input Features
      ↓
Multiply by Weights
      ↓
Add Results
      ↓
Add Bias
      ↓
Output

---

## Key Concepts

- Feature
- Weight
- Bias
- Multiple Inputs
- Weighted Sum

A neuron learns by adjusting weights and bias to reduce prediction error.

# Chapter 4 - Why Activation Functions Exist

Problem:
A neuron can only learn simple linear relationships.

Real-world problems are often non-linear.

Example:

0 hours sleep -> Bad
8 hours sleep -> Good
20 hours sleep -> Bad

A straight line cannot represent this pattern.

Activation Functions help neural networks learn more complex relationships.

Basic Flow:

Inputs
  ↓
Weighted Sum
  ↓
Activation Function
  ↓
Output

# Chapter 5 - From Neurons to Neural Networks

## Why One Neuron Is Not Enough

A single neuron can learn simple relationships.

Real-world problems are much more complex.

Examples:

- Image Recognition
- Speech Recognition
- Language Understanding

These require many neurons working together.

---

## Neural Network

A neural network is a collection of interconnected neurons.

Each neuron:

1. Receives inputs
2. Applies weights
3. Adds bias
4. Uses an activation function
5. Produces output

---

## Layers

### Input Layer

Receives raw data.

Examples:

- Study Hours
- Sleep Hours
- Attendance

---

### Hidden Layers

Learn intermediate patterns.

The network automatically discovers useful representations.

Examples:

- Work Ethic
- Consistency
- Discipline

These are not manually programmed.

---

### Output Layer

Produces the final prediction.

Examples:

- Pass Probability
- House Price
- Spam/Not Spam

---

## Deep Learning

Deep Learning refers to neural networks with many layers.

More layers allow the network to learn increasingly complex patterns.

Basic Architecture:

Input Layer
      ↓
Hidden Layer
      ↓
Output Layer


# Chapter 6 - Backpropagation (Intuition)

Problem:

A neural network may contain thousands or millions of weights.

When a prediction is wrong, we need to determine:

- Which weights contributed to the error?
- How much should each weight change?

Backpropagation solves this problem.

Core Idea:

1. Make Prediction
2. Calculate Loss
3. Send Error Backward Through Network
4. Assign Blame to Weights
5. Update Weights
6. Repeat

Mental Model:

Backpropagation is a blame assignment algorithm.

Weights that contribute more to the error receive larger updates.

Weights that contribute less receive smaller updates.


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