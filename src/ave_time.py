#! /bin/env python

import pandas as pd
import numpy as np

filePath = "../data/t1_t2_area.csv"
data = pd.read_csv(filePath, sep = "\t")
data.replace(0.00, np.NaN)
print data

valid_data = data.dropna()
print pd.to_datetime(valid_data['flytime'], format = "%H.%M")

# with open("t1_t2_area.csv.gst", 'r') as f:
#     n = 0
#     sum = 0.0
#     line = f.readline()
#     while True:
#         line = f.readline()
#         if line:
#             sdata = line.strip().split()
#             if sdata[1] != "00.00":
#                 n = n + 1
#                 diff = float(sdata[1]) - float(sdata[0])
#                 sum = sum + diff
#             else:
#                 continue
#         else:
#             break
#
#     res = sum/n
#     print "average time is :",res

# average time is : 1.31939000984




















