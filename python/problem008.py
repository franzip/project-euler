import urllib2
import re

def get_data():
    # read data from project-euler
    data = ''
    raw_html = re.search(r'>\s\d(?s).*</p>', 
               urllib2.urlopen('http://projecteuler.net/problem=8').read())
    # purge html and add digits to the returned data string
    for x in raw_html.group():
        if x.isdigit():
            data += str(x)
    return data

def largest_prod(data, sequence_length):
    # doesn't make sense to compute if sequence is longer than half of the data string
    assert sequence_length > 0 and sequence_length <= len(data) / 2
    result = 0
    for substring in range(0, len(data) - sequence_length):
        # compute the product for each subsequent sequence of sequence_length size
        product = reduce(lambda x, y: x * y,
                        [int(x) for x in 
                         data[substring:substring + sequence_length]])
        if product > result:
            result = product
    return result        

print largest_prod(get_data(), 5)
