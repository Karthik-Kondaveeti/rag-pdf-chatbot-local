📄 PDF Chatbot with Vector Search & Ollama LLM
==============================================

This project allows you to **upload PDF files**, convert them into **semantic chunks**, store them in a **vector database**, and **interact with the content via natural language questions** using an LLM (like Ollama's LLaMA models).

### 🔍 Features

*   ✅ Convert PDFs into structured, searchable text chunks
    
*   ✅ Store them in a persistent **Chroma vector database**
    
*   ✅ Ask questions in natural language and get context-aware answers
    
*   ✅ Built using **LangChain**, **Ollama**, and **ChromaDB**
    

🏁 Getting Started
------------------

### 1\. Clone the repo

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone [https://github.com/Karthik-Kondaveeti/rag-pdf-chatbot-local.git](https://github.com/Karthik-Kondaveeti/rag-pdf-chatbot-local.git)   `

### 2\. Install Dependencies

Create a virtual environment and install the dependencies:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

> Required packages include:
> 
> *   langchain
>     
> *   langchain\_community
>     
> *   langchain\_ollama
>     
> *   langchain\_chroma
>     
> *   python-dotenv
>     
> *   yaspin
>     
> *   and more…
>     

### 3\. Set Environment Variables

Create a .env file in the root directory like the following example:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   DOCUMENTS_PATH=pdfs   DATABASE_PATH=vector_db  EMBEDDING_MODEL=nomic-embed-text  MODEL_NAME=mistral:7b   `

> Make sure to:
> 
> *   Place your PDF files inside the ./pdfs folder (or update the path accordingly)
>     
> *   Have the specified models pulled with Ollama (e.g., ollama pull mistral:7b)
>     

🧠 Add PDFs to the Vector Database
----------------------------------

To ingest your PDF files and store their embeddings:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python addToDatabase.py   `

*   Splits PDFs into 1000-character chunks (with 200-character overlap)
    
*   Assigns unique IDs per page/chunk
    
*   Skips previously ingested chunks
    
*   To clear the database: run the clearDatabase.py
    

❓ Ask Questions
---------------

Once PDFs are indexed, you can ask questions using:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python askQuestion.py "What is the summary of chapter 2?"   `

*   Retrieves the top 5 relevant chunks
    
*   Sends prompt + context to the LLM
    
*   Returns a friendly, helpful response
    

📦 Project Structure
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   .  ├── addToDatabase.py     # Ingest and index PDFs into vector DB  ├── askQuestion.py       # Query the indexed data with natural language  ├── .env                 # Configurable paths and model names  ├── pdfs/                # Your PDF files go here  ├── chrojma/           # Persistent vector storage  └── README.md   `

🔧 Requirements
---------------

*   Python 3.8+
    
*   [Ollama](https://ollama.com/) is installed and running
    
*   An LLM model is pulled in Ollama
    
*   PDF files to upload
    

📌 Example Use Case
-------------------

> “I want to chat with my college lecture PDFs.”

1.  Put your PDFs in ./pdfs
    
2.  Run addToDatabase.py
    
3.  Ask:
    

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python askQuestion.py "What is quantum entanglement?"   `

🧠 Future Improvements
----------------------

*   Web UI
    
*   Support for non-PDF formats
