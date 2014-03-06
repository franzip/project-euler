# map numbers (base cases) to corresponding word length 
# i.e. to_char[1] -> len('one')
to_char = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 
             13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5,
             60:5, 70:7, 80:6, 90:6}

def count_letters(n):
    assert type(n) == int and n > 0 and n < 9999
    count = 0
    # 0 < n < 10
    if len(str(n)) == 1:
        # base case, return mapped input value
        count += to_char[n]
    # 10 <= n < 100
    elif len(str(n)) == 2:
        # base case, return mapped input value (10, 20, ..., 90)
        if n in to_char:
            count += to_char[n]
        # return tenths + units mapped value
        else:
            count += to_char[n // 10 * 10] + to_char[n % 10]
    # 100 <= n < 1000
    elif len(str(n)) == 3:
        # start adding hundredths + len('hundred')
        count += to_char[n // 100] + 7
        # base case, add mapped tenths value (10, 20, ..., 90)
        if n % 100 in to_char:
            count +=  to_char[n % 100]
        # add tenths + units mapped value 
        else:
            count += to_char[n // 10 % 10 * 10] + to_char[n % 10]
        # corner case for intervals such as (101 ... 109) -> add len('and')
        if n % 100:
            count += 3
    # 1000 <= n < 9999
    elif len(str(n)) == 4:
        # start adding thousands + len('thousand')
        count += to_char[n // 1000] + 8  
        # add hundredths + len('hundred')
        if n // 100 % 10: 
            count += to_char[n // 100 % 10] + 7
        # base case, add mapped tenths value (10, 20, ..., 90)
        if n % 100 in to_char:
            count +=  to_char[n % 100]
        # add tenths + units mapped value 
        else:
            count += to_char[n % 100 // 10 * 10] + to_char[n % 10]
        # # corner case for intervals such as (1001 ... 1009) -> add len('and')
        if n % 1000:
            count += 3
    return count


print sum([count_letters(x) for x in range(1, 1001)]) 
