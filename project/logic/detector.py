def is_research_query(text: str) -> bool:
    text = text.lower()
    keywords = [
        "paper", "research", "study", "studies", "scientific",
        "ai research", "academic", "openalex", "citations"
    ]
    return any(k in text for k in keywords)
