from utils import print_scaling, print_table

setup_code = '''
from random import choice
from string import ascii_uppercase

def random_string(length):
    return ''.join(choice(ascii_uppercase) for i in range(length))

collection = {{random_string(16) : i for i in range({N})}}
'''

print_scaling('"X" * {N} in collection',
              setup=setup_code,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='dict key not found')

print_table()
