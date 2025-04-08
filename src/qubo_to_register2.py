import numpy as np
from utils import clamp, max_outer


def hard_mapping2(
    n_lran : int, n_hran : int, max_dist : float = 50, blockade : float = 13.253644930249399, interaction_coeff : float = 5420158.53, target_weight : float = -1
):
    """ Specific implementation of qubo to register conversion, only works for Sopra Germany's qubo matrices

    Args:
        n_lran : number of LRANs
        n_hran : number of HRANs
        max_dist : Maximum allowed distance between points and (0, 0). Defaults to 50.
        blockade : Blockade radius. Defaults to 13.253644930249399.
        interaction_coeff : C6 in the formula. Defaults to 5420158.53.
        target_weight : Weight between incompatible qubits. Defaults to -1.

    Returns:
        _type_: _description_
    """
    max_dist -= blockade

    # Minimal distance between atoms
    min_dist_between_atoms = 4

    
    # Calculate optimal distance, following the formula:
    # Rij = (C_6 / weight)^(1/6)
    if target_weight > 0:
        inter_dist = clamp(
            (interaction_coeff / target_weight) ** (1 / 6),
            lower=4,
            upper=blockade,
        )
    # Check the number of lran that can be put on the outer circle
    max_lran = max_outer(max_dist, blockade, inter_dist)
    if n_lran > 2 * max_lran - 1:
        print(f"Cannot create more than {2 * max_lran - 1} lran")

    # Setup layers
    layers = []
    while n_lran > 0 and max_dist >= 0:
        layers.append((min(max_lran, n_lran), max_dist))
        max_dist -= 2 * blockade
        n_lran -= max_lran
        max_lran = max_outer(max_dist, blockade, inter_dist)

    # Place qubits on the array
    coords = []
    for n_lran, max_dist in layers:
        for i in range(n_lran):
            angle = i * 2 * np.pi / n_lran
            x = np.cos(angle) * (max_dist - 1)
            y = np.sin(angle) * (max_dist - 1)
            coords.append([x, y])  # for visual purposes only

            #Maximum hran that can be put around the point of coordinate (x,y)  
            max_hran = (2*np.pi*blockade)//min_dist_between_atoms
            if n_hran > max_hran :
                #raise ValueError('Too much hran')
                print('Too much hran')

            for j in range(min(n_hran, max_hran)):
                jangle = angle + j * 2*np.pi / n_hran + np.pi / 2
                xj = x + np.cos(jangle) * inter_dist
                yj = y + np.sin(jangle) * inter_dist
                coords.append([xj, yj])
    return coords
