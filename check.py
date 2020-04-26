import pandas as pd
import csv

data = pd.read_csv("test.csv")
print (data)

name1 = "thamarmo"
name2 = "Sanjay"
name3 = "Abhishek"
name4 = "NipPincher"
wealth1 = 10
wealth2 = 20
wealth3 = 30
wealth4 = 40

names = [name1,name2,name3,name4]
wealths = [wealth1,wealth2,wealth3,wealth4]

ocr = pd.DataFrame({'Game No':names,'Game':wealths})
print(ocr)


merging = pd.concat([data, ocr])
print(merging)



"""
players = ("Sanjay","thamarmo","Abhishek","Shishtaouk","NipPincher","Spartan")
df = pd.read_csv('test.csv')
name1 = "thamarmo"
name2  = "Sanjay"
name3 = "Spartan"
name4 = "Abhishek"
wealth1 = 10
wealth2 = 20
wealth3 = 30
wealth4 = 40

mylist=[wealth1,wealth2,wealth3,wealth4]
Dict = {"Sanjay":1,"thamarmo":2,"Abhishek":3,"Shishtaouk":4,"NipPincher":5,"Spartan":6}

name5 = players.drop(name1,name2,name3,name1)
print(name5)


myorder = [(Dict[name1]),(Dict[name2]),(Dict[name3]),(Dict[name4])]
print (myorder)
"""




