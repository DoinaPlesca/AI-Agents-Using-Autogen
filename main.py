from project.agent import run_agent
from project.tool import search_research_papers

def parse_agent_output(text: str):
    """Convert the agent output into usable parameters."""
    lines = text.strip().split("\n")
    params = {}

    for line in lines:
        key, value = line.split(":", 1)
        params[key.strip()] = value.strip()

    return (
        params["TOPIC"],
        params["YEAR_FILTER"],
        int(params["YEAR"]),
        int(params["CITATIONS"])
    )

if __name__ == "__main__":
    print("Running agent...")

    # user question(request)
    user_query = "Find a research paper on machine learning published after 2018 with at least 500 citations."

    # run the agent to extract parameters
    extracted = run_agent(user_query)
    print("\nAgent reply:\n", extracted, "\n")

    # convert extracted text into variables
    topic, year_filter, year, citations = parse_agent_output(extracted)

    # use the tool-OpenAlex API
    print("Searching papers via OpenAlex...\n")
    results = search_research_papers(topic, year_filter, year, citations)

    # print results
    print("RESULTS:\n")
    for r in results:
        print(f"- {r['title']} ({r['year']}) — {r['citations']} citations")
        print(r['url'], "\n")
