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
        email = input("Please introduce your email: ")
        password = input("Now, please introduce your password: ")