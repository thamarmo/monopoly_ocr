import pandas as pd
import csv

name1 = "thamar"
name2  = "sanjay"
wealth1 = 10
wealth2 = 20

names = [name1,name2]
wealths = [wealth1,wealth2]

name = ["thamar","Hrideek"]
wealth = [50,100]

data = pd.DataFrame({'Name':name,'Game':wealth})
print(data)

ocr = pd.DataFrame({'Name':names,'Game':wealths})
print(ocr)

"""result = data.append(ocr, ignore_index=True, sort=False)
print(result)"""

merging = pd.merge(data, ocr, on='Name', how='outer',suffixes=('_1', '_2'))
print(merging)


"""
newdata = pd.merge(data, ocr, how='left')
print(newdata)"""