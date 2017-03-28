import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
#import math
from operator import itemgetter

#vstack

#creating a gaussian distribution with 5000 data points
mu,sigma=-0.01,0.01
s=np.random.normal(mu,sigma,5000)
p=np.random.normal(mu+0.001,sigma-0.005,5000)
plt.scatter(s,p,color='red')
mat1=np.vstack((s,p)).T
#print(mat1)

#creating gaussian distribution with 5000 datappoints
mu2,sigma2=0.004,0.01
s2=np.random.normal(mu2,sigma2,5000)
p2=np.random.normal(mu2+0.001,sigma2-0.005,5000)
#print(s[0,0],"p")o id;
plt.scatter(s2,p2,color='blue')
mat2=np.vstack((s2,p2)).T


#concatenating the matrices
matrix=np.concatenate((mat1,mat2),axis=0)

#concatenating the y coordinates of two distributions to keep track of data points
p3=np.concatenate((p,p2),axis=0)

indexed=np.argsort(p3)


#generating the y vector
y = []
j = 0
for i in range(0,10000):
  if indexed[i] < 5000:
    y.append(0)
  else:
    y.append(1)


#sorting the matrix baasing on y coordinates
matrix=matrix[matrix[:, 1].argsort()]



#calculating  training data
y=np.asarray(y)
mask=np.random.rand(10000)<0.8
X=matrix[mask]
ytrain=y[mask]


#calculating testing data
mask2=np.logical_not(mask)
test=matrix[mask2]
ytest=y[mask2]
#rint(ytest)


#calculating beta
beta=[]
mats=np.dot(X.T,X)
inv=np.linalg.inv(mats)
beta=np.dot(inv,X.T)
beta=np.dot(beta,ytrain)
beta=np.asarray(beta)


#calculating y^, ycap matrix contains the value of X.t*beta
ycapmatrix=np.dot(beta,test.T)
ycap=[]
length=len(test)
length
for i in range(0,length):
    #print(ycapmatrix[i])
    if ycapmatrix[i] < 0.25:
     ycap.append(0)
    else:
     ycap.append(1)

trainingclass0=[]
trainingclass1=[]

#plotting correctly classified elements of class0
traininglength=len(X)
for i in range(0,traininglength):
    if ytrain[i]==0:
     trainingclass0.append(i)
    else:
     trainingclass1.append(i)

traininglength_0=len(trainingclass0)
traininglength_1=len(trainingclass1)
w,h=2,traininglength_0
class0matrix=[[0 for x in range(w)] for y in range(h)]

for i in range(0,traininglength_0): 
  for j in range(0,2):
    #lengthofclassoelements in training set
      leng=trainingclass0[i]
      class0matrix[i][j] = X[leng][j] 
      a1check=1 

trainingclass0=np.asarray(trainingclass0)
#choosing the x and y coordinates by slicing the matrix
if a1check==1:
 Xcoordinates_0=np.array(class0matrix)[:,0]
 ycoordinates_0=np.array(class0matrix)[:,1]
 plt.scatter(Xcoordinates_0,ycoordinates_0,color='red')
#plt.show()



#plotting training set elements from class1
traininglength_1=len(trainingclass1)
w,h=2,traininglength_1
class1matrix=[[0 for x in range(w)] for y in range(h)]

for i in range(0,traininglength_1): 
  for j in range(0,2):
     leng=trainingclass1[i]
     class1matrix[i][j] = X[leng][j] 
     a2check=1
     
if a2check==1:
 Xcoordinates_1=np.array(class1matrix)[:,0]
 ycoordinates_1=np.array(class1matrix)[:,1]
 plt.scatter(Xcoordinates_1,ycoordinates_1,color='green')
#plt.show()


#plotting correctly and incorrectly classified set elements from classes 0 and 1
correcttestclass0=[]
incorrecttestclass0=[]
correcttestclass1=[]
incorrecttestclass1=[]
traininglengthtest=len(test)
for i in range(0,traininglengthtest):
    if ytest[i]==0:
        if ycap[i]==0:
         correcttestclass0.append(i)
        else:
         incorrecttestclass0.append(i)
    else:
     if ycap[i]==1:
         correcttestclass1.append(i)
     else:
         incorrecttestclass1.append(i)

length_correctclass0=len(correcttestclass0)
length_incorrectclass0=len(incorrecttestclass0)
length_correctclass1=len(correcttestclass1)
length_incorrectclass1=len(incorrecttestclass1)
#plotting graph for correct class 0
w1,h1=2,length_correctclass0
a3check=0
a4check=0
a5check=0
a6check=0
correctclass0matrix=[[0 for x in range(w1)] for y in range(h1)]
for i in range(0,length_correctclass0): 
  for j in range(0,2):
     leng1=correcttestclass0[i]     
     correctclass0matrix[i][j] = test[leng1][j]
     a3check=1

if a3check==1:
  Xcoordinates_correct0=np.array(correctclass0matrix)[:,0]
  ycoordinates_correct0=np.array(correctclass0matrix)[:,1]
  plt.scatter(Xcoordinates_correct0,ycoordinates_correct0,color ='blue')
#plt.show()

#plotting graph for corrrect class1
w2,h2=2,length_correctclass1
correctclass1matrix=[[0 for x in range(w2)] for y in range(h2)]
for i in range(0,length_correctclass1): 
  for j in range(0,2):
     leng1=correcttestclass1[i]     
     correctclass1matrix[i][j] = test[leng1][j]
     a4check=1
if a4check==1:
  Xcoordinates_correct1=np.array(correctclass1matrix)[:,0]
  ycoordinates_correct1=np.array(correctclass1matrix)[:,1]
  plt.scatter(Xcoordinates_correct1,ycoordinates_correct1,color ='black')
#plotting for incorrect class0     
w3,h3=2,length_incorrectclass0
incorrectclass0matrix=[[0 for x in range(w3)] for y in range(h3)]
for i in range(0,length_incorrectclass0): 
  for j in range(0,2):
     leng1=incorrecttestclass0[i]     
     incorrectclass0matrix[i][j] = test[leng1][j]
     a5check=1

#print(a5check)
if a5check==1 :  
  Xcoordinates_incorrect0=np.array(incorrectclass0matrix)[:,0]
  ycoordinates_incorrect0=np.array(incorrectclass0matrix)[:,1]
  plt.scatter(Xcoordinates_incorrect0,ycoordinates_incorrect0,color='orange')



#plotting for incorrectclass1
w3,h3=2,length_incorrectclass1
incorrectclass1matrix=[[0 for x in range(w3)] for y in range(h3)]
for i in range(0,length_incorrectclass1): 
  for j in range(0,2):
     leng1=incorrecttestclass1[i]     
     incorrectclass1matrix[i][j] = test[leng1][j]
     #a6check==1

if a6check == 1:
  Xcoordinates_incorrect1=np.array(incorrectclass1matrix)[:,0]
  ycoordinates_incorrect1=np.array(incorrectclass1matrix)[:,1]
  plt.scatter(Xcoordinates_incorrect1,ycoordinates_incorrect1,color ='yellow')

plt.show()



