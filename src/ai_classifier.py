import os
import requests
import json
from dotenv import load_dotenv

# Puxa a chave de segurança .env
load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY")

# Configuraçao do modelo - OPENROUTER
# Para usar modelos pagos (GPT-4, Claude), basta trocar a string abaixo.
# Modelos gratuitos atuais: "google/gemini-2.0-flash-lite-preview-02-05:free", "meta-llama/llama-3-8b-instruct:free"

MODELO_IA = "openrouter/free"

def classificar_email(texto_email): 
    url = "https://openrouter.ai/api/v1/chat/completions"

    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODELO_IA,
        "messages": [
            {
                "role": "system",
                "content": "Você é um assistente de RH focado em triagem. Analise o e-mail e responda APENAS com uma destas palavras exatas: ADMISSAO, RESCISAO, FOLHA_PONTO ou DESCONHECIDO. Não dê explicações e nao use pontuação."
            },
            {
                "role": "user",
                "content": texto_email
            }
        ]
    }

    try:
        # 3. O carteiro enviando a carta: fazemos um pedido POST
        resposta = requests.post(url, headers=headers, data=json.dumps(payload))
        dados = resposta.json()
        
        # --- MODO DETETIVE (Novo) ---
        # Se a palavra 'choices' não estiver na resposta, algo deu errado
        if 'choices' not in dados:
            print("❌ O OpenRouter recusou o nosso pedido! Veja o motivo exato:")
            print(dados)  # Imprime a mensagem de erro que o servidor mandou
            return "ERRO_NA_API"
        # ----------------------------
        
        # Navega nas pastas do JSON para pegar apenas o texto final
        classificacao = dados['choices'][0]['message']['content'].strip()
        return classificacao.upper()
        
    except Exception as erro:
        print(f"Erro no código Python: {erro}")
        return "ERRO"
    
# Area de teste local (so roda se este arquivo for executado diretamente)
if __name__ == "__main__":
    print("Iniciando o Cérebro da Operação...\n")

    email_teste_1 = "Olá, gostaria de saber como faço para dar entrada no meu aviso prévio, vou sair da empresa no mês que vem e preciso me planejar"
    print(f"Mensagem do E-mail 1: {email_teste_1}")
    resultado_1 = classificar_email(email_teste_1)
    print(f"Veredito da IA -> {resultado_1}\n")
    print("-" * 50)

    email_teste_2 = "Bom dia, segue em anexo os documentos e o exame admissional do novo funcionário João para a vaga de vendedor."
    print(f"Mensagem do E-mail 2: {email_teste_2}")
    resultado_2 = classificar_email(email_teste_2)
    print(f"Veredito da IA -> {resultado_2}\n")

