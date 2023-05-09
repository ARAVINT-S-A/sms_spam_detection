# sms_spam_detection
dataset used: https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

The problem statement here is a classification problem

first we view the data and see its dimensions no of features ,null values etc.

1.removing columns with NULL values(3 columns in our dataset)

2.recognize the output column and label encoding it(giving unique numerical values to each unique value in a column)

3.make sure whether there is no NULL values

4.check for duplicate values

5.remove duplicate values if any

6.check for data imbalance

7.now we preprocess our input column

8.as our input column is a string we use NLTK(natural language tool kit) to process it

9.NLTK is used to tokenize the words in the string

10.using tokenize function of NLTK we find the no of characters,words and sentences in each input string

11.we use the concept of correlation to find the strength of relationship between two variables

12.using NLTk we analyse and reduce the input string

13.we remove special characters and punctuations using stopwords(words that dont have any important menaing but added inorder to get the grammer correct) from NLTK

14.we stem all the words in our tokenized string(stemming is a process of grouping words that produce similar meaning)

15.as we are done with preprocessing we create a ML model

16.here i have used naive bayers as it shows good results with language processing

17.now inorder to provide input to model we use bag of words(word to vector) concept as input given to a model should not be string

18.we make columns for each frequent words and we check how many times does these words come in a input string

19.we do train test split

20.we feed our model the training data

21.once model is trained we predict for x test and compare ypred and ytest to find test accuracy

22.precision is also important so we take a note of precision and accuracy.
