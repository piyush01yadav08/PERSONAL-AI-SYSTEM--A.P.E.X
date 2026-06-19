from services.database_service import DatabaseService


class ProfileService:

    def __init__(self):
        self.db = DatabaseService()

    def create_profile(self, user_id, name):

        self.db.create_user(
            user_id=user_id,
            name=name
        )

        return {
            "status": "success",
            "message": f"Profile created for {name}"
        }

    def get_profile(self, user_id):

        user = self.db.get_user(user_id)

        if not user:
            return {
                "status": "error",
                "message": "Profile not found"
        }

        return {
            "id": user[0],
            "user_id": user[1],
            "name": user[2],
            "created_at": user[3]
        }