from transformers import AutoModelForCausalLM, AutoTokenizer


def _tokenizer():
    # Load model and tokenizer
    model = AutoModelForCausalLM.from_pretrained(
        "microsoft/Phi-3-mini-4k-instruct",
        device_map="mps",
        torch_dtype="auto",
        trust_remote_code=True,
    )
    tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

    prompt = "Hi this is sahil singh, how may i guide you in this matter"

    input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to("mps")

    # generate the text
    generation_output = model.generate(input_ids=input_ids, max_new_tokens=20)

    print(tokenizer.decode(generation_output[0]))


def show_tokens(sentence, tokenizer_name):
    colors_list = ["102;194;165", "252;141;98", "141;160;203", "231;138;195", "166;216;84", "255;217;47"]
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    token_ids = tokenizer(sentence).input_ids
    for idx, t in enumerate(token_ids):
        print(f"\x1b[0;30;48;2;{colors_list[idx % len(colors_list)]}m" + tokenizer.decode(t) + "\x1b[0m", end=" ")


## Call Methods
text = """
English and CAPITALIZATION
🎵 鸟
show_tokens False None elif == >= else: two tabs:"    " Three tabs: "       "
12.0*50=600
"""

# _tokenizer()
models = ["bert-base-cased", "microsoft/Phi-3-mini-4k-instruct", "gpt2", "Xenova/gpt-4"]
show_tokens(text, "Xenova/gpt-4")
