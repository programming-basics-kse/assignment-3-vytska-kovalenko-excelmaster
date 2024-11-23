import argparse
import csv

def get_data(filepath):
    with open(filepath) as file:
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)
        rows  = []
        for row in reader:
            rows.append(row)
    return rows, header

def filter_data(rows, header,country, year):
    COUNTRY = header.index('Team')
    NOC = header.index('NOC')
    YEAR = header.index('Year')
    filtered = []
    year = str(year)
    for row in rows:
        if row[COUNTRY]==country or row[NOC]==country:
            if row[YEAR]==year:
                filtered.append(row)
    return filtered

def valid_medal(medal):
    if medal == 'Gold' or medal == 'Silver' or medal =='Bronze':
        return True
    return False

def valid_country(rows, header, country):
    COUNTRY = header.index('Team')
    NOC = header.index('NOC')
    for row in rows:
        if country.lower() in row[COUNTRY].lower() or country.lower() == row[NOC].lower():
            return True
    return False

def valid_year(rows, header, year):
    YEAR = header.index('Year')
    for row in rows:
        if str(year) == row[YEAR]:
            return True
    return False

def print_medalists(filepath, country, year, countries_set):
    rows, header = get_data(filepath)
    COUNTRY = header.index('Team')
    NOC = header.index('NOC')
    if country not in countries_set and not any(row[NOC] == country for row in rows):
        return f"{country} is not a valid country."
    if not valid_year(rows, header, year):
        return f"In {year} year Olympics did not took place"
    filtered_rows = filter_data(rows, header, country, year)
    NAME = header.index('Name')
    EVENT = header.index('Event')
    MEDAL = header.index('Medal')
    unique_medalists = set()
    results = []
    for row in filtered_rows:
        medalist = row[NAME]
        if medalist not in unique_medalists and valid_medal(row[MEDAL]):
            unique_medalists.add(medalist)
            results.append(f'{row[NAME]} - {row[EVENT]} - {row[MEDAL]}')
            if len(results)==10:
                break
    if results:
        return f"{len(results)} first results for {country} in {year}: {'\n'.join(results)}"
    else:
        return f"{country} didn't get anything in {year}"

def overall_statistics(filepath, countries, countries_set):
    rows, header = get_data(filepath)
    COUNTRY = header.index('Team')
    NOC = header.index('NOC')
    YEAR = header.index('Year')
    MEDAL = header.index('Medal')
    NAME = header.index('Name')
    valid_countries = []
    unique_medalists = set()
    for country in countries:
        if country in countries_set or any(row[NOC] == country for row in rows):
            valid_countries.append(country)
    results = {}
    for country in valid_countries:
        medals_by_year = {}
        for row in rows:
            medalist = row[NAME]
            if row[COUNTRY] == country or row[NOC] == country:
                if valid_medal(row[MEDAL]) and medalist not in unique_medalists:
                    year = row[YEAR]
                    medals_by_year.setdefault(year, 0)
                    medals_by_year[year] += 1

        if medals_by_year:
            best_year = max(medals_by_year, key=medals_by_year.get)
            max_medals = medals_by_year[best_year]
            results[country] = f"{best_year} with {max_medals} medals"
        else:
            results[country] = "No medals won."
    return results

def main():

    parser = argparse.ArgumentParser('Processing Olympic medalists data')
    parser.add_argument('filepath', help='Path to the data')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--medals', nargs=2, help='Enter country (Team or NOC) and year')
    group.add_argument('--overall', nargs='+', help='Enter one or more countries to get their overall')
    parser.add_argument('--output', help='Argument is optional: it is saving results to file')

    args = parser.parse_args()
    countries_set = {'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
                     'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
                     'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
                     'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei',
                     'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
                     'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
                     'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Czechoslovakia',
                     'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Germany', 'England'
                                                                                              'Ecuador', 'Egypt',
                     'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
                     'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia',
                     'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guyana',
                     'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran',
                     'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
                     'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos',
                     'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
                     'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives',
                     'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico',
                     'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique',
                     'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand',
                     'Nicaragua', 'Niger', 'Nigeria', 'North Korea', 'Norway', 'Oman', 'Pakistan',
                     'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
                     'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
                     'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines',
                     'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
                     'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia',
                     'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan',
                     'Soviet Union', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden',
                     'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo',
                     'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan',
                     'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United States',
                     'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'West Germany',
                     'Yemen', 'Yugoslavia', 'Zambia', 'Zimbabwe'}
    if args.medals:
        country, year = args.medals
        year = int(year)
        result = print_medalists(args.filepath, country, year, countries_set)
    elif args.overall:
        result_dict = overall_statistics(args.filepath, args.overall,countries_set)
        result = ''
        for country, info in result_dict.items():
            result += country + ": " + str(info) + "\n"
        result = result.strip()

    print(result)

    if args.output:
        with open(args.output, 'w') as file:
            file.write(result)
        print(f"Results saved to '{args.output}'")

if __name__ == '__main__':
    main()