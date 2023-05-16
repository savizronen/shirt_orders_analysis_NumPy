import csv_funcs
import analysis_funcs

file_path = 'random_shirts.csv'
data = csv_funcs.read_csv_to_np_array(file_path)

# 1. Calculate the average price
avg_price = analysis_funcs.calculate_average_price(data)
print("Average price:", avg_price)
print()

# 2. Find the maximum units in stock
max_stock = analysis_funcs.find_maximum_stock(data)
print("Maximum units in stock:", max_stock)
print()

# 3. Extract product names
product_names = analysis_funcs.extract_product_names(data)
print("Product names:", product_names)
print()

# 4. Calculate the total stock
total_stock = analysis_funcs.calculate_total_stock(data)
print("Total stock:", total_stock)
print()

# 5. Find the index of the most expensive product
most_expensive_index = analysis_funcs.find_most_expensive_product(data)
print("Index of the most expensive product:", most_expensive_index)
print()

# 6. Sort the data by price in descending order
sorted_data = analysis_funcs.sort_data_by_price(data)
print("Sorted data by price (descending):")
print(sorted_data)
print()

# 7. Get the number of products with price above $150
above_150_count = analysis_funcs.count_products_above_150(data)
print("Number of products with price above $150:", above_150_count)
print()

# 8. Calculate the total value of each product (price * units in stock)
product_values = analysis_funcs.calculate_product_values(data)
print("Product values:", product_values)
print()

# 10. Calculate the total value of all products (price * units in stock)
total_value = analysis_funcs.calculate_total_value(data)
print("Total value of all products:", total_value)
print()

# 11. Calculate the median price
median_price = analysis_funcs.calculate_median_price(data)
print("Median price:", median_price)
print()

# 12. Calculate the range of units in stock
stock_range = analysis_funcs.calculate_stock_range(data)
print("Range of units in stock:", stock_range)
print()

# 13. Count the number of products with even product IDs
even_ids_count = analysis_funcs.count_products_with_even_ids(data)
print("Number of products with even IDs:", even_ids_count)
print()

# 14. Calculate the standard deviation of prices
price_std = analysis_funcs.calculate_price_std(data)
print("Standard deviation of prices:", price_std)
print()

# 15. Get the products with stock less than 20
low_stock_products = analysis_funcs.get_products_with_low_stock(data)
print("Products with stock less than 20:")
print(low_stock_products)
print()

# 16. Get the products with stock greater than a given threshold
threshold = 498
products_with_high_stock = analysis_funcs.get_products_with_high_stock(data, threshold)
print("Products with stock greater than", threshold, ":")
print(products_with_high_stock)
print()

# 17. Calculate the average units in stock
average_stock = analysis_funcs.calculate_average_stock(data)
print("Average units in stock:", average_stock)
print()

# 18. Calculate the median units in stock
median_stock = analysis_funcs.calculate_median_stock(data)
print("Median units in stock:", median_stock)
print()

# 19. Calculate the 25th percentile of prices
percentile_value = 25  # The desired percentile value
price_percentile = analysis_funcs.calculate_price_percentile(data, percentile_value)
print(f"{percentile_value}th percentile of prices:", price_percentile)
print()

# 20. Count the number of products with names starting with a specific letter
letter = 'S'  # Specify the letter you want to count products starting with
product_count = analysis_funcs.count_products_starting_with_letter(data, letter)
print(f"Number of products starting with letter '{letter}': {product_count}")

print()

# 21. Calculate the total value of products with price below a given threshold
threshold = 150
total_value_below_threshold = analysis_funcs.calculate_total_value_below_threshold(data, threshold)
print("Total value of products with price below", threshold, ":", total_value_below_threshold)



