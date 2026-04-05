from bisect import bisect_left
from utils import print_scaling, print_table

def index_bisect(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

setup_code = '''
import random
random.seed(42)

collection = list(range({N}))
'''
print_scaling('collection.index(random.randint(0, {N}))',
              setup=setup_code, print_result=False, label='list.index')
    
setup_code_bisect = '''
from __main__ import index_bisect

import random
random.seed(42)

collection = list(range({N}))
'''
print_scaling('index_bisect(collection, random.randint(0, {N}))',
              setup=setup_code_bisect, print_result=False, label='bisect_left')

print_table()
