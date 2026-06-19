from core.assistant import BaseModule
from services.profile_service import ProfileService


class ProfileModule(BaseModule):

    def __init__(self):
        self.profile_service = ProfileService()

    def can_handle(self, query):

        query = query.strip().lower()

        return (
            query.startswith("who am i")
            or query.startswith("show my profile")
        )

    def execute(self, query, user_id):

        profile = self.profile_service.get_profile(user_id)

        if not profile:
            return {
                "module": "profile",
                "response": "Profile not found."
            }

        return {
            "module": "profile",
            "response": profile
        }