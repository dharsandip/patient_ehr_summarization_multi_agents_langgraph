In this project, an AI Application with Multi-agent workflows has been build in Python for a real world Healthcare case (Summarization of Electronic Health Record of Patient) with Langchain, LangGraph and Llama3 model (Open Source LLM) through Groq. Also used streamlit library, PyPDFLoader etc.. In the App, user only needs to upload the Patient's Electronic Health Record (EHR) in pdf format which contains the medical/health history of the patient for many years.
Then they just need to click on "Summarize Patient EHR" button. It will display the LangGraph multi-agent workflows graphically with all the nodes and edges there
and also then it will execute it and show the results. It will show the output messages from all the nodes (agents) so
that one can get a complete picture apart from the final summary of the patient's EHR. It will also write and save a copy of the summary in pdf
in the working directory.  

Following are the nodes (AI agents) and their roles in this multi-agent workflows:

Patient agent: It is the entry point. It just displays a message "Summarization of EHR of Patient by Generative AI".
Demographic agent: It extracts name and demographic information of the patient from EHR
Diagnosis agent: It extracts diagnosis information of the patient from EHR
Immunization agent: It extracts immunization information of the patient from EHR
PMH agent: It extracts Past Medical History information of the patient from EHR
PSH agent: It extracts Past Surgical History information of the patient from EHR
Vitals agent: It extracts vital signs information of the patient from EHR
Family history agent: It extracts family history information of the patient from EHR
Social history agent: It extracts social history information of the patient from EHR
Encounter progress notes agent: It extracts Encounter progress notes or Doctors visit information of the patient from EHR
Summary agent: It summarizes the patient EHR based on the section wise medical information that it receives from all other nodes.


Steps to setup and run:

1. Create your python environment

2. Install the dependencies (pip install -r requirements.txt)

3. Go to https://console.groq.com/keys, sign up and get your free API key for Groq and set the
   environment variable for the api key (GROQ_API_KEY) in your .env file and keep it in the working directory.
   Sample .env is provided in this GitHub repo.

4. Go to your working directory from console (command prompt), type and run:    streamlit run healthcare_multi_agents_langgraph_llama3.py

5. Streamlit App will be launched


