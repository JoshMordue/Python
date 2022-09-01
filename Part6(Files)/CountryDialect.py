import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = countries_data.read()
    country_dialect = csv.sn
    country_reader = csv.reader(countries_data, delimiter='|')
    for row in country_reader:
        print(row)

