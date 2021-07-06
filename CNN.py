#!/usr/bin/env python
# coding: utf-8

# In[1]:


from numpy import loadtxt


# In[2]:


from keras.datasets import mnist


# In[3]:


import os


# In[4]:


(X_train,y_train),(X_test,y_test) = mnist.load_data()


# In[5]:


X_train=X_train.reshape(60000,28,28,1)


# In[6]:


X_test=X_test.reshape(10000,28,28,1)


# In[7]:


from tensorflow.keras.utils import to_categorical


# In[8]:


y_train = to_categorical(y_train)


# In[9]:


y_test = to_categorical(y_test)


# In[10]:


from keras.models import Sequential


# In[11]:


from keras.layers import Dense, Conv2D,Flatten


# In[12]:


model = Sequential()


# In[13]:


model.add(Conv2D(2, kernel_size=3, activation="relu",input_shape=(28,28,1)))


# In[43]:


try:
   f=open("/layers.txt","r")
   i = f.read()
except:
   print(end="")
finally:
    f.close()
    print(i)
i = int(i)
n=4


# In[15]:


for i in range(i):
    model.add(Conv2D(filters=n,kernel_size=3,activation="relu"))
    n=n*2
    


# In[16]:


model.add(Flatten())


# In[17]:


model.add(Dense(10,activation="softmax"))


# In[18]:


model.compile(optimizer='adam', loss='categorical_crossentropy',metrics=['accuracy'])


# In[19]:


model.fit(X_train,y_train,epochs=1)


# In[21]:


Accuracy=model.evaluate(X_test,y_test)


# In[22]:


print("Accuracy is :-",Accuracy[1]*100)

# In[41]:


try:
   f=open("/data.txt","w")
   f.write(str(int(Accuracy[1]*100)))
except:
   print(end="")
finally:
    f.close()


