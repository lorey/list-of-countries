![a list of all countries worldwide in json and csv](https://github.com/lorey/list-of-countries/raw/master/list-of-countries.jpg)

# List of all countries worldwide
This is a repository containing lists of all countries worldwide in several formats. The data is taken from
[GeoNames](http://www.geonames.org/) and thus under [CC BY license](https://creativecommons.org/licenses/by/2.0/).

## Formats

There are currently three file formats: JSON, CSV, and PHP.

### JSON
The JSON files are located in [json/](json/). There are two versions A readable version with indentation:
[json/countries-readable.json](json/countries-readable.json)

    [
        {
            "alpha_2": "AD",
            "alpha_3": "AND",
            "area": "468",
            "capital": "Andorra la Vella",
            "continent": "EU",
            "currency_code": "EUR",
            "currency_name": "Euro",
            "eqivalent_fips_code": "",
            "fips": "AN",
            "geoname_id": "3041565",
            "languages": "ca",
            "name": "Andorra",
            "neighbours": "ES,FR",
            "numeric": "020",
            "phone": "376",
            "population": "84000",
            "postal_code_format": "AD###",
            "postal_code_regex": "^(?:AD)*(\\d{3})$",
            "tld": ".ad"
        },
        ...

And a compact version: [json/countries.json](json/countries.json)

    [{"alpha_2": "AD", "alpha_3": "AND", "area": "468", "capital": "Andorra la Vella", "continent": "EU", ...

### CSV
The CSV file is located under [csv/countries.csv](csv/countries.csv). It uses semicolons as separators as there are
commas in the country names. You can open CSV files in almost any spreadsheet software, e.g. Microsoft Excel, Libre
Office Calc, etc.

    phone;currency_name;geoname_id;alpha_2;currency_code;neighbours;area;numeric;capital;tld;eqivalent_fips_code;languages;postal_code_format;fips;postal_code_regex;alpha_3;continent;name;population
    376;Euro;3041565;AD;EUR;ES,FR;468;020;Andorra la Vella;.ad;;ca;AD###;AN;^(?:AD)*(\d{3})$;AND;EU;Andorra;84000
    971;Dirham;290557;AE;AED;SA,OM;82880;784;Abu Dhabi;.ae;;ar-AE,fa,en,hi,ur;;AE;;ARE;AS;United Arab Emirates;4975593
    93;Afghani;1149361;AF;AFN;TM,CN,IR,TJ,PK,UZ;647500;004;Kabul;.af;;fa-AF,ps,uz-AF,tk;;AF;;AFG;AS;Afghanistan;29121286
    ...

### PHP
The PHP file is located under [php/array.php](php/array.php) and contains the list of all countries in array notation.

    <?php
    $countries = [
        [
            "alpha_2" => "AD",
            "alpha_3" => "AND",
            "area" => "468",
            "capital" => "Andorra la Vella",
            "continent" => "EU",
            "currency_code" => "EUR",
            "currency_name" => "Euro",
            "eqivalent_fips_code" => null,
            "fips" => "AN",
            "geoname_id" => "3041565",
            "languages" => "ca",
            "name" => "Andorra",
            "neighbours" => "ES,FR",
            "numeric" => "020",
            "phone" => "376",
            "population" => "84000",
            "postal_code_format" => "AD###",
            "postal_code_regex" => "^(?:AD)*(\d{3})$",
            "tld" => ".ad",
        ],
        // ...

## Misc

Picture licensed under CC0 by [Lena Bell](https://unsplash.com/@lenabell?photo=mluSdDeOksc).