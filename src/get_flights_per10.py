
import datetime

def get_flights_per10(flightsfile,outfile,ind):
    with open(flightsfile,'r') as f1, open(outfile,'w+') as f2:
        itertime = datetime.datetime(2016, 9, 10, 10, 10)
        while itertime < datetime.datetime(2016, 9, 14, 23, 55):
            f1.close()
            f1 = open(flightsfile,'r')
            lines = f1.readlines()
            #print itertime
            #raw_input()
            nxtitertime = itertime + datetime.timedelta(0,600)
            itertime_str = itertime.strftime("%Y/%m/%d %H:%M:%S")
            print nxtitertime
            f2.write(itertime_str);f2.write("\t")
            for line in lines:
                # print 1
                sdata = line.strip().split(",")
                if "time" in sdata[ind]:
                    continue
                if sdata[ind] != "":
                    #print sdata[ind]
                    #raw_input()
                    if len(sdata[ind])>10:
                        flytime = datetime.datetime.strptime(sdata[ind],"%Y/%m/%d %H:%M:%S")
                        if itertime == datetime.datetime(2016, 9, 14, 23, 30):
                            print itertime,flytime,nxtitertime,sdata[0]
                            raw_input()

                        if itertime <= flytime and nxtitertime > flytime:
                            f2.write(sdata[0]);f2.write(",")
                        else:
                            continue
                    else:
                        #print sdata[ind],"not match format!"
                        continue
                else:
                    continue
            f2.write("\n")
            itertime = nxtitertime


if __name__ == "__main__":
    get_flights_per10("../data/airport_gz_flights_chusai_1stround.csv","../data/ss_scheduled_flights_per10.gst",1)
    get_flights_per10("../data/airport_gz_flights_chusai_1stround.csv","../data/ss_actual_flights_per10.gst",2)




