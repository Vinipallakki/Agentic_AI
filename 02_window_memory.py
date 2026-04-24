from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferWindowMemory

load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

# k=1: Remembers ONLY the literal last exchange
memory = ConversationBufferWindowMemory(k=1)
agent = ConversationChain(llm=llm, memory=memory, verbose=True)

agent.predict(input="I live in Tokyo.")
agent.predict(input="My colour is Blue.")

# Agent will likely FORGET the color because it's outside the window
print(agent.predict(input="where do i live?"))