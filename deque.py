from utils import print_scaling, print_table

print_scaling('d.pop()',
              setup='from collections import deque; d = deque(range({N}))', print_result=False, label='deque.pop()')

print_scaling('d.popleft()',
              setup='from collections import deque; d = deque(range({N}))', print_result=False, label='deque.popleft()')

print_scaling('d.append(1)',
              setup='from collections import deque; d = deque(range({N}))', print_result=False, label='deque.append(1)')

print_scaling('d.appendleft(1)',
              setup='from collections import deque; d = deque(range({N}))', print_result=False, label='deque.appendleft(1)')

print_scaling('collection[0]',
              setup='from collections import deque; collection = deque(range({N}))', print_result=False, label='deque[0]')

print_scaling('collection[{N} - 1]',
              setup='from collections import deque; collection = deque(range({N}))', print_result=False, label='deque[N-1]')

print_scaling('collection[int({N}/2)]',
              setup='from collections import deque; collection = deque(range({N}))', print_result=False, label='deque[N/2]')

from utils import print_table
print_table()
