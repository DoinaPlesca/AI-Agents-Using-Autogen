from autogen import AssistantAgent
from config import LLM_CONFIG

# Evaluation assistant: reads query + extracted parameters and answers Yes/No
eval_agent = AssistantAgent(
    name="eval_agent_v2",
    llm_config=LLM_CONFIG,
    system_message=(
        "You evaluate whether the extraction agent correctly extracted the 4 required parameters "
        "from the user query. "
        "Reply ONLY with 'Yes' or 'No'. No explanation, no extra words."
    ),
)


def evaluate(task_description: str, agent_output: str) -> str:
    """
    Run the evaluation agent and return a clean 'Yes' or 'No' string if possible.
    Otherwise, return the raw answer text.
    """
    msg = f"""
User Query:
{task_description}

Extracted Parameters:
{agent_output}

Question:
Did the agent correctly extract the four required parameters from the user query?
"""

    # Call the eval agent directly (no UserProxyAgent)
    reply = eval_agent.generate_reply(messages=[{"role": "user", "content": msg}])

    # Autogen usually returns a dict with a 'content' field
    if isinstance(reply, dict):
        answer = str(reply.get("content", "")).strip()
    else:
        answer = str(reply).strip()

    low = answer.lower()

    if "yes" in low and "no" not in low:
        return "Yes"
    if "no" in low and "yes" not in low:
        return "No"

    # If the model doesn't follow instructions, return raw text for debugging
    return answer
