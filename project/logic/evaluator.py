from project.evaluate import evaluate
from project.logic.formatter import format_results_for_eval

def evaluate_attempt(user_query, extracted, results):
    formatted = format_results_for_eval(results)
    return evaluate(user_query, formatted)
