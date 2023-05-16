import pandas as pd

class DataLoader:

    def __init__(self, path):
        self.data = pd.read_csv(path).iloc[:, -1:].sample(frac=1)
        print(self.data)

    def move_generator(self):
        for i in range(len(self.data)):
            yield self.data['1'].iloc[i]

# gen = DataLoader(r"../../Data/Data Handling Concat.csv").move_generator()
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