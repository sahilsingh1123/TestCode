import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, Trainer, TrainingArguments
from datasets import Dataset, DatasetDict
from sentence_transformers import SentenceTransformer
import faiss

# ---------------- Import fine tuned model ------------#
# Load fine-tuned model
model = AutoModelForQuestionAnswering.from_pretrained("fine_tuned_hospital_model")
tokenizer = AutoTokenizer.from_pretrained("fine_tuned_hospital_model")

# Check if MPS (Metal Performance Shaders) is available
device = "mps" if torch.backends.mps.is_available() else "cpu"
model.to(device)

# --------------- RAG Setup --------------- #

# Sample RAG data (for embedding and retrieval)
rag_data = [
    {"id": 1, "text": "After surgery, patients should avoid strenuous activity for 2 weeks."},
    {"id": 2, "text": "A fever can be controlled with hydration and antipyretics."},
    {"id": 3, "text": "Heart attack symptoms include chest pain and shortness of breath."},
]

# Load embedding model for FAISS
embedder = SentenceTransformer("all-MiniLM-L6-v2")
texts = [doc["text"] for doc in rag_data]
embeddings = embedder.encode(texts, convert_to_tensor=True)

# Initialize FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings.cpu().detach().numpy())  # Move embeddings to CPU for indexing


# Function to retrieve relevant documents based on query
def get_relevant_docs(query, k=1):
    query_embedding = embedder.encode([query], convert_to_tensor=True)
    query_embedding = query_embedding.cpu().detach().numpy()
    distances, indices = index.search(query_embedding, k)
    return [(rag_data[idx]["text"], distances[0][i]) for i, idx in enumerate(indices[0])]


# --------------- QA with RAG Integration --------------- #

def answer_query(query):
    # RAG retrieval
    relevant_docs = get_relevant_docs(query, k=1)
    context = " ".join([doc for doc, _ in relevant_docs])

    # Tokenize query with RAG context
    inputs = tokenizer(query, context, return_tensors="pt", max_length=256, truncation=True)
    inputs = {k: v.to(device) for k, v in inputs.items()}

    # Generate answer
    outputs = model(**inputs)
    start_logits = outputs.start_logits
    end_logits = outputs.end_logits
    answer_start = torch.argmax(start_logits)
    answer_end = torch.argmax(end_logits) + 1

    answer = tokenizer.convert_tokens_to_string(
        tokenizer.convert_ids_to_tokens(inputs["input_ids"][0]))

    print(f"Query: {query}")
    print(f"Answer: {answer}")
    print(f"Context Used: {context}")
    return answer


# Example usage
query = "How to manage fever and heart attack?"
answer_query(query)
