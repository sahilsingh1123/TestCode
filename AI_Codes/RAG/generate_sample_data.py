import json

# Sample data for fine-tuning in JSON format
fine_tune_data = [
    {"question": "What are the post-surgery instructions?", "answer": "Patients should rest for 24 hours, avoid heavy lifting, and take prescribed pain medication."},
    {"question": "How to manage fever?", "answer": "Use a cold compress, ensure hydration, and take fever-reducing medications like acetaminophen."},
    {"question": "What are the symptoms of a heart attack?", "answer": "Symptoms include chest pain, shortness of breath, and discomfort in the upper body."},
]

# Saving this to a JSON file
with open('hospital_fine_tune_data.json', 'w') as f:
    json.dump(fine_tune_data, f)
