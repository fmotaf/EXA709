import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters


def who_do_you_live_with():
    return filters.answers(
        dataset.file,
        "Mora com quem?",
        {"Família": "parents", "Só": "solo", "Amigos": "friends"},
    )


def plot_habitation(answer_habitation: dict):
    """
    Desenha grafico de pizza contendo as distribuicoes
    de moradia conforme os estudantes da UEFS respondem
    (com os pais/ sozinho/ amigos)
    """

    number_parents = answer_habitation.get("parents")
    number_solo = answer_habitation.get("solo")
    number_friends = answer_habitation.get("friends")

    data = [number_parents, number_solo, number_friends]
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
    parents_patch = mpatches.Patch(color="#d0e1f2", label="Pais")
    solo_patch = mpatches.Patch(color="#7fb9da", label="Sozinho")
    friends_patch = mpatches.Patch(color="#2e7ebc", label="Amigos")
    ax.legend(handles=[parents_patch, solo_patch, friends_patch])
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()


def run():
    habitation = who_do_you_live_with()
    plot_habitation(habitation)


if __name__ == "__main__":
    run()
