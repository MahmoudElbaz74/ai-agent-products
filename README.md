# 🛍️ AI Product Assistant

An AI-powered assistant that allows users to ask product-related questions in Arabic or English, with smart retrieval and context-aware responses in Arabic.

**Built with:** Python, FastAPI, LangChain, HuggingFace, ChromaDB, OpenRouter

---

## 🧠 Features

- Hybrid search: combines keyword filtering + vector embeddings.
- Uses HuggingFace embeddings for product similarity.
- Supports Arabic questions with automatic English translation.
- Remembers chat history per session.
- Answers in Arabic only.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/MahmoudElbaz74/ai-agent-products.git
cd ai-agent-products
```

### 2. Setup virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# Or on Linux/macOS:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your API key

Create a `.env` file and add your OpenRouter API key:
```env
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 📄 .env Example
```env
OPENROUTER_API_KEY=sk-or-your-api-key-here
```

### 5. Run the app
```bash
python main.py
```

Then open your browser and go to:
```
http://localhost:8000
```

---

## 🛠️ Commands

```bash
# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the web interface
python main.py
```

---

## 🌍 Language Notes

- Product data is in **English**.
- Questions can be in **Arabic or English**.
- Questions are translated to English before matching.
- Answers are returned in **Arabic only**.

---

## ✅ Testing
Try asking:
- "هل يوجد لابتوب بمعالج i7؟"
- "What is the price of MacBook?"

---

## 🧠 Future Improvements

- Improve Arabic product data support
- Use multilingual embeddings for better Arabic accuracy
- Streamlined chat history across sessions
