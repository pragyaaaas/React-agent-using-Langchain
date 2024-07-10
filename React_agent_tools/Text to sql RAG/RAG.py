from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor, create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_types import AgentType
from tools.time import check_system_time
from tools.weather import get_weather
from tools.wikipedia import search_wikipedia
from tools.maths import calculate

load_dotenv()

llm = ChatOpenAI(temperature=0, model="gpt-4")

database = 'postgres'
username = 'postgres'
password = 'root'
host = 'localhost'
port = '5432'

db_uri = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
db = SQLDatabase.from_uri(db_uri)
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

sql_agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

prompt_template = hub.pull("hwchase17/react")
tools = [check_system_time, get_weather, search_wikipedia, calculate]
react_agent = create_react_agent(llm, tools, prompt_template)
react_agent_executor = AgentExecutor(agent=react_agent, tools=tools, verbose=True)

def handle_query(query):
    if "salary" in query or "employee" in query or "database" in query:
        return sql_agent.run(query)
    else:
        return react_agent_executor.invoke({"input": query})

query = "Name of the employee with highest salary?"
result = handle_query(query)
print("Result:", result)

