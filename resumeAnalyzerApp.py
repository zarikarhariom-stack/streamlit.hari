import streamlit as st
from utils import extract_pdf, create_vector_text

from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

st.set_page_config(page_title="Help4code placement RAG")
st.title("Help4code resume analyzer AI")


resume_file = st.file_uploader("Upload resume (PDF format)", type=["pdf"])
jd_text = st.text_area("Paste Job Description here")
if st.button("Analyze Resume"):
    if resume_file and jd_text:
        #extract resume
        resume_text = extract_pdf(resume_file)
        
        #Combine rsume and job description
        combined_text = resume_text + "\n\n" + jd_text
        
        #create vector store
        vectorstore = create_vector_text(combined_text)
        retriever = vectorstore.as_retriever()
        
        
        #load and integrate ollama LLM
        llm = Ollama(model="gemma2:2b")
        
        #prompt templet design
        prompt = ChatPromptTemplate.from_template("""
        
        You are an AI placement coach for help4you
        
        context:
        {question}
        
        
        Question:
        {question}
        
        
        provide:
        1. Skills Gap Analysis
        2. Missing Technologies
        3. ATS Score (0-100)
        4. 10 Technical interview Questions
        5. Resume Improvement suggestions
        6. Further Skills
        
        
        "")
        
        chain =(
            {
                "context":retriever,
                "question": RunnablePassthrough()
            }
            | prompt
            | llm
            | StrOutputParser
        """)
        
        response = chain.invoke("Analyze resume against job description")
        
        st.subheader("Analysys Result")
        st.write("response")
    else:
        st.warning("please upload resume and job description")
        
        