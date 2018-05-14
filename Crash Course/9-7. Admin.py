class User:

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.city = city.title()
        self.login_attempts = 0

    def describe_user(self):
        print(
            f'{self.first_name} {self.last_name} is {self.age} years old and from {self.city}.')

    def greet_user(self):
        print(f'Hi {self.first_name}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = ['can add a post',
                           'can delete a post', 'can ban users']

    def show_privileges(self):
        print(f'As an admin, {self.first_name} {self.last_name} can:')
        for p in self.privileges:
            print(f'- {p}')


rebecca = Admin('Rebecca', 'Smith', 33, 'Prague')
rebecca.greet_user()
rebecca.describe_user()
rebecca.show_privileges()
