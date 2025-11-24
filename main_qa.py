from project.qa_agent import ask_question
from project.logic.pipeline import process_research_query
from project.logic.formatter import print_results
from project.logic.detector import is_research_query


if __name__ == "__main__":
    print("=== Enhanced AI Research Assistant ===\n")
    print("1 = General question")
    print("2 = Research papers")
    print("exit = quit\n")

    while True:
        mode = input("Mode (1/2/exit): ").strip().lower()

        if mode == "exit":
            break

        if mode == "1":
            q = input("Ask your question:\n> ")
            print("\n" + ask_question(q))
            print("-" * 40)
            continue

        if mode == "2":
            q = input("Enter your research query:\n> ")
            print("\nWorking... Please wait.\n")

            # not research > qa agent
            if not is_research_query(q):
                print("\nThis doesn't look like a research-paper request.")
                print("Using general QA instead...\n")
                print(ask_question(q))
                print("-" * 40)
                continue

            # otherwise full extraction etc.
            results, evaluation, debug = process_research_query(q)

            print("=== FINAL RESULTS ===\n")
            print_results(results)
            print("\nEvaluation:", evaluation)
            print("-" * 40)

            print("=== DEBUG: Query Attempts ===")
            for i, x in enumerate(debug, 1):
                print(f"{i}. {x}")
            print("-" * 40)
            continue

        print("Invalid input.\n")
