import csv


def print_web(csv_file_path):
    # Initialize an empty list to store the data from the CSV file
    data = []

    # Open the CSV file and read its content
    with open(csv_file_path, mode='r', newline='') as file:
        csv_reader = csv.DictReader(file)

        # Read the data from the CSV file and append it to the list
        for row in csv_reader:
            data.append(row)

    # Now, 'data' contains the content of the CSV file as a list of dictionaries
    # Each dictionary represents a row in the CSV file with keys as column headers
    return data



