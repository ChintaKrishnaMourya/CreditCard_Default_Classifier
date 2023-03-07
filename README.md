# CreditCard_Default_Classifier
My iNeuron internship

# User Interface
deployed this project on AWS using EC2 interface.

link : http://ec2-3-14-131-36.us-east-2.compute.amazonaws.com:8080/

# Overview

Problem Statement : Financial threats are displaying a trend about the credit risk of commercial banks as the incredible 
improvement in the financial industry has arisen. In this way, one of the biggest threats faces by 
commercial banks is the risk prediction of credit clients. The goal is to predict the probability of 
credit default based on credit card owner's characteristics and payment history.

About Dataset : This dataset contains information on default payments, demographic factors, credit data, history of 
payment, and bill statements of credit card clients in Taiwan from April 2005 to September 2005.
Collected from Lichman, M. (2013). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. 
Irvine, CA: University of California, School of Information and Computer Science. Dataset consists of 
30000 rows and 25 columns. 

# Approach:
The main goal is to classify the person whether he will be a defaulter or non defaulter based on different factors available in the dataset.

1.Data Exploration : Started exploring dataset using pandas,numpy,matplotlib and seaborn and PandasProfiling.

2.Data visualization : Ploted graphs to get insights about dependend and independed variables.

3.Feature Engineering : Removed duplicates, changes some unspecified values in some columns as per Data description and as per insights.

4.Model Selection I : Tested all base models to check the base accuracy and as well as clustered the training data and trained the each cluster with different models to check the best model. However checking with RandomForest Algorithm is giving same result as clustered approach.

5.Model Selection II : Performed Hyperparameter tuning using gridsearchCV for RandomForest to get best parameters.

6.Pickle File : Selected model as per best accuracy and created pickle file.

7. Built a flask app app.py to take the user input and preprocess it and return the prediction.

8.Webpage & deployment : Created a webform that takes all the necessary inputs from user and shows output.
After that I have deployed project on AWS cloud platform.

# Technologies Used:
Python, Sklearn, Flask, Html, Css, Pandas, Numpy, AWS cloud platform.

# Technical aspect:
1.Python 3.10.10
2.Front-end: HTML, CSS
3.Back-end: Flask
4.IDE: Jupyter Notebook, VisualStudio
5.Deployment: AWS.
