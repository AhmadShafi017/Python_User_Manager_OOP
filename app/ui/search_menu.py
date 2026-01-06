import stack as sk

class SearchMenu:
    def __init__(self,search_service):
        self.search_service = search_service

    def show(self,stack):
        while True:
            choice = input(
                "Search Menu\n" \
                "1 - All users\n" \
                "2 - By ID \n" \
                "3 - By Name\n " \
                "4 - By Age \n" \
                "5 - By Email\n" \
                "0 - Back \n"
            ).strip()

            if choice == '1':
                users = self.search_service.all_users()
                self.print_users(users)
            elif choice == "2":
                user_id  = input("Enter ID: ").strip()
                if user_id.isdigit():
                    users = self.search_service.by_id(int(user_id))
                    print(user or "❌ User not found")
            elif choice == "3":
                name = input("Enter Name: ")
                users = self.search_service.by_name(name)
                self.print_users(users)
            elif choice == "4":
                age = input("Enter Age: ").strip()
                if age.isdigit():
                    users = self.search_service.by_age(int(age))
                    self.print_users(users)
            elif choice == "5":
                email = input("Enter Email: ")
                users = self.search_service.by_email(email)
                print(user or "❌ User not found")
            elif choice == "0":
                sk.go_back(stack)
                return
            else:
                print("❌ Invalid option")

            def print_users(self,users):
                if not users:
                    print("❌ No users found")
                    return
                
                for user in users:
                    print(user)