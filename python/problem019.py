def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    return False

def count_sundays(start_year, end_year):
    # months[i][1] maps for leap years, months[i][0] for non leap years
    months = {1:(31, 31), 2:(28, 29), 3:(31, 31), 4:(30, 30), 5:(31, 31), 6:(30, 30),
    7:(31, 31), 8:(31, 31), 9:(30, 30), 10:(31, 31), 11:(30, 30), 12:(31, 31)}
    
    # week_day maps numbers 0 ... 6 to week days
    # 0 = Monday ... 6 = Sunday
    week_day = 0 
    matching_sundays = 0
    for years in range(start_year, end_year + 1):
        for month in range(1, len(months) + 1):
            leap_year = is_leap(years)
            if not leap_year:
                for day in range(1, months[month][0] + 1):
                    # increase week_day keeping it in range(0, 7)
                    week_day = (week_day + 1) % 7
                    # First month day on Sunday (week_day = 6)
                    if week_day == 6 and day == 1:
                        matching_sundays += 1
            else:            
                for day in range(1, months[month][1] + 1):
                    week_day = (week_day + 1) % 7
                    if week_day == 6 and day == 1:
                        matching_sundays += 1             
    return matching_sundays    
    

print count_sundays(1901, 2000)