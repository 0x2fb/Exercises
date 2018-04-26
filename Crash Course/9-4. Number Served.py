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


restaurant = Restaurant('Aglio es Olio', 'Italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.describe_status()
print(restaurant.number_served)
restaurant.number_served = 50
print(restaurant.number_served)
restaurant.set_number_served(100)
print(restaurant.number_served)
restaurant.increment_number_served()
print(restaurant.number_served)
restaurant.increment_number_served(49)
print(restaurant.number_served)
