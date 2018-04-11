def show_sandwich(*args):
    ingredients = [i for i in args]
    print(
        f"Your sandwich is made out of {', '.join(ingredients[:-1])} and {ingredients[-1]}.")


show_sandwich("tomatoes", "cheese", "lettuce")
show_sandwich("tomatoes", "cheese", "cucumber")
show_sandwich("tomatoes", "avodadoes")
