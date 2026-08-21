from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from pypdf import PdfReader


# Resume analyser using rag and LLM using streamlit

#it will exract the text from the pdf file and return a list of documents
# Rag document loading
def extract_pdf(file):
    reader = PdfReader(file)
    text= "" # str type
    for page in reader.pages:
        text += page.extract_text()
    return text

#Rag document splitting

#Documnet spliting
def split_text(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    return splitter.split_text(text)


#Embeding  and vector storage / means converting the textual data into tokens
def create_vector_text(text):
    chunks = split_text(text)
    docs = [Document(page_content=c) for c in chunks]
    embedding = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    vectorstore = FAISS.from_documents(docs, embedding)
    return vectorstore


    
    