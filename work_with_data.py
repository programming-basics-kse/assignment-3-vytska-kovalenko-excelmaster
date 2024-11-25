def get_data(filepath):
    with open(filepath) as file:
        header = file.readline().strip().split('\t')
        rows  = []
        for line in file:
            row = line.strip().split('\t')
            rows.append(row)
    return rows, header

