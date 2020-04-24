import numpy as np
import matplotlib.pyplot as plt




def compute(j,s,w,b,x,z):

    """ compute function for learn by update bias and wight
    
    Arguments:

        - j: Number of iteration
        - s: Input data
        - W: wight of hebb
        - b: bias
        - x: 2 point to use in drawing(X axis)
        - z: 2 point to use in drawing(Y axis)        
        
    """
    
    x1, x2, y = s[j][0], s[j][1], s[j][2]
    dw1 = x1 * y
    dw2 = x2 * y
    db  =  y
    w[0] += dw1
    w[1] += dw2
    b[0]  += db
    
    plt.subplot(1,4,j+1)
    plt.scatter(-1,-1)
    plt.scatter(-1, 1)
    plt.scatter( 1,-1)
    plt.scatter( 1, 1,)
    for i in range(2):    
        if(w[1]!=0):
            z[i] = (-(w[0]/w[1]) * x[i])-(b[0]/w[1])
        if(w[1]==0):
            z[i] = 0
        
      
    plt.ylim((-2, 2))
    plt.xlim((-2,2))
    plt.plot(x,z)
    plt.title("step %s"%(j+1))
    
    
def AND_hebb():

    """ AND_hebb function 
    
    Arguments:

        - AND: And list
        - s: Input data
        - AND_w: wight of AND
        - AND_b: bias of AND
        - x: 2 point to use in drawing(X axis)
        - z: 2 point to use in drawing(Y axis)        
        
    """

    AND   = [[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,-1]]
    AND_w = [0,0]
    AND_b = [0]
    x = [-2  ,2] 
    for j in range(4):
        z = np.zeros(2)
        compute(j,AND,AND_w,AND_b,x,z) 
    print("wight for AND_hebb is :%s"%AND_w)
    
def OR_hebb():

    """ OR_hebb function 
    
    Arguments:

        - OR: OR list
        - s: Input data
        - OR_w: wight of OR
        - OR_b: bias of OR
        - x: 2 point to use in drawing(X axis)
        - z: 2 point to use in drawing(Y axis)        
        
    """
    OR   = [[1,1,1],[1,-1,1],[-1,1,1],[-1,-1,-1]]
    OR_w = [0,0]
    OR_b = [0]
    x = [-2  ,2] 
    for j in range(4):
        z = np.zeros(2)
        compute(j,OR,OR_w,OR_b,x,z) 

    print("wight for  OR_hebb is :%s"%OR_w)
def main():
    
    
    plt.figure("AND_WITH_HEBB", figsize = (12, 3))    
    AND_hebb()

    plt.figure("OR_WITH_HEBB", figsize = (12, 3))  
    OR_hebb()
    
    plt.show()
    

main()
