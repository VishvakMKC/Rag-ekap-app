from retriever.vector_store import VectorStore
from llm.model import LLM

vectorstore = VectorStore()
llm = LLM()

def retrieve_docs(state):
    docs = vectorstore.similarity_search(state["query"], k=3)
    return {"retrieved_docs": docs}

def generate_answer(state):
    context = "\n".join(state["retrieved_docs"])

    prompt = f"""
Answer ONLY with a single direct response.
Do NOT include the context, question, or any extra explanation.
Do NOT use markdown, code blocks, or backticks.

Context:
{context}

Question:
{state['query']}
"""
    response = llm.invoke(prompt)
    return {"answer": response}