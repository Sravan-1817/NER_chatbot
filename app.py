import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline


# -------------------------
# Page config
# -------------------------
st.set_page_config(
    page_title="Telugu & Kannada NER Chatbot",
    page_icon="🧠",
    layout="centered"
)


# -------------------------
# Load Hugging Face model
# -------------------------
MODEL_NAME = "sravan1817/indicbertv2-ner-te-kn"

@st.cache_resource
def load_ner_pipeline():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForTokenClassification.from_pretrained(MODEL_NAME)

    ner_pipe = pipeline(
        "ner",
        model=model,
        tokenizer=tokenizer,
        aggregation_strategy="none"
    )
    return ner_pipe


# -------------------------
# Convert token predictions to word-level tags
# -------------------------
def predict_word_tags(text, ner_pipe):
    words = text.split()
    predictions = ner_pipe(text)

    word_tags = ["O"] * len(words)

    for pred in predictions:
        label = pred.get("entity", "O")
        token_word = pred.get("word", "").replace("##", "").strip()

        if not token_word:
            continue

        for i, word in enumerate(words):
            if token_word in word or word in token_word:
                if word_tags[i] == "O":
                    word_tags[i] = label
                break

    return list(zip(words, word_tags)), predictions


# -------------------------
# UI Header
# -------------------------
st.title("🧠 Telugu & Kannada NER Chatbot")

st.markdown(
    """
      model: sravan1817/indicbertv2-ner-te-kn

    💡 **Online virtual keyboards (recommended):**

    - **Telugu**:  
      [https://www.branah.com/telugu](https://www.branah.com/telugu)

    - **Kannada**:  
      [https://www.branah.com/kannada](https://www.branah.com/kannada)


    **Example Telugu sentences you can try:**

    - `సునీత అమెరికాకి వెళ్లింది`
    - `రాము హైదరాబాద్‌లో ఉంటాడు`

    **Example Kannada sentences you can try:**

    - `ಬೆಂಗಳೂರು ಕರ್ನಾಟಕದ ರಾಜಧಾನಿ ನಗರ.`
    - `ಪ್ರಜ್ವಲ್ ರೆಡ್ಡಿ ಕನ್ನಡ ಚಿತ್ರರಂಗದ ಪ್ರಸಿದ್ಧ ನಟ ಮಾದರಿಯಾಗಿದ್ದಾನೆ.`

    Type or copy‑paste these (or your own) into the chat box below.
    """,
    unsafe_allow_html=True,
)



# -------------------------
# Load model once
# -------------------------
ner_pipe = load_ner_pipeline()


# -------------------------
# Initialize chat history
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! Enter a Telugu or Kannada sentence, and I will return word-level NER tags."
        }
    ]


# -------------------------
# Display old messages
# -------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if "table" in msg:
            st.table(msg["table"])


# -------------------------
# Chat input (user types or pastes Telugu/Kannada here)
# -------------------------
prompt = st.chat_input(
    "Type or paste a Telugu / Kannada sentence "
)


if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Running NER..."):
            tagged_words, raw_predictions = predict_word_tags(prompt, ner_pipe)

        reply = "Here are the word-level NER tags:"
        st.markdown(reply)

        table_data = [{"Word": w, "NER Tag": t} for w, t in tagged_words]
        st.table(table_data)

        with st.expander("Raw model output"):
            st.json(raw_predictions)

        st.session_state.messages.append({
            "role": "assistant",
            "content": reply,
            "table": table_data
        })