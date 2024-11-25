import argparse
import sys
import csv


countries_set = {'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei',
'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros',
'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Czechoslovakia',
'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Germany', 'England'
'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia',
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

codes_set = {
    'AFG', 'ALB', 'ALG', 'AND', 'ANG', 'ANT', 'ARG', 'ARM', 'AUS', 'AUT', 'AZE',
    'BAH', 'BRN', 'BAN', 'BAR', 'BLR', 'BEL', 'BIZ', 'BEN', 'BHU', 'BOL', 'BIH',
    'BOT', 'BRA', 'BRU', 'BUL', 'BUR', 'BDI', 'CAM', 'CMR', 'CAN', 'CAF', 'CHA',
    'CHI', 'CHN', 'COL', 'COM', 'CRC', 'CRO', 'CUB', 'CYP', 'CZE', 'TCH', 'DEN',
    'DJI', 'DMA', 'DOM', 'GDR', 'ECU', 'EGY', 'ESA', 'GEQ', 'ERI', 'EST', 'ETH',
    'FIJ', 'FIN', 'FRA', 'GAB', 'GAM', 'GEO', 'GER', 'GHA', 'GRE', 'GRN', 'GUA',
    'GUI', 'GUY', 'HAI', 'HON', 'HUN', 'ISL', 'IND', 'INA', 'IRI', 'IRQ', 'IRL',
    'ISR', 'ITA', 'JAM', 'JPN', 'JOR', 'KAZ', 'KEN', 'KIR', 'KOS', 'KUW', 'KGZ',
    'LAO', 'LAT', 'LIB', 'LES', 'LBR', 'LBA', 'LIE', 'LTU', 'LUX', 'MAD', 'MAW',
    'MAS', 'MDV', 'MLI', 'MLT', 'MHL', 'MTN', 'MRI', 'MEX', 'MDA', 'MON', 'MGL',
    'MNE', 'MAR', 'MOZ', 'MYA', 'NAM', 'NRU', 'NEP', 'NED', 'NZL', 'NCA', 'NIG',
    'NGR', 'PRK', 'NOR', 'OMA', 'PAK', 'PLW', 'PLE', 'PAN', 'PNG', 'PAR', 'PER',
    'PHI', 'POL', 'POR', 'QAT', 'ROU', 'RUS', 'RWA', 'SKN', 'LCA', 'VIN', 'SAM',
    'SMR', 'STP', 'KSA', 'SEN', 'SRB', 'SEY', 'SLE', 'SGP', 'SVK', 'SLO', 'SOL',
    'SOM', 'RSA', 'KOR', 'SSD', 'URS', 'ESP', 'SRI', 'SDN', 'SUR', 'SWE', 'SUI',
    'SYR', 'TJK', 'TAN', 'THA', 'TOG', 'TGA', 'TTO', 'TUN', 'TUR', 'TKM', 'TUV',
    'UGA', 'UKR', 'UAE', 'USA', 'URU', 'UZB', 'VAN', 'VEN', 'VIE', 'FRG', 'YEM',
    'YUG', 'ZAM', 'ZIM'
}



parser = argparse.ArgumentParser('tasks 2 and 4')

parser.add_argument('-total', type=int, help='type year to get info about all medals for this year')

def get_data():
    with open('data.tsv') as file:
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)
        rows  = []
        for row in reader:
            rows.append(row)
    return rows, header

def total_arg():
    rows, header = get_data()
    year = parser.parse_args().total
    TEAM = header.index('Team')
    MEDAL = header.index('Medal')
    YEAR = header.index('Year')
    team_medals = {}
    for row in rows:
        if year == int(row[YEAR]) and row[MEDAL] not in ['N/A', 'NA']:
            team_medals.setdefault(row[TEAM], {}).setdefault(row[MEDAL], 0)
            team_medals[row[TEAM]][row[MEDAL]] += 1
    return team_medals

def fin_return():
    temp_dict = total_arg()
    fin_dict = {}
    if temp_dict == {}:
        return 'Error, no such year'
    for key in temp_dict.keys():
        if key in countries_set:
            fin_dict[key] = temp_dict[key]
    for country, medals_dict in fin_dict.items():
        bronze = medals_dict.get('Bronze', 0)
        silver = medals_dict.get('Silver', 0)
        gold = medals_dict.get('Gold', 0)
        print(f"'{country}' - {gold} - {silver} - {bronze}")

#task4

parser.add_argument('-interactive', help='Type anything to start interactive. There you can enter country(name or code) to get info(first participation in the Olympiad, best year, worst year, and average number of medals')

def interactive():
    start = parser.parse_args().interactive
    team = input("Enter team(exit to break) : ")
    if team == 'exit':
        return "Exit"
    rows, header = get_data()
    TEAM = header.index('Team')
    MEDAL = header.index('Medal')
    YEAR = header.index('Year')
    NOC = header.index('NOC')
    ID = header.index('ID')
    CITY = header.index('City')
    list_years = []
    unique_list = []
    year_medals = {}
    id_list = []
    medals = []
    year_city_dict = {}

    if len(team) ==3:
        team = team.upper()
    if len(team) > 3:
        team = team.lower().capitalize()
    if team in countries_set or team in codes_set:
        if len(team) == 3:
            for row in rows:
                if row[NOC] == team:
                    list_years.append(row[YEAR])
                    year_city_dict[row[YEAR]] = row[CITY]
        elif len(team) > 3:
            for row in rows:
                if row[TEAM] == team:
                    list_years.append(row[YEAR])
                    year_city_dict[row[YEAR]] = row[CITY]

        for item in sorted(list_years):
            if item not in unique_list:
                unique_list.append(item)

        for row in rows:
            if len(team) == 3 and row[NOC] == team and row[ID] not in id_list:
                year = row[YEAR]
                medal = row[MEDAL]
                if medal not in ['N/A', 'NA']:
                    id_list.append(row[ID])
                    year_medals.setdefault(team, {}).setdefault(year, {}).setdefault(medal, 0)
                    year_medals[team][year][medal] += 1
            if len(team) > 3 and row[TEAM] == team and row[ID] not in id_list:
                year = row[YEAR]
                medal = row[MEDAL]
                if medal not in ['N/A', 'NA']:
                    id_list.append(row[ID])
                    year_medals.setdefault(team, {}).setdefault(year, {}).setdefault(medal, 0)
                    year_medals[team][year][medal] += 1
    else:
        print("Sorry, no such team. Lets start again...")
        interactive()

    gold_overall = 0
    silver_overall = 0
    bronze_overall = 0
    year_medals[team] = dict(sorted(year_medals[team].items()))
    for year in sorted(unique_list):
        if year in year_medals.get(team, {}):
            medals.append(sum(year_medals[team][year].values()))
            if 'Gold' in year_medals[team][year]:
                gold_overall += year_medals[team][year]['Gold']
            if 'Silver' in year_medals[team][year]:
                silver_overall += year_medals[team][year]['Silver']
            if 'Bronze' in year_medals[team][year]:
                bronze_overall += year_medals[team][year]['Bronze']
        else:
            medals.append(0)
            continue

    total_medals_dict = {}
    for year in sorted(unique_list):
        if year in year_medals.get(team, {}):
            total_medals = sum(year_medals[team][year].values())
            total_medals_dict[year] = total_medals
        else:
            total_medals = 0
            total_medals_dict[year] = total_medals
    total_medals = list(sorted(total_medals_dict.items(), key=lambda item: item[1]))

    avg_gold = gold_overall // len(unique_list)
    avg_silver = silver_overall // len(unique_list)
    avg_bronze = bronze_overall // len(unique_list)


    max_medals_index = medals.index(max(medals))
    min_medals_index = medals.index(min(medals))
    year_with_max_medals = total_medals[-1][0]
    year_with_min_medals = total_medals[0][0]

    try:
        max_medals_dict = year_medals[team][year_with_max_medals]
    except KeyError:
        max_medals_dict = 0
    try:
        min_medals_dict = year_medals[team][year_with_min_medals]
    except KeyError:
        min_medals_dict = 0

    sorted_city = sorted(year_city_dict.items())

    print(f'Year with most medals is {year_with_max_medals}. Sum = {total_medals[-1][1]}. Here is all of them {max_medals_dict}')
    print(f'Year with least medals is {year_with_min_medals}. Sum = {total_medals[0][1]}. Here is all of them {min_medals_dict}')
    print(f'First participation in the Olympiad is {sorted_city[0][0]} in {sorted_city[0][1]}')
    print(f'Average amount of each medal : Gold - {avg_gold}, Silver - {avg_silver}, Bronze - {avg_bronze}.')
    stop = input('Type anything to continue. Type "stop" to stop :')
    if stop != 'stop':
        interactive()
    return "Stop"
