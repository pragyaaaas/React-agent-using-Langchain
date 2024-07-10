from dotenv import load_dotenv
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI

load_dotenv()

database='postgres'
username='postgres'
password='root'
host='localhost'
port='5432'

db_uri = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

db = SQLDatabase.from_uri(db_uri)

llm = ChatOpenAI(temperature=0,model="gpt-4")

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

db_agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

db_agent.run("Name of the employee with highest salary")