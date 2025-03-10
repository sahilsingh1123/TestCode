from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch
# import AutoModelForCasualLLM = since we are using traditional LLMs which generates text from left to right
# AutoModel = This can be used in case where we just want the embedding output not the generated text
# AutoTokenizer = It automatically picks the valid tokenizer and its mechanism without the manual intervention
# (word or sentence....)


def _run_pipeline(model, tokenizers, query):
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

def _run_manually(model, tokenizers, query):
    # we need to specify the device if we are using apple chips in tokenizer
    device = torch.device("mps")    # I guess we can use this to find device dynamically as well
    tokens = tokenizers(query, return_tensors="pt").to(device)
    output_tokens = model.generate(**tokens, max_new_tokens=500, do_sample=False)
    output_text = tokenizers.decode(output_tokens[0], skip_special_tokens=True)
    return output_text


def run_model(query):
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/Phi-3-mini-4k-instruct",
        device_map="mps",
        torch_dtype="auto",
        trust_remote_code=True,
        attn_implementation="eager"
    )
    tokenizers = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

    # There are two ways to get text generation done
    # 1 - By using pipeline - which handles everything, without manual intervention
    # 2 - By manual process - where we need to manually apply everything and decode it at the end
    # details = _run_pipeline(model, tokenizers, query)
    details = _run_manually(model, tokenizers, query)
    return details


if __name__ == "__main__":
    query = "Brief me about how ukraine war started"
    print(run_model(query))

