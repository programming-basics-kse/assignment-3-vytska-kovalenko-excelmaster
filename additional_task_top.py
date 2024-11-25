from david_main import get_data
import argparse
from parser import *

parser = argparse.ArgumentParser('tasks "top"')
parser.add_argument('--top_dav', help='Find top players by genders and age category. Made by David')


def top():
    ages = {
        '1' : (18, 25),
        '2' : (25, 35),
        '3' : (35, 50),
        '4' : (50, 999)
    }
    input = parser.parse_args().top_dav
    rows, header = get_data()
    NAME = header.index('Name')
    GENDER = header.index('Sex')
    AGE = header.index('Age')
    MEDAL = header.index('Medal')
    ID = header.index('ID')
    id_list = []
    genders = [item for item in input if item in ['M', 'F']]
    age_groups = [item for item in input if item in ages]
    for gender in genders:
        for age_group in age_groups:
            if age_group not in ages:
                print("Invalid input")
                continue
            age_min, age_max = ages[age_group]
            medals = {}
            for row in rows:
                try:
                    age = int(row[AGE])
                except ValueError:
                    continue
                if age in range(age_min, age_max) and row[ID] not in id_list and row[MEDAL] not in ['N/A', 'NA'] and row[GENDER] == gender:
                    medals.setdefault(row[NAME], {}).setdefault('Medals', 0)
                    medals[row[NAME]]['Medals'] += 1
            if medals:
                sorted_data = sorted(medals.items(), key=lambda x: x[1]['Medals'])
            top = sorted_data[-1]
            name = top[0]
            medals = top[1]['Medals']


            print(f'Output data : {gender}, {age_group}. Name : {name}, Amount of medals : {medals}')

