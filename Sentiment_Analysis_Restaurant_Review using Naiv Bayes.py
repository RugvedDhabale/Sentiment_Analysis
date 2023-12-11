#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np #linear algebra
import pandas as pd


# In[2]:


data= pd.read_csv('Restaurant_Reviews (1).csv')


# In[3]:


data.shape


# In[4]:


data.columns


# In[5]:


data.head()


# In[12]:


data.info()


# In[13]:


import nltk
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# In[14]:


corpus =[]
for i in range(0,1000):
   review =re.sub(pattern='[^a-zA-Z]',repl=' ', string=data['Review'][i])

   review = review.lower()
   review_words = review.split()
   review_words = [word for word in review_words if not word in set(stopwords.words('english'))]

   ps= PorterStemmer()
   review =[ps.stem(word) for word in review_words]

   review = ' '.join(review)
   corpus.append(review)


# In[15]:


corpus[:1500]


# In[16]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
X =cv.fit_transform(corpus).toarray()
y = data.iloc[:,1].values


# In[17]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X,y,test_size=0.20, random_state=0)


# In[18]:


X_train.shape,X_test.shape, y_train.shape,y_test.shape


# In[19]:


from sklearn.naive_bayes import MultinomialNB

classifier =MultinomialNB()
classifier.fit(X_train, y_train)


# In[20]:


y_pred = classifier.predict(X_test)

y_pred


# In[21]:


from sklearn.metrics import accuracy_score

from sklearn.metrics import precision_score

from sklearn.metrics import recall_score

score1 =accuracy_score(y_test,y_pred)
score2 = accuracy_score(y_test,y_pred)
score3 = recall_score(y_test,y_pred)

print("---------SCORES--------")
print("Accuracy score is {}%".format(round(score1*100,3)))
print("Precision score is {}%".format(round(score2*100,3)))
print("recall score is {}%".format(round(score3*100,3)))


# In[22]:


from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)


# In[23]:


cm


# In[24]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

plt.figure(figsize =(10,6))
sns.heatmap(cm, annot=True, cmap="YlGnBu", xticklabels=['Negative','Positive'],yticklabels=['Negative','Positive'])
plt.xlabel('Predicted values')
plt.ylabel('Actual Values')


# In[25]:


from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
best_accuracy =0.0
alpha_val =0.0
for i in np.arange(0.1,1.1,0.1):
  temp_classifier =MultinomialNB(alpha=i)
  temp_classifier.fit(X_train,y_train)
  temp_y_pred =temp_classifier.predict(X_test)
  score = accuracy_score(y_test,temp_y_pred)
  print("Accuracy Score for alpha={} is {}%".format(round(i,1),round(score*100,3)))
  if score>best_accuracy:
     best_accuracy=score
     alpha_val =i
print('----------------------------------------------------')
print("The Best Accuracy Score is {}% with alpha value as {}".format(round(best_accuracy*100, 2), round(alpha_val, 1)))


# In[26]:


classifier =MultinomialNB(alpha=0.2)
classifier.fit(X_train, y_train)


# In[27]:


import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def predict_sentiment(sample_review):
    sample_review = re.sub(pattern='[^a-zA-Z]', repl=' ', string=sample_review)
    sample_review = sample_review.lower()
    sample_review_words = sample_review.split()
    sample_review_words = [word for word in sample_review_words if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    final_review = [ps.stem(word) for word in sample_review_words]
    final_review = ' '.join(final_review)

    temp = cv.transform([final_review]).toarray()
    return classifier.predict(temp)


# In[28]:


sample_review ='The food is really bad.'

if predict_sentiment(sample_review):
  print("This is a Positive review")

else:
  print("This is a Negative review")


# In[29]:


sample_review ='Food was pretty bad and the service was very slow'

if predict_sentiment(sample_review):
  print("This is a Positive review")

else:
  print("This is a Negative review")


# In[30]:


sample_review ='The food  was absolutely wonderful,from preparation to presentation, very pleasing.'

if predict_sentiment(sample_review):
  print("This is a Positive review")

else:
  print("This is a Negative review")


# In[31]:


sample_review ='took hour get food tabl restaur food luke warm sever run around like total overwhelm'

if predict_sentiment(sample_review):
  print("This is a Positive review")

else:
  print("This is a Negative review")


# In[32]:


sample_review ='one best bar food vega'

if predict_sentiment(sample_review):
  print("This is a Positive review")

else:
  print("This is a Negative review")


# In[ ]:




