from core.assistant import BaseModule
from services.database_service import DatabaseService


class RecallModule(BaseModule):

    def __init__(self):
        self.db = DatabaseService()

    def can_handle(self, query):

        query = query.lower()

        triggers = [
            "what do you remember",
            "show my memories",
            "recall memories"
        ]

        return any(trigger in query for trigger in triggers)

    def execute(self, query, user_id):

        memories = self.db.get_memories(user_id)

        if not memories:
            return {
                "module": "memory",
                "response": "I don't remember anything yet."
            }

        memory_list = [memory[0] for memory in memories]

        return {
            "module": "memory",
            "response": memory_list
        }