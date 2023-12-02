## Heart Anomalies

[You may do this project by writing your own code, or using an ML framework such as scikit-learn or Keras. If you use a framework, you must also do Authorship (in addition to one other problem).]

[This paper](https://pubmed.ncbi.nlm.nih.gov/11583923/) Links to an external site. by Kurgan et al describes diagnosis of heart anomalies using machine learning on SPECT radiography data. The authors' dataset was made available for public use. There is an archive at https://github.com/pdx-cs-ai/heart-anomaly-hwLinks to an external site. containing background that you should read, but I would like you to use heart-anomalies.csv on our Github at https://github.com/pdx-cs-ai/miniproject-data-fall2023Links to an external site.. Each instance row in this dataset has binary class followed by features.

You will use machine learning to improve upon their results. Construct a machine learner that can achieve at least 70% accuracy in classifying instances as anomalous vs normal.

Hints:

There are only 267 instances in the dataset. You will almost certainly want to use cross-validation to estimate accuracy.

You will want a non-linear learner. Decision Trees (ID3) seem to work well.