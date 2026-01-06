class UpdateService:
    def __init__(self,db):
        self.db = db

    def update_name(self,user_id:int,name:str):
        query = "UPDATE users SET name = %s WHERE id = %s"
        self.db.execute(query(name,user_id))

    def update_age(self,user_id:int,age:int):
        query = "UPDATE users SET age = %s WHERE id = %s"
        self.db.execute(query(age,user_id))

    def update_email(self,user_Id:int,email:str):
        query = "UPDATE users SET email WHERE id = %s"
        self.db.execute(query(email,user_Id))