def valid_medal(medal):
    if medal == 'Gold' or medal == 'Silver' or medal =='Bronze':
        return True
    return False

def valid_country(country, rows, countries_set, NOC):
    return country in countries_set or any(row[NOC] == country for row in rows)

def valid_year(rows, header, year):
    YEAR = header.index('Year')
    for row in rows:
        if str(year) == row[YEAR]:
            return True
    return False

def valid_age(age, age_min, age_max):
    try:
        age = int(age)
        if age_min<= age < age_max:
            return age
        return None
    except ValueError:
        return None

