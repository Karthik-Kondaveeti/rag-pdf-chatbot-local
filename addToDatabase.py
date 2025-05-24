import os
from yaspin import yaspin
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

load_dotenv()

PATH = os.getenv("PATH")
DATABASE_PATH = os.getenv("DATABASE_PATH")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

def main():
    with yaspin(text="Loading files...", color="cyan") as sp:
        documents = loadDocuments()
        sp.ok("✅")
    with yaspin(text="Looking for new files...", color="cyan") as sp:
        chunks = splitText(documents)
        sp.ok("✅")

    if len(chunks) > 5000:
        print("\n Too many chunks to add to database. Try smaller files or clear the database. ")
        return
    else:
        with yaspin(text="Adding to database...", color="cyan") as sp:
            newChunksCount = addToDatabase(chunks)
            sp.ok("✅")
        print(f"\nAdding {newChunksCount} new chunks to the database.")

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
    print(f"\nSplit {len(documents)} documents into {len(chunks)} chunks.")
    return chunks

def addToDatabase(chunks):
    db = Chroma(
        persist_directory=DATABASE_PATH, embedding_function = OllamaEmbeddings(model=EMBEDDING_MODEL), 
    )
    caluculateChunkIds(chunks)

    existingDatabase = db.get(include=[])
    existingIds = set(existingDatabase["ids"])

    new_chunks = []
    for chunk in chunks:
        if chunk.metadata["id"] not in existingIds:
            new_chunks.append(chunk)

    if len(new_chunks) == 0:
        print("\nThere is nothing to add...")
    else:
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids = new_chunk_ids)

    return len(new_chunks)

def caluculateChunkIds(chunks):
    previousPageId, chunkIndex = None, 1
    for chunk in chunks:
        source = chunk.metadata.get("source", None)
        page = chunk.metadata.get("page", None)
        pageId = f"{source}:{page}"

        if pageId == previousPageId:
            chunkIndex += 1
        else:
            chunkIndex = 1
        
        previousPageId = pageId
        currentPageId = f"{pageId}:{chunkIndex}"
        chunk.metadata["id"] = currentPageId

if __name__ == "__main__":
    main()