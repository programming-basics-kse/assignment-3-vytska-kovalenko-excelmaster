from david_main import *
from tasks import *
from validation import *
from work_with_data import *
from countries import COUNTRIES_SET, CODES_SET
from additional_task_vytska import *
from additional_task_top import *


def main():
    parser = created_parser()
    args = parser.parse_args()
    if args.medals or args.overall or args.top_natali:
        parser = created_parser()
        args = parser.parse_args()
        if args.medals:
            country, year = args.medals
            year = int(year)
            result = print_medalists(args.filepath, country, year, COUNTRIES_SET)
        elif args.overall:
            result_dict = overall_statistics(args.filepath, args.overall, COUNTRIES_SET)
            result = ''
            for country, info in result_dict.items():
                result += country + ": " + str(info) + "\n"
            result = result.strip()
        elif args.top_natali:
            if len(args.top_natali) >= 2 and args.top_natali[1] not in ['M', 'F']:
                genders = args.top_natali[0]
                categories = list(map(str, args.top_natali[1:]))
            else:
                genders = args.top_natali[:2]
                categories = list(map(str, args.top_natali[2:]))
            result = top_player(args.filepath, genders, categories)
        print(result)

        if args.output:
            with open(args.output, 'w') as file:
                file.write(result)
            print(f"Results saved to '{args.output}'")
    else:
        if args.total:
            fin_return()
        elif args.interactive:
            interactive()
        elif args.top_dav:
            top()



main()