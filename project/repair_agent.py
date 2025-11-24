from autogen import AssistantAgent
from config import LLM_CONFIG

repair_agent = AssistantAgent(
    name="repair_agent",
    llm_config=LLM_CONFIG,
    system_message="""
You repair user queries when the AI extraction agent fails.

Given:
1. The user's original query
2. The incorrect list of research papers
3. The evaluator feedback

YOUR JOB:
Rewrite the user's query to be clearer and more precise,
so that the extraction agent will correctly infer the search parameters.

RULES:
- Keep the meaning of the question
- Clarify dates, ranges, or topics when missing
- Output ONLY the revised query
"""
)
