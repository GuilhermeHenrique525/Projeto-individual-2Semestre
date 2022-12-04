import matplotlib.pyplot as plt
import time
import os
import mysql.connector
import pymssql
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

# Conectando com o banco azure
connection = pymssql.connect("serverrabbit.database.windows.net", "rabbit", "RabMonSys@", "RabbitBanco")
cursor = connection.cursor()

predictCpu = []
predictRam = []


print(robjects.r('csvFinal <- read.csv("./csvFinal.csv")')) 

print(robjects.r('data.frame(csvFinal)'))

print(robjects.r('View(csvFinal)'))

print(robjects.r('linearModelCpu <- lm(cpu~ram, data = csvFinal)'))
print(robjects.r('linearModelRam <- lm(ram~cpu, data = csvFinal)'))

print(robjects.r('predictionCpu <- predict(linearModelCpu)'))
print(robjects.r('predictionRam <- predict(linearModelRam)'))

print(robjects.r('predictionCpu'))
print(robjects.r('predictionRam'))

predictCpu += (robjects.r('predictionCpu'))
predictRam += (robjects.r('predictionRam'))

plt.plot(robjects.r('predictionCpu'))
plt.plot(robjects.r('predictionRam'))
plt.title('Previsão da CPU e da RAM')
plt.xlabel('Dados capturados')
plt.ylabel('Porcentagem')
plt.legend(['CPU','RAM'])
plt.savefig('predict.png', format='png')
plt.show()

