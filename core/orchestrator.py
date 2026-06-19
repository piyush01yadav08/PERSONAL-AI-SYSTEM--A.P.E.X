from core.router import Router

from modules.ai.ai_module import AIModule
from modules.memory.memory_module import MemoryModule
from modules.memory.recall_module import RecallModule
from modules.memory.memory_extractor import MemoryExtractor
from modules.profile.profile_module import ProfileModule
from modules.knowledge.knowledge_extractor import KnowledgeExtractor


class Orchestrator:

    def __init__(self):

        self.memory_extractor = MemoryExtractor()
        self.knowledge_extractor = KnowledgeExtractor()

        self.modules = [
            MemoryModule(),
            RecallModule(),
            ProfileModule(),

            # Always keep AI last
            AIModule()
        ]

        self.router = Router(self.modules)

    def process(self, query, user_id):

        self.memory_extractor.extract(
            query=query,
            user_id=user_id
        )

        self.knowledge_extractor.extract(
            query=query,
            user_id=user_id
        )

        return self.router.handle(
            query=query,
            user_id=user_id
        )