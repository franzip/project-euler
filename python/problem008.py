import urllib2
import re

# Reading the data directly from project-euler
response = urllib2.urlopen('http://projecteuler.net/problem=8')
html = response.read()
rawstring = re.search(r'>\s\d(?s).*</p>', html)


def largestProd(rawstring):
    resultstring = ''
    for x in rawstring.group():
        if x.isdigit():
            resultstring += str(x)
    largestProd = 0
    for substring in range(0, len(resultstring) - 5):
        # compute the product for each sequence of 5 digits
        prod = reduce(lambda x, y: x * y,
                    [int(x) for x in resultstring[substring:substring+5]])
        if prod > largestProd:
            largestProd = prod
    return largestProd        

print largestProd(rawstring)
