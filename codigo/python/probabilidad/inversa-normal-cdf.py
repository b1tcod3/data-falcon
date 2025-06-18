import math
import matplotlib.pyplot as plt

# Constants
SQRT_TWO_PI = math.sqrt(2 * math.pi)

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p: float,
                       mu: float = 0,
                       sigma: float = 1,
                       tolerance: float = 0.00001) -> float:
    """Find approximate inverse using binary search"""

    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z = -10.0                      # normal_cdf(-10) is (very close to) 0
    hi_z  =  10.0                      # normal_cdf(10)  is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2     # Consider the midpoint
        mid_p = normal_cdf(mid_z)      # and the cdf's value there
        if mid_p < p:
            low_z = mid_z              # Midpoint too low, search above it
        else:
            hi_z = mid_z               # Midpoint too high, search below it

    return mid_z

# Example usage
if __name__ == "__main__":
    # Plotting the inverse normal CDF
    xs = [x / 100.0 for x in range(0, 101)]
    ys = [inverse_normal_cdf(x) for x in xs]

    plt.plot(xs, ys, label='Inverse Normal CDF')
    plt.title("Inverse Normal CDF")
    plt.xlabel("Probability")
    plt.ylabel("Z-value")
    plt.legend()
    plt.grid()
    plt.show()