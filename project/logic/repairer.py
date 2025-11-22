from project.repair_agent import repair_agent
from project.logic.formatter import format_results_for_eval

def repair_query(original, extracted, results, evaluation):
    formatted = format_results_for_eval(results)
    message = f"""
User asked: {original}
Extractor output: {extracted}
Returned papers: {formatted}
Evaluator: {evaluation}
Rewrite query. Output ONLY the new query.
"""
    reply = repair_agent.generate_reply(messages=[{"role": "user", "content": message}])
    return reply["content"].strip()
