import warnings
warnings.filterwarnings("ignore")
from langgraph.graph import END, START, StateGraph, MessagesState
from langchain_groq import ChatGroq
from typing import Annotated, Literal, TypedDict, Sequence
from langchain_core.messages import BaseMessage
import operator
import os
from langchain_community.document_loaders import PyPDFLoader
import streamlit as st
import matplotlib.pyplot as plt
from tempfile import NamedTemporaryFile
from IPython.display import Image, display
from PIL import Image, ImageEnhance
from fpdf import FPDF
from dotenv import load_dotenv
load_dotenv()


llm = ChatGroq(model="llama3-8b-8192")


def load_image(image_file):
    img = Image.open(image_file)
    return img


class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]

def patient_agent(AgentState):
    return {"messages": ["Summarization of EHR of Patient by Generative AI"]}
    


def demographic_agent(AgentState):
    
    try:

        pdf_file = "sample_patient.pdf"
        data = PyPDFLoader(pdf_file).load()

        string_text = [data[i].page_content for i in range(len(data))]
        patient_data = " ".join([text for text in string_text])

        response = llm.invoke("Your task is to extract the patient name and also the demographic information from the patient's electronic health record data. Only respond with the patient name and demographic information and nothing else. Please don't include any new line character like \n or tab charater like \t in the information. Patient Data: " + patient_data)

    except Exception as ex:
        print("Errors = {}".format(ex))
        
    return {"messages": [response.content]}


def diagnosis_agent(AgentState):
    
    try:

        pdf_file = "sample_patient.pdf"
        data = PyPDFLoader(pdf_file).load()

        string_text = [data[i].page_content for i in range(len(data))]
        patient_data = " ".join([text for text in string_text])

        response = llm.invoke("Your task is to extract the all the diagnosis information for the patient from the patient's electronic health record data. Only respond with the patient's diagnosis information and nothing else. Please don't include any new line character like \n or tab charater like \t in the information. Patient Data: " + patient_data)

    except Exception as ex:
        print("Errors = {}".format(ex))
        
    return {"messages": [response.content]}


def vitals_agent(AgentState):
    
    try:

        pdf_file = "sample_patient.pdf"
        data = PyPDFLoader(pdf_file).load()

        string_text = [data[i].page_content for i in range(len(data))]
        patient_data = " ".join([text for text in string_text])

        response = llm.invoke("Your task is to extract the vital signs information for the patient from the patient's electronic health record data. Only respond with the patient's vital signs information and nothing else. Please don't include any new line character like \n or tab charater like \t in the information. Patient Data: " + patient_data)

    except Exception as ex:
        print("Errors = {}".format(ex))
        
    return {"messages": [response.content]}


def immunization_agent(AgentState):
    
    try:

        pdf_file = "sample_patient.pdf"
        data = PyPDFLoader(pdf_file).load()

        string_text = [data[i].page_content for i in range(len(data))]
        patient_data = " ".join([text for text in string_text])

        response = llm.invoke("Your task is to extract the immunization information for the patient from the patient's electronic health record data. Only respond with the patient's immunization information and nothing else. Please don't include any new line character like \n or tab charater like \t in the information. Patient Data: " + patient_data)

    except Exception as ex:
        print("Errors = {}".format(ex))
        
    return {"messages": [response.content]}


def family_history_agent(AgentState):
    
    try:

        pdf_file = "sample_patient.pdf"
        data = PyPDFLoader(pdf_file).load()

        string_text = [data[i].page_content for i in range(len(data))]
        patient_data = " ".join([text for text in string_text])

        response = llm.invoke("Your task is to extract the family history information for the patient from the patient's electronic health record data. Only respond with the patient's family history information and nothing else. Please don't include any new line character like \n or tab charater like \t in the information. Patient Data: " + patient_data)

    except Exception as ex:
        print("Errors = {}".format(ex))
        
    return {"messages": [response.content]}


def social_history_agent(AgentState):
    
    try:

        pdf_file = "sample_patient.pdf"
        data = PyPDFLoader(pdf_file).load()

        string_text = [data[i].page_content for i in range(len(data))]
        patient_data = " ".join([text for text in string_text])

        response = llm.invoke("Your task is to extract the social history information for the patient from the patient's electronic health record data. Only respond with the patient's social history information and nothing else. Please don't include any new line character like \n or tab charater like \t in the information. Patient Data: " + patient_data)

    except Exception as ex:
        print("Errors = {}".format(ex))
        
    return {"messages": [response.content]}


def pmh_agent(AgentState):
    
    try:

        pdf_file = "sample_patient.pdf"
        data = PyPDFLoader(pdf_file).load()

        string_text = [data[i].page_content for i in range(len(data))]
        patient_data = " ".join([text for text in string_text])

        response = llm.invoke("Your task is to extract the past medical history information for the patient from the patient's electronic health record data. Only respond with the patient's past medical history information and nothing else. Please don't include any new line character like \n or tab charater like \t in the information. Patient Data: " + patient_data)

    except Exception as ex:
        print("Errors = {}".format(ex))
        
    return {"messages": [response.content]}


def psh_agent(AgentState):
    
    try:

        pdf_file = "sample_patient.pdf"
        data = PyPDFLoader(pdf_file).load()

        string_text = [data[i].page_content for i in range(len(data))]
        patient_data = " ".join([text for text in string_text])

        response = llm.invoke("Your task is to extract the past surgical history information for the patient from the patient's electronic health record data. Only respond with the patient's past surgical history information and nothing else. Please don't include any new line character like \n or tab charater like \t in the information. Patient Data: " + patient_data)

    except Exception as ex:
        print("Errors = {}".format(ex))
        
    return {"messages": [response.content]}


def enc_progress_notes_agent(AgentState):
    
    try:

        pdf_file = "sample_patient.pdf"
        data = PyPDFLoader(pdf_file).load()

        string_text = [data[i].page_content for i in range(len(data))]
        patient_data = " ".join([text for text in string_text])

#        response = llm.invoke("Your task is to extract the encounter progress notes information for the patient from the patient's electronic health record data. In the patient's encounter progress notes information, please include assessment, plan of treatments, chief complaints, history of present illness and review of systems. Information should be in fewer than 100 words. Only respond with the patient's encounter progress notes information and nothing else. Patient Data: " + patient_data)

        response = llm.invoke("Your task is to extract the encounter progress notes information for the patient from the patient's electronic health record data. Information should be in fewer than 300 words. Only respond with the patient's encounter progress notes information and nothing else. Please don't include any new line character like \n or tab charater like \t in the information. Patient Data: " + patient_data)

    except Exception as ex:
        print("Errors = {}".format(ex))
        
    return {"messages": [response.content]}

    
def summary_agent(AgentState):
    
    try:
        
        messages = AgentState['messages']
        data = messages
        data = str(data)   
        output = llm.invoke("Your task is to go through the extracted data of the patient for all the sections and then write a summary for this parient. The summary should be concise and precise. Please include patient's demographic information in the summary. Only respond with the summary and nothing else. Please don't include any new line character like \n or tab charater like \t in the summary. Data: " + data)
    except Exception as ex:
        print("Errors = {}".format(ex))

    return {"messages": [output.content]}


def save_summary(summary):
    
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 20)
        pdf.cell(200, 10, txt = "Summary of Patient EHR:", ln = 1, align = 'C')
    
        summary = str(summary).replace("Output from node Summary_agent:", "")
        summary = summary.replace("[", "")
        summary = summary.replace("]", "")
        summary = summary.replace("'Here is the summary:", "")
        summary = summary.replace("'", "")
        
        summary_list = summary.split("\n")

        pdf.set_font("Arial", size = 15)
        for text in summary_list:
            
            text = str(text).replace("\n", "")
            pdf.multi_cell(200, 10, txt = text, align = 'L')
        pdf.output("patient_summary.pdf")

    except Exception as ex:
        print("Errors = {}".format(ex))



def main():

    st.title("AI App for the Summarization of Electronic Health Record of Patient")
    html_temp = """
    <div style="background-color:orange;padding:9px">
    <h3 style="color:blue;text-align:center;">Summarization of Electronic Health Record (EHR) of Patient with Multi-agent workflows with LangGraph, Langchain and Llama3 model</h3>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    st.markdown("""

        <style>
            .stFileUploader label {
                font-size: 40px; /* Adjust font size as needed */
            }

        </style>

    """, unsafe_allow_html=True)

    pdf_file = st.file_uploader("Upload Patient EHR", type=["pdf"])
    
    if ((pdf_file is not None) and ('pdf' in str(pdf_file))):
        bytes_data = pdf_file.read()
        
        with open("patient_EHR.pdf", 'wb') as f: 
            f.write(bytes_data)
            f.close()
        
    
    if st.button("Summarize Patient EHR"):

        inputs = {"messages": ["Your are a healthcare/medical expert and your goal is to summarize a patient's health records with current status of health/medical problems and their treatments or treatment plans"]}
        
        workflow = StateGraph(AgentState)
        
        workflow.add_node("Patient_agent", patient_agent)
        workflow.add_node("Demographic_agent", demographic_agent)
        workflow.add_node("Diagnosis_agent", diagnosis_agent)
        workflow.add_node("Vitals_agent", vitals_agent)
        workflow.add_node("Immunization_agent", immunization_agent)
        workflow.add_node("Family_history_agent", family_history_agent)
        workflow.add_node("Social_history_agent", social_history_agent)
        workflow.add_node("PMH_agent", pmh_agent)
        workflow.add_node("PSH_agent", psh_agent)
        workflow.add_node("Encounter_progress_notes_agent", enc_progress_notes_agent)
        workflow.add_node("Summary_agent", summary_agent)
        workflow.set_entry_point("Patient_agent")
        workflow.add_edge("Patient_agent", "Demographic_agent")
        workflow.add_edge("Patient_agent", "Diagnosis_agent")
        workflow.add_edge("Patient_agent", "Vitals_agent")
        workflow.add_edge("Patient_agent", "Immunization_agent")
        workflow.add_edge("Patient_agent", "Family_history_agent")
        workflow.add_edge("Patient_agent", "Social_history_agent")
        workflow.add_edge("Patient_agent", "PMH_agent")
        workflow.add_edge("Patient_agent", "PSH_agent")
        workflow.add_edge("Patient_agent", "Encounter_progress_notes_agent")       
        workflow.add_edge("Demographic_agent", "Summary_agent")
        workflow.add_edge("Diagnosis_agent", "Summary_agent")        
        workflow.add_edge("Vitals_agent", "Summary_agent")
        workflow.add_edge("Immunization_agent", "Summary_agent")
        workflow.add_edge("Family_history_agent", "Summary_agent")
        workflow.add_edge("Social_history_agent", "Summary_agent")
        workflow.add_edge("PMH_agent", "Summary_agent")
        workflow.add_edge("PSH_agent", "Summary_agent")
        workflow.add_edge("Encounter_progress_notes_agent", "Summary_agent")
        
        workflow.add_edge("Summary_agent", END)
        app = workflow.compile()        

        img = app.get_graph().draw_mermaid_png()
        with open("workflows.png", "wb") as f:
            f.write(img)
        filename = "workflows.png"        
        st.image(load_image(filename))

        outputs = app.stream(inputs)
        results = []
        for output in outputs:
            for key,value in output.items():
                
                results.append("Output from node "+str(key)+":  "+str(value['messages']) + "  ")
            
        summary = results[-1]

        save_summary(summary)

        st.success('Results: {}'.format(str(results)))


        
if __name__=='__main__':
    main()


