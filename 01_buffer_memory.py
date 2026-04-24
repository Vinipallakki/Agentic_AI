from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory

load_dotenv()

# Stores raw history
memory = ConversationBufferMemory()
agent = ConversationChain(llm=llm, memory=memory, verbose=True)

print(agent.predict(input="My name is Vinayaka. I'm building a saas app."))
print(agent.predict(input="What am I building?"))