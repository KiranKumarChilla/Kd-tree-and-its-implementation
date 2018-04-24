import sys
import operator
import sys

#It has basic implementation of Kd tree
def inputarr():
 matrix = []
 count = 0
 while True:
      if count>1:break
      if count==0: 
        print ("x co-ordinates:")
      if count==1: 
        print ("y co-ordinates:")
      line = input()
      values = line.split()
      if count>0:
        if len(values)!=len(matrix[0]):
          print ("Missing y co-ordinates")
          sys.exit()
      count+=1
      row = [int(value) for value in values]
      matrix.append(row)

 return matrix

class kdTree:
    def __init__(self,matrix):
       self.x=1
       self.matrix=matrix
       
    def getTree(self,matrix):
       
      kd=kdTree(matrix)
      if len(matrix[0])<=1:
          return matrix 
      else:  
       if self.x==0:
           self.x=1
           X=sorted(zip(matrix[0],matrix[1]),key=operator.itemgetter(1))
           matrix[0], matrix[1] = zip(*X)
           
           if len(matrix[1])%2==1:
               mid=matrix[1][int(len(matrix[1])/2)]
               
           else:
               mid=(matrix[1][int(len(matrix[1])/2)] + matrix[1][int((len(matrix[1])-1)/2)])/2
               
           lefty = [x for x in matrix[1] if x<mid]
           leftx = [matrix[0][matrix[1].index(y)] for y in matrix[1] if y<mid]
           middley = [x for x in matrix[1] if x==mid]
           middlex = [matrix[0][matrix[1].index(y)] for y in matrix[1] if y==mid]
           righty = [x for x in matrix[1] if x>mid]
           rightx = [matrix[0][matrix[1].index(y)] for y in matrix[1] if y>mid]
           left=[leftx,lefty]
           middle=[middlex,middley]
           right=[rightx,righty]
           return self.getTree(left) + self.getTree(middle) + self.getTree(right)
       else:
           self.x=0
           X=sorted(zip(matrix[0],matrix[1]),key=operator.itemgetter(0))
           matrix[0], matrix[1] = zip(*X)
            
           if len(matrix[0])%2==1:
               mid=matrix[0][int(len(matrix[0])/2)]
               
           else:
               mid=(matrix[0][int(len(matrix[0])/2)] + matrix[0][int((len(matrix[0])-1)/2)])/2
           try:
                     
             leftx = [x for x in matrix[0] if x<mid]
             lefty = [matrix[1][matrix[0].index(y)] for y in matrix[0] if y<mid]
             middlex = [x for x in matrix[0] if x==mid]
             middley = [matrix[1][matrix[0].index(y)] for y in matrix[0] if y==mid]
             rightx = [x for x in matrix[0] if x>mid]
             righty = [matrix[1][matrix[0].index(y)] for y in matrix[0] if y>mid]
             left=[leftx,lefty]
             middle=[middlex,middley]
             right=[rightx,righty]
             return self.getTree(left) + self.getTree(middle) + self.getTree(right)
           except RecursionError as e:
              return self.getTree(left) + self.getTree(middle) + self.getTree(right)
           

def main():
    matrix=inputarr()
    kd=kdTree(matrix)
    matrix=kd.getTree(matrix)
    ##matrix = [x for x in matrix if x]
    print (matrix)
    

if __name__ == "__main__":
     main()
