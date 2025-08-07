# 🍽️ Restaurant AI Assistant – LangChain + Streamlit

An AI-powered assistant built using **LangChain** and **Streamlit**, designed to suggest restaurant names and menu items based on selected cuisine types. It uses the **Google Gemini API** for intelligent content generation.

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/restaurant-ai-assistant-langchain.git
cd restaurant-ai-assistant-langchain
```

### 2. Add Your Google Gemini API Key

Create a file named `secret_key.py` in the root directory and add the following content:

```python
gemni_key = "your-google-gemini-api-key"
```

Replace `"your-google-gemini-api-key"` with your actual key from [Google AI Studio](https://makersuite.google.com/app).

### 3. Install Dependencies

Make sure you have Python 3.10+ installed, then run:

```bash
pip install -r requirements.txt
```

### 4. Run the Application

Start the Streamlit app with:

```bash
streamlit run main.py
```

---

## 🧠 Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Google Gemini API**
