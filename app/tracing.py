"""Helpers for LangSmith traces, spans and run events."""

import os
from datetime import datetime, timezone
from functools import partial
from typing import Any

from langsmith import Client, get_current_run_tree, traceable as langsmith_traceable

from app.config import load_dotenv as _load_dotenv

_load_dotenv()

_tracing_enabled = os.getenv("LANGSMITH_TRACING", "").lower() == "true"
_langsmith_client = (
    Client()
    if _tracing_enabled and os.getenv("LANGSMITH_API_KEY")
    else None
)

traceable = partial(langsmith_traceable, client=_langsmith_client)


def record_event(name: str, **details: Any) -> None:
    """Registra um evento no span ativo, se houver um."""
    current_run = get_current_run_tree()
    if current_run is None:
        return

    current_run.add_event(
        {
            "name": name,
            "time": datetime.now(timezone.utc),
            "kwargs": details,
        }
    )


def flush_traces() -> None:
    """Aguarda o envio dos traces pendentes antes de encerrar o CLI."""
    if _langsmith_client is None:
        return

    try:
        _langsmith_client.flush(timeout=5)
    except Exception as error:  # Tracing must not prevent the chatbot from exiting.
        print(
            "Aviso: não foi possível enviar os traces ao LangSmith "
            f"({type(error).__name__})."
        )
