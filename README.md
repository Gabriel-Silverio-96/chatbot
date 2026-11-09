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

<img alt="Trace LangSmith" src="https://github.com/user-attachments/assets/e56d5380-837a-4881-9d15-389b30572227" />

| Componente               | Descrição                                                              |
| ------------------------ | ---------------------------------------------------------------------- |
| `python_chatbot_session` | Trace principal que representa a sessão completa do chatbot.           |
| `chatbot_turn`           | Registra cada interação realizada pelo usuário.                        |
| `python_qa_chain`        | Representa a cadeia de processamento da pergunta utilizando LangChain. |
| `chat_prompt`            | Registra a etapa de construção do prompt enviado ao modelo.            |
| `openai_generation`      | Monitora a chamada ao LLM e a geração da resposta.                     |

Os eventos `chat_session_started`, `question_received`, `generation_completed`, `generation_failed` e `chat_session_ended` marcam o fluxo. O CLI aguarda até cinco segundos pelo envio de traces pendentes ao encerrar.

<video src="https://github.com/user-attachments/assets/c75bb6e8-aecd-43c5-a594-ee83bb8cd036" controls>

