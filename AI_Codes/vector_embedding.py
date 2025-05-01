import torch
import weaviate
from transformers import AutoModel, AutoTokenizer

# Connect to Weaviate instance
client = weaviate.Client(
    url="https://odrxnpqqrto0rsivtpmw.c0.asia-southeast1.gcp.weaviate.cloud",  # Your Weaviate cluster URL
    auth_client_secret=weaviate.AuthApiKey("5p7OJmfqBIpCKm7f4zG1uc51gjJ76bHlmnFQ"),  # API Key for auth
)

# Define schema for Weaviate
schema = {
    "classes": [
        {
            "class": "Document",
            "description": "A class for storing text documents and their embeddings",
            "properties": [
                {"name": "text", "dataType": ["text"], "description": "The original document text"},
                {"name": "embedding", "dataType": ["number[]"], "description": "The document's embedding vector"},
            ],
            "vectorizer": "none",  # Disabling Weaviate's built-in vectorizer
        }
    ]
}

# Create schema if it doesn't already exist
try:
    client.schema.create(schema)
except Exception as e:
    print("Exception while creating schema")
# Load pre-trained transformer model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")


# Function to get embedding from text
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embedding = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return embedding


# Function to add a document to Weaviate
def add_document_to_weaviate(text):
    embedding = get_embedding(text)

    client.data_object.create(
        {"text": text, "embedding": embedding.tolist()}, class_name="Document"  # Convert embedding to list format
    )


# Function to search similar documents using vector search
def search_similar_documents(query_text, limit=3):
    query_embedding = get_embedding(query_text)

    results = (
        client.query.get("Document", ["text"]).with_near_vector({"vector": query_embedding}).with_limit(limit).do()
    )

    return results["data"]["Get"]["Document"]


# Example usage
if __name__ == "__main__":
    # Add a document to Weaviate
    add_document_to_weaviate("AI is dominating the world")

    # Search for similar documents
    search_results = search_similar_documents("AI is dominating the globe", limit=3)
    for result in search_results:
        print(result["text"])
