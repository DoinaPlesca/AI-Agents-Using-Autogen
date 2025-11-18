from autogen import AssistantAgent, UserProxyAgent
from config import LLM_CONFIG

# ---create assistant agent(the extractor agent)----

assistant = AssistantAgent(
    name="paper_agent",
    llm_config=LLM_CONFIG,
    system_message="""
ROLE:
You extract structured parameters for a research paper search tool.

OUTPUT FORMAT (MANDATORY):
TOPIC: <topic>
YEAR_FILTER: <in/after/before>
YEAR: <integer>
CITATIONS: <integer>

CONSTRAINTS:
- Output ONLY the 4 lines above.
- No extra spaces.
- No quotes.
- No markdown.
- No natural language.
- Failure to follow format = failed task.

GOAL:
Infer missing values if necessary.
"""
)

# user agent
user = UserProxyAgent(
    name="user",
    human_input_mode="NEVER"
)

# validate the respons
def validate_output(text: str):
    lines = text.strip().split("\n")
    if len(lines) != 4:
        raise ValueError("Agent output is not exactly 4 lines.")

    for line in lines:
        if ":" not in line:
            raise ValueError(f"Invalid line (missing ':'): {line}")

    return True

# takes the user’s question-> sent to AI(assistent)
# get text and validate
def run_agent(query: str):
    reply = assistant.generate_reply(messages=[{"role": "user", "content": query}])
    content = reply["content"].strip()
    validate_output(content)
    return content