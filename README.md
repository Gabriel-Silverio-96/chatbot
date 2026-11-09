# Chatbot de programação em Python

Chatbot de terminal que usa LangChain para compor o prompt e gerenciar o histórico da conversa, e `ChatOpenAI` para gerar respostas. O exemplo mantém o histórico em memória durante a execução e responde em português a dúvidas sobre Python.

## Estrutura

```text
app/
├── __init__.py
├── __main__.py   # Permite executar com python -m app
├── chatbot.py    # Cadeia LangChain e processamento de perguntas
├── cli.py        # Loop do terminal e mensagens de erro
├── config.py     # Variáveis de ambiente e configurações
├── prompts.py    # Instruções de sistema do chatbot
└── tracing.py    # Traces, spans, eventos e envio ao LangSmith
chatbot.py        # Atalho compatível: python chatbot.py
```

## Requisitos

- Python 3.10 ou superior
- Uma chave de API da OpenAI
- (Opcional) Uma chave do LangSmith para registrar traces

## Instalação

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

No PowerShell, ative o ambiente com `.venv\Scripts\Activate.ps1`.

Em `.env` preencha a `OPENAI_API_KEY` com sua chave.

O modelo padrão é `gpt-6-luna`. Para selecionar outro modelo disponível na sua conta, defina `OPENAI_MODEL`

## Executar

```bash
python chatbot.py
```



Digite perguntas no terminal. Para encerrar, digite `/sair`, `sair`, `exit` ou `quit`.

## Exemplos de perguntas

### Perguntas sobre Python

Estas perguntas estão dentro do escopo do chatbot:

1. Como criar uma lista em Python e adicionar itens a ela?
2. Qual é a diferença entre uma lista e uma tupla em Python?
3. Como tratar erros usando `try` e `except`?

### Perguntas fora do escopo

O chatbot não responde perguntas sobre outras linguagens de programação. Para perguntas como estas, deve informar que atende apenas dúvidas sobre Python e convidar a pessoa a perguntar sobre Python:

1. Como declarar uma variável em JavaScript?
2. Como criar uma classe em Java?
3. Como escrever um loop `for` em C++?

## Observabilidade com LangSmith

Para habilitá-lo, defina as variáveis abaixo no `.env`:

```env
LANGSMITH_API_KEY=sua-chave-langsmith
```

## Rastreamento de execuções (Tracing)

A imagem apresenta o rastreamento de uma sessão do chatbot, contendo três interações e suas respectivas etapas de execução.

<img alt="Trace LangSmith" src="https://private-user-images.githubusercontent.com/53228013/695398875-4c2149c5-ca58-488c-9ebe-c4508a70fac8.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3OTM4Mjk0ODQsIm5iZiI6MTc5MzgyOTE4NCwicGF0aCI6Ii81MzIyODAxMy82OTUzOTg4NzUtNGMyMTQ5YzUtY2E1OC00ODhjLTllYmUtYzQ1MDhhNzBmYWM4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjExMDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYxMTA0VDIxNTMwNFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWYyOGE0Y2Q3ODRmNjY5NzM0YWIyNGNmMGMxZmY2ZTk2YzMxZWY3ZTU3MWM3OTE4ZjFkZWM1ODJmY2Q4YjNjYjMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.tOfXCFhYs5_1lmUODO_OfeDA4MVr4qxK26ziFNjvwXk" />

| Componente               | Descrição                                                              |
| ------------------------ | ---------------------------------------------------------------------- |
| `python_chatbot_session` | Trace principal que representa a sessão completa do chatbot.           |
| `chatbot_turn`           | Registra cada interação realizada pelo usuário.                        |
| `python_qa_chain`        | Representa a cadeia de processamento da pergunta utilizando LangChain. |
| `chat_prompt`            | Registra a etapa de construção do prompt enviado ao modelo.            |
| `openai_generation`      | Monitora a chamada ao LLM e a geração da resposta.                     |

Os eventos `chat_session_started`, `question_received`, `generation_completed`, `generation_failed` e `chat_session_ended` marcam o fluxo. O CLI aguarda até cinco segundos pelo envio de traces pendentes ao encerrar.
