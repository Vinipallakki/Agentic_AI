from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

load_dotenv()

vectorstore = FAISS.from_texts(
    ["User name is Vinay", "User likes AI","User lives in India",],
    embedding=OpenAIEmbeddings()
)

docs = vectorstore.similarity_search("What does user like?")
print(docs[0].page_content)