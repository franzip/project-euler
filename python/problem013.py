import urllib2
import re

def large_number_sum(first_n_digits):
    # read data from project-euler
    data = re.search(r'>\s\d(?s).*</div><b', 
           urllib2.urlopen('http://projecteuler.net/problem=13').read())
    lines = []
    pattern = re.compile(r'\d+')
    # data is still mixed with html now
    for char in data.group().splitlines():
        # purge data from html and add digits to the list
        match = re.search(pattern, char)
        if match:
            lines.append(int(match.group()))
    # return the first_n_digits of the big number sum
    return str(sum(lines))[:first_n_digits]

print large_number_sum(10)