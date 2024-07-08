import csv
import random
from faker import Faker

fake = Faker()

def generate_csv(filename, num_records):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['first_name', 'last_name', 'address', 'date_of_birth'])
        for _ in range(num_records):
            first_name = fake.first_name()
            last_name = fake.last_name()
            address = fake.address().replace('\n', ' ')
            date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90)
            writer.writerow([first_name, last_name, address, date_of_birth])

# Generate a large CSV file with 2 million records
generate_csv('input.csv', 2000000)
