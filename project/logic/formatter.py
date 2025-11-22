def format_results_for_eval(results):
    if not results:
        return "No results found."
    return "\n".join(f"{r['title']} ({r['year']}) — {r['citations']} citations" for r in results)


def print_results(results):
    if not results:
        print("No results returned.\n")
        return
    for r in results:
        print(f"- {r['title']} ({r['year']}) — {r['citations']} citations")
        print(r['url'], "\n")
