import pandas as pd
import statistics
import os
from prettytable import PrettyTable

csvlist = []


def readdir():
    path = "."
    dir_list = os.listdir(path)
    for i in dir_list:
          if i.endswith(".csv"):
                csvlist.append(i)
    for j in csvlist:
          print("FILE =", j)
          delayjitter(j)
          packetlossdef(j)
          print("========================================================================================")
def delayjitter(csvname):
    delay = []
    jitter = []
    df = pd.read_csv(csvname)
    time_array = df['Time'].tolist()
    for i in range (len(time_array)-1):
            delay.append(time_array[i+1]-time_array[i])
    for j in range (len(delay)-2):
            jitter.append(abs(delay[j]-delay[j+1]))
    print("Delay Total =",'{:.3f}'.format(sum(delay)))
    print("Rata-Rata Delay =",'{:.3f}'.format(statistics.mean(delay)),"|",int(statistics.mean(delay)*1000),"ms")
    print("Jitter Total =",'{:.3f}'.format(sum(jitter)))
    print("Rata-Rata Jitter =",'{:.3f}'.format(statistics.mean(jitter)),"|",int(statistics.mean(jitter)*1000),"ms")
    return
def packetlossdef(csvname):
    pllist = []
    df = pd.read_csv(csvname)
    time_array = df['Time'].tolist()
    info_array = df['Info'].tolist()
    for i in range (len(info_array)):
          if 'not captured' in info_array[i]:
                pllist.append(i)
    print("Packet Loss =", '{:.4f}'.format(100-((len(time_array)-len(pllist))*100)/len(time_array)))
    print(len(time_array),"-",len(pllist),"=",len(time_array)-len(pllist),"|", len(time_array)-len(pllist),"* 100 =",(len(time_array)-len(pllist))*100,"|",((len(time_array)-len(pllist))*100),"/",len(time_array),"=",'{:.4f}'.format(((len(time_array)-len(pllist))*100)/len(time_array)),"|","100 -", '{:.4f}'.format(((len(time_array)-len(pllist))*100)/len(time_array)),"=",'{:.4f}'.format(100-((len(time_array)-len(pllist))*100)/len(time_array)))
    return
readdir()



