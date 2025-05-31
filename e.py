# Rectangle Intersection Detection

def rectangles_intersect(r1, r2):
    # Unpack rectangle coordinates
    x1_min, y1_min, x1_max, y1_max = r1
    x2_min, y2_min, x2_max, y2_max = r2

    # If one rectangle is to the left of the other
    if x1_max < x2_min or x2_max < x1_min:
        return False

    # If one rectangle is above the other
    if y1_max < y2_min or y2_max < y1_min:
        return False

    # Otherwise, they overlap
    return True


# Test cases
print(rectangles_intersect((0, 0, 2, 2), (1, 1, 3, 3)))  # True
print(rectangles_intersect((0, 0, 1, 1), (2, 2, 3, 3)))  # False
