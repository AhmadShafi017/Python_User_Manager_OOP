class SearchService:
    def __init__(self,db):
        self.db = db
        
    def all_users(self):
        cursor = self.execute(
            "SELECT id,name,age,email FROM users"
        )
        return cursor.fetchall()
    
    def by_id(self,user_id:int):
        cursor = self.db.execute(
            "SELECT id,name,age,email FROM users WHERE id = %s",
            (user_id,)
        )
        return cursor.fetchone()
    
    def by_name(self,name:str):
        cursor = self.db.execute(
            "SELECT id,name,age,email FROM users WHERE name LIKE %s",
            (f"%{name}%",)
        )
        return cursor.fetchall()
    
    def by_age(self,age:int):
        cursor = self.db.execute(
            "SELECT id,name,age,email FROM users WHERE age = %s",
            (age,)
        )
        return cursor.fetchall()
    
    def by_email(self, email:str):
        cursor = self.db.execute(
            "SELECT id,name,age,email FROM users WHERE email = %s",
            (email,)
        )
        return cursor.fetchone()
    
