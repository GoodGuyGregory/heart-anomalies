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
        X, y, test_size=0.5, random_state=100)


    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    clf = svm.SVC(kernel='linear', C=1, random_state=42)
    scores = cross_val_score(clf, X, y, cv=5)
    print(scores)

    print(accuracy_score(y_test, y_pred) * 100)


main()