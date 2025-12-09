def make_chai(tea, milk, sugar):
    print(f"Making Chai with {'Milk,' if milk == True else ''} {tea} tea, {sugar} sugar ")

make_chai("Black", True, "Low")
make_chai(tea="Ginger", sugar="Medium", milk=False)

def special_chai(*ingredients, **extras):
    print(f"Ingredients: {ingredients}")
    print(f"Extras: {extras}")

special_chai("Green", "Ginger", sugar="Low", foam="Yes")