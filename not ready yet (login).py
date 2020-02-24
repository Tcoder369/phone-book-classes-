class User():
    def __init__(self, name, password):
        self.name = name
        self.password = password


users = {}


def add_user():
    name = input('what would you like your username to be: ')
    password = input('what would you like your password: ')
    confirmation = input('please type your password again for confermation: ')

    while password != confirmation:
        confirmation = input(
            'please type your password again for confermation: ')

    users[name] = password
