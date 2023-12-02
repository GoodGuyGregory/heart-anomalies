from sklearn import tree
import pandas as pd




def setUpSkLearn():
    ## determine the length of the data set.

    X = pd.read_csv("heart-anomalies.csv",header=None)

    print(X)
    # Y = [0,1]
    # clf = tree.DecisionTreeClassifier()
    # clf = clf.fit(X,Y)
    # clf.predict(X)




def main():
    setUpSkLearn()


main()