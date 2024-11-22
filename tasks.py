import csv
import sys

def get_data():
    with open('data.tsv') as file:
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)
        rows  = []
        for row in reader:
            rows.append(row)
    return rows, header

def filter_data(country,year):
    rows, header = get_data()
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
def valid_country(country):
    rows, header = get_data()
    COUNTRY = header.index('Team')
    NOC = header.index('NOC')
    for row in rows:
        if country.lower() in row[COUNTRY].lower() or country.lower() == row[NOC].lower():
            return True
    return False

def valid_year(year):
    rows, header = get_data()
    YEAR = header.index('Year')
    for row in rows:
        if str(year) == row[YEAR]:
            return True
    return False

def print_medalists(country, year):
    if not valid_country(country):
        return f"{country} country does not exist"
    if not valid_year(year):
        return f"In {year} year Olympics did not took place"
    rows, header = get_data()
    filtered_rows = filter_data(country, year)
    NAME = header.index('Name')
    EVENT = header.index('Event')
    MEDAL = header.index('Medal')
    results = []
    for row in filtered_rows[:10]:
        if valid_medal(row[MEDAL]):
            results.append(f'{row[NAME]} - {row[EVENT]} - {row[MEDAL]}')
    if results:
        return f"{len(results)} first results: {'\n'.join(results)}"
    else:
        return f"{country} didn't get anything in {year}"

print(print_medalists('Poland', 1952))


def main():
    if len(sys.argv)<5:
        print('Invalid number of arguments')

    filepath = sys.argv[1]
    medal_flag = sys.argv[2]
    country = sys.argv[3]
    year = sys.argv[4]
    if len(sys.argv)>5 and sys.argv[5]=='--output':
        output_file = sys.argv[6]

    if medal_flag != '--medals':
        print('Second argument should be "--medals"')




