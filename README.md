![a list of all countries worldwide in json and csv](https://github.com/lorey/list-of-countries/raw/master/list-of-countries.jpg)

# List of all countries worldwide
This is a repository containing lists of all countries worldwide in several formats. The data is taken from
[Wikipedia](https://en.wikipedia.org/wiki/ISO_3166-1) and thus under
[CC BY-SA unported license](https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3.0_Unported_License).

## Formats

There are currently two file formats: CSV and JSON.

### CSV
The CSV file is located under [csv/countries.csv](csv/countries.csv). It uses semicolons as separators as there are
commas in the country names. You can open CSV files in almost any spreadsheet software, e.g. Microsoft Excel, Libre
Office Calc, etc.

    name;code_alpha_two;code_numeric;code_alpha_three
    Afghanistan;AF;004;AFG
    Åland Islands;AX;248;ALA
    Albania;AL;008;ALB
    Algeria;DZ;012;DZA
    ...

### JSON
The JSON files are located in [json/](json/). There are two versions A readable version with indentation:
[json/countries-readable.json](json/countries-readable.json)

    [
        {
            "code_alpha_three": "AFG",
            "code_alpha_two": "AF",
            "code_numeric": "004",
            "name": "Afghanistan"
        },
        {
            "code_alpha_three": "ALA",
            "code_alpha_two": "AX",
            "code_numeric": "248",
            "name": "Åland Islands"
        },
        {
            "code_alpha_three": "ALB",
            "code_alpha_two": "AL",
            "code_numeric": "008",
            "name": "Albania"
        },
        {
            "code_alpha_three": "DZA",
            "code_alpha_two": "DZ",
            "code_numeric": "012",
            "name": "Algeria"
        },
        {
            "code_alpha_three": "ASM",
            "code_alpha_two": "AS",
            "code_numeric": "016",
            "name": "American Samoa"
        },
        ...

And a compact version: [json/countries.json](json/countries.json)

    [{"code_alpha_three": "AFG", "code_alpha_two": "AF", "code_numeric": "004", "name": "Afghanistan"}, ...

## Misc

Picture licensed under CC0 by [Lena Bell](https://unsplash.com/@lenabell?photo=mluSdDeOksc).