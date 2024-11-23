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
