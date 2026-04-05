from utils import print_scaling, print_table
from string import ascii_uppercase
import random
random.seed(42)

def random_string(length):
    return ''.join(random.choice(ascii_uppercase) for i in range(length))

strings = [random_string(32) for i in range(10000)]

setup_code = '''
from itertools import islice
from random import choice, seed, shuffle
from string import ascii_uppercase
seed(42)

strings = [''.join(choice(ascii_uppercase.replace('A', '')) for i in range(32)) for j in range({N})]

strings = ['AA' + s[2:] if i < 10 else s for i, s in enumerate(strings)]

shuffle(strings)
'''

print_scaling('[s for s in strings if s.startswith("AA")]',
              setup=setup_code,
              sizes=[10000, 20000, 30000],
              repeat=False, units='us',
              print_result=False,
              label='list comprehension')

setup_code = '''
from patricia import trie
from random import choice, seed, shuffle
from string import ascii_uppercase
from itertools import islice
seed(42)

strings = [''.join(choice(ascii_uppercase.replace('A', '')) for i in range(32)) for j in range({N})]

strings = ['AA' + s[2:] if i < 10 else s for i, s in enumerate(strings)]

shuffle(strings)
strings_dict = {s: 0 for s in strings}
strings_trie = trie(**strings_dict)
'''

print_scaling('list(strings_trie.iter("AA"))',
              setup=setup_code,
              sizes=[10000, 20000, 30000],
              units='us',
              print_result=False,
              label='patricia trie')

print_table()