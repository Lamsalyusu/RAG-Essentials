from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough,RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic import BaseModel,Field
from typing import List
from dotenv import load_dotenv
import tempfile

load_dotenv()

embedding_model= HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

KNOWLEDGE_BASE = """# LANGCHAIN Framework 
LangChain is a framework for developing application by language models.
## Core Components
1. **Models**: LangChain supports various LLM providers including OpenAI, Groq, Anthropic, and HuggingFace.
2. **Prompts**: Templates that structure input to language models, supporting variables and few-shot examples.
3. **Chains**: Sequences of calls that combine models, prompts, and other components into a single pipeline.
4. **Retrievers**: Components that fetch relevant documents from a knowledge base, commonly backed by a vector store.
5. **Agents**: Systems that use an LLM to decide which actions to take, often calling external tools.

## Vector Stores
Vector stores like Chroma, FAISS, and Pinecone store document embeddings and support similarity search,
which is the retrieval step in Retrieval-Augmented Generation (RAG) pipelines.
"""

def create_kb():
    '''create a vector store for knowledge base'''
    splitter = RecursiveCharacterTextSplitter(chunk_size = 500,chunk_overlap=50)
    doc = Document(page_content = KNOWLEDGE_BASE,metadata={'source':'langchain_knowledge_base'})

    chunks = splitter.split_documents([doc])
    vector_store = Chroma.from_documents(
        documents = chunks,
        embedding = embedding_model,
        persist_directory= tempfile.mkdtemp()
    )
    return vector_store

def demo_basic_rag():
    vector_store = create_kb()
    retiever = vector_store.as_retriever(search_type = "similarity",search_kwargs ={'k':2})
    # llm = init_chat_model()
    prompt = ChatPromptTemplate.from_template(
        '''Answer the question based on the following context:
        {context}
        Question:{question}
        Answer:
        Make sure you answer in a concide manner,
        and if you dont know the answer ,just say "I dont know".
        '''
    )
    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])



    llm = ChatGroq(model='llama-3.3-70b-versatile',temperature=0)
    rag_chain = (

        {"context":retiever |format_docs,"question":RunnablePassthrough()}

        | prompt
        | llm
        | StrOutputParser()
        
        )

    query = "What are the core components of LangChain?"
    answer = rag_chain.invoke(query)

    print(f"Question: {query}")
    print(f"Answer:{answer}")


if __name__ == "__main__":
    demo_basic_rag()
