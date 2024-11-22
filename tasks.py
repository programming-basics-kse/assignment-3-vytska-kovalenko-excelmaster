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

def filter_data():
    pass
def print_medalists():
    pass


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




