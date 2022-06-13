import numpy as np
import random
from utils import add_class

output_el = Element('output').element

arr = np.array([23,543,234,12])
# pyscript.write('output', f'{arr}')
output_el.innerHTML = f'{arr}'

def shuffle_array(*args):
    # shuffle
    shuffled = sorted(arr, key=lambda k: random.random())

    # change color
    add_class(output_el, 'text-blue-500')

    # pyscript.write('output', shuffled)
    output_el.innerHTML = shuffled