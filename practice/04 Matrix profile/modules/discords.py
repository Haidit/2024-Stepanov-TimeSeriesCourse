import numpy as np

from modules.utils import *


def top_k_discords(matrix_profile: dict, top_k: int = 3) -> dict:
    """
    Find the top-k discords based on matrix profile

    Parameters
    ---------
    matrix_profile: the matrix profile structure
    top_k: number of discords

    Returns
    --------
    discords: top-k discords (indices, distances to its nearest neighbor and the nearest neighbors indices)
    """
 
    # Extract distances and indices from the matrix profile
    distances = matrix_profile['mp']
    indices = matrix_profile['mpi']
    
    # Create a list of tuples (distance, index, nn_index)
    discord_candidates = [(distances[i], i, indices[i]) for i in range(len(distances))]
    
    # Sort the candidates based on distance in descending order (largest distance first)
    discord_candidates.sort(reverse=True, key=lambda x: x[0])
    
    # Select the top-k discords
    top_k_discords = discord_candidates[:top_k]
    
    # Prepare the output lists
    discords_idx = [item[1] for item in top_k_discords]  # Indices of discords
    discords_dist = [item[0] for item in top_k_discords]  # Distances to nearest neighbor
    discords_nn_idx = [item[2] for item in top_k_discords]  # Indices of nearest neighbors

    return {
        'indices' : discords_idx,
        'distances' : discords_dist,
        'nn_indices' : discords_nn_idx
        }
