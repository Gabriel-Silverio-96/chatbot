"""Carregamento da configuração do chatbot."""

import os

from dotenv import load_dotenv


load_dotenv()

MAX_HISTORY_MESSAGES = 20
EXIT_COMMANDS = {"/sair", "sair", "exit", "quit"}


def get_model_name() -> str:
    """Retorna o modelo configurado ou o modelo padrão."""
    return os.getenv("OPENAI_MODEL")


def validate_configuration() -> None:
    """Garante que a chave da OpenAI esteja configurada."""
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "A variável OPENAI_API_KEY não está definida. Configure sua chave da OpenAI."
        )
