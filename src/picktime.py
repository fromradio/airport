
with open("flights.csv",'r') as f, open("st_at_gate",'w+') as f2:
    lines = f.readlines()
    for line in lines:
        sdata = line.strip().split()
        if len(sdata) < 5:
            f2.write(sdata[2]);f2.write("\t");f2.write(sdata[2]);f2.write("\t");
            f2.write(sdata[-1]);f2.write("\n")
        else:
            f2.write(sdata[2]);f2.write("\t");f2.write(sdata[4]);f2.write("\t");
            f2.write(sdata[-1]);f2.write("\n")





