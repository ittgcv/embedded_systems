import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
miCorreo=pd.read_csv('correos.csv',  index_col=1,  sep=str(u','))
miCorreoT=miCorreo.T    # se transpone
sentences_train=[]
indice_banco=[152, 234, 370]    # texto de bancos para entrenamiento
selected=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 152, 234, 370]     # datos de entrenamiento
counter=0
y_train=np.zeros((len(selected), 1))
#for i in range(0, 2500):
#    msg=miCorreoT.iloc[i]
#    print(i, msg[0][:])     # crea bocavulario de asuntos
for j in selected:
    msg=miCorreoT.iloc[j]
    sentences_train.append(msg[0][:])     # crea bocavulario de asuntos
    if j in indice_banco:
        y_train[counter]=1
    counter=counter+1
    try:
        print(j, 'asunto:', msg[0][:], 'from:', msg[1][:])
    except:
        pass
print(sentences_train)
vectorizer = CountVectorizer(min_df=0, lowercase=False)
vectorizer.fit(sentences_train)
#print(vectorizer.vocabulary_)   # indice de palabras
#print(vectorizer.transform(sentences_train).toarray())
X_train = vectorizer.transform(sentences_train)
classifier.fit(X_train, y_train)    # entrena
prediction=classifier.predict(X_train)  # valida el entrenamiento
print(prediction)
asunto=[]
for i in range(0, 2500):
    msg=miCorreoT.iloc[j]
    sentences_train.append(msg[0][:])     # crea bocavulario de asuntos
X_test=vectorizer.transform(sentences_train)
prediction=classifier.predict(X_test)
counter=0
for i in prediction:
    if i==1:
        print(counter, sentences_train[counter])
    counter=counter+1
