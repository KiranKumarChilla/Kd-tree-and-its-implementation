import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math
from operator import itemgetter

#vstack

#creating 1000 datapoints from 10 different gaussian distributions
#gaussian distribution1
mu,sigma=-0.01,0.01
s=np.random.normal(mu,sigma,1000)
p=np.random.normal(mu+0.001,sigma-0.005,1000)
plt.scatter(s,p,color='blue')

mat1=np.vstack((s,p)).T
#print(mat1)

#gaussiandistribution2
mu2,sigma2=-0.02,0.01
s2=np.random.normal(mu2,sigma2,1000)
p2=np.random.normal(mu2+0.001,sigma2-0.005,1000)
#print(s[0,0],"p")o id;
plt.scatter(s2,p2,color='blue')
mat2=np.vstack((s2,p2)).T
#plt.show()

#gaussian distribution3
mu,sigma=-0.03,0.02
s3=np.random.normal(mu,sigma,1000)
p3=np.random.normal(mu+0.001,sigma-0.005,1000)
plt.scatter(s,p,color='blue')
mat3=np.vstack((s3,p3)).T
#print(mat1)

#gaussian distribution4
mu2,sigma2=-0.04,0.01
s4=np.random.normal(mu2,sigma2,1000)
p4=np.random.normal(mu2+0.001,sigma2-0.005,1000)
#print(s[0,0],"p")o id;
plt.scatter(s4,p4,color='blue')
mat4=np.vstack((s4,p4)).T

#gaussian distribution5
mu,sigma=-0.05,0.01
s5=np.random.normal(mu,sigma,1000)
p5=np.random.normal(mu+0.001,sigma-0.005,1000)
plt.scatter(s,p,color='blue')
mat5=np.vstack((s5,p5)).T


##gaussian distribution6
mu2,sigma2=-0.06,0.01
s6=np.random.normal(mu2,sigma2,1000)
p6=np.random.normal(mu2+0.001,sigma2-0.005,1000)
#print(s[0,0],"p")o id;
plt.scatter(s6,p6,color='red')
mat6=np.vstack((s6,p6)).T

#gaussian distribution7
mu,sigma=-0.07,0.01
s7=np.random.normal(mu,sigma,1000)
p7=np.random.normal(mu+0.001,sigma-0.005,1000)
plt.scatter(s,p,color='red')
mat7=np.vstack((s7,p7)).T

#gaussian distribution8
mu,sigma=-0.08,0.01
s8=np.random.normal(mu,sigma,1000)
p8=np.random.normal(mu+0.001,sigma-0.005,1000)
plt.scatter(s,p,color='red')
mat8=np.vstack((s8,p8)).T

#gaussian distribution9
mu,sigma=-0.09,0.01
s9=np.random.normal(mu,sigma,1000)
p9=np.random.normal(mu+0.001,sigma-0.005,1000)
plt.scatter(s,p,color='red')
mat9=np.vstack((s9,p9)).T

#gaussian distribution10
mu,sigma=-0.1,0.01
s10=np.random.normal(mu,sigma,1000)
p10=np.random.normal(mu+0.001,sigma-0.005,1000)
plt.scatter(s,p,color='red')
mat10=np.vstack((s10,p10)).T


#concatenating all datapoints
matrix=np.concatenate((mat1,mat2,mat3,mat4,mat5,mat6,mat7,mat8,mat9,mat10),axis=0)

#pfinal is concatenation of all y coordinates since it is useful in sorting entire distribution basing on y coordinates
pfinal=np.concatenate((p,p2,p3,p4,p5,p6,p7,p8,p9,p10 ),axis=0)

indexed=np.argsort(pfinal)

#generating the y vector
y = []
j = 0
for i in range(0,10000):
  if indexed[i] < 5000:
    y.append(0)
  else:
    y.append(1)


#matrix sort basing on ycoordinates
matrix=matrix[matrix[:, 1].argsort()]



#calculating  training data
y=np.asarray(y)
mask=np.random.rand(10000)<0.8
X=matrix[mask]
#print(X)
ytrain=y[mask]
#print(ytrain)

#calculating testing data
mask2=np.logical_not(mask)
test=matrix[mask2]
ytest=y[mask2]
#print(ytest)


#calculating beta
beta=[]
mats=np.dot(X.T,X)

inv=np.linalg.inv(mats)
#print(inv)
#print(X.T)
beta=np.dot(inv,X.T)
#print(beta)
beta=np.dot(beta,ytrain)
#print(beta)

beta=np.asarray(beta)



#calculating y^,ycap matrice contains the value of X.T*beta
ycapmatrix=np.dot(beta,test.T)
#print(ycapmatrix.size)
ycap=[]
length=len(test)
length
for i in range(0,length):
    #print(ycapmatrix[i])
    if ycapmatrix[i] < 0.5:
     ycap.append(0)
    else:
     ycap.append(1)



trainingclass0=[]
trainingclass1=[]

#plotting training set elements from class0
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
#class0matrix=np.asarray(Xcoordinates)
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



#plotting trainingset elements from class1
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


#plotting correct and incorrectly classified elements from class 0 and class1
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

a3check=0
a4check=0
a5check=0
a6check=0
length_correctclass0=len(correcttestclass0)
length_incorrectclass0=len(incorrecttestclass0)
length_correctclass1=len(correcttestclass1)
length_incorrectclass1=len(incorrecttestclass1)
#plotting graph for correct class 0
w1,h1=2,length_correctclass0
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
#plt.show()

#plotting for incorrect class0     
w3,h3=2,length_incorrectclass0
incorrectclass0matrix=[[0 for x in range(w3)] for y in range(h3)]
for i in range(0,length_incorrectclass0): 
  for j in range(0,2):
     leng1=incorrecttestclass0[i]     
     incorrectclass0matrix[i][j] = test[leng1][j]
     a5check=1

if a5check==1 :  
  Xcoordinates_incorrect0=np.array(incorrectclass0matrix)[:,0]
  ycoordinates_incorrect0=np.array(incorrectclass0matrix)[:,1]
  plt.scatter(Xcoordinates_incorrect0,ycoordinates_incorrect0,color='orange')
#plt.show()

#plotting for incorrectclass1
w3,h3=2,length_incorrectclass1
incorrectclass1matrix=[[0 for x in range(w3)] for y in range(h3)]
for i in range(0,length_incorrectclass1): 
  for j in range(0,2):
     leng1=incorrecttestclass1[i]     
     incorrectclass1matrix[i][j] = test[leng1][j]
     a6check==1
print(a6check)
if a6check==1:
  Xcoordinates_incorrect1=np.array(incorrectclass1matrix)[:,0]
  ycoordinates_incorrect1=np.array(incorrectclass1matrix)[:,1]
  plt.scatter(Xcoordinates_incorrect1,ycoordinates_incorrect1,color ='yellow')

plt.show()
