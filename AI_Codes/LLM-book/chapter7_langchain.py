"""
# Use of langchain and LlamaCpp[run locally with cpu or GPU, both]


"""

from langchain import LLMChain, PromptTemplate
from langchain_community.llms import LlamaCpp


class Langchain:
    def __init__(self):
        self._model = self._initialise_model()

    def _initialise_model(self):
        return LlamaCpp(
            model_path="./model_dir/Phi-3-mini-4k-instruct-fp16.gguf",
            n_gpu_layers=-1,
            max_tokens=500,
            n_batch=512,
        )

    def invoke_model(self, query):
        template = f"""<s><|user|>
        {query}<|end|>
        <|assistant|>"""
        resp = self._model.invoke(template)
        print(f"_sahil - Model output = {resp}")

    def _generate_prompt_template(self):
        template = """<s><|user|>
            {query}<|end|>
        <|assistant|>"""
        return PromptTemplate(template=template, input_variables=["query"])

    def basic_chain(self, query):
        prompt = self._generate_prompt_template()
        basic_chain = prompt | self._model
        resp = basic_chain.invoke({"query": query})
        print(f"basic_chain output - {resp}")

    def multiple_chain(self):
        # create a chain for title of our story
        template = """<s><|user|>
        Create a title for a story about {summary}. Only return the title.<|end|>
        <|assistant|>"""
        title_prompt = PromptTemplate(template=template, input_variables=["summary"])
        title = LLMChain(llm=self._model, prompt=title_prompt, output_key="title")

        # title.invoke({"summary": "a girl that lost her mother"})    # we can check the response for title here

        # create a chain for character description using summary and title
        template = """<s><|user|>
        Describe the main character of a story about {summary} with the title {title}. Use only two sentences.<|end|>
        <|assistant|>"""
        character_prompt = PromptTemplate(template=template, input_variables=["summary", "title"])
        character = LLMChain(llm=self._model, prompt=character_prompt, output_key="character")

        # Create a chain for the story using the summary, title, and character description
        template = """<s><|user|>
        Create a story about {summary} with the title {title}. The main character is: {character}. Only return the story and it cannot be longer than one paragraph<|end|>
        <|assistant|>"""
        story_prompt = PromptTemplate(template=template, input_variables=["summary", "title", "character"])
        story = LLMChain(llm=self._model, prompt=story_prompt, output_key="story")

        llm_chain = title | character | story

        resp = llm_chain.invoke("a girl that lost her mother")
        print(resp)


query = "Hi, my name is matrix, what is 1+1?"
Lg = Langchain()
# Lg.invoke_model(query)
# Lg.basic_chain(query)
Lg.multiple_chain()
