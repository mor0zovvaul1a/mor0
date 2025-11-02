import csv
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sample.csv")

def read_csv(path):
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

if __name__ == "__main__":
    data = read_csv(DATA_PATH)
    for row in data:
        print(f"{row['name']} ({row['age']}) - {row['city']}")
