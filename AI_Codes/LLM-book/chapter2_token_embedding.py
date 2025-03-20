from transformers import AutoModel, AutoTokenizer
from transformers.agents.tools import Tool
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import faiss
import numpy as np


class TextEmbedding:

    def __init__(self):
        self.model = None
        self._initialise_model()

    @staticmethod
    def _tokenizer_model_contextual(self):
        # Text embedding for words with contextual embedding
        tokenizer = AutoTokenizer.from_pretrained("microsoft/deberta-base")
        model = AutoModel.from_pretrained("microsoft/deberta-v3-xsmall")

        tokens = tokenizer("Hello world", return_tensors="pt")
        # tokens = [CLS][Hello][world][SEP]

        output = model(**tokens)
        print(output)

    def _initialise_model(self):
        # Text embeddings for sentence
        self.model = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

    def _perform_embedding(self):
        # convert text to text embedding
        vector = self.model.encode("Best movie ever")
        print(vector)

    def _find_cosine_similarity(self):
        # finding similar sentences
        sentence1 = "I love programming in python"
        sentence2 = "Python is my favorite programming language"

        # encode sentences
        embedding1 = self.model.encode([sentence1])
        embedding2 = self.model.encode([sentence2])

        # compute cosine similarity
        similarity = cosine_similarity(embedding1, embedding2)
        print(f"Similarity score: {similarity[0][0]:.4f}")

    def _text_clustering(self):
        sentences = [
            "I love programming in Python.",
            "Machine learning is amazing.",
            "Python is great for data science.",
            "I enjoy deep learning projects.",
            "Data science is an exciting field."
        ]

        embedding = self.model.encode(sentences)

        # apply K means clustering
        num_clusters = 2
        kmeans = KMeans(n_clusters=num_clusters, random_state=42)
        kmeans.fit(embedding)

        # Print cluster assignments
        for sentence, cluster in zip(sentences, kmeans.labels_):
            print(f"Sentence: {sentence} -> Cluster: {cluster}")

    def _retrieval_with_FAISS(self):
        # FAISS helps efficiently search similar text in a large dataset.
        # Encode sentences
        sentences = [
            "I love programming in Python.",
            "Machine learning is amazing.",
            "Python is great for data science.",
            "I enjoy deep learning projects.",
            "Data science is an exciting field."
        ]
        embeddings = self.model.encode(sentences)
        dimension = embeddings.shape[1]

        # Create FAISS index
        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(embeddings))

        # Query sentence
        query = "What is the best programming language?"
        query_embedding = self.model.encode([query])

        # Search in the index
        D, I = index.search(query_embedding, k=2)  # Top-2 closest sentences

        # Print results
        print("Query:", query)
        print("Best matches:")
        for idx in I[0]:
            print(sentences[idx])


if __name__ == "__main__":
    tEmbd = TextEmbedding()
    tEmbd._find_cosine_similarity()
    tEmbd._text_clustering()
    tEmbd._retrieval_with_FAISS()



