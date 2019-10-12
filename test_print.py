def esc(code=0):
 return f'\033[{code}m'
print(esc('31;1;0') + 'Error:'+esc()+'important')



import json
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(json.dumps(my_mapping, indent=4, sort_keys=True))


import numpy as np
import pysnooper

# @pysnooper.snoop()
@pysnooper.snoop("pysnooper_debug.log")
def one(number):
    mat = []
    while number:
        mat.append(np.random.normal(0, 1))
        number -= 1
    return mat


one(3)
