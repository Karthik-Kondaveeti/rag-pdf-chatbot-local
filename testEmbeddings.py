from langchain_ollama import OllamaEmbeddings

def main():
    # input strings
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    # embedding model
    model = "nomic-embed-text:v1.5"
    # embedding vectors
    embedder = OllamaEmbeddings(model=model)
    vector1 = embedder.embed_query(str1)
    vector2 = embedder.embed_query(str2)
    # calculate cosine similarity
    dotProduct = calculateDotProduct(vector1, vector2)
    productOfMagnitudes = calculateMagnitude(vector1, vector2)
    score = calculateCosineSimilarity(dotProduct, productOfMagnitudes)

    # print the result
    print(f"Cosine Similarity: {1 - score}")

def calculateDotProduct(vector1, vector2):
    dotProduct = 0
    for i in range(min(len(vector1), len(vector2))):
        dotProduct += vector1[i] * vector2[i]
    return dotProduct

def calculateMagnitude(vector1, vector2):
    magnitude1 = 0
    for i in range(len(vector1)):
        magnitude1 += vector1[i] ** 2
    magnitude1 = magnitude1 ** 0.5

    magnitude2 = 0
    for i in range(len(vector2)):
        magnitude2 += vector2[i] ** 2
    magnitude2 = magnitude2 ** 0.5

    return magnitude1 * magnitude2

def calculateCosineSimilarity(dotProduct, productOfMagnitudes):
    if productOfMagnitudes == 0:
        return 0
    else:
        return dotProduct / productOfMagnitudes

if __name__ == "__main__":
    main()
