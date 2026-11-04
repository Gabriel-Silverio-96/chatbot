"""Interface de terminal do chatbot."""

from openai import (
    APIConnectionError,
    APIStatusError,
    AuthenticationError,
    OpenAIError,
    RateLimitError,
)
from langchain_core.messages import BaseMessage

from app.chatbot import ask_question, build_chain
from app.config import EXIT_COMMANDS, get_model_name, validate_configuration
from app.tracing import flush_traces, record_event, traceable


def _show_api_error(error: OpenAIError) -> None:
    """Mostra uma orientação adequada para falhas comuns da API."""
    if isinstance(error, AuthenticationError):
        print(
            "Bot: A OpenAI rejeitou a chave. Confira se OPENAI_API_KEY no .env "
            "contém uma chave válida e ativa."
        )
    elif isinstance(error, RateLimitError):
        if getattr(error, "code", None) == "insufficient_quota":
            print(
                "Bot: A conta da API está sem cota disponível. Confira o faturamento "
                "e os limites do projeto na plataforma OpenAI."
            )
        else:
            print(
                "Bot: A OpenAI aplicou um limite de requisições. Aguarde um pouco "
                "e tente novamente."
            )
    elif isinstance(error, APIConnectionError):
        print(
            "Bot: Não consegui conectar à OpenAI. Confira sua conexão com a internet "
            "e tente novamente."
        )
    elif isinstance(error, APIStatusError):
        print(
            f"Bot: A OpenAI retornou HTTP {error.status_code}. "
            "Confira se o modelo configurado em OPENAI_MODEL está disponível "
            "para sua conta."
        )
    else:
        print(f"Bot: Erro da API OpenAI ({type(error).__name__}). Confira a configuração.")


@traceable(name="python_chatbot_session", run_type="chain")
def run_chat() -> None:
    """Executa o loop de conversa no terminal."""
    validate_configuration()
    chain = build_chain(get_model_name())
    history: list[BaseMessage] = []

    record_event("chat_session_started", model_name=get_model_name())
    try:
        print("Chatbot de Python iniciado. Digite /sair para encerrar.")
        while True:
            try:
                question = input("Você: ").strip()
            except EOFError:
                print("\nAté logo!")
                return

            if not question:
                continue
            if question.lower() in EXIT_COMMANDS:
                print("Até logo!")
                return

            try:
                answer, history = ask_question(chain, question, history)
            except OpenAIError as error:
                _show_api_error(error)
                continue

            print(f"Bot: {answer}\n")
    finally:
        record_event("chat_session_ended")


def main() -> None:
    """Ponto de entrada da aplicação de terminal."""
    try:
        run_chat()
    except RuntimeError as error:
        print(f"Erro de configuração: {error}")
    except KeyboardInterrupt:
        print("\nAté logo!")
    finally:
        flush_traces()
