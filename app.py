import streamlit as st
from graph.workflow import graph
from ingestion.pdf_loader import load_and_split_pdfs
from graph.nodes import vectorstore
from pathlib import Path

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Enterprise Knowledge Assistant Platform",
    page_icon="🏢",
    layout="wide"
)

# -----------------------------
# Custom Styling (Enterprise Look)
# -----------------------------
st.markdown("""
<style>

/* Title */


/* Subtitle */
.sub-title {
    font-size: 14px;
    color: #6b7280;
    margin-bottom: 20px;
}

/* Chat bubbles */
[data-testid="stChatMessage"] {
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;
}

/* User message */
[data-testid="stChatMessage"]:has(div[aria-label="user"]) {
    background-color: #e0f2fe;
}

/* Assistant message */
[data-testid="stChatMessage"]:has(div[aria-label="assistant"]) {
    background-color: #ffffff;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Load PDFs (Backend)
# -----------------------------
@st.cache_resource
def initialize_data():
    folder = Path("data/pdfs")
    docs = load_and_split_pdfs(folder)
    vectorstore.add_documents(docs)

initialize_data()

# -----------------------------
# Sidebar (Enterprise Panel)
# -----------------------------
st.sidebar.markdown("## 🏢 Enterprise Assistant")
st.sidebar.markdown("### Navigation")
st.sidebar.markdown("- 💬 Chat")
st.sidebar.markdown("- 📄 Documents")
st.sidebar.markdown("- ⚙️ Settings")

st.sidebar.markdown("---")

if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.sidebar.markdown("---")
st.sidebar.caption("© 2026 Enterprise AI System")

# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="main-title">Enterprise Knowledge Assistant Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Ask questions about company policies, processes, and internal knowledge</div>', unsafe_allow_html=True)

# -----------------------------
# Chat Memory
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Display Chat
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# User Input
# -----------------------------
query = st.chat_input("Ask about company policies...")

if query:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.chat_message("user"):
        st.markdown(query)

    # Generate response
    with st.spinner("Analyzing and retrieving answer..."):
        result = graph.invoke({"query": query})
        answer = result.get("answer", "Sorry, I couldn't find an answer.").strip()

    # Store assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
    # Display response
    with st.chat_message("assistant"):
        st.markdown(answer)