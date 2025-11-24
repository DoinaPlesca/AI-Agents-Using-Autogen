from autogen import AssistantAgent, UserProxyAgent
from config import LLM_CONFIG

eval_agent = AssistantAgent(
    name="eval_agent",
    llm_config=LLM_CONFIG,
    system_message=(
        "You evaluate whether the extraction agent correctly extracted the four required parameters. "
        "Be tolerant: accept variations as long as the meaning is correct. For example, 'after' + '2018', "
        "'after 2018', 'newer than 2018', or '>' + '2018' all represent the same meaning and are correct. "
        "Only mark incorrect if the meaning truly does not match the user query. "
        "Respond with 'Yes — <short reason>' if correct, or 'No — <short reason>' if incorrect. "
        "Keep the reason brief."
    )
    ,
    max_consecutive_auto_reply=1
)



# create a user proxy to automate conversation(no human types anything,everything runs automatically

user = UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=1,
)

# checks if agent did its job correctly
def evaluate(task_description: str, agent_output: str, use_chat_loop=False):

    msg = f"""
Task:
{task_description}

Extracted Output:
{agent_output}

Question:
Did the agent correctly extract the four required parameters? 
Return Yes or No, plus a short explanation.
"""

    if use_chat_loop:
        # Version 1 style
        return user.initiate_chat(eval_agent, message=msg)
    else:
        # Version 2 style
        reply = eval_agent.generate_reply(messages=[
            {"role": "user", "content": msg}
        ])
        return reply["content"].strip()

