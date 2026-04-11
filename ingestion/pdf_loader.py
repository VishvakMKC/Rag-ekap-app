import fitz  # PyMuPDF
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_pdfs(folder_path):
    documents = []

    for file in folder_path.glob("*.pdf"):
        doc = fitz.open(file)
        text = ""

        for page in doc:
            text += page.get_text()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=100
        )

        chunks = splitter.split_text(text)

        for chunk in chunks:
            documents.append(chunk)

    return documents