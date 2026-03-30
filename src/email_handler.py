import os
from dotenv import load_dotenv
from imap_tools import MailBox, AND

# Carrega as variaveis de segurança do arquivo .env
load_dotenv()

#Puxa os dados do email e da senha configurados no .env
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

def buscar_email_nao_lidos():
    print("[Carteiro] Procurando novos e-mails...")
    lista_emails = []

    try:
        with MailBox('imap.gmail.com').login(EMAIL_USER, EMAIL_PASS) as mailbox:
            # Busca e-mails nao lidos (limitados a 3 para testes)
            # Obs: Ao fazer esse 'fetch', o e-mail ja é marcado como lido no seu E-mail.
            mensagens = mailbox.fetch(AND(seen=False), limit=3, reverse=True)
            
            for msg in mensagens:
                # Pega apenas os primeiros 500 caracteres do corpo do e-mail para evitar sobrecarga
                texto_limpo = msg.text.strip()[:500] if msg.text else "E-mail sem texto."

                lista_emails.append({
                    "assunto": msg.subject,
                    "remetente": msg.from_,
                    "corpo": texto_limpo
                })

        print(f"[Carteiro] {len(lista_emails)} novos e-mmails encontrados.")
        return lista_emails
    
    except Exception as erro:
        print(f"[Carteiro] Erro ao conectar: {erro}")
        return []


