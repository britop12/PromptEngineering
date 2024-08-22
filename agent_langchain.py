from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType
import pandas as pd
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def main():
    st.set_page_config(page_title="Ask your SpreadSheet", page_icon="📊")
    st.header("Pregunta sobre tus datos 📊")
    
    # upload file
    data = st.file_uploader("Sube tu SpreadSheet", type=["xlsx", "csv"])
    
    # extract the text
    if data is not None:
      if data.name.endswith('.csv'):
        df = pd.read_csv(data)
      else:
        df = pd.read_excel(data)

      # Create the instance of the model
      llm = ChatOpenAI(
          model_name="gpt-3.5-turbo-16k",
          temperature=0)
      
      # Initialize the agent
      agent_pd = create_pandas_dataframe_agent(
        llm, df, verbose=True, allow_dangerous_code=True, agent_type=AgentType.OPENAI_FUNCTIONS
      )
      # show user input
      user_question = st.text_input("Haz tu pregunta:")
      if user_question:
        # invoke the agent
        response = agent_pd.invoke(user_question)
        st.write(response["output"])
    

if __name__ == '__main__':
    main()
