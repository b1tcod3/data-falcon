from utils import print_scaling
from utils import print_table

print_scaling('lst.pop()',
              setup='lst = list(range({N}))', print_result=False, label='list.pop()')

print_scaling('lst.pop(0)',
              setup='lst = list(range({N}))', print_result=False, label='list.pop(0)')

print_scaling('lst.append(1)',
              setup='lst = list(range({N}))', print_result=False, label='list.append(1)')

print_scaling('lst.insert(0, 1)',
              setup='lst = list(range({N}))', print_result=False, label='list.insert(0, 1)')

print_scaling('lst.insert(5000, 1)',
              setup='lst = list(range({N}))', print_result=False, label='list.insert(5000, 1)')

print_table()


