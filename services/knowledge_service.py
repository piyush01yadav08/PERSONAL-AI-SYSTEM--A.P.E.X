from services.database_service import DatabaseService


class KnowledgeService:

    def __init__(self):
        self.db = DatabaseService()

    def add_fact(
        self,
        user_id,
        category,
        key_name,
        value
    ):

        self.db.save_knowledge(
            user_id,
            category,
            key_name,
            value
        )

        return {
        "status": "success",
        "category": category,
        "key": key_name,
        "value": value
        }

    def get_facts(self, user_id):

        return self.db.get_knowledge(user_id)