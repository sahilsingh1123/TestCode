from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


class InsideLLM:
    def __init__(self):
        self._model_name = "microsoft/Phi-3-mini-4k-instruct"
        self.tokenizer = self._initialise_tokenizer()
        self.model = self._initialise_model()
        self.generator = self._create_pipeline()

    def _initialise_tokenizer(self):
        return AutoTokenizer.from_pretrained(self._model_name)

    def _initialise_model(self):
        return AutoModelForCausalLM.from_pretrained(
            self._model_name, device_map="mps", torch_dtype="auto", trust_remote_code=True
        )

    def _create_pipeline(self):
        return pipeline(
            "text-generation",
            model=self.model,
            tokenizer=self.tokenizer,
            return_full_text=False,
            max_new_tokens=50,
            do_sample=False,
        )

    def visualise_input_output(self):
        prompt = "Write an email to HR for salary increment"
        output = self.generator(prompt)
        print(output[0]["generated_text"])
        print(self.model)

    def probability_distribution(self):
        prompt = "Capital of india is"

        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to("mps")

        # get the output of the model before the lm_head
        model_output = self.model.model(input_ids)

        # get the output of lm_head
        lm_head = self.model.lm_head(model_output[0])

        # fetch token id of the last element
        token_id = lm_head[0, -1].argmax(-1)
        answer = self.tokenizer.decode(token_id)
        print(answer)

    def model_with_cache(self):
        prompt = "write an email to HR for raise in salary. It should be in detail"
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids.to("mps")
        generated_output = self.model.generate(
            input_ids=input_ids,
            max_new_tokens=100,
            use_cache=True,  # default is True always [set False to see the difference]
        )


if __name__ == "__main__":
    llm = InsideLLM()
    # llm.visualise_input_output()
    # llm.probability_distribution()
    llm.model_with_cache()
