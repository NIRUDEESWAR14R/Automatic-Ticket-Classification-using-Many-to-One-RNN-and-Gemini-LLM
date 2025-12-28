# Automatic Ticket Classification using Many-to-One RNN and Gemini LLM

## 📌 Project Overview
Organizations receive thousands of customer support tickets daily, making manual categorization time-consuming, error-prone, and costly.  
This project builds an **end-to-end intelligent ticket handling system** that:

1. Automatically **classifies customer support tickets** into the correct department using a **Many-to-One LSTM model**.
2. Generates a **polite, professional acknowledgment reply** using **Google Gemini (Generative AI)**.

The system demonstrates how **traditional NLP models and Generative AI** can be combined to automate customer support workflows.

---

## 🎯 Problem Statement
Manual ticket triaging leads to:
- Delayed issue resolution  
- Increased operational costs  
- Poor customer experience  

The goal is to:
- Automatically route tickets to the correct queue
- Instantly acknowledge customer issues using AI-generated responses

---

## 💡 Business Use Cases
- **Customer Support Automation** – Auto-routing tickets to correct departments  
- **Faster Response Time** – Immediate acknowledgment replies  
- **Cost Optimization** – Reduced manual triage effort  
- **Improved Customer Satisfaction** – Consistent and empathetic communication  

---

## 🧠 Solution Architecture
Customer Ticket Text

↓

Text Preprocessing & Tokenization

↓

Many-to-One LSTM Model

↓

Queue Prediction (e.g., Technical Support)

↓

Google Gemini API

↓

AI-Generated Polite Reply

---

## 🛠 Tech Stack
- **Python**
- **TensorFlow / Keras** – LSTM model
- **Scikit-learn** – Label encoding, evaluation
- **Hugging Face Datasets** – Customer support ticket data
- **Google Gemini (GenAI)** – Automated reply generation
- **VS Code** – Development
- **Git & GitHub** – Version control

---

## 📂 Project Structure

![Untitled - Frame 1 (8)](https://github.com/user-attachments/assets/897af339-ca49-427d-b11f-f2f46549a4bb)

---

## 📊 Dataset
- **Source:** Hugging Face – `Tobi-Bueck/customer-support-tickets`
- **Key Fields:**
  - `body` – Ticket text (input)
  - `queue` – Department label (target)
- **Characteristics:**
  - Multi-class (50+ categories)
  - Real-world class imbalance
  - Noisy, natural language text

---

## 🧪 Model Details
- **Architecture:** Many-to-One LSTM
- **Input:** Tokenized and padded text sequences
- **Output:** Ticket queue (multi-class classification)
- **Loss Function:** Sparse Categorical Crossentropy
- **Optimizer:** Adam

---

## 📈 Evaluation
- Accuracy: ~23%  
- Precision, Recall, F1-Score (per class)
- Confusion Matrix analysis

📌 Note:  
Due to **high class imbalance and semantic overlap** across 50+ queues, accuracy alone is not a sufficient metric. The confusion matrix shows most misclassifications occur between **semantically similar categories**, indicating meaningful learning.

---

## 🤖 Gemini Integration
- Uses **Google Gemini free-tier API**
- Dynamically selects an available model to avoid hardcoded dependencies
- Generates:
  - Polite
  - Professional
  - Non-promissory acknowledgment replies

---

# 👨‍💻 Developer
 
  Nirudeeswar R
 
 📍 Chennai
 
 🎓 B.Tech CSE
 
 📧 nirudeeswarr14@gmail.com
