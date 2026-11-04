"""Construção da cadeia LangChain e processamento de perguntas."""

from langchain_core.messages import AIMessage, BaseMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from openai import OpenAIError

from app.config import MAX_HISTORY_MESSAGES
from app.prompts import SYSTEM_PROMPT
from app.tracing import record_event, traceable


def _trace_turn_inputs(inputs: dict[str, object]) -> dict[str, object]:
    """Evita registrar o objeto da cadeia e o histórico inteiro no span do turno."""
    question = inputs.get("question", "")
    history = inputs.get("history", [])
    return {
        "question": question,
        "history_message_count": len(history) if isinstance(history, list) else 0,
    }


def build_chain(model_name: str):
    """Cria a cadeia LangChain que combina prompt, histórico e modelo."""
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{question}"),
        ]
    ).with_config({"run_name": "chat_prompt", "tags": ["prompt"]})
    model = ChatOpenAI(model=model_name).with_config(
        {
            "run_name": "openai_generation",
            "tags": ["generation"],
            "metadata": {"model_name": model_name},
        }
    )
    return (prompt | model).with_config({"run_name": "python_qa_chain"})


@traceable(
    name="chatbot_turn",
    run_type="chain",
    process_inputs=_trace_turn_inputs,
)
def ask_question(
    chain,
    question: str,
    history: list[BaseMessage],
) -> tuple[str, list[BaseMessage]]:
    """Envia uma pergunta e devolve a resposta e o histórico atualizado."""
    record_event("question_received", character_count=len(question))
    try:
        response = chain.invoke({"history": history, "question": question})
    except OpenAIError as error:
        record_event("generation_failed", error_type=type(error).__name__)
        raise

    answer = response.content

    if not isinstance(answer, str):
        answer = "".join(
            block.get("text", "")
            for block in answer
            if isinstance(block, dict) and isinstance(block.get("text"), str)
        )

    updated_history = [
        *history,
        HumanMessage(content=question),
        AIMessage(content=answer),
    ]
    record_event("generation_completed", answer_character_count=len(answer))
    return answer, updated_history[-MAX_HISTORY_MESSAGES:]
