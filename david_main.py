import argparse
import sys
import csv

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
    year = 1964
    # year = parser.parse_args().total
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

def pretty_return():
    year = parser.parse_args().total
    temp_dict = total_arg()
    for country, medals_dict in temp_dict.items():
        bronze = medals_dict.get('Bronze', 0)
        silver = medals_dict.get('Silver', 0)
        gold = medals_dict.get('Gold', 0)
        print(f"'{country}' - {gold} - {silver} - {bronze}")

pretty_return()