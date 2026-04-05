# This cell contains some utility functions to prepare and execute the benchmarks
import timeit
from statistics import median
from random import choice
from string import ascii_uppercase

def random_string(length):
    """Produce a random string made of *length* uppercase ascii characters"""
    return ''.join(choice(ascii_uppercase) for i in range(length))

_results = []

def print_scaling(stmt, setup, sizes=[10000, 20000, 30000], repeat=False, units='us', print_result=True, label=None):
    """Print scaling information for the statement *stmt*, executed after *setup*.
    
    The *setup* and *stmt* arguments take a template string where "{N}"
    will be replaced as the size of the input.
    
    The *repeat* flags determined if the setup needs to be run between
    each test run.
    """
    values = []
    for size in sizes:
        stmt_formatted = stmt.replace('{N}', str(size))
        setup_formatted = setup.replace('{N}', str(size))
        if repeat:
            timings = timeit.repeat(stmt_formatted,
                                    setup=setup_formatted,
                                    number=1, repeat=1000)
            values.append(min(timings))
        else:
            timings = timeit.repeat(stmt_formatted,
                                    setup=setup_formatted,
                                    number=1000, repeat=3)
            values.append(min(t/1000 for t in timings))
    unit_factor = {'us': 1e6,
                   'ms': 1e3}[units]

    display = label if label else stmt
    _results.append((display, values, sizes, units))

    if not print_result:
        return

    col_width = 35
    header = 'Code'.ljust(col_width)
    for n in sizes:
        header += f'  N={n}'
    print(header)
    print('-' * len(header))
    
    for display, values, sizes, units in _results:
        unit_factor = {'us': 1e6, 'ms': 1e3}[units]
        row = display[:col_width].ljust(col_width)
        for t in values:
            row += f'  {t * unit_factor:.2f} {units}'
        print(row)


def print_table():
    """Print all collected results as a table"""
    if not _results:
        return
    
    col_width = 25
    sizes = _results[0][2]
    units = _results[0][3]
    unit_factor = {'us': 1e6, 'ms': 1e3}[units]
    
    header = 'Code'.ljust(col_width)
    for n in sizes:
        header += f'  N={n}'
    print(header)
    print('-' * len(header))
    
    for display, values, sizes, units in _results:
        unit_factor = {'us': 1e6, 'ms': 1e3}[units]
        row = display[:col_width].ljust(col_width)
        for t in values:
            row += f'  {t * unit_factor:.2f} {units}'
        print(row)
