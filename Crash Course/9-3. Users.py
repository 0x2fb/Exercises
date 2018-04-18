class User:

    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.city = city.title()

    def describe_user(self):
        print(
            f'{self.first_name} {self.last_name} is {self.age} years old and from {self.city}.')

    def greet_user(self):
        print(f'Hi {self.first_name}!')


helen = User('helen', 'smith', 44, 'london')
george = User('george', 'stevenson', 33, 'Paris')
angela = User('angela', 'durham', 35, 'Berlin')

helen.describe_user()
helen.greet_user()
george.describe_user()
george.greet_user()
angela.describe_user()
angela.greet_user()
