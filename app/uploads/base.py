from abc import ABC, abstractmethod
from app.models.user import User

class UploadBase(ABC):
    def __init__(self,user_service):
        self.user_service = user_service

        @abstractmethod
        def read_file(self,filepath):
            """Return list of dicts"""
            pass

        def upload(self,filepath):
            records = self.read_file(filepath)

            users = []
            for record in records:
                users.append(
                    User(
                        name = record["name"],
                        age = int(record["age"]),
                        email = record["email"]
                    )
                )

                self.user_service.add_users_bulk(users)
                print(f"✅ {len(users)} users uploaded successfully.")