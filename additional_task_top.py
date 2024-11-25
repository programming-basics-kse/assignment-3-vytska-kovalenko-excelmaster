from david_main import get_data

def top():
    ages = {
        '1' : (18, 25),
        '2' : (25, 35),
        '3' : (35, 50),
        '4' : (50, 999)
    }

    rows, header = get_data()
    NAME = header.index('Name')
    GENDER = header.index('Sex')
    AGE = header.index('Age')
    MEDAL = header.index('Medal')
    ID = header.index('ID')
    id_list = []
    input = 'M F 1 2'.split(' ')
    for item in input:
        if item not in ages and item not in ['M', 'F']:
            print("Invalid input")
        if item not in ['M', 'F']:
            age_min, age_max = ages[item]
            medals = {}
            for row in rows:
                try:
                    age = int(row[AGE])
                except ValueError:
                    continue
                if age in range(age_min, age_max) and row[ID] not in id_list and row[MEDAL] not in ['N/A', 'NA']:
                    medals.setdefault(row[NAME], {}).setdefault('Medals', 0)
                    medals[row[NAME]][row[ME]] += 1
    print(medals)

top()