import re

""" to run doctest: python -m doctest -v {filename}"""

def input_valid(s):
    '''
    str --> str
        if re.match: "Match found"
        else: "No Match"
    
    >>> from re_match import input_valid as iv
    >>> print iv('0d8')
    None
    >>> print iv('00d10')
    None
    >>> print iv('10d0')
    None
    >>> print iv('10d01')
    None
    >>> print iv('10d00')
    None
    >>> print iv('2d100') is None
    False
    ''' 

    result = re.match(r'^([^0]\d|[^0])[d][^0]\d?\d?$', s)
    '''
    I THINK changing the section AFTER the [d] to "[1-9][02]?[0]?" should
    mean only 'normal' D&D dice + d100s can be rolled. But do I want to
    lock it down like that?

    Actually, the above logic is wrong. I may need another capture for that.
    "([468]|[1][02]|[2][0]|[1][0][0])"
    '''
    return result

#######################################
# Beyond This point, lies MADNESS!!
#######################################

'''
manual test cases: NOT The Way!

from re_match import input_valid as iv

print iv('0d8') #should fail
print iv('1d10') #should pass
print iv('99d8') #should pass
print iv('2d100') #should pass
print iv('00d10') #should fail
print iv('10d0') #should fail
print iv('10d01') #should fail
print iv('10d00') #should fail

'''

def re_test(s):
    result = re.match(r'^([^0]\d|[^0])[d]([468]|[1][02]|[2][0]|[1][0][0])$',s)
    print (result)

'''
MORE manual testing. Again, NOT THE WAY!!
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