import numpy as np


axis=0


class kdtree:
    
    def __init__(self, matrix):
        global axis 
        #print(axis)
        self.matrix=matrix
        #print(self.matrix)   
        self.leftchild=None
        self.rightchild=None
        self.x=0
     #calculatibg the length of matrix
        if len(matrix) > 1:
            xco=matrix[: ,0]
            yco=matrix[: ,1]
            
            axis=axis+1
        
            #if loop decides whether the partition along xaxis or not
            #partition along xaxis
            if (axis)%2 > 0:
              self.matrix[:]=self.matrix[self.matrix[:,0].argsort()] 
              
              #calculating midpoint         
              if len(xco)%2==1:
                mid=((len(matrix)/2)+0.5)
                #print(mid,"mid")
              else:
                mid=(len(matrix)/2)
              #print("left")
              #recursive call
              self.x=axis  
              print(axis)
              self.leftchild=kdtree(self.matrix[:mid])
              #print(self.matrix [:mid],"left1")
              axis=self.x
              self.rightchild=kdtree(self.matrix[mid:])
              #print(self.matrix [mid:],"right1")
              
            else:
              self.matrix[:]=self.matrix[self.matrix[:,1].argsort()] 
              print(axis)      
              #calculating midpoint         
              if len(xco)%2==1:
                mid=((len(matrix)/2)+0.5)
                #print(mid,"mid")
              else:
                mid=(len(matrix)/2)
              
              #recursive call
              self.x=axis
              self.leftchild=kdtree(self.matrix[:mid])
              #print(self.matrix [:mid],"left2")
              axis=self.x
              self.rightchild=kdtree(self.matrix[mid:])
              #print(self.matrix [mid:],"right2")
        else:
             
             return None
          
    def find_nearest(self,vector):
        
        axises=0
       
        p=matrix
        p2=matrix
        print(p,"p")
       #if len(p) > 1:
        print(len(p),"size")
        for i in range(0,11000):
            if len(p) > 1:
             if (len(p)%2) == 1:

                 mid = (len(p)/2)+0.5
                 print(mid,"mid")
             else:
                    mid=(len(p)/2)
         #find mean basing on x axis
             if axises==0:
                      axises=1
                      q=p[mid-1:mid]
                      if(vector[0][0]<=q[0][0]):
                          p=p[:mid]
                      else:
                          p=p[mid:]

             else:
                      axises=0
                      q=p[mid-1:mid]
                      if(vector[0][1]<=q[0][1]):
                          p=p[:mid]
                      else:
                          p=p[mid:]
                          
            else:
             i=11001
        bestdistance=np.linalg.norm(vector-p)      
        print(p,"nearest sort")
        
        
        #euclideance distance 
        for i in range(0,11000):
            if len(p2) > 1:
             if (len(p2)%2) == 1:

                 mid = (len(p2)/2)+0.5
                 
             else:
                    mid=(len(p2)/2)
         #find mean basing on x axis
             if axises==0:
                      axises=1
                      q=p2[mid-1:mid]
                      if(vector[0][0]<=q[0][0]):
                          p2=p2[:mid]
                          q2=p2[mid:]
                          q2[:]=q2[q2[:,1].argsort()] 
                          for i in range(1,len(q2)+1):
                           ond=q2[i:i-1]
                           otherneardistance=np.linalg.norm(vector-ond)
                           if bestdistance <= otherneardistance:
                               break
                           else:
                               bestdistance = otherneardistance
                               p=q2[i:i-1]
                      else:
                          p2=p2[mid:]
                          q2=q2[:mid]
                          q2[:]=q2[q2[:,1].argsort()] 
                          for i in range(1,len(q2)+1):
                           ond=q2[i:i-1]
                           otherneardistance=np.linalg.norm(vector-ond)
                           if bestdistance <= otherneardistance:
                               break
                           else:
                               bestdistance = otherneardistance
                               p=q2[i:i-1]

             else:   
                      axises=0
                      q2=p2[mid-1:mid]

                      if(vector[0][1]<=q[0][1]):
                          p2=p2[:mid]
                          q2=p2[mid:]
                          q2[:]=q2[q2[:,0].argsort()] 
                          for i in range(1,len(q2)+1):
                           ond=q2[i:i-1]
                           otherneardistance=np.linalg.norm(vector-ond)
                           if bestdistance <= otherneardistance:
                               break
                           else:
                               bestdistance = otherneardistance
                               p=q2[i:i-1]
                      else:
                          
                          p2=p2[mid:]
                          q2=q2[:mid]
                          q2[:]=q2[q2[:,0].argsort()] 
                          for i in range(1,len(q2)+1):
                           ond=q2[i:i-1]
                           otherneardistance=np.linalg.norm(vector-ond)
                           if bestdistance <= otherneardistance:
                               break
                           else:
                               bestdistance = otherneardistance
                               p=q2[i:i-1]
                               


                          
            else:
             i=11001

        print(p,"nearest sortfinal")
        #for i in range(0,11000):
            

#initial function call
#matrix=np.random.rand(100,2)
matrix = np.array([[2,3],[4,7],[8,1],[5,4],[7,2],[1,2],[7,1],[4,6]])
kdt=kdtree(matrix)
v1=np.array([[1,2,3]])
v2=np.array([[4,5,6]])
distance=np.linalg.norm(v1-v2)
print(distance)
vector=np.array([[1,4]])
print(matrix)
kdt.find_nearest(vector)
#print(kdtree.axis)
