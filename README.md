# Enterprise Knowledge Assistant Platform (EKAP)

A Retrieval-Augmented Generation (RAG) system designed for enterprise knowledge management, built with Streamlit, LangChain, and LangGraph.

## 🚀 Features

- **Document Ingestion**: Load and process PDF documents for knowledge base creation
- **Vector Search**: FAISS-powered semantic search for efficient document retrieval
- **Conversational AI**: LangGraph-based workflow for natural language question answering
- **Dual Interfaces**: Both web-based Streamlit app and command-line interface
- **Enterprise Ready**: Designed for HR and organizational knowledge management

## 🏗️ Architecture

The system consists of several key components:

- **Ingestion Layer**: PDF loading and text splitting (`ingestion/pdf_loader.py`)
- **Retrieval Layer**: Vector store and document retrieval (`retriever/vector_store.py`)
- **LLM Layer**: Language model integration (`llm/model.py`)
- **Graph Layer**: LangGraph workflow orchestration (`graph/`)
- **Interfaces**: Streamlit web app (`app.py`) and console app (`app_console.py`)

## 📋 Prerequisites

- Python 3.8+
- Required packages listed in `requirements.txt`

## 🛠️ Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd rag_ekap
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Place your PDF documents in the `data/pdfs/` directory

## 🚀 Usage

### Web Interface (Recommended)

Run the Streamlit application:
```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your browser.

### Command Line Interface

Run the console application:
```bash
python app_console.py
```

Type your questions and get answers interactively. Type 'exit' to quit.

## 📁 Project Structure

```
rag_ekap/
├── app.py                 # Streamlit web interface
├── app_console.py         # Command-line interface
├── requirements.txt       # Python dependencies
├── questions.txt          # Sample questions for testing
├── data/
│   └── pdfs/             # Directory for PDF documents
├── graph/
│   ├── nodes.py          # Graph nodes (retrieve, generate)
│   ├── state.py          # State management
│   └── workflow.py       # LangGraph workflow definition
├── ingestion/
│   └── pdf_loader.py     # PDF loading and processing
├── llm/
│   └── model.py          # Language model configuration
└── retriever/
    └── vector_store.py   # Vector store and retrieval logic
```

## 🔧 Configuration

The system uses the following key technologies:

- **LangChain**: For LLM integration and document processing
- **LangGraph**: For workflow orchestration
- **FAISS**: For vector similarity search
- **Sentence Transformers**: For text embeddings
- **PyMuPDF**: For PDF text extraction
- **Streamlit**: For web interface

## 📝 Sample Questions

The system can answer questions like:
- How to apply for leave?
- How to access company VPN?
- What are working hours?
- How to check salary details?
- How to request reimbursement?

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions, please open an issue in the repository or contact the development team.