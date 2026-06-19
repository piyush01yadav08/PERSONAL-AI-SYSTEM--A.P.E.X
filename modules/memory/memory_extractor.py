from services.database_service import DatabaseService
from services.profile_service import ProfileService


class MemoryExtractor:

    def __init__(self):
        self.db = DatabaseService()
        self.profile_service = ProfileService()

    def extract(self, query, user_id):

        query_lower = query.strip().lower()

        if "my name is" in query_lower:

            start_index = query_lower.find("my name is")

            name = query[
                start_index + len("my name is"):
            ].strip()

            self.profile_service.create_profile(
                user_id=user_id,
                name=name
            )

            return True

        patterns = [
            "i am preparing for",
            "my exam is",
            "my favorite subject is"
        ]

        for pattern in patterns:

            if pattern in query_lower:

                self.db.save_memory(
                    user_id=user_id,
                    memory=query
                )

                return True

        return False