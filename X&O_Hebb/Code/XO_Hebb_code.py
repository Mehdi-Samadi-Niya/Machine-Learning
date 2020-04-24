from sklearn.model_selection import train_test_split
import numpy as np
import random


def Probability(X_num,O_num,NOD):  

    """ Probability function for choise random index in 5*5 square
    
    Arguments:
        - X_num: X index
        - O_num: Y index
        - NOD: Number of create Data
        
    Output:
        - X_Prob, O_Prob
    """
    
    X_Prob = np.zeros((NOD,10), dtype=bool)
    X_Prob[0] =  True
    for i in range(1,NOD):
        my_randoms = [random.randrange(0, 10, 1) for _ in range(10)]    
        my_randoms = list(dict.fromkeys(my_randoms))    
        for j in range(len(my_randoms)):        
            X_Prob[i][my_randoms[j]]=True

    O_Prob = np.zeros((NOD,12), dtype=bool)
    O_Prob[0] = True 
    for i in range(1,NOD):
        my_randoms = [random.randrange(0, 12, 1) for _ in range(12)]    
        my_randoms = list(dict.fromkeys(my_randoms))
        for j in range(len(my_randoms)):        
            O_Prob[i][my_randoms[j]]=True
    return X_Prob,O_Prob


def Create_Data(X_num,O_num,NOD):

    """ Create_Data function for create dataset
    
    Arguments:
        - X_num: X index
        - O_num: Y index
        - NOD: Number of create Data
        
    Output:
        - X_O_Data, X_O_target
    """

    X_Prob, O_Prob = Probability(X_num,O_num,NOD)
    
    X_O_Data = np.zeros(((2*NOD),25))-1
    X_O_target = np.zeros(((2*NOD),1))
    
    # Create Data
    for i in range (NOD):
        for j in range(9):
            if( X_Prob[i][j] == True):
                X_O_Data[i][X_num[j]]= +1
    for i in range (NOD,(2*NOD)):
        for j in range(12):
            if( O_Prob[i-NOD][j] == True):
                X_O_Data[i][O_num[j]]= +1
    
    # Create lable
    for i in range(NOD):
        X_O_target[i] = +1
    for i in range(NOD,(2*NOD)):
        X_O_target[i] = -1
    
    return X_O_Data,X_O_target


def hebbian(X_train,y_train,W,b):
    
    """ hebbian function for learn by update bias and wight
    
    Arguments:

        - X_train: data for train
        - y_train: target for trian
        - W: wight of hebb
        - b: bias
        
    Output:
        
    """
    dw = np.zeros(25)
    for i in range(X_train.shape[0]):
        for j in range(25):        
            db = y_train[i]
            dw[j] = X_train[i][j] * y_train[i]        
            W[j] += dw[j]
            b[0]  += db
    
def X_O_Show(wrong,X_test):
    
    """ X_O_Show function for show wrong predict
    
    Arguments:

        - wrong: wrong index
        - wrong: data for test
        
    Output:
        
    """
    for k in range(len(wrong)):
        print("No: %i"%(k+1))
        test = np.reshape(X_test[k],(5,5))
        show = np.zeros((5,5),dtype='U')
        for i in range(5):
            for j in range(5):
                if(test[i][j] == True):
                    show[i][j]= "#"
                else:
                    show[i][j] = " "
            
       
        print(show)
        print("\n\n")


def predict(X_test,y_test,W,b):

    """ predict function for Predict 
    
    Arguments:

        - X_test: data for test
        - y_test: target for test
        - W: wight of hebb
        - b: bias
        
    Output:
        - score: Average of predict
        - wrong: wrong prediction index
        
    """
    sum = 0
    wrong = []
    for i in range(X_test.shape[0]):
        
        pre = 0
        for j in range(25):
            pre = X_test[i][j]*W[j]
        pre += b[0]

        if(pre>=0):
            p = 1
        else:
            p = -1
        
        if(p == y_test[i]):
            sum += 1
        else:
            wrong.append(i)    
    score = sum/X_test.shape[0]
    return score,wrong


def main():

    # X and O index in 5*5 Square
    X_num = [0,4,6,8,12,16,18,20,24]
    O_num = [1,2,3,5,9,10,14,15,19,21,22,23]

    # NOD is the number of data for create dataset
    NOD = 100
    W = np.zeros(25)    
    b = [0]
    # for create random X & O data
    X,y = Create_Data(X_num,O_num,NOD)
    
    #  split data to test and train
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size =1/3, 
                                                    random_state = 123,stratify=y)
    
    hebbian(X_train,y_train,W,b)
    
    score, wrong = predict(X_test,y_test,W,b)
    print("Average  Score: %1.3f"%(score))
    print("count of wrong is %i"%len(wrong))
    
    # for show the wrong predict you can use below code 
    # X_O_Show(wrong,X_test)

    
main()

