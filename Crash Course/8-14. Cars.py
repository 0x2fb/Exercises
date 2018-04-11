def make_car(manufacturer, model, **car_info):
    car_data = {}
    car_data["manufacturer"] = manufacturer
    car_data["model"] = model
    for key, value in car_info.items():
        car_data[key] = value
    return car_data


car = make_car('Subaru', 'Outback', color='blue', tow_package=True)
print(car)
