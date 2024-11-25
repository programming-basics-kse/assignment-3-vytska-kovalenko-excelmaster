
from validation import valid_medal, valid_year, valid_country, valid_age, valid_gender
from parser import created_parser
from countries import COUNTRIES_SET
from work_with_data import get_data, filter_data
from additional_task_vytska import top_player

def print_medalists(filepath, country, year, countries_set):
    rows, header = get_data(filepath)
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
        if row[NAME] not in unique_medalists and valid_medal(row[MEDAL]):
            unique_medalists.add(row[NAME])
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
    valid_countries = [country for country in countries if valid_country(country, rows, countries_set, NOC)]
    unique_medalists = set()
    results = {}
    for country in valid_countries:
        medals_by_year = {}
        for row in rows:
            if row[COUNTRY] == country or row[NOC] == country:
                if valid_medal(row[MEDAL]) and row[NAME] not in unique_medalists:
                    year = row[YEAR]
                    medals_by_year.setdefault(year, 0)
                    medals_by_year[year] += 1

        if medals_by_year:
            best_year = max(medals_by_year, key=medals_by_year.get)
            max_medals = medals_by_year[best_year]
            results[country] = f"{best_year} with {max_medals} medals"
        else:
            results[country] = "No medals won"
    return results

def main():
    parser = created_parser()
    args = parser.parse_args()
    if args.medals:
        country, year = args.medals
        year = int(year)
        result = print_medalists(args.filepath, country, year, COUNTRIES_SET)
    elif args.overall:
        result_dict = overall_statistics(args.filepath, args.overall,COUNTRIES_SET)
        result = ''
        for country, info in result_dict.items():
            result += country + ": " + str(info) + "\n"
        result = result.strip()
    elif args.top:
        if len(args.top) >= 2 and args.top[1] not in ['M', 'F']:
            genders = args.top[0]
            categories = list(map(str, args.top[1:]))
        else:
            genders = args.top[:2]
            categories = list(map(str, args.top[2:]))
        result = top_player(args.filepath, genders, categories)

    print(result)

    if args.output:
        with open(args.output, 'w') as file:
            file.write(result)
        print(f"Results saved to '{args.output}'")

if __name__ == '__main__':
    main()