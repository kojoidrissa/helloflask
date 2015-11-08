import re

def input_valid(s):
    '''
    str --> str
        if re.match: "Match found"
        else: "No Match"
    ''' 

    result = re.match(r'^\d?[1-9][dD][1-9]\d?\d?$', s)
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

# roll_list = ['d8', 'd10', '1d8', '1d10', '10d10', '10d8', '2d100']

# for die in roll_list:
#     print die
#     print input_valid(die)