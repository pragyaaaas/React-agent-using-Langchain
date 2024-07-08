from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage 
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI (model="gpt-4")
query = "Who is Katy Pery"
messages = [
    SystemMessage(content="you're a helpful assistant"),
    HumanMessage (content=query)
]

result = llm.invoke(messages)
print(result)