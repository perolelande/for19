from typing import List

class User:
    def __init__(self, f_name, l_name, email, password):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.password = password


class Users:
    def __init__(self):
        self.users:List[User] = []

    def add(self, user):
        self.users.append(user)
    
    def get_all(self):
        return self.users
    
    def get_name(self):
        for i in self.users:
            print(i.f_name)

    def valid_login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return True
        return False
    
    def get_full_name(self, email):
        for user in self.users:
            if user.email == email:
                return user.f_name + " " + user.l_name




