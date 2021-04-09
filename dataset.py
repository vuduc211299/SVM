import math
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(dataset, target, test_size=0.4, random_state = 109)

clf = svm.SVC(kernel='linear')

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
