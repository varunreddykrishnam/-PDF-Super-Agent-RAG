def validate_question(question: str):
    if not question or len(question.strip()) < 3:
        return False
    return True
