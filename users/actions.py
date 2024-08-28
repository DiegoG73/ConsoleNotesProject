import users.user as model


#* Creating the actions with modules
class Actions:

    def register(self):
        print("\nLet's sign you up ")
        
        name = input("Please introduce your name: ")
        surname = input("Please introduce your surname: ")
        email = input("Please introduce your email: ")
        password = input("Now, please introduce your password: ")
        passwordValidate = input("Now, please reintroduce your password: ")
        
        if password == passwordValidate:
            print("You've registered")
            
        user = model.User(name, surname, email, password)
        #! Creating the register for data base on Python (to register the user)
        register = user.register()
        
        if register[0] >= 1:
            print(f"Perfect, {register[1].name}, you have registered with email: {register[1].email}")
            
        else: 
            print("\nYou've not registered correctly")

    def login(self):
        print("Please sign in with your email and password")
        try:
            email = input("Please introduce your email: ")
            password = input("Now, please introduce your password: ")
            
            user = model.User('', '', email, password)
            login = user.identify()
            
            if email == login[3]:
                print(f"\nWelcome {login[1]}, you have registered on: {login[5]}")
                self.nextActions(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Incorrect, please try again later")
            
    def nextActions(self, user):
        print("""
            Available actions:
            - Create a note (create)
            - Show notes    (show)
            - Delete notes  (delete)
            - Exit          (EXIT)
        """)
        
        action = input("What do you wanna do? ")
        
        if action == "create":
            print("Let's create")
            self.nextActions(user)
        elif action == "show":
            print("Let me show you your notes")
            self.nextActions(user)
        elif action == "delete":
            print("Tell me, which one do you want to delete?")
            self.nextActions(user)
        elif action == "exit":
            exit()
        else:
            print("Please, introduce a valid option")
            self.nextActions(user)
