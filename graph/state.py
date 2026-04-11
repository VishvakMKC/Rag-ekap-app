from typing import TypedDict, List

class RAGState(TypedDict):
    query: str
    retrieved_docs: List[str]
    answer: str