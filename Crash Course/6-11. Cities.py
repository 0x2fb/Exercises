cities = {
    'Paris': {'country': 'france', 'population': '2.2 m'},
    'Berlin': {'country': 'germany', 'population': '3.6 m'},
    'Tokio': {'country': "japan", 'population': '9.5 m'}
}

for k, v in cities.items():
    print(f"{k} is in {v['country'].title()}"
          f" and has a population of {v['population']}.")
