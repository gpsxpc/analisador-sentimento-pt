# 📊 Sentiment Analyzer in Portuguese

An open-source project that uses a pre-trained multilingual BERT model to classify the sentiment of a text input in Portuguese, returning a score from 1 to 5 stars (like customer reviews).

> ✅ Deployed on Hugging Face Spaces: [Click to try it](https://huggingface.co/spaces/gpsxpc/analisador-sentimento-pt)

---

## 🔧 Technologies
- Python
- Hugging Face Transformers
- Gradio
- Torch (PyTorch backend)
- Hugging Face Spaces (free deployment)

---

## 📌 Features
- Accepts any text input in Portuguese
- Classifies the sentiment using a multilingual BERT model
- Outputs probability scores from 1 to 5 stars
- Runs fully in the browser (Gradio interface)

---

## 🚀 Getting Started

### Run locally:
```bash
pip install gradio transformers torch
python app.py
