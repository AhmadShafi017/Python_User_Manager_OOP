from app.models.user import User

class UserService:
    def __init__(self,db):
        self.db = db

    def add_user(self,user:User):
        query = """
        INSERT INTO users (name,age,email)
        VALUES (%s,%s,%s)
        """
        self.db.execute(query,user.to_tuple())

    def get_all_users(self):
        cursor = self.db.execute("SELECT id,name,age,email FROM users")
        return cursor.fetchall()
    
    def delete_user(self,user_id: int):
        self.db.execute("DELETE FROM users WHERE id=%s",(user_id,))

    def add_users_bulk(self,users):
        if not users:
            return
        
        query = """
            INSERT INTO users(name,age,email)
            VALUES (%s,%s,%s)
        """

        values = [
            (user.name, user.age, user.email)
            for user in users
        ]

        self.db.executemany(query,values)