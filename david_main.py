import argparse
import sys
import csv

parser = argparse.ArgumentParser('tasks 2 and 4')

parser.add_argument('-total', type=int, help='type year to get info about all medals for this year')
year = parser.parse_args()

def get_data():
    with open('data.tsv') as file:
        reader = csv.reader(file, delimiter='\t')
        header = next(reader)
        rows  = []
        for row in reader:
            rows.append(row)
    return rows, header

def total_arg(year):
    rows, header = get_data()
    TEAM = header.index('Team')
    MEDAL = header.index('Medal')
    YEAR = header.index('Year')
    team_medals = {}
    for row in rows:
        if year == int(row[YEAR]) and row[MEDAL] not in ['N/A', 'NA']:
            team_medals.setdefault(row[TEAM], {}).setdefault(row[MEDAL], 0)
            team_medals[row[TEAM]][row[MEDAL]] += 1
    if team_medals == {}:
        return 'Error, no such year'
    return team_medals


print(total_arg(1964))




