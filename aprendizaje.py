from sklearn.svm import SVC 
import numpy as np 
# datos de entrada
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
# clases de salida
y = np.array([1, 1, 2, 2])
# metodo de aprendizaje lineal basado en la tecnica Support Vector Machine
clf = SVC(kernel='linear')
# entrena usando los datos de entrada
clf.fit(X, y)
# predice la clase de salida de un nuevo dato usando el modelo entrenado
prediction = clf.predict([[0,6]])
# imprime los resultados
print(prediction)
