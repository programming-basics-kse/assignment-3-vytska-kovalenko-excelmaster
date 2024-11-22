import argparse

parser = argparse.ArgumentParser('tasks 2 and 4')

parser.add_argument('-total', type=int, help='type year to get info about all medals for this year')
year = parser.parse_args()
