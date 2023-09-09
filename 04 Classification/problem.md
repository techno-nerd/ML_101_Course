# Animal Classification

Try the problem presented by the following data set:

https://www.kaggle.com/datasets/uciml/zoo-animal-classification?resource=download

The file is inside the data folder and is named **zoo.csv** 

First, you should try a binary classification problem, for which you will have to run the following code:

``` python
    labels.replace(np.arange(2, 10, 1), 0, inplace=True)
```

This will replace all non-mammal classes with class 0.

You can use the code from Titanic prediction problem as a template.

If needed, refer to the Logit_AnimalBinary.ipynb file for my approach to the problem