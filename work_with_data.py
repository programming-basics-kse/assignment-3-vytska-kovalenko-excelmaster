def get_data(filepath):
    with open(filepath) as file:
        header = file.readline().strip().split('\t')
        rows  = []
        for line in file:
            row = line.strip().split('\t')
            rows.append(row)
    return rows, header

def filter_data(rows, header,country, year):
    COUNTRY = header.index('Team')
    NOC = header.index('NOC')
    YEAR = header.index('Year')
    filtered = []
    year = str(year)
    for row in rows:
        if row[COUNTRY]==country or row[NOC]==country:
            if row[YEAR]==year:
                filtered.append(row)
    return filtered