import json
import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document

load_dotenv()

def load_and_embed_data():
    with open("src/interfaces/products.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    docs = [
    Document(
        page_content=(
            f"Title: {item.get('title', '')}. "
            f"Description: {item.get('description', '')}. "
            f"Brand: {item.get('brand', 'Unknown')}. "
            f"Price: {item.get('price', 'N/A')} USD. "
            f"Discount: {item.get('discountPercentage', 0)}%. "
            f"Rating: {item.get('rating', 'N/A')}/5. "
            f"Availability: {item.get('availabilityStatus', 'N/A')}. "
            f"Warranty: {item.get('warrantyInformation', 'N/A')}. "
            f"Return Policy: {item.get('returnPolicy', 'N/A')}. "
            f"Shipping: {item.get('shippingInformation', 'N/A')}. "
            f"Top Review: {item.get('reviews', [{}])[0].get('comment', 'No reviews')}."
        )
    )
    for item in data if item.get("description", "").strip() != ""
]


    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    db = Chroma.from_documents(docs, embeddings, persist_directory="vectors")
    db.persist()
    return db