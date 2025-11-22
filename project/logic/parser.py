def parse_agent_output(text):
    lines = [l.strip() for l in text.strip().split("\n")]
    parts = {l.split(":",1)[0].strip(): l.split(":",1)[1].strip() for l in lines}
    return (
        parts["TOPIC"],
        parts["YEAR_FILTER"],
        int(parts["YEAR"]),
        int(parts["CITATIONS"])
    )
