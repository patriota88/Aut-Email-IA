import os
import requests
from dotenv import load_dotenv

# Puxa a URL dentro do .env
load_dotenv()
WEBHOOK_URL = os.getenv("BITRIX_WEBHOOK_URL")

def criar_tarefa_bitrix(assunto, corpo, classificacao, email_destinatario):
    """ 
    Simula o envio de dados para criar uma tarefa no CRM via webhook
    """
    if not WEBHOOK_URL:
        print("❌ Erro: URL do Webhook nao configurada no .env!")
        return False
    
    # 1. Regra de Negocios
    # Defina quem vai cuidar da tarefa dependendo de qual e-mail recebeu a mensagem
    responsaveis = {
        "rh@empresa.com": "Maria (RH)",
        "financeiro@empresa.com": "Carlos (Financeiro)",
        "default": "Admin (Geral)"
    }

    # Pega o responsavel da lista. Se nao achar o e-mail, usa o 'default'
    responsavel_tarefa = responsaveis.get(email_destinatario, responsaveis["default"])

    # 2. Pacote de dados (payload)
    # Desta forma que o Bitrix24 ira receber as informaçoes para criar um "Card"
    payload = {
        "fields": {
            "TITLE": f"[{classificacao}] {assunto}",
            "DESCRIPTION": corpo,
            "RESPONSIBLE_ID": responsavel_tarefa,
            "TASK_TYPE": classificacao,
            "ORIGIN": "Automação Python Patriota"
        }
    }

    try:
        print(f"Enviando tarefa [{classificacao}] para o CRM...")
        # Usando a request.post para enviar os dados para Bitrix24
        resposta = requests.post(WEBHOOK_URL, json=payload)

        if resposta.status_code in [200, 201]: # Os codigos 200 e 201 indicam sucesso
            print("✅ Tarefa criada com sucesso no CRM!")
            return True
        else:
            print(f"❌ Erro ao criar tarefa. Status Code do servidor: {resposta.status_code}")
            return False
    except Exception as erro:
        print(f"❌ Erro de conexão: {erro}")
        return False

# Area de teste local
if __name__ == "__main__":
    print("Testando o Mensageiro..\n")

    # Simular que ja classificou e agora estamos enviando
    criar_tarefa_bitrix(
        assunto="Aviso Prévio - João Silva",
        corpo="Ola, gostaria de saber como faço para dar entrada no meu aviso prévio.",
        classificacao="RESCISAO",
        email_destinatario="rh@empresa.com"
    )    
