class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.status = 'closed'

    def describe_restaurant(self):
        print(f'{self.restaurant_name} offers {self.cuisine_type} cuisine.')
        self.describe_status()

    def open_restaurant(self):
        self.status = 'open'

    def close_restaurant(self):
        self.status = 'close'

    def describe_status(self):
        print(f'It is {self.status} now.')


restaurant = Restaurant('Aglio es Olio', 'Italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.describe_status()
