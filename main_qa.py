from project.agent import run_agent
from project.tool import search_research_papers
from project.qa_agent import ask_question
from project.evaluate import evaluate
from project.repair_agent import repair_agent


def parse_agent_output(text: str):
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


def format_results_for_eval(results):
    if not results:
        return "No results found."

    formatted = ""
    for r in results:
        formatted += f"{r['title']} ({r['year']}) — {r['citations']} citations\n"
    return formatted.strip()


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

        # -------------------- MODE 1 --------------------
        if mode == "1":
            question = input("Ask your question:\n> ")
            print("\nAnswering...\n")
            answer = ask_question(question)
            print(answer)
            print("\n" + "-" * 40 + "\n")
            continue

        # -------------------- MODE 2 --------------------
        if mode == "2":
            original_query = input("Enter your research query:\n> ")

            user_query = original_query
            MAX_ATTEMPTS = 3
            attempt = 1

            # store all generated queries for debug
            debug_queries = [user_query]

            print("\nWorking on your request... Please wait.\n")

            final_results = None
            final_evaluation = None
            final_extracted = None

            while attempt <= MAX_ATTEMPTS:

                # ---- Extraction ----
                try:
                    extracted = run_agent(user_query)
                    final_extracted = extracted
                except Exception as e:
                    final_evaluation = f"Extractor failed: {e}"
                    break

                try:
                    topic, year_filter, year, citations = parse_agent_output(extracted)
                except Exception as e:
                    final_evaluation = f"Parsing error: {e}"
                    break

                # ---- Search ----
                results = search_research_papers(topic, year_filter, year, citations)
                final_results = results
                formatted_results = format_results_for_eval(results)

                # ---- Evaluate ----
                evaluation = evaluate(original_query, formatted_results)
                final_evaluation = evaluation

                # ---- If correct → stop ----
                if evaluation.lower().startswith("yes") or evaluation.lower() == "correct":
                    break

                # ---- Otherwise repair ----
                reply = repair_agent.generate_reply(messages=[
                    {"role": "user", "content": f"""
                    The user asked:
                    {original_query}

                    Your extraction produced:
                    {extracted}

                    Returned papers:
                    {formatted_results}

                    Evaluator says:
                    {evaluation}
                    
                    Rewrite the query to fix the issue. Output ONLY the new query.
                    """}
                ])

                user_query = reply["content"].strip()
                debug_queries.append(user_query)
                attempt += 1

            # -------------------- OUTPUT SECTION --------------------
            print("=== FINAL RESULTS ===\n")

            if final_results:
                for r in final_results:
                    print(f"- {r['title']} ({r['year']}) — {r['citations']} citations")
                    print(r['url'], "\n")
            else:
                print("No results returned.\n")

            print("Evaluation:", final_evaluation)
            print("-" * 40 + "\n")

            # -------------------- DEBUG SECTION --------------------
            print("=== DEBUG: Query Attempts ===")
            for idx, q in enumerate(debug_queries, 1):
                print(f"{idx}. {q}")
            print("-" * 40 + "\n")

            continue

        print("Invalid input. Try again.\n")
