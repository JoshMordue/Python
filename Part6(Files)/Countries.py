input_filename = 'country_info.txt'

countries = {}

with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing code': dialing,
            'timezone': timezone,
            'currency': currency,
        }

        countries[country.casefold()] = country_dict
        countries[code.casefold()] = country_dict


countries_no_capitals = []

print(f"The following countries do not have an Capital city :")

for entries in countries.values():
    if entries['capital'] == '':
        countries_no_capitals.append(entries['name'])

no_capitals = (sorted(set(countries_no_capitals)))

for i in range(len(no_capitals)):
    print(f"{no_capitals[i]}"
    )

print()

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(country_data['capital'])
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country == 'quit':
        break


#
# countries_no_capitals = set()
#
# print(f"The following countries do not have an Capital city :")
#
# for entries in countries.values():
#     if entries['capital'] == '':
#         countries_no_capitals.add(entries['name'])
#
# print(countries_no_capitals, sep='\n\t')