from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


def run_model(query):
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/Phi-3-mini-4k-instruct",
        device_map="mps",
        torch_dtype="auto",
        trust_remote_code=True,
        attn_implementation="eager"
    )
    tokenizers = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")
    generator = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizers,
        return_full_text=False,
        max_new_tokens=500,
        do_sample=False
    )

    messages = [
        {"role": "user", "content": query}
    ]
    output = generator(messages)
    return output[0]["generated_text"]

if __name__ == "__main__":
    query = "Brief me about how ukraine war started"
    print(run_model(query))

