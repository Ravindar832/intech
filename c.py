# Trapping Rain Water (Discrete + Analog)

import numpy as np
import math

# Discrete height array version
def trap_water_discrete(height):
    if not height:
        return 0
    n = len(height)
    left, right = 0, n - 1
    lmax, rmax = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] > lmax:
                lmax = height[left]
            else:
                water += lmax - height[left]
            left += 1
        else:
            if height[right] > rmax:
                rmax = height[right]
            else:
                water += rmax - height[right]
            right -= 1
    return water

# Analog / Function-based version
def trap_water_function(f, a, b, steps=1000):
    x = np.linspace(a, b, steps)
    y = f(x)
    left_max = np.maximum.accumulate(y)
    right_max = np.maximum.accumulate(y[::-1])[::-1]
    min_height = np.minimum(left_max, right_max)
    water_heights = np.maximum(min_height - y, 0)
    dx = (b - a) / steps
    return np.sum(water_heights * dx)

# Test both methods
if __name__ == "__main__":
    print("Discrete Rainwater Trap")
    height = [2, 1, 3, 0, 1, 2, 3]
    print(f"Input heights: {height}")
    print(f"Water trapped: {trap_water_discrete(height)} units\n")

    print("Analog (Function-Based) Rainwater Trap")
    print("Function: sin(x) from 0 to 2π")
    analog_result = trap_water_function(np.sin, 0, 2 * math.pi)
    print(f"Water trapped (approx): {analog_result:.4f} units")
