from dotenv import load_dotenv
from langchain_classic.agents import initialize_agent
from langchain_classic.tools import Tool
from langchain_classic.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(temperature=0)

def calculator(expr):
    return str(eval(expr))

tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Useful for math calculations"
    )
]

memory = ConversationBufferMemory(memory_key="chat_history")

agent = initialize_agent(
    tools=tools,
    llm=llm,
    memory=memory,
    agent="zero-shot-react-description",
    verbose=True,
    handle_parsing_errors=True
)

agent.run("My name is Vinay")
agent.run("What is my name?")
agent.run("What is 10 + 5?")
agent.run("What is my name?")