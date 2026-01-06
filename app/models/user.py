class User:
    def __init__(self,name:str,age:int,email:str,user_id:int | None=None):
        self.id = user_id
        self.name = name
        self.age = age
        self.email = email

    
    def to_tuple(self):
        return (self.name,self.age,self.email)
    

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', age={self.age}, email='{self.email}')"
    