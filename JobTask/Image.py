import numpy as np
import pandas as pd
from random import randint



#reating a method to obtain a dataframe
def get_df():
    #setting up an array of the required length
    a =  np.ones(1000)
    
    #Creating a loop to assign appropriate values at each index
    for i in range(len(a)):
            #assigning a random variable at index "i"
            a[i] = a[i]*randint(0,100)
    
    #creating a second array to take the modulo 10 at each index of "a"
    b = np.ones(1000)
    b = a%10
    
    #Setting up the dataframe as required
    df = pd.DataFrame(
        {
             "a":a,
             "b":b
         }    
         )
    
    #returning the Dataframe in JSON format
    return df.to_json(orient='split')
