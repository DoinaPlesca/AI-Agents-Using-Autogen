from autogen import AssistantAgent, UserProxyAgent
from config import LLM_CONFIG


# create an evaluation assistant to read the task, read the agent’s output, say corect or incorect
eval_agent = AssistantAgent(
    name="eval_agent",
    llm_config=LLM_CONFIG,
    system_message="You evaluate whether the agent completed the task correctly. Reply briefly."
)


# create a user proxy to automate conversation(no human types anything,everything runs automatically
user = UserProxyAgent(
    name="student",
    human_input_mode="NEVER"
)


# checks if agent did its job correctly
def evaluate(task_description: str, agent_output: str):
    msg = f"""
Task:
{task_description}

Agent Output:
{agent_output}

Did the agent complete the task correctly?
"""
    return user.initiate_chat(eval_agent, message=msg)