import re

def input_valid(s):
    result = re.match(r'^\d?\d?[d,D]\d?\d$', s)

    if result == None:
        print "No Match"
    else:
        print "Match found"


'''
test cases
input_valid('d8')
input_valid('d10')
input_valid('1d8')
input_valid('1d10')
input_valid('10d10')
'''

# roll_list = ['d8', 'd10', '1d8', '1d10', '10d10', '10d8', '2d100']

# for die in roll_list:
#     print die
#     print input_valid(die)