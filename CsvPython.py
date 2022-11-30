import psutil
import time
import os
import csv

def gigas(value):
    return f'{value / 1024 / 1024 / 1024: .2f}GB'    

cpu = []
disco = []
ram = []


while True:

    cpu.append(str(psutil.cpu_percent(interval=None)))
    disco.append(str(gigas(psutil.disk_usage('/').free)))
    ram.append(str(psutil.virtual_memory().percent))

    with open('./cpu.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerows(cpu)

    with open('./disco.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerows(disco)

    with open('./ram.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=' ')
        writer.writerows(ram)

    print(cpu)
    print(disco)
    print(ram)

    time.sleep(5)
    os.system("clear")