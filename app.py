from flask import Flask, render_template, request
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch

app = Flask(__name__)

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("tokenizer")
model = AutoModelForSeq2SeqLM.from_pretrained("pegasus-samsum-model")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        input_text = request.form['input_text']
        
        # Tokenize input text
        input_text_encoded = tokenizer(input_text, return_tensors="pt", max_length=1024, truncation=True, padding=True)
        input_text_encoded = input_text_encoded.to(device)
        
        # Generate summary
        summary_ids = model.generate(input_text_encoded.input_ids, 
                                     max_length=128, 
                                     num_beams=8, 
                                     length_penalty=0.8, 
                                     early_stopping=True)
        
        # Decode and return summary
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        
        return render_template('index.html', input_text=input_text, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
