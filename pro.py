import csv
import math

with open ("data.csv" , newline = "")as f:
    reader = csv.reader(f)
    file_data = list(reader)

    
    
Data = file_data[0]
def mean (Data):
    n =  len(Data)
    sum = 0
    for x in Data:
        sum = sum+int(x)

    mean =     sum / n 
    return mean   


  #squaring

squared_list = []

for a in Data:
    sq = int(a)-mean(Data)
    sq = sq**2
    squared_list.append(sq)

total = 0 

for b in squared_list:
    total = total+b

result = total / (len(Data)-1)

SD = math.sqrt(result)

print(SD)

    



