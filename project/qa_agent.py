from autogen import AssistantAgent
from config import LLM_CONFIG

qa_agent = AssistantAgent(
    name="qa_agent",
    llm_config=LLM_CONFIG,
    system_message="""
You are a helpful expert assistant.
Your job is to answer any general question clearly and concisely.
Do NOT output any special formatting unless necessary.
"""
)

def ask_question(question: str) -> str:
    reply = qa_agent.generate_reply(
        messages=[{"role": "user", "content": question}]
    )
    return reply["content"].strip()
