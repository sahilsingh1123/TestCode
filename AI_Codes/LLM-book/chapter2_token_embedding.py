from transformers import AutoModel, AutoTokenizer
from transformers.agents.tools import Tool

# Text embedding for words
tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-base")
model = AutoModel.from_pretrained("microsoft/deberta-v3-xsmall")

tokens = tokenizer("Hello world", return_tensors="pt")

output = model(**tokens)
print(output)

# Text embeddings for sentence
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

# convert text to text embedding
vector = model.encode("Best movie ever")
