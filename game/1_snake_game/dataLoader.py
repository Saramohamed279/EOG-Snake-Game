import pandas as pd
import sys
import os

script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..', '..', 'Test')
sys.path.append( mymodule_dir )

import test_script_py_file
class DataLoader:

    def __init__(self):
        self.data = test_script_py_file.get_predictions()
        print(self.data)

    def move_generator(self):
        for i in range(len(self.data)):
            yield self.data[i]

# print("eyad")

# gen = DataLoader().move_generator()
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))