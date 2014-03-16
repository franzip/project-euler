import urllib2
              
def sum_scores():
    # fetch data and sort them
    data = urllib2.urlopen('http://projecteuler.net/project/names.txt').read()
    data = data.replace('"', '').split(',') 
    data.sort()  
    total = 0
    # loop through the list
    for position in range(len(data)):
        for char in data[position]:
            # (1 + ord(char) - ord('A')), A -> 1, B -> 2 ... Z -> 26
            # (position + 1) also add 1 as constant since we start at 0
            total += (1 + ord(char) - ord('A')) * (position + 1)
    return total
                
print sum_scores()
