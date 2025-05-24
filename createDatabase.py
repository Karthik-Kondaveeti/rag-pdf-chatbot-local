import os
import shutil
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

load_dotenv()

PATH = "data"
DATABASE_PATH = "chroma"
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

def main():
    documents = loadDocuments()
    chunks = splitText(documents)
    createDatabase(chunks)

def loadDocuments():
    documents = []

    pdf_loader = DirectoryLoader(PATH, glob="*.pdf", loader_cls=PyPDFLoader)
    documents.extend(pdf_loader.load())

    return documents

def splitText(documents):
    text_splitter  = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    return chunks

def createDatabase(chunks):
    if os.path.exists(DATABASE_PATH):
        shutil.rmtree(DATABASE_PATH)
    db = Chroma.from_documents(
        chunks, OllamaEmbeddings(model=EMBEDDING_MODEL), persist_directory=DATABASE_PATH,
    )
    print(f"Saved {len(chunks)} chunks to {DATABASE_PATH}.")

if __name__ == "__main__":
    main()