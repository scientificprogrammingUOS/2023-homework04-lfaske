import numpy as np

# implement the function strange pattern

def strange_pattern(pattern_shape):
    # Create an array in the given shape and with values "False"
    pattern = np.full(shape=pattern_shape, fill_value=False)
    # Iterate through the first dimension of the array and set the values at the correct positions to True
    for idx, i in enumerate(pattern):
        i[(0-idx)%3::3] = True
    
    return pattern



if __name__ == "__main__":
    # use this for your own testing!

    #strange_pattern((6, 8))
    pass
