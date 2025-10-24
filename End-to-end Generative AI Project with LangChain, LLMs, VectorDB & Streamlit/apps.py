
import streamlit as st
import time
from helper import get_pdf_text,get_text_chunks,get_vector_store,get_conversational_chain

def user_input(user_question):
    response=st.session_state.conversation({'question':user_question})
    st.session_state.chatHistory=response['chat_history']
    for i,message in enumerate(st.session_state.chatHistory):
        if i%2==0:
            st.write("User:",message.content)
        else:
            st.write("Reply:",message.content)

def main():
    st.set_page_config("Information Retrieval")
    st.header("Information-Retrieval")
    user_questions=st.text_input("Ask a question")
    if "conversation" not in st.session_state:
        st.session_state.conversation=None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory=None
    if user_questions: 
        user_input(user_questions)

    with st.sidebar:
        st.tile("Menu")
        pdf_docs=st.file_uploader("Upload your pdf files",accept_multiple_files=True)
        if st.button("Submit and process"):
            with st.spinner("processing"):
                raw_text=get_pdf_text(pdf_docs)
                text_chunks=get_text_chunks(raw_text)
                vector_store=get_vector_store(text_chunks)
                st.session_state.conversations=get_conversational_chain(vector_store)
        st.success("Done")


if __name__=="__main__":
    main()