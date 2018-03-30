import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from random import choice


class Author:

    def __init__(self, author_tag):
        self.name = author_tag.contents[0]
        self.author_url = author_tag.find_next_sibling()['href']
        self.born = self.get_born(self.author_url)
        self.quotes = []

    def __repr__(self):
        return self.name

    def get_author_site(self, author_url):
        a_response = requests.get(urljoin(url, self.author_url))
        return BeautifulSoup(a_response.text, 'html.parser')

    def get_born(self, author_soup):
        a_soup = self.get_author_site(author_soup)
        return a_soup.find(class_='author-born-date').contents[0]

    def add_quote(self, quote_tag):
        self.quotes.append(Quote(quote_tag, self.name, self.born))


class Quote:

    def __init__(self, quote_tag, author, born):
        self.text = self.get_quote(quote_tag)
        self.author = author

    def __repr__(self):
        return self.text

    def get_quote(self, quote_tag):
        return quote_tag.contents[0]


def find_author(tag, db):
    for item in db:
        if item.name == tag:
            return item
    return None


def scrape_site(soup, db, url):
    quotes = soup.find_all(class_='quote')
    for q in quotes:
        author_tag = q.find(class_='author')
        quote_tag = q.find(class_='text')
        current_author = find_author(author_tag.contents[0], db)
        if current_author is None:
            current_author = Author(author_tag)
            db.append(current_author)
        current_author.add_quote(quote_tag)


def crawl_site(url, db):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    scrape_site(soup, quotes_db, url)
    next_button = soup.find(class_='next')
    if next_button:
        next_page = next_button.contents[1]['href']
        url = urljoin(url, next_page)
        crawl_site(url, db)


def print_db(db):
    for author in sorted(quotes_db, key=lambda x: x.name):
        print('-' * 80)
        print(f'\n{author.name}:\n')
        for quote in author.quotes:
            print(f'- {quote}')


def random_quote():
    return choice(
        tuple(quote[0] for quote in (author.quotes for author in quotes_db))
    )


def play():

    def hint(num):
        if num == 3:
            print(
                f"Here's a hint: The author was born in "
                f"{find_author(rand_quote.author, quotes_db).born}.")
        elif num == 2:
            print(
                f"Here's a hint: The author's first "
                f"name starts with {rand_quote.author[0]}")
        elif num == 1:
            print(f"Here's a hint: The author's last "
                  f"name starts with {rand_quote.author.split()[-1][0]}")

    def check(num):

        nonlocal guesses
        my_choice = input(f'Who said this? Guesses remaining: {guesses} ')
        if my_choice == rand_quote.author:
            print('You guessed correctly! Congratulations!')
            guesses = 0
        else:
            guesses -= 1
            hint(guesses)

    print("Here's a quote:\n")
    rand_quote = random_quote()
    guesses = 4
    print(f'{rand_quote}\n')
    while guesses:
        check(guesses)
    print(f"The author's name was {rand_quote.author}")
    game_input = input("Would you like to play again (y/n)? ")
    if game_input[0] == 'y':
        play()


quotes_db = []
url = 'http://quotes.toscrape.com'
crawl_site(url, quotes_db)
play()
print("Here's a list of every author and their quotes:\n")
print_db(quotes_db)
