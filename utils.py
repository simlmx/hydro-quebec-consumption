def get_winter(date):
    year, month, _ = date.split('-')
    year = int(year)
    month = int(month)
    if month < 6:
        return year
    else:
        return year + 1
