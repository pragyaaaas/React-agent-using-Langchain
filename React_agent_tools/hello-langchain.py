from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from tools.system_time_tool import check_system_time
from tools.weather import get_weather
from tools.news import get_latest_news
from tools.wikipedia import search_wikipedia
from tools.maths import calculate


load_dotenv()

llm = ChatOpenAI(model="gpt-4")

query = "What is 2+2?"
prompt_template = hub.pull("hwchase17/react")



tools = [check_system_time, get_weather,search_wikipedia,calculate,get_latest_news]
agent = create_react_agent(llm, tools, prompt_template)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = agent_executor.invoke({"input": query})
print(result)
