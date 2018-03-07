import requests
import termcolor
import random
import pyfiglet

print(termcolor.colored(pyfiglet.figlet_format('DadJoke300'), color='magenta'))

searchterm = input('Let me tell you a joke! Give me a topic: ')
response = requests.get(
    'https://www.icanhazdadjoke.com/search',
    headers={"Accept": "application/json"},
    params={'term': f'{searchterm}'}
)
data = response.json()['results']
if len(data) > 1:
    print(f"I've got {len(data)} jokes about {searchterm}. Here's one:")
    selection = random.choice([i['joke'] for i in data])
    print(selection)
elif len(data) == 1:
    print(f"I've got one joke about {searchterm}. Here it is:")
    print(data[0]['joke'])
else:
    print(
        f'Sorry, I don\'t have any jokes about '
        f'{searchterm}! Please try again.')
