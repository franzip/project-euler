import urllib2
import re

# Reading the data directly from project-euler

html = urllib2.urlopen('http://projecteuler.net/problem=18').read()
rawstring = re.search(r';">\d(?s).*\d</p>', html)
data = ''
lines = 1
for x in rawstring.group():
    if x.isdigit():      
        data += x     
    if x == '\n':
        lines +=1
        
# Make a flat list
data = [int(data[x:x+2]) for x in range(0, len(data), 2)]


def max_path_sum(data):
    row = 0
    branch = 0
    def scroll_triangle(data, branch, row):
        if branch < len(data):
            row += 1
            left_path = data[branch] + scroll_triangle(data, branch + row, row)
            right_path = data[branch] + scroll_triangle(data, branch + row + 1, row)
            return left_path if left_path > right_path else right_path        
        else:
            return 0        
    return scroll_triangle(data, row, branch)


print max_path_sum(data)    

