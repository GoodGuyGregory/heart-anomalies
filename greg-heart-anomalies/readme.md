## Heart Anomalies

This purpose of this project was to build a learner to determine and classify heart data to determine, based on features provided, if
the heart in question is defective. To do this I used the **pandas** frame work to import 
all csv entries from the provided data set. I was able to explore the data a bit with **pandas**. After doing building a solver for **Tentmates** with some success
with the framework I decided to get more familiar with it. I used it to parse a set of two arrays. 
`X` representing the entries within the provided data from the 1st column to the end. to have all 45 features included and the lables were assigned to `Y`
which was just the entries from the first column of the data.

After this the Decision tree was build with an `min_impurity_decrease` to allow for some control on the splitting logic within each node of the tree. 
meaning this will split within my application on 30% impurity on each split.
I used the criterion of "entropy" to classify how the tree's splitting logic is determined this allows for the entropy to be the focus at each node split from what I understand.

After this I moved to splitting the data into test and training sets with a `test_size` set to 0.2 so that 80% of the data will be training and 20% will be established as testing
all of this is done to prevent over fitting for the test data.

Next the training data for both X and y were fit to the model. predictions were called against the `X_test` training set.

as part of the assignment. There is a call to `cross_val_score` with a setting of 20 way cross validation and also a mean value
of this 20 way cross validation is printed as the Accuracy for the model.

**Running the Application**

ensure the heart data file the `heart-anomalies.csv` is within the same directory of the python file.

There are a few dependencies that might need to be installed globally or inside of this project.
I am using **pip** to install the following packages.


```shell
pip install sklearn
pip install pandas

# to run the program after installing the above packages 
python heartAnomalies.py

```

This worked for me. I am running python 3.10 and had no issues.

Please let me know if you run into any problems and I will be happy to assist.

Greg

if you wish to delete them after I believe you can run `pip uninstall <package>` and it will remove 
the installed python packages for this assignment.






### Resources

[Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
[SciKit Learn Video Demo](https://www.youtube.com/watch?v=YkYpGhsCx4c)

