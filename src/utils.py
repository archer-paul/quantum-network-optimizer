from math import pi

def max_outer(circle_radius : float, blockade : float, inter_dist : float = 4) -> int:
    """ Calculates the maximum number of atoms that can be placed on a circle of radius circle_radius, considering the blockade radius and the minimal distance between atoms

    Args:
        circle_radius (float): Radius of the circle atoms will be placed upon
        blockade (float): Interaction radius of each atom
        inter_dist (float): Minimum distance between atoms

    Returns:
        int: number of atoms that can be placed on the circle
    """
    return int(2 * pi * circle_radius // (blockade + inter_dist))

def clamp(n : float, lower : float, upper : float) -> float:
    """Gets the value closest to n between lower and upper"""
    if n < lower:
        return lower
    if n > upper:
        return upper
    return n
