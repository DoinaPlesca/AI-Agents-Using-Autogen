from project.agent import run_agent
from project.tool import search_research_papers
from project.qa_agent import ask_question

def parse_agent_output(text: str):
    """Same parse function from original main."""
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
    print("=== Enhanced AI Research Assistant ===\n")
    print("Choose a mode:")
    print("  1 = Ask a general question")
    print("  2 = Search for research papers")
    print("  exit = quit the program\n")

    while True:
        mode = input("Mode (1/2/exit): ").strip().lower()

        if mode == "exit":
            print("Goodbye!")
            break

        # ------------------------------
        # MODE 1: Question-answering
        # ------------------------------
        if mode == "1":
            question = input("Ask your question:\n> ")

            print("\nAnswering...\n")
            answer = ask_question(question)
            print(answer)
            print("\n" + "-"*40 + "\n")
            continue

        # ------------------------------
        # MODE 2: Research paper search
        # ------------------------------
        if mode == "2":
            user_query = input("Enter your research query:\n> ")

            print("\nRunning research agent...\n")
            extracted = run_agent(user_query)
            print("Agent reply:\n", extracted, "\n")

            try:
                topic, year_filter, year, citations = parse_agent_output(extracted)
            except Exception as e:
                print("Error parsing:", e)
                continue

            print("Searching papers via OpenAlex...\n")
            results = search_research_papers(topic, year_filter, year, citations)

            print("=== RESULTS ===\n")
            for r in results:
                print(f"- {r['title']} ({r['year']}) — {r['citations']} citations")
                print(r['url'], "\n")
            print("-"*40 + "\n")
            continue

        print("Invalid input. Try again.\n")
