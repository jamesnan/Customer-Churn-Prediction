# Customer-Churn-Prediction
# Define the problem
Churn is a one of the biggest problem in the telecom industry. Research has shown that the average monthly churn rate among the top 4 wireless carriers in the US is 1.9%. 2%. Customer churn prediction is to measure why customers are leaving a business. While it's not the happiest measure, it's a number that can give your company the hard truth about its customer retention. 


# STEPS
1. Loading Data 

The data set is taken from [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn) and stems the IBM sample data set collection .

2. Exploratory Data Analysis

EDA includes few steps as the following: data cleaning, identify and handling inconsistencies (i.e. missing values, duplicated values, skewness, outliers), format correction

3. Feature Engineering
* Transform tenure to tenure_grounp
* Normolize numerical columns with MinMaxScaler
* One-hot encoding for Categorical columns
* Correlation Analysis 
* Removing highly corelated and unrelated  features 

4. Train-Test-Split
* Split the data set into 80% training data and 20% test data. The “Churn” column is defined as the target (the “y”), the remaining columns as the features (the “X”).
* Oversampling due to skewness of data

5. Building Model 
* Building following models:Logistic Regression, Random Forest, Decision Tree, SVM, K-Nearest Neighbor, Naive Bayes, Ridge Classifier, Bagging Classifier, XGboost, LightGBM, Multilayer Perceptron (Neural Network), Adaboost, Gradiant Boosting, CatBoost, Voting Classifier, Deep Learning model (ANN)
* Model Evaluation : Compare Several models according to their accuracies
* Save random forest model for flask app

6. Deployment
Creating a flask app and deploy it to Heroku at: https://customerchurnpredict.herokuapp.com/

# Built with
* numpy
* pandas 
* seaborn
* matplotlib
* sklearn
* xgboost
* lightgbm
* catboost
* imblearn
* tensorflow 
* pickle
