from func import *


if __name__ == '__main__':
    	# get_area_total("wifi.csv","test.rm")
    	area_gate_dict = dict_area_gate("airport_gz_gates.csv")
	#fid_gate_dict = dict_fid_gateorflytime("flightid_gate.csv")
	#fid_flytime_dict = dict_fid_gateorflytime("flightid_flytime.csv")

	with open("st_at_gate.csv.gst",'r') as f1, open("st_at_area.csv.gst",'w+') as f2:
		f2.write("sche_time	actu_time	area\n")


'''
	with open("security_flightid.csv",'r') as f1, open("securtime_flytime_area_flight.csv.gst",'w+') as f2:
		f2.write("securitytime	flytime	area	flightid\n")
		while True:
			line = f1.readline()
			if line:
				sdata = line.strip().split(",")
				f2.write(sdata[0][0:-3]);f2.write("\t");
				if fid_flytime_dict.has_key(sdata[1]):
					f2.write(fid_flytime_dict[sdata[1]][0:-3]);f2.write("\t");
				else:
					f2.write("00:00");f2.write("\t")
				for k_area in area_gate_dict:
					if fid_gate_dict.has_key(sdata[1]):
						if fid_gate_dict[sdata[1]] in area_gate_dict[k_area]:
							f2.write(k_area);f2.write("\t")
							break
					else:
						f2.write("absent");f2.write("\t")
						break
				f2.write(sdata[1]);f2.write("\n")
			else:
				break

'''
