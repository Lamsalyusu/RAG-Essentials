# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
# from langchain_community.docstore.document import Document
from langchain_core.documents import Document
# from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
import tempfile
from dotenv import load_dotenv
load_dotenv()
# def similarity_search_with_scores():
#     documents = [
#         Document(page_content="Hello World", metadata={"id": "doc1"}),
#         Document(page_content="This is the second document.", metadata={"id": "doc2"}),
#         Document(page_content="This is the third document.", metadata={"id": "doc3"}),
#     ]
#     embedding_function = SentenceTransformerEmbeddings()
#     with tempfile.TemporaryDirectory() as tmpdir:
#         vectorstore = Chroma.from_documents(
#             documents = documents,
#             embedding= embedding_function,
#             persist_directory=tmpdir

#         )
#         query = 'hello world'
#         results = vectorstore.similarity_search_with_score(query,k=3)

#         for doc,score in results:
#             # this scores are the distace scores
#             print(f'Score {score}')
#             print(f'Content:{doc.page_content}')
#             print(f'Metadata:{doc.metadata}')
#             print('---')



def metadata_filtering():
    documents = [
        Document(page_content="Hello World", metadata={"id": "doc1","topic":"greeting"}),
        Document(page_content="This is the second document.",  metadata={"id": "doc2", "topic": "greeting"}),
        Document(page_content="This is the third document.", metadata={"id": "doc3","topic": "general"}),
    ]

    # embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    embedding_function = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    with tempfile.TemporaryDirectory() as tmpdir:
        vectorstore = Chroma.from_documents(
            documents= documents,
            embedding = embedding_function,
            persist_directory=tmpdir
        )

        query = 'hello'
        filter_cr = {'topic':'greeting'}
        results = vectorstore.similarity_search(query,filter=filter_cr,k=4)


        for doc in results:
            #  yesle mathi ko document 1 id =1 ko content haru load garchha kina bhane hamle filtering lagako chham meta data ma/
            # topic j hos but based on the metadata filtering hunchha 
            # main difference between similrity_search_with_scores ra similarity_scores bhaneko chai 
            # with scores --> returns: [(Document, score), (Document, score), (Document, score)] 
            # without scores ---> returns [Document,Document,Document]
            print(doc.page_content,doc.metadata)
        
if __name__ =="__main__":
    # similarity_search_with_scores()
    metadata_filtering()
