# 🧠 OCR Agent with LangSmith Tracing

A **Streamlit-based OCR Agent** powered by **Gemini 2.0 Flash** and **LangSmith**.  
It extracts text from uploaded images using Google's Vision-Language model while maintaining **traceable execution** via LangSmith — giving full transparency into the model's decision process.

---

## 🚀 Features

- 🖼️ Upload any image (PNG, JPG, JPEG)
- 🤖 Extract text using **Gemini Vision Model**
- 🧩 Modular pipeline with **LangGraph**
- 📊 Full **traceability with LangSmith**
- 🧠 AI Agent uses **tool invocation** for OCR
- 🔒 Environment variables protected via `.env` (not pushed to Git)

---

## 🧩 Project Structure

```
OCR_Agent/
│
├── app.py              # Streamlit UI
├── main.py             # LangGraph pipeline
├── agent/
│   └── tools.py        # OCR tools & LangSmith-traceable functions
├── .env                # API keys (excluded from repo)
├── .gitignore
└── README.md
```

---

## 🔁 Process Flow

```
┌──────────────┐
│  User Upload │
└──────┬───────┘
       │
       ▼
┌─────────────────┐
│   app.py (UI)   │
└────────┬────────┘
         │ calls
         ▼
┌───────────────────────────┐
│   main.py (Pipeline)      │
│   @traceable run_pipeline()│
└────────┬──────────────────┘
         │ calls
         ▼
┌────────────────────────────┐
│   agent/tools.py           │
│   @traceable extract_text()│
│   → Read image             │
│   → OCR text               │
│   → Return result          │
└────────┬───────────────────┘
         │
         ▼
┌────────────────────────────┐
│   LangSmith Dashboard      │
│   Trace Visualization      │
└────────────────────────────┘
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/owais825/OCR_Agent.git
cd OCR_Agent
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate  # Windows
# source myenv/bin/activate  # macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` File

Create a `.env` file in the root directory with the following content:

```env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
GOOGLE_API_KEY=your_google_key
```

⚠️ **Never push `.env`** — it contains private API keys.

### 5️⃣ Run the App

```bash
streamlit run app.py
```

---

## 📈 LangSmith Tracing

Each function is annotated with `@traceable` for detailed tracking:

- `extract_text` → Traces OCR extraction process
- `run_pipeline` → Traces the entire workflow execution

You can view these traces on your [LangSmith dashboard](https://smith.langchain.com/).

---

## 🛠️ Technologies Used

- **Streamlit** - Web UI framework
- **LangChain** - LLM orchestration
- **LangGraph** - Agent workflow management
- **LangSmith** - Observability and tracing
- **Google Gemini 2.0 Flash** - Vision-Language model
- **Python 3.x**

---

## 🔒 Security Note

This repository contains integrations with paid API keys (LangSmith + Gemini).

- All secrets are stored locally in `.env` and are **not shared publicly**
- Unauthorized use of these APIs will incur charges
- Please **do not reuse or redistribute** this project with keys included

---

## 📝 License

This project is for educational and demonstration purposes.

---

## 👤 Author

**Owais**  

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  

---

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!
