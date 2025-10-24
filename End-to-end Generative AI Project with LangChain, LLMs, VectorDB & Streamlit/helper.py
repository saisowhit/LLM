

from langchain.memeory import ConversationalBufferMemory
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecuriveCharacterTextSplitter
from langchain.embeddings import GooglePalmEmbeddings
from langchain.vectorstore import FAISS
from langchain.chains import
from langchain.memory import ConverstionBufferMemory
from langchain.llms import GooglePalm

load_dotenv()
GOOLGE_API_KEY=os.getenv("")
os.environ["GOOGLE_API_KEY"]=GOOLGE_API_KEY

def get_chuncks(text):
    text_splitter=RecurssiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=20)
    chunks=text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings=GooglePalmEmbeddings()
    vector_store=FAISS.from_texts(text_chunks,embeddings=embeddings)
    return vector_store
def get_conversational_chain(vector_store):
    llm=GooglePalm()
    memory=ConversationalBufferMemory(memory_key="chat_history",return_messages=True)
    conversation_chain=ConversationalRetrievalChain.from_llm(llm=llm,retriever=vector_store.as_retriever())
    return conversation_chain