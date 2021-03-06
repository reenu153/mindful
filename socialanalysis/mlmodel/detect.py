import json
import pandas as pd
import time
import numpy as np
import itertools
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics
import os
import pickle
from sklearn import tree


tweets_data = []
x = []
y = []
vectorizer = CountVectorizer(stop_words='english')


def retrieveTweet(data_url):

    tweets_data_path = data_url
    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue


def retrieveProcessedData(Pdata_url):
    sent = pd.read_excel(Pdata_url)
    for i in range(len(tweets_data)):
        if tweets_data[i]['id'] == sent['id'][i]:
            x.append(tweets_data[i]['text'])
            y.append(sent['sentiment'][i])


def nbTrain():
    from sklearn.naive_bayes import MultinomialNB
    start_timenb = time.time()
    train_features = vectorizer.fit_transform(x)

    actual = y

    nb = MultinomialNB()
    nb.fit(train_features, [int(r) for r in y])

    test_features = vectorizer.transform(x)
    predictions = nb.predict(test_features)
    fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
    nbscore = format(metrics.auc(fpr, tpr))
    nbscore = float(nbscore)*100

    print("Naive Bayes  Accuracy : \n", nbscore, "%")
    print(" Completion Speed", round((time.time() - start_timenb), 5))
    print()


def datree():
    from sklearn import tree
    start_timedt = time.time()
    train_featurestree = vectorizer.fit_transform(x)
    actual1 = y
    test_features1 = vectorizer.transform(x)
    dtree = tree.DecisionTreeClassifier()

    dtree = dtree.fit(train_featurestree, [int(r) for r in y])

    prediction1 = dtree.predict(test_features1)
    ddd, ttt, thresholds = metrics.roc_curve(actual1, prediction1, pos_label=1)
    dtreescore = format(metrics.auc(ddd, ttt))
    dtreescore = float(dtreescore)*100
    print("Decision tree Accuracy : \n", dtreescore, "%")
    print(" Completion Speed", round((time.time() - start_timedt), 5))
    print()


def runall():
    # retrieveTweet(os.getcwd() + '/socialanalysis/mlmodel/data/tweetdata.txt')
    # retrieveProcessedData(os.getcwd() + '/socialanalysis/mlmodel/processed_data/output.xlsx')
    # nbTrain()
    # datree()
    pass


def datreeINPUT(inputtweet):
    with open('x.data', 'rb') as xfilehandle:
        x = pickle.load(xfilehandle)
    with open('y.data', 'rb') as yfilehandle:
        y = pickle.load(yfilehandle)
    train_featurestree = vectorizer.fit_transform(x)
    dtree = tree.DecisionTreeClassifier()

    dtree = dtree.fit(train_featurestree, [int(r) for r in y])

    inputdtree = vectorizer.transform([inputtweet])
    predictt = dtree.predict(inputdtree)

    if predictt == 1:
        predictt = "Positive"
    elif predictt == 0:
        predictt = "Neutral"
    elif predictt == -1:
        predictt = "Negative"
    else:
        print("Nothing")
        
    return predictt

# datreeINPUT(inputtweet)
