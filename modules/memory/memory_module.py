from core.assistant import BaseModule
from services.database_service import DatabaseService


class MemoryModule(BaseModule):

    def __init__(self):
        self.db = DatabaseService()

    def can_handle(self, query):

        query = query.strip().lower()

        return query.startswith("remember")

    def execute(self, query, user_id):

        memory = query.replace("remember", "", 1).strip()

        self.db.save_memory(
            user_id=user_id,
            memory=memory
        )

        return {
            "module": "memory",
            "response": f"I'll remember: {memory}"
        }