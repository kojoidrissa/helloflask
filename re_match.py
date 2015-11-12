import re

def input_valid(s):
    '''
    str --> str
        if re.match: "Match found"
        else: "No Match"
    ''' 

    result = re.match(r'^([^0][^0]|\d\d|[1-9])[d][1-9]\d?\d?$', s)
    return result
'''
test cases

from re_match import input_valid as iv

iv('d8')
iv('d10')
iv('1d8')
iv('1d10')
iv('10d10')

'''

def re_test(s):
    result = re.match(r'^(\d\d|[1-9]|[^0][^0])$',s)
    print result

'''
from re_match import re_test as rt

rt('10') #should pass, does
rt('01') #should pass, does
rt('0') #should fail, does
rt('00') #should fail, doesn't
'''


# roll_list = ['d8', 'd10', '1d8', '1d10', '10d10', '10d8', '2d100']

# for die in roll_list:
#     print die
#     print input_valid(die)