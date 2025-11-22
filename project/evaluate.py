from autogen import AssistantAgent, UserProxyAgent
from config import LLM_CONFIG


# create an evaluation assistant to read the task, read the agent’s output, say corect or incorect
eval_agent = AssistantAgent(
    name="eval_agent",
    llm_config=LLM_CONFIG,
    system_message=(
        "You evaluate whether the extraction agent correctly extracted the 4 required parameters "
        "from the user query. "
        "Reply ONLY with 'Yes' or 'No'. No explanation, no extra words."
    ),
    max_consecutive_auto_reply = 1
)


# create a user proxy to automate conversation(no human types anything,everything runs automatically
user = UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=1
)


# checks if agent did its job correctly
def evaluate(task_description: str, agent_output: str):
    msg = f"""
User Query:
{task_description}

Extracted Parameters:
{agent_output}

Question:
Did the agent correctly extract the four required parameters from the user query?
"""
    return user.initiate_chat(eval_agent, message=msg)