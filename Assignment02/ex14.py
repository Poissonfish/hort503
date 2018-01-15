from sys import argv

script, user_name, arg1, arg2 = argv
prompt = '** '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have")
computer = input(prompt)

print(f"Do you like {arg1}?")
likearg1 = input(prompt)
print(f"Do you like {arg2}?")
likearg2 = input(prompt)

print(f"""
Alright, so you said {likes} about like me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
