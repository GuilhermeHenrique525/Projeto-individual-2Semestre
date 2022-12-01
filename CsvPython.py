import psutil
import time
import os
import csv
import pandas as pd

def gigas(value):
    return f'{value / 1024 / 1024 / 1024: .2f}'    

cpu = []
disco = []
ram = []
final = []

headerList = ['Cpu','Disco','Ram']

while True:

    cpu.append(str(psutil.cpu_percent(interval=None)))
    disco.append(str(gigas(psutil.disk_usage('/').free)))
    ram.append(str(psutil.virtual_memory().percent))

    with open('./cpu.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerows(['Cpu'])
        writer.writerows(cpu)

    with open('./disco.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerows(['Disco'])
        writer.writerows(disco)

    with open('./ram.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerows(['Ram'])
        writer.writerows(ram)

    cpuCsv = ['cpu.csv']
    discoCsv = ['disco.csv']
    ramCsv = ['ram.csv']
    
    for i in range(len(cpuCsv)):
        final.append([cpu[i-1],disco[i-1],ram[i-1]])

    with open('./tudo.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(final)
    
    csvFinal = pd.read_csv("tudo.csv")
    csvFinal.to_csv("tudoagora.csv", index=False,encoding='utf-8-sig', header=headerList)

    #csvCombined = pd.concat(map(pd.read_csv, ['cpu.csv','disco.csv','ram.csv']),ignore_index=True)
    #csvCombined.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig', header=headerList)



    print(cpu)
    print(disco)
    print(ram)
    print(final)

    time.sleep(5)
    os.system("clear")