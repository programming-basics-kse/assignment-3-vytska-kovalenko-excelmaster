def valid_medal(medal):
    if medal == 'Gold' or medal == 'Silver' or medal =='Bronze':
        return True
    return False

def valid_country(rows, header, country):
    COUNTRY = header.index('Team')
    NOC = header.index('NOC')
    for row in rows:
        if country.lower() in row[COUNTRY].lower() or country.lower() == row[NOC].lower():
            return True
    return False

def valid_year(rows, header, year):
    YEAR = header.index('Year')
    for row in rows:
        if str(year) == row[YEAR]:
            return True
    return False