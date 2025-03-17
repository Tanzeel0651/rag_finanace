from langchain.schema import Document
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory

from dotenv import load_dotenv
import os
import pandas as pd
import gradio as gr

MODEL = "gpt-4o-mini"
db_name = "vector_db"

load_dotenv(override=True)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


## Handling Data
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

## process text
with open("data/financial_summaries.txt", "r") as file:
    financial_summaries = file.read()

summary_chunks = text_splitter.split_text(financial_summaries)
print(f"Financial summaries split into {len(summary_chunks)} chunks.")

## process numerical csv data
def convert_csv_to_text(file_path):
    df = pd.read_csv(file_path)
    text_chunks = []

    for index, row in df.iterrows():
        row_text = ", ".join([f"{col}: {row[col]}" for col in df.columns])
        text_chunks.append(row_text)

    return text_chunks


income_text = convert_csv_to_text("data/income_statement.csv")
balance_text = convert_csv_to_text("data/balance_sheet.csv")
cash_flow_text = convert_csv_to_text("data/cash_flow_statement.csv")

all_chunks = summary_chunks + income_text + balance_text + cash_flow_text

print(f"Total financial document chunks: {len(all_chunks)}")


embeddings = OpenAIEmbeddings()

if os.path.exists(db_name):
    Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()


document_objects = []
for chunk in all_chunks:
    doc = Document(page_content=chunk, metadata={"source":"financial_data"})
    document_objects.append(doc)

vectorstore = Chroma.from_documents(
        documents=document_objects,
        embedding=embeddings,
        persist_directory=db_name)

print(f"VectorStore created with {vectorstore._collection.count()} documents")

collection = vectorstore._collection
count = collection.count()

sample_embedding = collection.get(limit=1, include=["embeddings"])["embeddings"][0]
dimensions = len(sample_embedding)
print(f"There are {count:,} vectors with {dimensions:,} dimensions in the vector store")

llm = ChatOpenAI(temperature=0.7, model_name=MODEL)

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

retriever = vectorstore.as_retriever()

conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=retriever, memory=memory)

# question as a query
query = "What was the company's revenue in 2023?"
result = conversation_chain.invoke({"question": query})
print(result["answer"])

## gradio implement
def chat(question, history):
    result = conversation_chain.invoke({"question":question})
    return result["answer"]

view = gr.ChatInterface(chat, type="messages").launch(inbrowser=True)



