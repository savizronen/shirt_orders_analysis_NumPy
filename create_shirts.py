import csv
import random


def generate_random_shirt_name():
    adjectives = ["Cool", "Awesome", "Funky", "Stylish", "Trendy", "Hip", "Unique", "Vibrant", "Sleek", "Elegant"]
    colors = ["Red", "Blue", "Green", "Yellow", "Black", "White", "Gray", "Purple", "Pink", "Orange"]
    patterns = ["Striped", "Polka Dot", "Plaid", "Tie-Dye", "Camouflage", "Geometric", "Floral", "Abstract", "Checkered", "Houndstooth"]
    nouns = ["T-Shirt", "Hoodie", "Polo", "Tank Top", "Sweater", "Blouse", "Button-Up", "Long Sleeve", "Crop Top", "Sweatshirt"]

    random_name = f"{random.choice(adjectives)} {random.choice(colors)} {random.choice(patterns)} {random.choice(nouns)}"
    return random_name



def generate_random_shirts_csv(filename, num_shirts):
    header = ["product_id", "product_name", "price", "units_in_stock"]
    shirts = []

    for i in range(1,num_shirts):
        product_id = i
        product_name = generate_random_shirt_name()
        price = random.randint(5, 1000)
        units_in_stock = random.randint(2, 500)
        shirts.append([product_id, product_name, price, units_in_stock])

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(shirts)

    print(f"{num_shirts} random shirts have been generated and saved to {filename}.")


# Usage example
generate_random_shirts_csv("random_shirts.csv", 1000)
