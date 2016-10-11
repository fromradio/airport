# learn a and b in : y = ax + b
# EC and T1 need all data, while others only need corresponding data

def ab_EW(awfile,tafile):
	areadict = {0:"E1",1:"E2",2:"E3",3:"EC",4:"T1",5:"W1",6:"W2",7:"W3"}
	with open(awfile,'r') as f1, open(tafile,'r') as f2:
		sumx = [0 for i in range(0,8)]
		sumy = [0 for i in range(0,8)]
		sumx2 = [0 for i in range(0,8)]
		sumxy = [0 for i in range(0,8)]
		n = [0 for i in range(0,8)]
		a = [0 for i in range(0,8)]
		b = [0 for i in range(0,8)]
		lines = f1.readlines()
		for line in lines:
			sdata = line.strip().split()
			if sdata[0]=="time" or sdata[0]=="begin":
				continue
			for j in range(0,8):
				sumy[j] = sumy[j] + int(sdata[j+1])
				x = [0 for i in range(0,8)]
				line2 = f2.readline()
				if j != 3 and j != 4:
					while True:
						line2 = f2.readline()
						if line2:
							sdata2 = line2.strip().split()
							#print "in line2----------"
							#print sdata2[2]
							#print areadict[j]
							#raw_input()
							if (sdata2[2] == areadict[j] or sdata2[2] == "absent") and sdata2[1]!="00.00":
								#print "in line2 2-------------"
								#print float(sdata2[1]) - float(sdata[0])
								#raw_input()
								if float(sdata2[1]) - float(sdata[0]) < 1.35 and float(sdata2[1]) - float(sdata[0]) > 0:
									#print "in line2 there's one----------"
									x[j] = x[j] + 1
						else:
							break
				else:
					while True:
						line2 = f2.readline()
						if line2:
							sdata2 = line2.strip().split()
							if sdata2[1]!="00.00":
								if float(sdata2[1]) - float(sdata[0]) < 1.35 and float(sdata2[1]) - float(sdata[0]) > 0:
									x[j] = x[j] + 1
						else:
							break
				#print x[j]
				#raw_input()
				sumx[j] = sumx[j] + x[j]
				sumx2[j] = sumx2[j] + x[j]*x[j]
				sumxy[j] = sumxy[j] + x[j]*int(sdata[j+1])
				n[j] = n[j] + 1
			#print line
			#print sumx
			#print sumy
			#raw_input()

		print "prepare done."
		print sumx
		print sumy

		for j in range(0,8):
			if sumx[j]*sumx[j]-n[j]*sumx2[j] == 0 :
				print areadict[j],"some wrong"
				print "sumx:",sumx[j],"sumx2:",sumx2[j]
				continue
			a[j] = 1.0*(sumx[j]*sumy[j]-n[j]*sumxy[j])/(sumx[j]*sumx[j]-n[j]*sumx2[j])
			b[j] = 1.0*(sumy[j]-a[j]*sumx[j])/n[j]
		print "a is:\n",a
		print "b is:\n",b


if __name__ == "__main__":
	ab_EW("area_wifi.csv","t1_t2_area.csv.gst")




