from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
import requests
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# Template for the prompt
prompt_template = """Usa las siguientes piezas de información para responder a la pregunta.
Si no puedes responder la pregunta, por favor, responde con "No puedo responder la pregunta".
Solo responde a la pregunta si esta relacionada con las piezas de información.

Piezas de información:
{context}

Pregunta: {question}
Respuesta:
"""

# Splitter for the text
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

def main():
    st.set_page_config(page_title="Hazme una pregunta", page_icon="🧠")
    st.header("ChatDoc")

    # Initialize the session state
    if 'url_content' not in st.session_state:
        st.session_state.url_content = ""

    # Select the source of information
    option = st.selectbox(
    'Seleccionar fuente de información',
    ('Web', 'Texto', 'pdf'))

    if option == "Web":
        url_input = st.text_input("Escribe la URL")

        if st.button("Enviar"):
            url = url_input
            # get the content of the url
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                text = soup.get_text()
            
                texts = text_splitter.split_text(text)

                st.session_state.url_content = texts


    elif option == "Texto":
        text_input = st.text_area("Write the text")

        if st.button("Enviar", key="btn3"):
            # split into chunks
            texts = text_splitter.split_text(text_input)
            st.session_state.url_content = texts

    elif option == "pdf":
        pdf = st.file_uploader("Upload your PDF", type="pdf")
        
        if pdf is not None:
            pdf_reader = PdfReader(pdf)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
                
            # split into chunks
            texts = text_splitter.split_text(text)
            st.session_state.url_content = texts
        

                
    if st.session_state.url_content:

        # show user input
        user_question = st.text_input("Escibe tu pregunta:")

        if st.button("Enviar", key="btn2"):
            # create the prompt
            prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
            # Create the instance of the model
            llm = ChatOpenAI(
                model_name="gpt-3.5-turbo-16k",
                temperature=0
            )
    
            # create embeddings
            embedding=OpenAIEmbeddings()
            # create the vector database
            vectordb = FAISS.from_texts(st.session_state.url_content, embedding)
            question = user_question
            
            # create the chain type kwargs (custom parameters for the chain type)
            chain_type_kwargs = {"prompt": prompt}
            dbqa = RetrievalQA.from_chain_type(llm=llm, # this is the model
                                                chain_type='stuff', # this is the chain type name
                                                retriever=vectordb.as_retriever(search_kwargs={'k': 10}), # this is the retriever
                                                return_source_documents=True, # this is the return source documents
                                                chain_type_kwargs=chain_type_kwargs # this is the chain type kwargs
                                                   )
       
            st.write(dbqa.invoke(question)["result"]) # this is the result of the chain

if __name__ == '__main__':
    main()