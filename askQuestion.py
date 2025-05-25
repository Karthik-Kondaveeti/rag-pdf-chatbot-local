import os
import argparse
from pathlib import Path
from yaspin import yaspin
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from dotenv import load_dotenv

load_dotenv()

PROMPT_TEMPLATE = """
    You are used to answer questions based on the provided document.
    Talk to me in a friendly and helpful manner. 
    Be creative when asked creative questions. 
    Read the following document: 
    {context}
    -----
    Answer the following question using the given document for context.
    {question}
"""
MODEL_NAME = os.getenv("MODEL_NAME")
DATABASE_PATH = os.getenv("DATABASE_PATH")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

with yaspin(text="Loading model...", color="cyan") as spinner:
    model = ChatOllama(model=MODEL_NAME)
    spinner.ok("✅")

def main():
    parser = argparse.ArgumentParser(description="Ask a question to the database.")
    parser.add_argument("question", type=str, help="The question to ask.")
    args = parser.parse_args()
    question = args.question

    folder = Path(DATABASE_PATH)
    if not folder.exists() or not folder.is_dir():
        print("First, you need to upload your files to the database...")
        return

    db = Chroma(persist_directory = DATABASE_PATH, embedding_function = OllamaEmbeddings(model = EMBEDDING_MODEL))

    with yaspin(text="Searchin database...", color="cyan") as spinner:
        results = db.similarity_search_with_relevance_scores(query = question, k = 5)
        spinner.ok("✅")

    if len(results) == 0 or results[0][1] < 0.4:
        print(f"Unable to find matching results.")
        return

    # for result, score in results:
    #     print(f"Score: {score}")
    #     print(f"Result: {result.page_content}")
    #     print("________________________")

    for result in results:
        result[0].page_content = " ".join(result[0].page_content.split())
        result[0].page_content = result[0].page_content.strip()
    context = "\n-----\n".join([doc.page_content for doc, _score in results])

    prompt = PROMPT_TEMPLATE.format(context=context, question=question)
    with yaspin(text="Thinking...", color="cyan") as sp:
        response = askAI(prompt)
        sp.ok("✅")
    
    sources = list(set([doc.metadata.get("id", None) for doc, _score in results]))
    formatted_response = f"Response: {response}\nSources: {sources}"
    print(formatted_response)

def askAI(prompt):
    response = model.invoke(prompt)
    return response.content

def predict(question):
    folder = Path(DATABASE_PATH)
    if not folder.exists() or not folder.is_dir():
        return {
            "success": False,
            "response": "First, you need to upload your files to the database...",
        }
    embedding_function = OllamaEmbeddings(model = EMBEDDING_MODEL)
    db = Chroma(persist_directory=DATABASE_PATH, embedding_function=embedding_function)
    results = db.similarity_search_with_relevance_scores(query = question, k = 5)
    if len(results) == 0 or results[0][1] < 0.4:
        return {
            "success": False,
            "response": "Unable to find matching results.",
        }
    for result in results:
        result[0].page_content = " ".join(result[0].page_content.split())
        result[0].page_content = result[0].page_content.strip()
    context = "\n-----\n".join([doc.page_content for doc, _score in results])
    prompt = PROMPT_TEMPLATE.format(context=context, question=question)
    response = askAI(prompt)
    sources = list(set([doc.metadata.get("id", None) for doc, _score in results]))
    return {
        "success": True,
        "response": response,
        "sources": sources
    }

if __name__ == "__main__":
    main()