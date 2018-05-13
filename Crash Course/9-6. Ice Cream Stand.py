class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.status = 'closed'
        self.number_served = 0

    def describe_restaurant(self):
        print(f'{self.restaurant_name} offers {self.cuisine_type} cuisine.')
        self.describe_status()

    def open_restaurant(self):
        self.status = 'open'

    def close_restaurant(self):
        self.status = 'close'

    def describe_status(self):
        print(f'It is {self.status} now.')

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num=1):
        self.number_served += num


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type="ice cream", flavors=["strawberry", "vanilla", "chocolate"]):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_restaurant(self):
        print(f'{self.restaurant_name} offers {self.cuisine_type}.')
        self.describe_status()

    def show_flavors(self):
        print(f'{self.restaurant_name} has the following ice cream flavors:')
        for i in self.flavors:
            print(f'- {i.title()}')


frozenbanana = IceCreamStand("Frozen Banana", flavors=[
                             "banana", "mango", "vanilla"])
frozenbanana.open_restaurant()
frozenbanana.describe_restaurant()
frozenbanana.show_flavors()
