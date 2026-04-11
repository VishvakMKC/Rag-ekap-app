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
    
    Answer ONLY from the context below and return the suitable answer alone, don't include any extra text.

    Context:
    {context}

    Question:
    {state['query']}
    """

    response = llm.invoke(prompt)
    return {"answer": response}