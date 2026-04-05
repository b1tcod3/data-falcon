from utils import print_scaling, print_table

setup_code = '''
import heapq

collection = list(range({N}))
heapq.heapify(collection)
'''

print_scaling('heapq.heappop(collection)',
              setup=setup_code,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='heapq.heappop')

setup_code = '''
import heapq

collection = list(range({N}))
heapq.heapify(collection)
'''

print_scaling('heapq.heappush(collection, {N})',
              setup=setup_code,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='heapq.heappush')

setup_code = '''
import heapq

collection = list(range({N}))
'''

print_scaling('heapq.heapify(collection)',
              setup=setup_code,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='heapq.heapify')

setup_code_priority = '''
from queue import PriorityQueue

collection = list(range({N}))
queue = PriorityQueue()
for element in collection:
    queue.put(element)
'''

print_scaling('queue.get()',
              setup=setup_code_priority,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='PriorityQueue.get')

print_scaling('queue.put({N})',
              setup=setup_code_priority,
              sizes=[1000, 2000, 3000],
              print_result=False,
              label='PriorityQueue.put')

print_table()