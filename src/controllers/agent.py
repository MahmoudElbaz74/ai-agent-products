from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from src.models.embedding import load_and_embed_data
from dotenv import load_dotenv
import os

load_dotenv()

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant specialized in answering product questions.

1. Understand the user's question in English or Arabic.
2. If it's in Arabic, translate it internally to English for processing.
3. Search the product context for relevant information.
4. Generate the answer in fluent, formal Arabic.

Context: {context}

Question: {query}

Chat History: {chat_history}
""")

chat_history = []

def ask_question(query: str):
    retriever = load_and_embed_data().as_retriever(search_kwargs={"k": 5})
    docs = retriever.get_relevant_documents(query)
    context = "\n".join([doc.page_content for doc in docs])

    model = ChatOpenAI(
        model="mistralai/mistral-7b-instruct",
        openai_api_key=os.environ.get("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        max_tokens=2000,
        temperature=0.2
    )

    chat_history.append(f"User {query}")
    response = prompt | model
    answer = response.invoke({"context": context, "query": query, "chat_history": "\n".join(chat_history)}).content
    chat_history.append(f"Agent {answer}")
    return answer