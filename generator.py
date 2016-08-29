import codecs
import urllib

import requests

import csv
import json

mapping = [
    'alpha_2',
    'alpha_3',
    'numeric',
    'fips',
    'name',
    'capital',
    'area',
    'population',
    'continent',
    'tld',
    'currency_code',
    'currency_name',
    'phone',
    'postal_code_format',
    'postal_code_regex',
    'languages',
    'geoname_id',
    'neighbours',
    'eqivalent_fips_code',
]

countries = []
url = "http://download.geonames.org/export/dump/countryInfo.txt"
stream = urllib.request.urlopen(url)
reader = codecs.getreader("utf-8")
reader = csv.reader(reader(stream), delimiter='\t')

non_comment_rows = [row for row in reader if row[0][0] != '#']
for row in non_comment_rows:
    if row[0][0] != '#':
        country = {}

        # read files from csv and map them to dict
        for i in range(0, len(row)):
            csv_row = row[i]
            csv_row_title = mapping[i]

            country[csv_row_title] = csv_row

        # add missing keys as None
        for key in mapping:
            if key not in country:
                country[key] = None

        countries.append(country)

# csv
keys = countries[0].keys()
with open('csv/countries.csv', 'w') as file:
    dict_writer = csv.DictWriter(file, sorted(keys), delimiter=";")
    dict_writer.writeheader()
    dict_writer.writerows(countries)

# json
json_string = json.dumps(countries, sort_keys=True, ensure_ascii=False)
with open('json/countries.json', 'w') as file:
    file.write(json_string)

# readable json
json_string = json.dumps(countries, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
with open('json/countries-readable.json', 'w') as file:
    file.write(json_string)

# php (I'm sorry)
php_string = '<?php\n$countries = [\n'
for country in countries:
    php_string += '    [\n'
    for key in sorted(country):
        value = country[key]
        if value is not None and value != "":
            php_string += '        "' + key + '" => "' + value + '",\n'
        else:
            php_string += '        "' + key + '" => null,\n'
    php_string += '    ],\n'
php_string += '\n];'
with open('php/array.php', 'w') as file:
    file.write(php_string)
