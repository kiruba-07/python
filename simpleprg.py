#Library Management system
class Library:
    def __init__(self, roll_no, name, password, books=0):
        self.__roll_no = roll_no
        self.__name = name
        self.__password = password
        self.__books = books
 
 
        def get_roll_no(self):
            return self.__roll_no
        def get_name(self):
            return self.__name
        def verify_password(self):
            return self.__password==password
        def get_books(self):
            return self.__books
        def new_books(self,no_of_books):
            self.__books += no_of_books
            return self.__books
        def books_submit(self,no_of_books):
            if no_of_books == self.__books:
                self.__books =0
                return self.__books
            else:
                return "yet you not submitted some books"
 
class system:
    def __init__(self):
        self.accounts = {}
    def create_account(self,roll_no,name,password,books=0):
        if roll_no in self.accounts:
            return "Account already exists"
        self.accounts[roll_no]=Library(roll_no,name,password,books)
        return "Account created successfully"
    def update_account(self,roll_no,new_book):
        if roll_no in self.accounts:
            self.accounts[roll_no].get_books(new_book)
            return "new book updated successfully"
        else:
            return "Account not found"
    def del_account(self,roll_no):
        if roll_no in self.accounts:
            del self.accounts[roll_no]
            return "Account deleted successfully"
        else:
            return "Account not found"
    def authenticate_user(self,roll_no,password):
        if roll_no in self.accounts and self.accounts[roll_no].verify_password(password):
            return self.accounts[roll_no]
        return None
 
class admin:
    def menu(system):
        while True:
            print("\nAdmin Menu")
            print("1. Create Account")
            print("2. Update Account ")
            print("3. Delete Account")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")
 
            if choice=="1":
                roll_no = input("Enter roll number: ")
                name = input("Enter account holder's name: ")
                password = input("Enter password: ")
                books= input("Enter first book: ")
                system.create_account(roll_no,name,password,books)
            elif choice=="2":
                roll_no = input("Enter roll number: ")
                new_book =input("Enter new book: ")
                system.update_account(roll_no,new_book)
            elif choice=="3":
                roll_no = input("Enter account number: ")
                system.del_account(roll_no)
            elif choice=="4":
                break
            else:
                print("Invalid choice. Please try again.")
 
class User():
    def menu(system):
        while True:
            print("\nUser Menu")
            print("1. new_books_taken")
            print("2. books_submitted")
            print("3. Back to Main Menu")
            choice = input("Enter your choice: ")
 
            if choice in ["1","2"]:
                roll_no = input("Enter roll number: ")
                password = input("Enter password: ")
                account=system.authenticate_user(roll_no,password)
 
                if account:
                    if choice=="1":
                        no_of_books = input("Enter the no of new_books taken: ")
                        new_book=account.new_books(no_of_books)
                        print(f"New book: {new_book}")
                    elif choice=="2":
                        no_of_books = input("Enter the no_of_books submitted: ")
                        new_book=account.books_submit(no_of_books)
                        print(f"New book: {new_book}")
                else:
                    print("Invalid roll number or password.")
            elif choice=="3":
                break
            else:
                print("Invalid Choice!")
 
def main_menu():
    Library=system()
    while True:
        print("\nLibrary Management System")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        choice = input("Enter your choice: ")
 
        if choice=="1":
            admin.menu(Library)
        elif choice=="2":
            User.menu(Library)
        elif choice=="3":
            break
        else:
            print("Invalid choice. Please try again.")
main_menu()
 
 
 
 
           
 