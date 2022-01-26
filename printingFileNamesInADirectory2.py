
import os
from os import walk
path="/Users/bhavikmangla/Documents"
for path,folders , files in os.walk(path):
    for file in files :
        if file.endswith(".cpp"):
            print(os.path.join(path, file))