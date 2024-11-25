import argparse
def created_parser():
    parser = argparse.ArgumentParser('Processing Olympic medalists data')
    parser.add_argument('filepath', help='Path to the data')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--medals', nargs=2, help='Enter country (Team or NOC) and year')
    group.add_argument('--overall', nargs='+', help='Enter one or more countries to get their overall')
    group.add_argument('--top', nargs='+', help='Find top players by genders and age category')

    parser.add_argument('--output', help='Argument is optional: it is saving results to file')
    return parser