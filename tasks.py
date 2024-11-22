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

def print_medalists(filepath, country, year):
    rows, header = get_data(filepath)
    if not valid_country(rows, header, country):
        return f"{country} country does not exist"
    if not valid_year(rows, header, year):
        return f"In {year} year Olympics did not took place"
    filtered_rows = filter_data(rows, header, country, year)
    NAME = header.index('Name')
    EVENT = header.index('Event')
    MEDAL = header.index('Medal')
    results = []
    for row in filtered_rows[:10]:
        if valid_medal(row[MEDAL]):
            results.append(f'{row[NAME]} - {row[EVENT]} - {row[MEDAL]}')
    if results:
        return f"{len(results)} first results for {country} in {year}: {'\n'.join(results)}"
    else:
        return f"{country} didn't get anything in {year}"

def overall_statistics(filepath, countries):
    rows, header = get_data(filepath)
    COUNTRY = header.index('Team')
    NOC = header.index('NOC')
    YEAR = header.index('Year')
    MEDAL = header.index('Medal')
    results = {}
    for country in countries:
        countries_data = []

        for row in rows:
            if row[COUNTRY] == country or row[NOC] == country:
                countries_data.append(row)

        medals_by_year = {}
        for row in countries_data:
            if valid_medal(row[MEDAL]):
                year = row[YEAR]
                medals_by_year.setdefault(year, 0)
                medals_by_year[year] += 1

        if medals_by_year:
            best_year = max(medals_by_year, key=medals_by_year.get)
            max_medals = medals_by_year[best_year]
            results[country] = f"{best_year} with {max_medals} medals"
    return results

def main():

    parser = argparse.ArgumentParser('Processing Olympic medalists data')
    parser.add_argument('filepath', help='Path to the data')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--medals',nargs=2, required=True, help='Enter country (Team or NOC) and year')
    group.add_argument('--overall', nargs='+', help='Enter one or more countries to get their overall')
    parser.add_argument('--output', help='Argument is optional: it is saving results to file')


    args = parser.parse_args()
    country, year = args.medals
    year = int(year)
    result = print_medalists(args.filepath, country, year)
    print(result)
    if args.output:
        with open(args.output, 'w') as file:
            file.write(result)
        print(f"Results saved to '{args.output}'")

if __name__ == '__main__':
    main()








