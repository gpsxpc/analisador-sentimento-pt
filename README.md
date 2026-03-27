# 📊 Analisador de Sentimentos em Português

> **Versão:** 1.0.0

Projeto de código aberto que utiliza um modelo BERT multilingual pré-treinado para classificar o sentimento de um texto em português, retornando uma pontuação de 1 a 5 estrelas (como avaliações de clientes).

> ✅ Disponível no Hugging Face Spaces: [Clique para testar](https://huggingface.co/spaces/gpsxpc/analisador-sentimento-pt)

---

## 🔧 Tecnologias
- Python
- Hugging Face Transformers
- Gradio
- Torch (backend PyTorch)
- Hugging Face Spaces (hospedagem gratuita)

---

## 📌 Funcionalidades
- Aceita qualquer texto em português como entrada
- Classifica o sentimento utilizando um modelo BERT multilingual
- Exibe pontuações de probabilidade de 1 a 5 estrelas
- Roda completamente no navegador (interface Gradio)

---

## 📁 Estrutura do Projeto

```
├── app.py              # Código principal da aplicação
├── requirements.txt    # Dependências para o Hugging Face Spaces
└── README.md           # Documentação do projeto
```

---

## 🚀 Como Executar Localmente

### Pré-requisitos

Instale as dependências necessárias:

```bash
pip install gradio transformers torch
```

### Executando

```bash
python app.py
```

Em seguida, acesse: [http://localhost:7860](http://localhost:7860)

---

## 🧠 Créditos

- **Modelo:** [nlptown/bert-base-multilingual-uncased-sentiment](https://huggingface.co/nlptown/bert-base-multilingual-uncased-sentiment)
- **Interface:** [Gradio](https://gradio.app/)

---

## 📬 Contato

Fique à vontade para se conectar via [LinkedIn](https://www.linkedin.com/in/gabrielxpc/) ou abrir uma *issue*!

---

## 📝 Licença

Este projeto está sob a Licença MIT.

