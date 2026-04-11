from langgraph.graph import StateGraph
from graph.state import RAGState
from graph.nodes import retrieve_docs, generate_answer

builder = StateGraph(RAGState)

builder.add_node("retrieve", retrieve_docs)
builder.add_node("generate", generate_answer)

builder.set_entry_point("retrieve")

builder.add_edge("retrieve", "generate")

graph = builder.compile()