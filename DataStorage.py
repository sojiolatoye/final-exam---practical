import csv

class DataStorage:
    @staticmethod
    def get_data():
        data = []
        with open("input_file.csv", "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                data.append(row)
        return data