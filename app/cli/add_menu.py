from app.models.user import User

def add_single_user_cli(user_service):
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    user = User(name,age,email)
    user_service.add_user(user)

    print("✅ User added successfully")