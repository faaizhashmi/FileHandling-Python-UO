# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import numpy as np
import math


data_path = 'C:/Users/l1s16bscs0064/Downloads/clustering_lab/points.csv'
with open(data_path, 'r') as f:
    reader = csv.reader(f, delimiter=',')
    data = list(reader)
    data = np.array(data).astype(float)


x1 = 27.33836151
y1 = 40.58221376
res1 = []

for i in range(20):
    x = (data[i][1] - x1) * (data[i][1] - x1)
    y = (data[i][2] - y1) * (data[i][2] - y1)
    dis = math.sqrt(x+y)
    res1.append(dis)

#print(res1)

x2 = 21.91374752
y2 = 19.07159524
res2 = []

for i in range(20):
    x = (data[i][1] - x2) * (data[i][1] - x2)
    y = (data[i][2] - y2) * (data[i][2] - y2)
    dis = math.sqrt(x+y)
    res2.append(dis)
    
#print(res2)

res = []

for i in range(20):
    if(res1[i] < res2[i]):
        res.append(4)
    elif(res2[i] < res1[i]):
        res.append(8)
        
print(res)

output = []

for i in range(20):
    output.append(data[i])
    output.append(res[i])
    
print(output)
    

        
        