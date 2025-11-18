import requests

OPENALEX_URL = "https://api.openalex.org/works"

## search engine helper(it talks to a big online db of research papers and filters the results
def search_research_papers(topic: str, year_filter: str, year: int, min_citations: int):
    params = {
        "search": topic,
        "per-page": 50,
        "sort": "cited_by_count:desc"
    }

## sent request to db
    response = requests.get(OPENALEX_URL, params=params)

    if response.status_code != 200:
        print("API error:", response.text)
        return []

## return a JSON FORMAT
    works = response.json().get("results", [])
    results = []

## filter the papers based on in/after/before( in =year must be exactly equal; after =year must be larger; before = year must be smaller)
    for w in works:
        pub_year = int(w.get("publication_year", 0))
        citations = w.get("cited_by_count", 0)

        # filter by year
        if year_filter == "in" and pub_year != year:
            continue
        if year_filter == "after" and pub_year <= year:
            continue
        if year_filter == "before" and pub_year >= year:
            continue

        # filter by citation count
        if citations < min_citations:
            continue

        results.append({
            "title": w.get("title"),
            "year": pub_year,
            "citations": citations,
            "url": w.get("id")   # link to paper page
        })

    return results
