import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os  # Make sure os is imported for file system operations

load_dotenv()  # Load environment variables from .env file

def main(): 
    st.header("Hello!")
    
    # File uploader for PDF
    pdf = st.file_uploader("Upload your pdf here!", type='pdf')
    
    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Initialize text splitter
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )

        chunks = text_splitter.split_text(text=text)

        # Display the chunks
        st.write(chunks)

        store_name = pdf.name[:4]

        if os.path.exists(f"{store_name}"):
            vector_store= FAISS.load_local(f"{store_name}", OpenAIEmbeddings(), allow_dangerous_deserialization=True) 
            st.write("Empeddings loaded from the disk.")
        else:
            embeddings = OpenAIEmbeddings()
            vector_store = FAISS.from_texts(chunks, embedding=embeddings)
            vector_store.save_local(f"{store_name}")
            st.write("Embeddings computation completed.")
            pass


if __name__ == '__main__':
    main()
