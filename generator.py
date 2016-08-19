import json

import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/ISO_3166-1'

r = requests.get(url)
page = r.text
soup = BeautifulSoup(page, 'html.parser')

rows = [row for row in soup.table.find_all('tr')]
country_rows = rows[1:]
countries = []
for row in country_rows:
    columns = row.find_all('td')

    first_column_links = columns[0].find_all('a')
    name = [a for a in first_column_links if a.has_attr('title')][0]['title']

    code_alpha_two = columns[1].text
    code_alpha_three = columns[2].text
    code_numeric = columns[3].text

    country = {
        'name': name,
        'code_numeric': code_numeric,
        'code_alpha_two': code_alpha_two,
        'code_alpha_three': code_alpha_three,
    }
    countries.append(country)

# json
json_string = json.dumps(countries, ensure_ascii=False)
with open('json/countries.json', 'w') as file:
    file.write(json_string)

# readable json
json_string = json.dumps(countries, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
with open('json/countries-readable.json', 'w') as file:
    file.write(json_string)