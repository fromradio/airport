
with open("t1_t2_area.csv.gst",'r') as f:
    n = 0
    sum = 0.0
    line = f.readline()
    while True:
        line = f.readline()
        if line:
            sdata = line.strip().split()
            if sdata[1] != "00.00":
                n = n + 1
                diff = float(sdata[1]) - float(sdata[0])
		# print diff,sum
		# raw_input()
                sum = sum + diff
            else:
                continue
        else:
            break

    res = sum/n
    print "average time is :",res

# average time is : 1.31939000984




















