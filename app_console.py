from graph.workflow import graph
from ingestion.pdf_loader import load_and_split_pdfs
from graph.nodes import vectorstore
from pathlib import Path

# -----------------------------
# Load PDFs (same as Streamlit)
# -----------------------------
def initialize_data():
    folder = Path("data/pdfs")
    docs = load_and_split_pdfs(folder)
    vectorstore.add_documents(docs)

print("🔄 Loading documents...")
initialize_data()
print("✅ Documents loaded successfully!\n")

# -----------------------------
# Chat Loop (CMD Interface)
# -----------------------------
print("🏢 Enterprise Knowledge Assistant (CLI)")
print("Type 'exit' to quit\n")

chat_history = []

while True:
    query = input("👤 You: ")

    if query.strip().lower() in ["exit", "quit"]:
        print("👋 Exiting...")
        break

    # Store user message
    chat_history.append({
        "role": "user",
        "content": query
    })

    print("🤖 Assistant: Thinking...")

    try:
        # Invoke LangGraph
        result = graph.invoke({"query": query})
        answer = result.get("answer", "Sorry, I couldn't find an answer.").strip()

    except Exception as e:
        answer = f"⚠️ Error: {str(e)}"

    # Store assistant response
    chat_history.append({
        "role": "assistant",
        "content": answer
    })

    print(f"🤖 Assistant: {answer}\n")