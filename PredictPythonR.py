import matplotlib.pyplot as plt
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

print(robjects.r('csvFinal <- read.csv("./csvFinal.csv")')) 

print(robjects.r('data.frame(csvFinal)'))

print(robjects.r('View(csvFinal)'))

print(robjects.r('linearModelCpu <- lm(cpu~ram, data = csvFinal)'))
print(robjects.r('linearModelRam <- lm(ram~cpu, data = csvFinal)'))

print(robjects.r('predictionCpu <- predict(linearModelCpu)'))
print(robjects.r('predictionRam <- predict(linearModelRam)'))

print(robjects.r('predictionCpu'))
print(robjects.r('predictionRam'))

plt.plot(robjects.r('predictionCpu'))
plt.plot(robjects.r('predictionRam'))
plt.show()