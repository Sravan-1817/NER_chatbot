# Telugu & Kannada NER Chatbot

A **multilingual Named Entity Recognition (NER) chatbot** for **Telugu and Kannada**, built with **Streamlit** and powered by a **multilingual Indic‑NER model**  sravan1817/indicbertv2-ner-te-kn. The app takes a sentence in Telugu or Kannada and returns **word‑level NER tags** (`PER`, `LOC`, `ORG`, `MISC`, `O`) in a clean chat interface.

---

## 🌐 What it does

- Accepts **Telugu and Kannada text** via a chat‑style input box.
- Runs **Named Entity Recognition** on the input using a multilingual transformer model.
- Displays:
  - A **word‑level NER table** (Word → Tag).
  - The **raw token‑level NER output** (spans, confidence, etc.) inside an expandable section.
- Includes:
  - Example Telugu/Kannada sentences.
  - Links to online virtual keyboards (Telugu and Kannada) for easy typing.

This is suitable for **research, education, or demo** use with Indic language NER.

---

## 🚀 Features

- **Languages**: Telugu, Kannada (and other Indic languages, depending on the model).
- **NER tags**: `PER`, `LOC`, `ORG`, `MISC`, `O`.
- **Interactive UI**: Chat‑based Streamlit interface with message history.
- **Debug mode**: Expandable section showing the full model pipeline output.
- **Reproducible**: Single `app.py` + `requirements.txt`; easy to run locally or deploy on Streamlit Cloud, Hugging Face Spaces, or Docker.

---

## 📦 Installation and usage (local)

1. Install requirements:

```bash
pip install streamlit transformers torch sentencepiece
```

2. Run the app:

```bash
streamlit run app.py
```

3. Open `http://localhost:8501` in your browser and start typing Telugu/Kannada sentences.

---

## ☁️ Deployment options

- **Streamlit Community Cloud**  
  Push your repo to GitHub and deploy via https://share.streamlit.io/ for a **public URL**.

- **Hugging Face Spaces (Streamlit template)**  
  Create a Streamlit Space and upload `app.py` and `requirements.txt` for a hosted web app.

- **Docker / personal server**  
  Use the provided `Dockerfile`‑style setup to run the app on a VPS or cloud server.

---

## 🧠 Motivation

- Demonstrate **multilingual Indic NER** in a **user‑friendly, interactive interface**.
- Provide a **ready‑to‑use playground** for Telugu and Kannada NER, useful for:
  - NLP researchers,
  - Indic‑language developers,
  - Students learning NER or multilingual models.

---

## 📄 License

This project is MIT‑licensed unless otherwise specified. The underlying NER model (e.g., IndicNER) has its own license (check Hugging Face / model card).

---

## 🤝 How to contribute

- Improve **word‑level tag alignment** for Telugu/Kannada.
- Add **more example sentences** and language hints.
- Extend the app to **more Indic languages** or **multi‑model support**.
- Add tests or a simple evaluation script.

Feel free to open issues or PRs with improvements!
