import csv
import numpy as np

def read_csv_to_np_array(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
    return np.array(data)