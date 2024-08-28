from users import actions

print("""
    AVAILABLE ACTIONS
        - Sign Up
        - Login
""")

doThe = actions.Actions()

action = input("What do you want to do? ")


if action == "sign up":
    doThe.register()
elif action == "login":
    doThe.login()