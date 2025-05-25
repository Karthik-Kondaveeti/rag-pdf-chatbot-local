# 📄 PDF Chatbot with Vector Search & Ollama LLM

This project allows you to **upload PDF files**, convert them into **semantic chunks**, store them in a **vector database**, and **interact with the content via natural language questions** using an LLM (like Ollama's LLaMA models).

### 🔍 Features

-   ✅ Convert PDFs into structured, searchable text chunks
-   ✅ Store them in a persistent **Chroma vector database**
-   ✅ Ask questions in natural language and get context-aware answers
-   ✅ Built using **LangChain**, **Ollama**, and **ChromaDB**
    
----------

## 🏁 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Karthik-Kondaveeti/rag-pdf-chatbot-local.git
cd pdf-chat-ollama
```

### 2. Install Dependencies

Create a virtual environment and install the dependencies:

```bash
pip install -r requirements.txt
```

> Required packages include:
> 
> -   `langchain`
> -   `langchain_community`
> -   `langchain_ollama`
> -   `langchain_chroma`
> -   `python-dotenv`
> -   `yaspin`
>  -  and some more...

### 3. Set Environment Variables

Create a `.env` file in the root directory with the following:

```
DOCUMENTS_PATH=pdfs
DATABASE_PATH=vector_db
EMBEDDING_MODEL=nomic-embed-text
MODEL_NAME=mistral:7b
```

> Make sure to:
> -   Place your PDF files inside the `DOCUMENTS_PATH` folder (or update the path accordingly)
> -   Have the specified models pulled with Ollama (e.g., `ollama pull llama3`)
----------

## 🧠 Add PDFs to the Vector Database

To ingest your PDF files and store their embeddings:

```bash
python addToDatabase.py

```

-   Splits PDFs into 1000-character chunks (with 200-character overlap)
-   Assigns unique IDs per page/chunk
-   Skips previously ingested chunks
-   To clear the database: run clearDatabase script
----------

## ❓ Ask Questions

Once PDFs are indexed, you can ask questions using:

```bash
python askQuestion.py "What is the summary of chapter 2?"
```
-   Retrieves top 5 relevant chunks
-   Sends prompt + context to the LLM
-   Returns a friendly, helpful response
    

----------

## 🔧 Requirements

-   Python 3.8+
    
-   [Ollama](https://ollama.com/) installed and running locally
    
-   PDF files to upload
    

----------

## 📌 Example Use Case

> “I want to chat with my college lecture PDFs.”

1.  Put your lectures in `./pdfs`
    
2.  Run `addToDatabase.py`
    
3.  Ask:
    

```bash
python askQuestion.py "What did the professor say about quantum entanglement?"
```

----------

## 🚀 API Usage Guide

This project includes a FastAPI backend that exposes endpoints to interact with your PDF-based chatbot system. Below is a guide on how to use these APIs.

---

### 📦 Endpoint Summary

| Method | Endpoint     | Description                               |
|--------|--------------|-------------------------------------------|
| POST   | `/upload`    | Upload a PDF file                         |
| POST   | `/add`       | Process uploaded PDFs and update database |
| POST   | `/ask`       | Ask a question to the chatbot             |
| POST   | `/clear`     | Clear the current database                |

---

### 🔄 Upload a PDF

```bash
curl -X POST "http://localhost:8000/upload" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_file.pdf"
```

-   📥 This will save the uploaded PDF file to the path specified by the `PATH` variable in your `.env` file.
    

----------

### ➕ Add PDFs to the Vector Database

After uploading PDFs, use the `/add` endpoint to process and add them to the vector store.

```bash
curl -X POST "http://localhost:8000/add"
```
-   ⚙️ This runs the embedding + indexing process using `addToDatabase.main()`. This will add any new pdfs in the folder onto the database. 
    

----------

### ❓ Ask a Question

Send a prompt to the chatbot and get an intelligent response based on your documents.

```bash
curl -X POST "http://localhost:8000/ask?prompt=What%20is%20this%20paper%20about"
```

-   💬 Replace the prompt text with your actual question.
    

----------

### 🧹 Clear the Vector Database

Use this when you want to reset the database and remove all indexed documents.

```bash
curl -X POST http://localhost:8000/clear
```
-   🗑️ This will call `clearDatabase.clear_database()` to reset everything.
    
----------

### 🔧 Environment Variable

Ensure you have a `.env` file with a `PATH` variable that defines where uploaded files should be stored:
```
DATABASE_PATH=./uploads
```
----------

### 🏁 Run the FastAPI Server

Start the API locally using:

```bash
uvicorn main:app --reload
```
-   Make sure your FastAPI code is in a file named `main.py` or change the command accordingly.
    
----------

### ✅ Requirements

Install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn python-dotenv
```
----------
Now you're all set to build and query your PDF-based AI assistant through a clean and powerful API 🚀

## 🧠 Future Improvements

-   Web UI
-   Support for non-PDF formats
----------
