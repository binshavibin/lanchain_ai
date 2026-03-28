# LangChain Learning Project

This repository contains a collection of Jupyter notebooks demonstrating various LangChain concepts and implementations, including data ingestion, embeddings, OpenAI integration, and vector databases.

## Overview

LangChain is a framework for developing applications powered by language models. This project serves as a learning resource and reference implementation for common LangChain use cases.

## Project Structure

### DataIngension/
Contains notebooks exploring different data ingestion and text splitting techniques:
- `characterSplitter.ipynb` - Character-based text splitting
- `dataIngension.ipynb` - General data ingestion patterns
- `htmlHeaderTextSplitter.ipynb` - HTML header-aware text splitting
- `jsonTextSplitter.ipynb` - JSON document splitting
- `textSplitter.ipynb` - Basic text splitting methods
- Sample files: `records.xml`, `speech.txt`

### Embeddings/
Demonstrates various embedding techniques and providers:
- `embedding.ipynb` - Basic embedding concepts
- `huggingFace.ipynb` - HuggingFace transformer embeddings
- `ollamaEmbedding.ipynb` - Local Ollama embeddings

### openai/
OpenAI integration examples:
- `GettingStarted.ipynb` - Basic OpenAI API usage
- `Simpleapp.ipynb` - Simple application using OpenAI

### VectorDB/
Vector database implementations:
- `Faiss.ipynb` - Facebook AI Similarity Search (FAISS) usage
- `faiss_index/` - Contains pre-built FAISS index files

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd langchain
```

2. Create a virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
# Add other required API keys as needed
```

## Usage

Each folder contains Jupyter notebooks that can be run individually. Start with the notebooks in the following order for a comprehensive learning path:

1. **DataIngension/** - Learn about text splitting and data preparation
2. **Embeddings/** - Understand different embedding techniques
3. **openai/** - Get started with OpenAI integration
4. **VectorDB/** - Explore vector storage and retrieval

To run the notebooks:
```bash
jupyter notebook
```

Navigate to the desired notebook and execute the cells.

## Requirements

- Python 3.8+
- Jupyter Notebook
- API keys for OpenAI and other services as needed

See `requirements.txt` for a complete list of Python dependencies.

## Key Dependencies

- **langchain**: Core LangChain framework
- **langchain-openai**: OpenAI integrations
- **langchain-community**: Community-contributed components
- **langchain-text-splitters**: Text splitting utilities
- **faiss-cpu**: Facebook AI Similarity Search
- **sentence-transformers**: Sentence embedding models
- **chromadb**: Chroma vector database
- **ollama**: Local LLM integration

## Learning Objectives

This project covers:
- Text preprocessing and splitting strategies
- Various embedding techniques (OpenAI, HuggingFace, Ollama)
- Vector database operations (FAISS, Chroma)
- Building RAG (Retrieval-Augmented Generation) applications
- Integration with different LLM providers

## Contributing

Feel free to contribute by:
- Adding new notebooks for additional LangChain features
- Improving existing implementations
- Adding documentation or examples
- Reporting issues or suggesting enhancements

## License

This project is for educational purposes. Please refer to individual package licenses for commercial use.