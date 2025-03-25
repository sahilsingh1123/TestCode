"""
RAG and semantic search
"""
import cohere
import numpy as np
import faiss
import pandas as pd

cohere_api_key = "vr6snVbxFmKcSBepcoyYOZhZNMoEXrWDcsLSIS05"

class SemanticSearch:
    def __init__(self):
        self._co = self._get_cohere_api_instance()
        self._texts = self._get_texts()
        self._embeds = self._embed_text_chunks()
        self._index = self._build_search_index()

    def _get_cohere_api_instance(self):
        return cohere.Client(cohere_api_key)

    def _get_texts(self):
        text = """
        Interstellar is a 2014 epic science fiction film co-written, directed, and produced by Christopher Nolan.
        It stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, Bill Irwin, Ellen Burstyn, Matt Damon, and Michael Caine.
        Set in a dystopian future where humanity is struggling to survive, the film follows a group of astronauts who travel through a wormhole near Saturn in search of a new home for mankind.

        Brothers Christopher and Jonathan Nolan wrote the screenplay, which had its origins in a script Jonathan developed in 2007.
        Caltech theoretical physicist and 2017 Nobel laureate in Physics[4] Kip Thorne was an executive producer, acted as a scientific consultant, and wrote a tie-in book, The Science of Interstellar.
        Cinematographer Hoyte van Hoytema shot it on 35 mm movie film in the Panavision anamorphic format and IMAX 70 mm.
        Principal photography began in late 2013 and took place in Alberta, Iceland, and Los Angeles.
        Interstellar uses extensive practical and miniature effects and the company Double Negative created additional digital effects.

        Interstellar premiered on October 26, 2014, in Los Angeles.
        In the United States, it was first released on film stock, expanding to venues using digital projectors.
        The film had a worldwide gross over $677 million (and $773 million with subsequent re-releases), making it the tenth-highest grossing film of 2014.
        It received acclaim for its performances, direction, screenplay, musical score, visual effects, ambition, themes, and emotional weight.
        It has also received praise from many astronomers for its scientific accuracy and portrayal of theoretical astrophysics. Since its premiere, Interstellar gained a cult following,[5] and now is regarded by many sci-fi experts as one of the best science-fiction films of all time.
        Interstellar was nominated for five awards at the 87th Academy Awards, winning Best Visual Effects, and received numerous other accolades"""

        # Split into a list of sentences
        texts = text.split('.')

        # Clean up to remove empty spaces and new lines
        return [t.strip(' \n') for t in texts]


    def _embed_text_chunks(self):
        response = self._co.embed(
            texts=self._texts,
            input_type="search_document",
        ).embeddings

        return np.array(response)
    def _build_search_index(self):
        dimension = self._embeds.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(np.float32(self._embeds))
        return index

    def search(self, query, number_of_results=3):
        # get the query embedding
        query_embed = self._co.embed(texts=[query], input_type="search_query").embeddings[0]

        # retrieve the nearest neighbors
        distances, similar_item_ids = self._index.search(np.float32([query_embed]), number_of_results)

        # format the results
        texts_np = np.array(self._texts)    # convert texts list to numpy for easier indexing
        results = pd.DataFrame(data={'texts': texts_np[similar_item_ids[0]],
                              'distance': distances[0]})
        # 4. Print and return the results
        print(f"Query:'{query}'\nNearest neighbors:")
        print(results)


ss = SemanticSearch()
ss.search("how precise was the science")
ss.search("what is the mass of moon?")