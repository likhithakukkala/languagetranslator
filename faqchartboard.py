import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# PAGE CONFIG
st.set_page_config(
    page_title="Enterprise AI FAQ Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e3a8a, #2563eb);
}

.main-title {
    text-align: center;
    color: white;
    font-size: 52px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #dbeafe;
    font-size: 20px;
    margin-bottom: 30px;
}

.question-label {
    color: white;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
}

.chat-box {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(15px);
    padding: 25px;
    border-radius: 20px;
    margin-top: 20px;
}

.user-msg {
    background: #2563eb;
    color: white;
    padding: 15px;
    border-radius: 15px;
    margin: 10px 0;
    font-size: 16px;
}

.bot-msg {
    background: white;
    color: black;
    padding: 15px;
    border-radius: 15px;
    margin: 10px 0;
    font-size: 16px;
}

.stButton > button {
    background: linear-gradient(to right,#06b6d4,#3b82f6);
    color: white;
    border: none;
    border-radius: 10px;
    height: 50px;
    width: 150px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background: linear-gradient(to right,#0891b2,#2563eb);
    color: white;
}

.footer {
    text-align:center;
    color:white;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:

    st.title("🤖 AI Assistant")

    st.markdown("---")

    st.subheader("Features")

    st.write("✅ FAQ Chatbot")
    st.write("✅ NLP Processing")
    st.write("✅ TF-IDF Vectorization")
    st.write("✅ Cosine Similarity")

    st.markdown("---")

    st.subheader("Technologies")

    st.write("🐍 Python")
    st.write("⚡ Streamlit")
    st.write("🤖 Machine Learning")
    st.write("📊 Scikit-Learn")

    st.markdown("---")

    st.success("CodeAlpha Internship Project")

# DATASET
faq_data = {
    "Question":[
        "What is AI?",
        "What is Python?",
        "What is Machine Learning?",
        "What is Deep Learning?",
        "What is NLP?",
        "What is Data Science?",
        "Who developed Python?",
        "What is Streamlit?",
        "What is Java?",
        "What is Cloud Computing?"
    ],

    "Answer":[
        "AI stands for Artificial Intelligence.",
        "Python is a popular programming language.",
        "Machine Learning is a subset of AI.",
        "Deep Learning uses neural networks.",
        "NLP stands for Natural Language Processing.",
        "Data Science extracts insights from data.",
        "Python was developed by Guido van Rossum.",
        "Streamlit is used to build Python web apps.",
        "Java is an object-oriented programming language.",
        "Cloud Computing provides computing services over the internet."
    ]
}

df = pd.DataFrame(faq_data)

# NLP
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(df["Question"])

def get_response(user_query):

    user_vector = vectorizer.transform([user_query])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    index = similarity.argmax()

    score = similarity[0][index]

    if score < 0.20:
        return "Sorry, I couldn't find a suitable answer."

    return df["Answer"][index]

# HEADER
st.markdown(
    '<div class="main-title">🤖 Enterprise AI FAQ Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Intelligent Question Answering System Using NLP</div>',
    unsafe_allow_html=True
)

# SESSION STATE
if "messages" not in st.session_state:
    st.session_state.messages = []

# QUESTION SECTION
st.markdown(
    '<div class="question-label">💬 Ask Your Question</div>',
    unsafe_allow_html=True
)

user_input = st.text_input(
    "",
    placeholder="Type your question here..."
)

# BUTTON
if st.button("Send"):

    if user_input.strip():

        response = get_response(user_input)

        st.session_state.messages.append(
            ("You", user_input)
        )

        st.session_state.messages.append(
            ("Bot", response)
        )

# CHAT DISPLAY
st.markdown(
    '<div class="chat-box">',
    unsafe_allow_html=True
)

for sender, msg in st.session_state.messages:

    if sender == "You":

        st.markdown(
            f'<div class="user-msg">👤 {msg}</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f'<div class="bot-msg">🤖 {msg}</div>',
            unsafe_allow_html=True
        )

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

# FOOTER
st.markdown(
    '<div class="footer">Powered by AI • NLP • Machine Learning • Streamlit</div>',
    unsafe_allow_html=True
)