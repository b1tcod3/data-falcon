from utils import print_scaling, print_table

setup_code = r"""from collections import Counter, defaultdict
import random
random.seed(42)
collection = [random.randint(0, 100) for i in range({N})]

def counter_defaultdict(items):
    counter = defaultdict(int)
    for item in items:
        counter[item] += 1
    return counter

def counter_dict(items): 
    counter = {} 
    for item in items: 
        if item not in counter: 
            counter[item] = 0 
        else: 
            counter[item] += 1 
    return counter"""

print_scaling('Counter(collection)',
              setup=setup_code,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='Counter()')

print_scaling('counter_defaultdict(collection)',
              setup=setup_code,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='defaultdict(int)')

print_scaling('counter_dict(collection)',
              setup=setup_code,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='dict manual')

print_table()
