import time
from src.email_handler import buscar_email_nao_lidos
from src.ai_classifier import classificar_email
from src.bitrix_sync import criar_tarefa_bitrix

def executar_automacao():
    print("=== INICIANDO SISTEMA DE TRIAGEM DE E-MAILS ===\n")

    emails = buscar_email_nao_lidos()

    if not emails:
        print("Nenhum e-mail novo para processar. Encerrando o sistema.")
        return
    # Repassando para a equipe de triagem
    for email in emails:
        print("-" * 50)
        print(f"Processando e-mail de: {email['remetente']}")
        print(f"Assunto: {email['assunto']}")

        # Envia para leitura da IA e calssificar o tipo do e-mail
        print("Enviando para a IA analisar o conteudo do e-mail...")
        classificacao = classificar_email(email['corpo'])
        print(f"Classificação da IA: {classificacao}")

        # Despacha a tarefa para o CRM (Bitrix24)
        sucesso = criar_tarefa_bitrix(
            assunto=email['assunto'],
            corpo=email['corpo'],
            classificacao=classificacao,
            email_destinatario="rh@empresa.com" # Simulando caixa de entrada
        )

        # Uma pausa entre os envios para evitar sobrecarga
        time.sleep(2)

    print("\n=== SISTEMA DE TRIAGEM DE E-MAILS ENCERRADO ===")

if __name__ == "__main__":
    executar_automacao()

