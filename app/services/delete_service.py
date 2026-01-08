class DeleteService:
    def __init__(self,db):
        self.db = db

    def delete_user(self,user_id:int):
        query = "DELETE FROM user WHERE id = %s"
        self.db.execute(query(user_id,))

    def delete_users_bulk(self,user_ids:list[int]):
        if not user_ids:
            return
        
        placeholders = ",".join(["%s"] * len(user_ids))
        query = f"DELETE FROM users WHERE id IN ({placeholders})"
        self.db.execute(query(tuple(user_ids)))

    def delete_table(self,table_name:str):
        query = f"DROP TABLE {table_name}"
        self.db.execute(query)

    def delete_database(self, database_name:str):
        query = f"DROP DATABASE {database_name}"
        self.db.execute(query)