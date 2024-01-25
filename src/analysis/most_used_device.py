import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters


def get_most_used_device():
    return filters.answers(
        dataset.file,
        "Qual o dispositivo que você mais acessa?",
        {
            "Computador/Notebook": "computer_counter",
            "Celular": "smartphone_counter",
            "Tablet": "tablet_counter",
        },
    )


def plot_most_used_device(devices_result: dict):
    """
    Desenha um grafico de pizza mostrando a
    distribuição dos alunos que responderam
    a pergunta turno (vespertino / noturno)
    """
    plt.style.use("_mpl-gallery-nogrid")
    computer = devices_result.get("computer_counter")
    smartphone = devices_result.get("smartphone_counter")
    tablet = devices_result.get("tablet_counter")

    data = [computer, smartphone, tablet]
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
    computer_patch = mpatches.Patch(color="#d0e1f2", label="Vespertino")
    smartphone_patch = mpatches.Patch(color="#2e7ebc", label="Noturno")
    ax.legend(handles=[computer_patch, smartphone_patch])
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()


def run():
    devices_answers = get_most_used_device()
    plot_most_used_device(devices_answers)


if __name__ == "__main__":
    run()
