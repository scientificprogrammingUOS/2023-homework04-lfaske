import numpy as np 

# implement your function to combine two numpy arrays 

def combination(array_a, array_b, axis=0):
    array_a = array_a.squeeze()
    array_b = array_b.squeeze()
    try: 
        combined = np.concatenate((array_a,array_b), axis)
    except:
        raise ValueError("These arrays cannot be combined")
    
    return combined




if __name__ == "__main__":
    #a = np.arange(40).reshape(4,-1)
    #b = np.arange(20).reshape(2,-1)

    #print(combine(a, b))
    pass
