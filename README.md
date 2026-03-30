# 🤖 Automação Inteligente de Triagem de E-mails com IA

Um sistema backend desenvolvido em Python para automatizar a leitura, classificação contextual e roteamento de e-mails corporativos, integrando servidores de e-mail (IMAP), Inteligência Artificial Generativa e CRMs via Webhook.

## 🎯 O Problema de Negócio
Departamentos como Recursos Humanos e Administração costumam receber dezenas de e-mails diários (envio de atestados, pedidos de demissão, dúvidas de folha de pagamento, etc.). A triagem manual dessas mensagens gera atrasos, perda de informações e consome tempo produtivo da equipe, que precisa ler cada e-mail e repassar para o responsável correto no sistema de gestão.

## 💡 A Solução
Esta aplicação atua como um "assistente virtual" que roda em segundo plano:
1. **Conecta** ativamente à caixa de entrada do departamento.
2. **Lê** os e-mails não lidos.
3. **Analisa** o contexto da mensagem utilizando Inteligência Artificial (sem depender de palavras-chave rígidas).
4. **Classifica** a solicitação (Ex: *ADMISSAO*, *RESCISAO*, *FOLHA_PONTO*).
5. **Integra** com o CRM da empresa via Webhook, criando uma tarefa automaticamente e atribuindo-a ao funcionário responsável com base na classificação.

O sistema também possui um mecanismo de *fallback*: caso a IA não consiga identificar o assunto com precisão, o e-mail é classificado como *DESCONHECIDO* e encaminhado para uma fila de triagem manual, garantindo que nenhuma mensagem seja perdida.

## 🛠️ Tecnologias Utilizadas
* **Python 3.x:** Linguagem principal da automação.
* **imap_tools:** Biblioteca moderna para interação com servidores IMAP (leitura e manipulação de e-mails).
* **requests:** Para consumo da API de IA e envio dos Webhooks para o CRM.
* **OpenRouter API:** Roteamento flexível de LLMs (Large Language Models) para processamento de linguagem natural e classificação de texto.
* **python-dotenv:** Gerenciamento seguro de variáveis de ambiente e credenciais sensíveis.

## 🏗️ Arquitetura do Projeto
O código foi estruturado de forma modular para facilitar a manutenção e a escalabilidade:

```text
/
├── src/
│   ├── email_handler.py   # Módulo responsável pela conexão IMAP e extração de dados
│   ├── ai_classifier.py   # Módulo de integração com a LLM para análise de contexto
│   └── bitrix_sync.py     # Módulo de disparo de Webhooks para sistemas externos
├── main.py                # Orquestrador que une os módulos e dita o fluxo da automação
├── requirements.txt       # Dependências do projeto
└── .env.example           # Modelo de variáveis de ambiente

