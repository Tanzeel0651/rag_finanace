# RAG-Finance 📊🧠
A Retrieval-Augmented Generation (RAG) system for interactive question answering over structured and unstructured financial documents using LangChain, OpenAI embeddings, and a local vector database.

## 🔍 Overview

This project enables natural language interaction with company financial reports—including income statements, balance sheets, and cash flow statements—through a conversational interface. It leverages OpenAI's LLMs to answer queries grounded in a hybrid corpus of CSV and free-text financial data.

## 💡 Key Features

- 🔗 **Retrieval-Augmented Generation** with `LangChain` and `Chroma`
- 📄 **Hybrid Document Embedding** from structured CSVs and unstructured summaries
- 🧠 **OpenAI GPT-4o-mini** based conversational interface
- 🗃️ **Vector Store Management** with persistence and refresh options
- 🧪 **Synthetic Financial Dataset Generator** for experimentation
- 💬 **Gradio Chat UI** for interactive QA

## 📁 Project Structure

```
├── data/
│   ├── income_statement.csv
│   ├── balance_sheet.csv
│   ├── cash_flow_statement.csv
│   └── financial_summaries.txt
├── vector_db/                # Chroma vector store (auto-generated)
├── chat.py                   # Main LangChain RAG pipeline + Gradio app
├── generate_syntetic_data.py # Synthetic financial data generator
├── environment.yml           # Conda environment file
└── .gitignore
```

## 🚀 Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/Tanzeel0651/rag_finanace.git
cd rag_finanace
```

### 2. Set up the Environment
```bash
conda env create -f environment.yml
conda activate rag_finance
```

### 3. Set Your OpenAI API Key
Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Generate Synthetic Data
```bash
python generate_syntetic_data.py
```

### 5. Launch the Gradio Chat App
```bash
python chat.py
```

A browser window will open where you can ask questions like:
- “What was the company's revenue in 2023?”
- “Summarize the 2024 financial performance.”
- “How has the net income changed over the years?”

## 🧠 How It Works

1. **Data Loading & Processing**  
   - Loads unstructured financial summaries from text.
   - Converts CSV rows (income, balance sheet, cash flow) to readable text chunks.

2. **Embedding & Vectorization**  
   - All text chunks are embedded using `OpenAIEmbeddings`.
   - Documents are stored in a `Chroma` vector DB for retrieval.

3. **Conversational QA**  
   - Uses `ConversationalRetrievalChain` from LangChain with a memory buffer.
   - Queries are matched to relevant documents and answered using `ChatOpenAI`.

## 📦 Dependencies

- `langchain`
- `openai`
- `pandas`
- `gradio`
- `chromadb`
- `python-dotenv`

Install all dependencies via:
```bash
conda env create -f environment.yml
```

## 📈 Example Query

```
User: What was the company's revenue in 2023?
Model: The company’s revenue in 2023 was $550 million.
```

## 🛠️ Future Work

- Fine-tuning LLMs on domain-specific finance QA pairs
- Integration with live financial APIs
- UI/UX improvements for non-technical users
- Docker containerization for scalable deployment

## 📄 License

MIT License. Feel free to use, modify, and distribute with attribution.

## 🙌 Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI](https://openai.com/)
- [Gradio](https://www.gradio.app/)
- [ChromaDB](https://www.trychroma.com/)

## 🔗 Connect

Project maintained by [Tanzeel0651](https://github.com/Tanzeel0651)