import regex as re

username = input("What is your username? ")

pattern = r'[root]{4}'

t = re.search(pattern, username).group()

if t == "root":
    print(f"This username has root in it {username}.")
else:
    print(f"This username does not have root in it {username}.")
