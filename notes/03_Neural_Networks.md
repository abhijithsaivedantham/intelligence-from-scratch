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


Chapter 15 - Gradient Descent

Single Neuron

Prediction = x*w + b

Error = y_pred - y_true

Loss = abs(error)

Gradient Descent:

w = w - lr * error * x

b = b - lr * error

Learning Rate

Small LR:
- Stable
- Slow

Large LR:
- Fast
- Can Diverge

Convergence

Loss:
100 -> 50 -> 10 -> 2 -> 0.5

Divergence

Loss:
100 -> 1000 -> 10000

Experiments:

lr = 0.01
Result: Diverged

lr = 0.0001
Result: Stable but slow

lr = 0.001
Result: Good convergence

Bias Experiment

Dataset:

(1,10)
(2,20)
(3,30)
(4,40)
(5,50)

Observation:

y = 10x

passes through origin.

Bias is not required.

Important Insight:

Weight = Importance

Bias = Baseline Output

Example:

score =
study_hours*w1
+
sleep_hours*w2
+
bias

If all inputs are zero:

score = bias

Therefore bias allows non-zero predictions even when inputs are zero.