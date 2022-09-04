import csv

input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'


countries = {}
with open(input_filename, encoding='utf-8', newline='') as country_file:
    dict_reader = csv.DictReader(country_file, delimiter='|')
    for row in dict_reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row

print(countries)

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['Capital']} with capital code: {country_data['CC']}")

    elif chosen_country == 'quit':
        break
