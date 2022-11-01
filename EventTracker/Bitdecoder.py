import time,os
import pandas as pd

dataorg = "01111"
data = dataorg.replace("*","11110")

bits = []
Decimal = []
Char = []

temp = ""
offset = ord("A")-1

#split data in 5 equal parts
for i in range(0, len(data), 5):
    temp = data[i:i+5]
    bits.append(temp)
    Decimal.append(eval("0b"+temp))
    Char.append(chr(Decimal[-1]+offset))
    # dict = {"Bits":bits,"Decimal":Decimal,"Char":Char}
    # print(pd.DataFrame(dict).to_string())
    # time.sleep(0.5)

for i in Char:
    dataorg.split("*")
    if i == '^':
        print(" ",end="")
    else:
        print(i,end="")