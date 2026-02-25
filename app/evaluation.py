def compute_precision_at_k(docs):
    return round(len(docs) / 3, 2)

def compute_context_coverage(answer, context_chunks):
    answer_words = set(answer.lower().split())
    context_words = set(" ".join(context_chunks).lower().split())
    if not context_words:
        return 0
    overlap = answer_words.intersection(context_words)
    return round(len(overlap) / len(answer_words), 2)

def compute_faithfulness(answer, context_chunks):
    context_text = " ".join(context_chunks).lower()
    hallucination_count = 0
    for sentence in answer.split("."):
        if sentence.strip() and sentence.lower() not in context_text:
            hallucination_count += 1
    total_sentences = len(answer.split("."))
    if total_sentences == 0:
        return 0
    return round(1 - (hallucination_count / total_sentences), 2)

def compute_confidence(precision, coverage, faithfulness):
    return round((precision + coverage + faithfulness) / 3, 2)
