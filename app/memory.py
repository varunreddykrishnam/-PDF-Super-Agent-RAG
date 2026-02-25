from collections import defaultdict

class MemoryStore:
    def __init__(self):
        self.store = defaultdict(list)

    def add(self, session_id: str, question: str, answer: str):
        self.store[session_id].append({
            "question": question,
            "answer": answer
        })

    def get_history(self, session_id: str):
        return self.store.get(session_id, [])

memory_store = MemoryStore()
