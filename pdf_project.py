import streamlit as st
from PyPDF2 import PdfReader
ffrom langchain.text_splitter import RecursiveCharacterTextSplitter

def main(): Usage
    st.header("Hello!")
    pdf  = st.file_uploader("Upload your pdf here!", type='pdf')
    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text=""
        for page in pdf_reader.pages:
            text+=page.extract_text()

            text_splitter = RecursiveCharacterTextSplitter(
                chink_size=1000,
                chunk_overlap=200,
                length_function=len
                )

            chuks = text_splitter.split_text(text=text)

            st.write(chunks)

if __name__=='__main__':
    main()
    
