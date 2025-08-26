import gradio as gr
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name= "nlptown/bert-base-multilingual-uncased-sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

def analisar_sentimento(texto):
    inputs = tokenizer(texto, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        scores = torch.nn.functional.softmax(outputs.logits, dim=1)[0]
        sentimentos = ["1 estrela", "2 estrelas", "3 estrelas", "4 estrelas", "5 estrelas"]
        resultado = {sentimentos[i]: float(scores[i]) for i in range(len(scores))}
    return resultado

interface = gr.Interface(fn=analisar_sentimento,
             inputs=gr.Textbox(lines=3, label="Digite um texo"), 
             outputs="label",
             title= "Analisador de Sentimentos (Português)",
             description="Este modelo classifica o sentimento de 1 a 5 estrelas."
             )

interface.launch()