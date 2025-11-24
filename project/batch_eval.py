from project.agent import run_agent
from project.evaluate_v2 import evaluate

TEST_QUERIES = [
    "Find a research paper on machine learning published after 2018 with at least 500 citations.",
    "Find a research paper about transformers in natural language processing after 2020 with at least 300 citations.",
    "Find a research paper in computer vision published before 2015 with at least 200 citations.",
    "Find a research paper on reinforcement learning in 2019 with at least 150 citations.",
    "Find a research paper on large language models published after 2021 with at least 400 citations.",
]


def run_batch_evaluation():
    total = len(TEST_QUERIES)
    correct = 0

    for idx, query in enumerate(TEST_QUERIES, start=1):
        print("=" * 80)
        print(f"Query {idx}/{total}:")
        print(query)
        print()

        extracted = run_agent(query)
        print("Extracted parameters:")
        print(extracted)
        print()

        eval_label = evaluate(query, extracted)
        print("Evaluation:", repr(eval_label))
        print()

        if eval_label == "Yes":
            correct += 1

    print("=" * 80)
    print(f"Summary: {correct} / {total} extractions judged correct.")
    if total > 0:
        accuracy = correct / total * 100
        print(f"Accuracy: {accuracy:.1f}%")
    print("=" * 80)


if __name__ == "__main__":
    run_batch_evaluation()
