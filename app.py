import chromadb
# chroma_client = chromadb.Client()
chroma_client = chromadb.PersistentClient(path="./chroma_db")  # Specify the path to the persistent database

from chromadb.utils import embedding_functions
sentence_embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
collection= chroma_client.get_or_create_collection(name="my_collection", embedding_function=sentence_embedding_function)

# collection_name = 'my_collection'
# collection = chroma_client.get_or_create_collection(name=collection_name)

documents = [
    {"id": "doc1","text": "Hello World"},
    {"id": "doc2","text": "This is the second document."},
    {"id": "doc3","text": "This is the third document."},
]

for doc in documents:
    # pass
    collection.add(ids=[doc["id"]], documents=[doc["text"]])

query = 'Hello World'

results = collection.query(query_texts=[query], n_results=3)
print(results)