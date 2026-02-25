def classify_intent(question: str):
    if "summarize" in question.lower():
        return "summarization"
    elif "compare" in question.lower():
        return "comparison"
    else:
        return "qa"
