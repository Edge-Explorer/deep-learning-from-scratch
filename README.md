# Deep-Learning-from-Scratch 🧠

This repository contains my hands-on implementation of various deep learning models—starting from Multi-Layer Perceptrons (MLPs) to Convolutional Neural Networks (CNNs)—using the **TensorFlow low-level API** and **Keras**. It’s part of my deep learning journey through the **Scaler Deep Learning Course**.

---

## 📘 Notebooks Included

### 🔹 MLP Architectures (MNIST)
- `Softmax_classifier`: Basic softmax-based linear classifier
- `MLP_Sigmoid`: MLP with sigmoid activation
- `MLP_ReLU`: MLP with ReLU activation
- `MLP_ReLU_Dropout`: MLP with ReLU and Dropout
- `MLP_ReLU_BatchNorm`: MLP with ReLU and Batch Normalization
- `MLP_LeakyReLU_BatchNorm`: MLP with Leaky ReLU and BatchNorm
- `MLP_Keras_ReLU_Softmax`: MLP using Keras with ReLU and softmax
- `MLP_Keras_ReLU_RMSprop`: MLP using Keras with ReLU, RMSprop, and softmax

### 🔹 CNN Architectures (MNIST)
- `CNN_Manual_TF`: CNN implemented from scratch using TensorFlow low-level API (without Keras)
- `CNN_Keras_TF`: CNN built using TensorFlow's Keras API for fast prototyping and training

---

## 🧪 Dataset

All experiments are performed on the **MNIST Handwritten Digit Dataset**:
- 60,000 training images
- 10,000 test images
- 28x28 grayscale format
- Labels: digits from 0 to 9

---

## 🚀 Goals

- Build deep learning models **from scratch** using TensorFlow low-level operations
- Understand and experiment with core components like:
  - Activation functions (ReLU, Sigmoid, Leaky ReLU)
  - Dropout regularization
  - Batch normalization
  - Optimizers (SGD, RMSprop, Adam)
- Compare low-level TensorFlow coding with high-level Keras APIs
- Explore how CNNs outperform MLPs on image data

---

## 📊 Results & Visualizations

Each notebook includes:
- Training/validation accuracy and loss plots
- Epoch-wise progress and performance metrics
- Notes on the behavior of different configurations

---

## 🛠️ Tech Stack

- Python 3.x
- Jupyter Notebook
- TensorFlow 2.x
- Keras
- Matplotlib & NumPy
