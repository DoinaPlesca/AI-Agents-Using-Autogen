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
    print("=== Interactive Research Assistant ===\n")

    while True:
        # Ask for input
        user_query = input("Enter your research question (or type 'exit' to quit):\n> ").strip()

        if user_query.lower() == "exit":
            print("Goodbye!")
            break

        if not user_query:
            print("Please enter a valid question.\n")
            continue

        # Step 1 — run agent
        print("\nRunning agent...\n")
        extracted = run_agent(user_query)
        print("Agent reply:\n", extracted, "\n")

        # Step 2 — parse results
        try:
            topic, year_filter, year, citations = parse_agent_output(extracted)
        except Exception as e:
            print("Error parsing agent output:", e)
            continue

        # Step 3 — search OpenAlex
        print("Searching papers via OpenAlex...\n")
        results = search_research_papers(topic, year_filter, year, citations)

        # Step 4 — print results
        print("=== RESULTS ===\n")
        for r in results:
            print(f"- {r['title']} ({r['year']}) — {r['citations']} citations")
            print(r['url'], "\n")

        print("-" * 40 + "\n")
