import numpy as np

# 1. Calculate the average price
def calculate_average_price(data):
    prices = data[:, 2].astype(float)
    return np.mean(prices)

# 2. Find the maximum units in stock
def find_maximum_stock(data):
    stock = data[:, 3].astype(int)
    return np.max(stock)

# 3. Extract product names
def extract_product_names(data):
    return data[:, 1]

# 4. Calculate the total stock
def calculate_total_stock(data):
    stock = data[:, 3].astype(int)
    return np.sum(stock)

# 5. Find the index of the most expensive product
def find_most_expensive_product(data):
    price = data[:, 2].astype(int)  # Convert price column to int data type
    max_price_index = np.argmax(price)
    return max_price_index+1


# 6. Sort the data by price in descending order
def sort_data_by_price(data):
    # Convert price and units in stock columns to numeric data types
    price = data[:, 2].astype(int)
    units_in_stock = data[:, 3].astype(int)

    # Sort the data based on price in descending order
    sorted_indices = np.argsort(price)[::-1]
    sorted_data = data[sorted_indices]

    return sorted_data

# 7. Get the number of products with price above $150
def count_products_above_150(data):
    prices = data[:, 2].astype(int)  # Convert 'price' column to int
    return np.sum(prices > 150)

# 8. Calculate the total value of each product (price * units in stock)
def calculate_product_values(data):
    return data[:, 2].astype(int) * data[:, 3].astype(int)

# 9. Calculate the median price
def calculate_median_price(data):
    return np.median(data[:, 2].astype(int))

# 10. Calculate the range of units in stock
def calculate_stock_range(data):
    return np.ptp(data[:, 3].astype(int))

# 11. Count the number of products with even product IDs
def count_products_with_even_ids(data):
    return np.sum(data[:, 0].astype(int) % 2 == 0)

# 12. Calculate the standard deviation of prices
def calculate_price_std(data):
    return np.std(data[:, 2].astype(int))

# 13. Get the products with stock less than 20
def get_products_with_low_stock(data):
    return data[data[:, 3].astype(int) < 20]

# 14. Get the products with stock greater than a given threshold
def get_products_with_high_stock(data, threshold):
    return data[data[:, 3].astype(int)  > threshold]

# 15. Calculate the total value of all products (price * units in stock)
def calculate_total_value(data):
    return np.sum(data[:, 2].astype(int) * data[:, 3].astype(int))

# 16. Calculate the average units in stock
def calculate_average_stock(data):
    return np.mean(data[:, 3].astype(int))

# 17. Calculate the median units in stock
def calculate_median_stock(data):
    return np.median(data[:, 3].astype(int))

# 18. Calculate the 25th percentile of prices
def calculate_price_percentile(data, percentile):
    return np.percentile(data[:, 2].astype(int), percentile)

# 19. Count the number of products with names starting with a specific letter
def count_products_starting_with_letter(data, letter):
    count = 0
    for name in data[:, 1]:
        if name.startswith(letter):
            count += 1
    return count

# 20. Calculate the total value of products with price below a given threshold
def calculate_total_value_below_threshold(data, threshold):
    prices = data[:, 2].astype(int)
    units_in_stock = data[:, 3].astype(int)
    mask = prices < threshold
    return np.sum(prices[mask] * units_in_stock[mask])
