import wordcloud, matplotlib.pyplot as plt
import rpy2
import rpy2.robjects as robjects
from rpy2.robjects.packages import importr

print(robjects.r('data = read.csv("./realCostMonthly.csv")')) 

print(robjects.r('View(data)')) 

print(robjects.r('data$X <- as.POSIXct(data$X, format="%Y-%m-%d")')) 

print(robjects.r('data$X <- as.Date(data$X)')) 

print(robjects.r('nextMonths <- data.frame(X = as.Date(c("2022-11-01", "2022-12-01")))'))

print(robjects.r('monthlyCostLinearModel <- lm(Custo.total....~X, data = data)'))
 
print(robjects.r('prediction <- predict(monthlyCostLinearModel, newdata = nextMonths)')) 