from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import pandas as pd
from sklearn import svm


def main():
    x_data = pd.read_csv("heart-anomalies.csv", header=None)

    X = x_data.values[:, 1:45]
    y = x_data.values[:, 0]

    clf = tree.DecisionTreeClassifier(criterion='entropy', min_impurity_decrease=0.3)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2)

    # train on the training set
    clf = clf.fit(X_train, y_train)
    # predict on the test set
    y_pred = clf.predict(X_test)

    scores = cross_val_score(clf, X, y, cv=20)
    print('Accuracy: {0}%'.format(scores.mean()*100))
    print('+/-: {0}%'.format(scores.std()))




main()