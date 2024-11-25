import argparse
def created_parser():
    parser = argparse.ArgumentParser('Processing Olympic medalists data')
    parser.add_argument('--filepath', help='Path to the data')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--medals', nargs=2, help='Enter country (Team or NOC) and year')
    group.add_argument('--overall', nargs='+', help='Enter one or more countries to get their overall')
    group.add_argument('--top_natali', nargs='+', help='Find top players by genders and age category. Made by Natali')
    group.add_argument('--top_dav', help='Find top players by genders and age category. Made by David')
    parser.add_argument('-total', type=int, help='type year to get info about all medals for this year')
    parser.add_argument('-interactive', help='Type anything to start interactive. There you can enter country(name or code) to get info(first participation in the Olympiad, best year, worst year, and average number of medals')
    parser.add_argument('--output', help='Argument is optional: it is saving results to file')
    return parser