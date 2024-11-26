import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, Trainer, TrainingArguments
from datasets import Dataset, DatasetDict
from sentence_transformers import SentenceTransformer
import faiss

# Define fine-tuning data
fine_tune_data = [
    {
        "context": "Patients should rest for 24 hours after surgery, avoid heavy lifting, and take prescribed medication.",
        "question": "What are the post-surgery instructions?",
        "answers": {"text": ["rest for 24 hours after surgery"], "answer_start": [8]},
    },
    {
        "context": "Fever can be managed by using a cold compress, staying hydrated, and taking acetaminophen.",
        "question": "How to manage fever?",
        "answers": {"text": ["use a cold compress"], "answer_start": [23]},
    },
    {
        "context": "Symptoms of a heart attack include chest pain, shortness of breath, and discomfort in the upper body.",
        "question": "What are the symptoms of a heart attack?",
        "answers": {"text": ["chest pain, shortness of breath"], "answer_start": [34]},
    },
]

# Load the data into a Dataset object
dataset = Dataset.from_list(fine_tune_data)

# Initialize tokenizer and model for fine-tuning
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased")


# Check if MPS (Metal Performance Shaders) is available
device = "mps" if torch.backends.mps.is_available() else "cpu"
model.to(device)

# Tokenize data
def preprocess_data(examples):
    inputs = tokenizer(
        examples["question"],
        examples["context"],
        truncation=True,
        padding="max_length",
        max_length=128,
    )
    answer_starts = examples["answers"]["answer_start"][0]
    answer_text = examples["answers"]["text"][0]
    answer_ends = answer_starts + len(answer_text)
    start_positions = inputs.char_to_token(answer_starts)
    end_positions = inputs.char_to_token(answer_ends - 1)
    if start_positions is None:
        start_positions = tokenizer.model_max_length
    if end_positions is None:
        end_positions = tokenizer.model_max_length
    inputs.update({"start_positions": start_positions, "end_positions": end_positions})
    return inputs


# Apply preprocessing
tokenized_data = dataset.map(preprocess_data)

# Prepare dataset
train_dataset = DatasetDict({"train": tokenized_data})

# Training arguments
training_args = TrainingArguments(
    output_dir="./fine_tuned_model",
    evaluation_strategy="no",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    save_strategy="no",
    logging_dir='./logs',
    no_cuda=True,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset["train"],
    tokenizer=tokenizer
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
model.save_pretrained("fine_tuned_hospital_model")
tokenizer.save_pretrained("fine_tuned_hospital_model")

