import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    if not (type(loc) or type(scale) or type(lower_bound) or type(upper_bound) in [int, float]):
        raise TypeError("All parameters have to be integers or floats")
    if lower_bound >= upper_bound:
        raise ValueError("lower_bound has to be smaller than upper_bound")
    sample = np.random.normal(loc=loc, scale=scale, size=100)
    #sample = np.arange(10)
    mask = (sample <= upper_bound) & (sample >= lower_bound)
    sample = sample[mask]
    stats = (np.mean(sample), np.std(sample))
    return stats


if __name__ == "__main__":
    # use this for your own testing!
    #gaussian_analysis(0, 1, 2, 6)

    pass
