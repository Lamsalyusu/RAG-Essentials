from langchain_community.vectorstores import Chroma
from langchain_community.docstore.document import Document
from langchain_community.embeddings import SentenceTransformerEmbeddings
import tempfile
def similarity_search_with_scores():
    documents = [
        Document(page_content="Hello World", metadata={"id": "doc1"}),
        Document(page_content="This is the second document.", metadata={"id": "doc2"}),
        Document(page_content="This is the third document.", metadata={"id": "doc3"}),
    ]
    embedding_function = SentenceTransformerEmbeddings()
    with tempfile.TemporaryDirectory() as tmpdir:
        vectorstore = Chroma.from_documents(
            documents = documents,
            embedding= embedding_function,
            persist_directory=tmpdir

        )
        query = 'hello world'
        results = vectorstore.similarity_search_with_score(query,k=3)

        for doc,score in results:
            print(f'Score {score}')
            print(f'Content:{doc.page_content}')
            print(f'Metadata:{doc.metadata}')
            print('---')

if __name__ =="__main__":
    similarity_search_with_scores()
