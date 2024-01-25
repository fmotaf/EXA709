import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def pie(legend: list, data: dict):
    print(legend[0], legend[1])
    print(type(legend[0]))
    data = [data.get(legend[0]), data.get(legend[1])]
    print(data)
    colors = plt.get_cmap("Blues")(np.linspace(0.2, 0.7, len(data)))
    fig, ax = plt.subplots()
    ax.pie(
        data,
        colors=colors,
        radius=3,
        center=(4, 4),
        wedgeprops={"linewidth": 1, "edgecolor": "white"},
        frame=True,
    )
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
    men_patch = mpatches.Patch(color="#d0e1f2", label=legend[0])
    women_patch = mpatches.Patch(color="#2e7ebc", label=legend[1])
    ax.legend(handles=[women_patch, men_patch])
    plt.show()
