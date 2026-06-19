from services.knowledge_service import KnowledgeService


class KnowledgeExtractor:

    def __init__(self):
        self.knowledge_service = KnowledgeService()

    def extract(self, query, user_id):

        query_lower = query.strip().lower()

        if "i am preparing for" in query_lower:

            start = query_lower.find("i am preparing for")

            exam = query[
                start + len("i am preparing for"):
            ].strip()

            self.knowledge_service.add_fact(
                user_id=user_id,
                category="exam",
                key_name="target_exam",
                value=exam
            )

            return True

        return False