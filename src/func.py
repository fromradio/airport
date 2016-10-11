def dict_area_gate(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
        a_g_dict = {}
        for line in lines:
            sdata = line.strip().split(',')
            if a_g_dict.has_key(sdata[1]):
                a_g_dict[sdata[1]].append(sdata[0])
            else:
                a_g_dict[sdata[1]] = [sdata[0]]
        return a_g_dict


def dict_fid_gateorflytime(infile):
	fid_dict = {}
	with open(infile,'r') as f:
		while True:
			line = f.readline()
			if line:
				sdata = line.strip().split()
				if fid_dict.has_key(sdata[0]):
					continue
				else:
					fid_dict[sdata[0]] = sdata[1]
			else:
				break
	return fid_dict
				


def get_area_total(wififile,outfile):
    with open(wififile,'r') as f, open(outfile,'w+') as f2:
        lines = f.readlines()
	dictarea = {"E1":0,"E2":0,"E3":0,"EC":0,"T1":0,"W1":0,"W2":0,"W3":0}
        # ne1 = 0; ne2 = 0; ne3 = 0; nec = 0; nt1 = 0; nw1 = 0; nw2 = 0; nw3 = 0;
	f2.write("time	E1	E2	E3	EC	T1	W1	W2	W3\n")
        time0 = 'begin'
        for line in lines:
            sdata = line.strip().split(',')
            time1 = sdata[2][11:16]
	    if time0 != time1:
		    f2.write(time0);f2.write("\t")
		    f2.write(str(dictarea["E1"]));f2.write("\t");
		    f2.write(str(dictarea["E2"]));f2.write("\t");
		    f2.write(str(dictarea["E3"]));f2.write("\t");
		    f2.write(str(dictarea["EC"]));f2.write("\t");
		    f2.write(str(dictarea["T1"]));f2.write("\t");
		    f2.write(str(dictarea["W1"]));f2.write("\t");
		    f2.write(str(dictarea["W2"]));f2.write("\t");
		    f2.write(str(dictarea["W3"]));f2.write("\n");
		    dictarea = {"E1":0,"E2":0,"E3":0,"EC":0,"T1":0,"W1":0,"W2":0,"W3":0}
		    time0 = time1
		    if dictarea.has_key(sdata[0][0:2].upper()):
		    	dictarea[sdata[0][0:2].upper()] = dictarea[sdata[0][0:2].upper()]+int(sdata[1])
	    else:
		    if dictarea.has_key(sdata[0][0:2].upper()):
		    	dictarea[sdata[0][0:2].upper()] = dictarea[sdata[0][0:2].upper()]+int(sdata[1])























