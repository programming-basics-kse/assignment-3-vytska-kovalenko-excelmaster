from validation import valid_medal, valid_gender, valid_age
from work_with_data import get_data

def top_player(filepath, genders:list, categories:list):
    age_ranges = {
        '1': (18, 25),
        '2':(25, 35),
        '3':(35,50),
        '4':(50, float('inf'))
    }
    rows, header = get_data(filepath)
    NAME = header.index('Name')
    GENDER = header.index('Sex')
    AGE = header.index('Age')
    MEDAL = header.index('Medal')
    ID = header.index('ID')
    unique_ids = set()
    for gender in genders:
        if not valid_gender(gender):
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
                age = valid_age(row[AGE], age_min, age_max)
                if gender == row[GENDER] and valid_medal(row[MEDAL]) and age and row[ID] not in unique_ids:
                    player = row[NAME]
                    player_medals.setdefault(player, 0)
                    player_medals[player] += 1
            if player_medals:
                best_player = max(player_medals, key=player_medals.get)
                max_medals = player_medals[best_player]
                result.append(f"{best_player} with {max_medals} medals is the best in category {category} ({age_min}-{age_max} years)")
            else:
                result.append(f"No medals won in category {category} ({age_min}-{age_max} years)")
    return '\n'.join(result)
