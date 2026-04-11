from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = None
        self.texts = []

    def add_documents(self, docs):
        embeddings = self.model.encode(docs)
        self.texts.extend(docs)

        dim = embeddings.shape[1]

        if self.index is None:
            self.index = faiss.IndexFlatL2(dim)

        self.index.add(np.array(embeddings))

    def similarity_search(self, query, k=3):
        query_embedding = self.model.encode([query])
        distances, indices = self.index.search(np.array(query_embedding), k)

        return [self.texts[i] for i in indices[0]]