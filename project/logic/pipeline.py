from project.agent import run_agent
from project.tool import search_research_papers
from project.logic.parser import parse_agent_output
from project.logic.evaluator import evaluate_attempt
from project.logic.repairer import repair_query


def process_research_query(user_query, max_attempts=3):
    debug_queries = [user_query]
    final_results = None
    final_evaluation = None

    for _ in range(max_attempts):
        # extract
        try:
            extracted = run_agent(user_query)
            topic, yf, year, cit = parse_agent_output(extracted)
        except Exception as e:
            return None, f"Extraction failed: {e}", debug_queries

        # search
        results = search_research_papers(topic, yf, year, cit)
        final_results = results

        # evaluate
        evaluation = evaluate_attempt(debug_queries[0], extracted, results)
        final_evaluation = evaluation

        if evaluation.lower().startswith("yes") or evaluation.lower() == "correct":
            return final_results, final_evaluation, debug_queries

        # repair
        user_query = repair_query(debug_queries[0], extracted, results, evaluation)
        debug_queries.append(user_query)

    return final_results, final_evaluation, debug_queries
