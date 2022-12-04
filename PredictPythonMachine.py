import sklearn
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataset = pd.read_csv('csvFinal.csv')
dataset.columns = ['cpu','disco','ram']
dataset.head()

print(dataset)

# Carregar o dataset
#data = load_breast_cancer()

# Organizar nossos dados
#label_names = data['target_names']
#labels = data['target']
#feature_names = data['feature_names']
#features = data['data']

# Olhando para os nossos dados
#print(label_names)
#print(labels[0])
#print(feature_names[0])
#print(features[0])

# Dividir nossos dados
train, test = train_test_split(dataset,
                               test_size=0.20,
                               random_state=42)

print('teste e treino')
print(train.shape)
print(test.shape)
print('--------------------')

regr = linear_model.LinearRegression()
training_test = train.iloc[:,1]
print('--------------------')
print(training_test)
print('--------------------')

#lfit = regr.fit(training_data, training_test)
#print(regr.coef_)

#testing_data = test.loc[:,['cpu','disco','ram']]


#pred = regr.predict(testing_data)

# Inicializar nosso classificador
#gnb = GaussianNB()

# Treinar nosso classificador
#model = gnb.fit(train, train_labels)



# Fazer previsões
#preds = gnb.predict(test)
#print(preds)

# Avaliar a precisão
#print(accuracy_score(test_labels, preds))