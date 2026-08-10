import chromadb
chroma_client = chromadb.Client()

collection_name = 'my_collection'
collection = chroma_client.get_or_create_collection(name=collection_name)

documents = [
    {"id": "doc1","text": "Hello World",},
    {"id": "doc2","text": "This is the second document.",},
    {"id": "doc3","text": "This is the third document.",},
]

for doc in documents:
    # collection.upsert(ids=doc["id"], texts=doc["text"])

query = 'Hello World'