from utils import print_scaling, print_table

setup_code = '''
from random import choice
from string import ascii_uppercase

def random_string(length):
    return ''.join(choice(ascii_uppercase) for i in range(length))

collection = {{random_string(16) : i for i in range({N})}}
'''

print_scaling('"ITEM" in collection',
              setup=setup_code,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='dict.__contains__')

print_scaling('collection["ITEM"] if "ITEM" in collection else None',
              setup=setup_code,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='dict.__getitem__')

print_scaling('collection["ITEM"] = 0',
              setup=setup_code,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='dict.__setitem__')

print_table()
