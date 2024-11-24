
from validation import valid_medal, valid_year, valid_country
from parser import created_parser
from countries import COUNTRIES_SET
from work_with_data import get_data, filter_data

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
            results[country] = "No medals won."
    return results

def top_player(filepath, genders:list, categories:list):
    age_ranges = {
        "1": (18, 25),
        "2": (25, 35),
        "3": (35, 50),
        "4": (50, float('inf'))
    }
    rows, header = get_data(filepath)
    NAME = header.index('Name')
    GENDER = header.index('Sex')
    AGE = header.index('Age')
    MEDAL = header.index('Medal')

    valid_genders = ['M', 'F']
    for gender in genders:
        if not gender in valid_genders:
            print(f'Invalid gender {gender} input. "M" for male and "F" for female')
            return

    result = []
    for gender in genders:
        for category in categories:
            if category not in age_ranges:
                print(f'Sorry, invalid age category {category}')
                return
            age_min, age_max = age_ranges[category]
            player_medals = {}
            for row in rows:
                if gender == row[GENDER] and valid_medal(row[MEDAL]):
                    try:
                        age = int(row[AGE])
                        if age_min <= age < age_max:
                            player = row[NAME]
                            player_medals.setdefault(player, 0)
                            player_medals[player] += 1
                    except ValueError:
                        continue
            if player_medals:
                best_player = max(player_medals, key=player_medals.get)
                max_medals = player_medals[best_player]
                result.append(f"{best_player} with {max_medals} medals is the best in category {category} ({age_min}-{age_max} years)")
            else:
                result.append(f"No medals won in category {category} ({age_min}-{age_max} years)")
    return '\n'.join(result)

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