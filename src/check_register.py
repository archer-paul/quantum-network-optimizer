import numpy as np
from scipy.spatial.distance import pdist, squareform
from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt

def _normalize(q):
    if np.sum(q) == 0:
        print("what",q)
    return q / np.sum(q)

class RegisterChecker():
    def __init__(self, qubo, blockade = 13.253644930249399, interaction_coefficient = 5420158.53) -> None:
        self.qubo = qubo - np.diag(np.diag(qubo))
        self.blockade = blockade
        self.C6 = interaction_coefficient

    def map_to_qubo(self, mapping : list):
        return squareform(self.C6 / (pdist(mapping) ** 6))
    
    def evaluate_register(self, mapping : list):
        new_qubo = squareform(self.C6 / (pdist(mapping) ** 6))
        error = np.linalg.norm(_normalize(self.qubo) - _normalize(new_qubo))
        print("Score :", 100 * (1 - error), "%")
        return (1 - error)

    def show_register(self, mapping : list, shape = (12, 12)):    
        zipped = list(zip(*mapping))
        fig = plt.figure(figsize=shape)
        ax = fig.add_subplot()
        plt.rcParams.update({"font.size": 12})

        # Rydberg blockade radius
        for i in range(len(mapping)):
            coord = mapping[i]
            ax.add_patch(
                plt.Circle((coord[0], coord[1]), radius=self.blockade / 2, color="g", alpha=0.12)
            )
            ax.annotate(str(i), (coord[0] + 0.6, coord[1]))

        # Lines between close neighbors
        distances = squareform(pdist(mapping))
        lines = []
        for i in range(len(distances)):
            for j in range(i + 1, len(distances)):
                dist = distances[i][j]
                if dist <= self.blockade:
                    lines.append((mapping[i], mapping[j]))
        plt.gca().add_collection(LineCollection(lines, linewidth=(0.8, 0.8), color="gray"))

        ax.set_aspect("equal", adjustable="box")
        plt.plot(list(zipped[0]), list(zipped[1]), "go")
        plt.axis((-60, 60, -60, 60))
        plt.show()