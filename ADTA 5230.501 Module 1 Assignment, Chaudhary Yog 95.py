#!/usr/bin/env python
# coding: utf-8

# #YC95

# Q1. Solve Problem 2.1 of Chapter 2 (a through h) on page 56 of your textbook. 
# 
# 2.1 Assuming that data mining techniques are to be used in the following cases, identify whether. The task required is supervised or unsupervised learning. 
# 
# a. Deciding whether to issue a loan to an applicant based on demographic and financial data (with reference to a database of similar data on prior customers). 
# 
# Supervised learning: Supervised learning requires labeled data, such as the historical customer. database with loan approval status. It is possible to forecast loan issuance for new applicants by training a model with demographic and financial data as input characteristics and loan approval as the goal variable. 
# 
# b. In an online bookstore, making recommendations to customers concerning additional items to buy based on the buying patterns in prior transactions. 
# 
#  Unsupervised learning: Unsupervised learning is a sort of machine learning in which the model is. trained using data that has not been labeled, i.e., there are no goal variables or predefined labels. Without any clear direction, the objective is to find patterns, structures, or correlations in the data. 
# 
# c. Identifying a network data packet as dangerous (virus, hacker attack) based on comparison to other packets whose threat status is known. 
# 
#  Supervised learning: Supervised learning encompasses the challenge of classifying network data. packet as harmful based on comparison to other packets with known threat status. This is supervised learning because the status is known for the other packets. 
# 
# d. Identifying segments of similar customers. 
# 
# Unsupervised learning: Unsupervised learning, which groups clients based on patterns and correlations within their data rather than using predetermined labels or known outcomes, is in fact. used to find segments of comparable customers. 
# 
# e. Predicting whether a company will go bankrupt based on comparing its financial data to those of similar bankrupt and nonbankrupt firms. 
# 
# Supervised learning: An example of supervised learning is the problem of forecasting a company. bankruptcy based on a comparison of its financial data to similar bankrupt and nonbankrupt. enterprises. The model is trained using labeled data, with the labels being financial data from organizations that have filed for bankruptcy and those that have not. The program learns patterns. and associations to categorize new firms as bankrupt or nonbankrupt by examining financial metrics. 
# 
# f. Estimating the repair time required for an aircraft based on a trouble ticket. 
# 
# Supervised learning: Historical data with labeled repair times is used to train the model, which analyses trouble ticket features to make predictions. 
# 
# g. Automated sorting of mail by zip code scanning. 
# 
# Unsupervised learning: The model analyses zip codes without predefined labels to identify. patterns and cluster similar zip codes for sorting. This is supervised learning because you would probably know if the sorting was correct. 
# 
# h. Printing of custom discount coupons at the conclusion of a grocery store checkout based on what. you just bought and what others have bought previously. 
# 
# Unsupervised learning: Custom discount coupons based on your purchase history and the behavior of others involve unsupervised learning, specifically collaborative filtering. No predefined labels are needed as the system analyses collective purchasing behavior to generate personalization. coupons. 

# Q2. Solve Problem 2.2 of Chapter 2 on page 56 of your textbook. 
# 
# 2.2 Describe the difference in roles assumed by the validation partition and the test partition. 
# 
# Answer: The validation partition is used to pick the best model (where multiple models are trained on the training data) whereas the test partition is used to provide an estimate of how the chosen model will perform with unknown data. 

# Q3. Solve Problem 2.3 of Chapter 2 on page 56 of your textbook. 
# 
# 2.3 Consider the sample from a database of credit applications shown in Figure 2.16. Comment on the likelihood that it was sampled randomly, and whether it is likely to be a useful sample. 
# 
# Answer: As it can be seen from the OBS number, there is a pattern in the observations selected for the sample. More accurately, samples are selected based on multiples of 8. Therefore, these samples are likely. selected based on a pre-decided pattern and seems not to be random. Besides that, samples are probably not selected randomly, and that questions their usefulness, there are too many variables in the (columns) compared to samples (rows), which makes any kind of prediction inaccurate due to a low number of samples. 

# Q4. What are the nine characteristics of big data? Instantiate a generation of big data in our daily life. 
# 
# Answer: The nine characteristics of big data, often referred to as the nine characteristics, are: 
# 
# a) Volume: Big data involves vast amounts of data that exceed the storage capacity of conventional databases and tools. 
# 
# b) Velocity: Data is generated and collected at high speeds, often in real-time or near-real-time. 
# 
# c) Variety: Big data comes in various forms, including structured, semi-structured, and unstructured data. It can include text, images, videos, sensor data, and more. 
# 
# d) Veracity: Data quality and reliability can vary significantly. Big data may contain errors, inconsistencies, and inaccuracies. 
# 
# e) Validity: Data should be relevant and accurate for the intended analysis or application. 
# 
# f) Variability: Data can have inconsistent formats, structures, or meanings, making it challenging to work with. 
# 
# g) Volatility: Data can change rapidly, requiring frequent updates and management. 
# 
# h) Visualization: Effective visualization tools and techniques are needed to make sense of the data and communicate insights. 
# 
# i) Value: Ultimately, the goal of big data is to extract valuable insights and knowledge that can drive informed decision-making. 
# 
# An example of big data in our daily lives is social media platforms like Facebook or Twitter. These platforms collect and process vast amounts of user-generated data, including text posts, images, videos, and user interactions. They analyze this data to provide personalized content recommendations, targeted advertisements, and insights into user behavior. The data is generated and processed in real-time, exhibiting characteristics like high volume, velocity, variety, and value. 

# Q5. Solve Problem 2.4 of Chapter 2 on page 56 of your textbook. 
# 
# Consider the sample from a bank database shown in Table 2.17, It was selected randomly from a large database to be training set. Personal Loan indicates whether a solicitation for a personal loan was accepted and is the response variable. A campaign is planned for a similar solicitation in the future and the bank is looking for a model that will identify a likely response. Examine the data carefully and indicate what your next step would be.  
# 
#  
# Answer: The dataset represents a sample from a bank database, specifically selected to be used as a training set for a campaign aimed at soliciting personal loans. The key variable of interest is "Personal Loan," which indicates whether individuals accepted the solicitation for a personal loan (with values 1 for accepted and 0 for not accepted). This dataset contains various attributes for each individual that can potentially be used as predictors for identifying likely responders to the loan solicitation. 
# 
# After summarizing (dataset in Table 2.17) the columns and understanding their possible meanings, your next steps for building a model to identify likely responders to the personal loan solicitation campaign would typically involve data preprocessing, feature engineering, model selection, and evaluation. These steps are outlined in the previous response to ensure that you prepare the data and build a predictive model that can effectively identify potential responders. 

# Q6. What is overfitting and why do we refrain from it? 
# 
# Answer: Overfitting is a phenomenon in machine learning where a model learns the training data too well, including its noise and random fluctuations. This leads to a model that performs exceptionally well on the training data but fails to generalize to new, unseen data. We refrain from overfitting because it results in models that are overly complex and not robust, making them unreliable for real-world applications. To combat overfitting, techniques like cross-validation, regularization, and using larger and more diverse datasets are employed. 

# Q7. Solve Problem 2.7 of Chapter 2 on page 57 of your textbook. 
# A data set has 100 records and 50 variables with 5% of the values missing, spread randomly throughout the record and variable. An analyst decides to remove records with missing values. About how many records would you expect to be removed?  
# 
# Answer:  Data set has 1000 records and 50 variables; we assume that each variable has 1000 records then 1000*50 = 50,000 values for missing values 5% of 50,000 = 2500 values are missing;  
# 
# The number of records that may contain theses missing values = 2500/50 = 50 
# Therefore; 50 records are to be removed  

# Q8. Why are there so many different methods for classification and prediction? 
# 
# Answer: There are many different methods for classification and prediction in machine learning because different problems require different approaches. The choice of method depends on factors such as the nature of the data, the problem's complexity, the amount of data available, and the desired trade-off between accuracy and interpretability. No single method is universally superior, so researchers and practitioners develop and use various algorithms to address the diversity of real-world problems.  
# 
# The diversity of data, the complexity of problems, the availability of algorithms, and the specific needs of different applications all contribute to the wide array of classification and prediction methods available. The choice of method should be driven by careful consideration of the problem at hand, the characteristics of the data, and the goals of the analysis. 

#  Q9. Solve Problem 2.8 of Chapter 2 on page 57 of your textbook. 
# 
# Table 2.18 
# 
# Age                         Income ($) 
# 
# 25                          49,000 
# 
# 56                          156,000 
# 
# 65                          99,000 
# 
# 32                          192,000 
# 
# 41                          39,000 
# 
# 49                          57,000 
# 
# Answer: Normalization of a measurement is obtained by subtracting the average from each measurement and dividing the difference by the standard deviation. 
# 
# Number of Items (N) = 6 
# 
# Mean (M2) of Age = (25 + 56 + 65 + 32 + 41 + 49) / 6 =   44.6667 
# 
# Mean (M1) of Income = (49000+156000+99000+192000+39000+5700) /6 = 98666.67 
# 
# Standard Deviation (σ) =  
# 
# Difference of mean and Normalized given values:
# 

# In[4]:


# python 
import statistics 
ages = [25,56,65, 32,41,49]
# Claculation mean average ages
mean_age = statistics.mean(ages)
# Saandeard Deviations 
std_dev_age = statistics.stdev(ages)


# Q10. What is the key difference between classification and prediction in data mining? 
# 
# Answer: The key difference between classification and prediction in data mining is as follows: Classification: Classification is a supervised learning task where the goal is to assign predefined labels or categories to input data based on its features. It involves training a model on a labeled dataset, and the model's primary objective is to classify new, unseen data points into one of the predefined classes. For example, classifying emails as spam or spam. Prediction: Prediction, also known as regression, is another supervised learning task. Instead of assigning categorical labels, prediction aims to estimate a continuous or numerical value as the output. It involves learning the relationships between input features and a target variable, allowing the model to make predictions about numerical outcomes. For instance, predicting house prices based on features like size, location, and number of bedrooms. 

# Q11. Give an example to the association rule that is used in marketing.
# 
# Answer: An example of an association rule used in marketing is the "Market Basket Analysis." In this context, market basket analysis identifies patterns in customer shopping behaviors by analyzing the items that tend to be purchased together. For instance, a common association rule could be: "If a customer buys product A, they are likely to also buy product B. "Supermarkets and online retailers use this type of association rule to improve product placement, optimize cross-selling strategies, and offer personalized product recommendations to customers. For example, if a customer adds coffee to their online shopping cart, the system might suggest purchasing coffee filters or a coffee maker as well.

# Q12. Solve Problem 2.10 of Chapter 2 on page 56 of your textbook. 
# 
# Answer: A model is developed based on a training set; the model learns from the training data set. A trained model is validated on the test data set. Based on test results, accuracy measures will be calculated. The accuracy measures tell the quality of a model. The efficiency of a model depends on how accurately it is classifying unknown data, and test data but on classifying known data training data. Therefore, the more accurate model (Model B) is considered for final deployment. Based on a training set, a model is created, and the model learns from the training data set. The test dataset is used to validate the trained model. Accuracy measures will be computed using test outcomes. The accuracy metrics reveal a model's quality. A model's effectiveness depends on how well it can identify both test and unknown data, as well as training and known data. The more accurate model (Model B) is therefore taken into consideration for the final deployment. 

# Q13. What are outliers and how do we treat them in big data? 
# 
# Answer: Outliers are data points that significantly deviate from the majority of data in a dataset. They can be unusually high or low values and are often considered noise or anomalies. In big data, treating outliers is essential to ensure the quality and reliability of analyses and predictions. Various methods can be used to handle outliers, such as: 
# 
# a) Removing outliers: In some cases, it may be appropriate to remove outliers from the dataset if they are genuine errors or extreme values that do not represent the underlying patterns. 
# 
# b) Transforming data: Data transformation techniques, like logarithmic scaling or winsorization, can help reduce the impact of outliers on statistical analyses. 
# 
# c) Model-based approaches: Some machine learning models are robust to outliers, while others are sensitive. Choosing an appropriate model can help mitigate the influence of outliers. 
# 
# d) Imputation: For missing values caused by outliers, imputation methods can be used to estimate or replace the missing values. 
# 
# The treatment of outliers depends on the specific problem, the nature of the data, and the goals of the analysis. 

#  Q14. What do we partition any data set into for machine learning? 
# 
# In machine learning, a dataset is typically partitioned into three main subsets: 
# 
# a) Training Set: The training set is the largest portion of the dataset and is used to train the machine learning model. The model learns patterns, relationships, and features from this set. Essentially, it's like a teacher providing examples to a student. 
# 
# b) Validation Set: The validation set is used to fine-tune the model's hyperparameters and evaluate its performance during training. It helps prevent overfitting by providing an independent dataset that the model hasn't seen during training. The model's performance on the validation set guides the adjustments to its configuration. 
# 
# c) Test Set: The test set is a completely independent dataset that is not used during model training or hyperparameter tuning. It serves as the final evaluation of the model's performance. By assessing how well the model generalizes to new, unseen data in the test set, we can gauge its overall effectiveness. 
# 
# The reason for partitioning a dataset into these subsets is to ensure that the machine learning model learns from one portion of the data, generalizes to another (validation set), and is rigorously tested on a third (test set) to assess its real-world performance. This process helps in building models that can make accurate predictions or classifications when exposed to new, unseen data. 

# # HO1 Download and Installation is completed Jupyter Notebook  
# 

# # HO2 Completed code blocks with comments are run 
# 
# 
# 

# In[4]:


print("Welcome to python Programing and Data Mining analysis ")


# In[1]:


#**Integer**

int1 = 12
print(int1)
print(type(int1))


# In[2]:


#**Float**

flt1 = 3.1414
print(flt1)
print(type(flt1))


# In[3]:


#**Complex**

cmplx1 = 2+3j
print(cmplx1)
print(type(cmplx1))


# In[4]:


#**Boolean**

bavindra = True
print(bavindra)
print(type(bavindra))


# In[5]:


#**Boolean**

bavindra = False
print(bavindra)
print(type(bavindra))


# In[6]:


#**String**

str1 = 'Python Programming'
print(str1)
print(type(str1))
     


# In[7]:


#**String**

str1 = """\'Python Programming\' """
print(str1)
print(type(str1))
str1


# In[8]:


str1 = My name is 'Yog Chaudhary'. I like "Python Language".


# In[9]:


str1 = """My name is 'Yog Chaudhary'. I like "Python Language"."""
print(str1)
     


# In[13]:


str1 = "Python Programming"


# In[14]:


str1[0]


# In[17]:


print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])


# In[18]:


str1 = " apple , banana, cherry"


# In[21]:


# print "apple "
str1[0:6]


# In[22]:


str1 = "Python Programming"


# In[23]:


print(str1[:])
print(str1[::])


# In[24]:


print(str1[::1])
print(str1[::2])
print(str1[::3])
print(str1[::4])
print(str1[::5])
print(str1[::6])


# In[25]:


print(str1[::-1])


# In[26]:


str1 = 'Harry Potter - Goblet of Fire'

# +ve indexing +ve slicing (left to right)
print(str1[0:len(str1):1])

print(-(len(str1)+1))

# -ve indexing -ve slicing (right to left)
print(str1[-1:-(len(str1)+1):-1])

# +ve indexing -ve slicing (right to left)
print(str1[28::-1])

# -ve indexing +ve slicing (left to right)
print(str1[-29::1])


# In[27]:


str1 = 'PYTHON PROGRAMMING'

# +ve indexing +ve slicing (left to right)
print(str1[0:len(str1):1])

print(-(len(str1)+1))

# -ve indexing -ve slicing (right to left)
print(str1[-1:-(len(str1)+1):-1])

# +ve indexing -ve slicing (right to left)
print(str1[28::-1])

# -ve indexing +ve slicing (left to right)
print(str1[-29::1])


# In[ ]:


# God job

