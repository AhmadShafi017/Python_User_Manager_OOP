import stack as sk

class UpdateMenu:
    def __init__(self,update_service):
        self.update_service = update_service

    def show(self,stack):
        while True:
            choice = input(
                "Update Menu\n" \
                "1 - Update name\n" \
                "2 - Update age \n" \
                "3 - Update email\n" \
                "0 - Back \n"
            ).strip()

            if choice == "0":
                sk.go_back(stack)
                return
            
            user_id = input("Enter user ID: ").strip()
            if not user_id.isdigit():
                print("❌ Invalid ID")
                continue

            user_id = int(user_id)
            if choice == "1":
                name = input("Enter new name: ")
                self.update_service.update_name(user_id,name)
                print("✅ Name updated")

            elif choice == "2":
                age = input("Enter new age: ")
                if not age.isdigit():
                    print("❌ Age must be a number")
                    continue
                self.update_service.update_age(user_id,int(age))
                print("✅ Age updated")

            elif choice == "3":
                email = input("Enter email: ")
                self.update_service.update_email(user_id,email)
                print("✅ Email updated")

            else:
                print("❌ Invalid option")