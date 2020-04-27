import pandas as pd
import csv

name1 = "thamarmo"
name2  = "Sanjay"
name3 = "Spartan"
name4 = "Abhishek"
wealth1 = 10
wealth2 = 20
wealth3 = 30
wealth4 = 40



f = open("test.csv", "w")
writer = csv.DictWriter(f, fieldnames=["sanjay", "thamar"])
writer.writeheader()
f.close()

