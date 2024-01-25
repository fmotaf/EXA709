import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.plot as plot
import utils.filters as filters


def number_of_male_female():
    return filters.answers(
        dataset.file, "Gênero", {"Masculino": "males", "Feminino": "females"}
    )


def plot_females_males(dist_males_females: dict):
    """
    Desenha um grafico de pizza mostrando a
    distribuição dos alunos que responderam
    entre os gêneros masculino/ feminino
    """

    plt.style.use("_mpl-gallery-nogrid")
    number_males = dist_males_females.get("males")
    number_females = dist_males_females.get("females")

    print("number_Males", number_males)
    print("number_feMales", number_females)

    data = [number_males, number_females]
    colors = plt.get_cmap("Blues")(np.linspace(0.2, 0.7, len(data)))
    sizes = np.array(data)

    def absolute_value(val):
        a = np.round(val / 100.0 * sizes.sum(), 0)
        return a

    # plot
    fig, ax = plt.subplots()
    ax.pie(
        data,
        colors=colors,
        radius=3,
        center=(4, 4),
        wedgeprops={"linewidth": 1, "edgecolor": "white"},
        autopct=absolute_value,
        frame=True,
    )
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))
    men_patch = mpatches.Patch(color="#d0e1f2", label="Homens")
    women_patch = mpatches.Patch(color="#2e7ebc", label="Mulheres")
    ax.legend(handles=[men_patch, women_patch])
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()


def run():
    male_female = number_of_male_female()
    plot.pie(legend={"males": "Homens", "females": "Mulheres"}, data=male_female)


if __name__ == "__main__":
    run()
