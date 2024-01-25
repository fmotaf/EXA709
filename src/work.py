import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import dataset


def do_you_work():
    """
    Coleta as respostas a pergunta
    Trabalha? (sim/ não) em um dicionário
    """

    working = 0
    not_working = 0

    for answer in dataset.file["Você trabalha?"]:
        if answer == "Sim":
            working += 1
        else:
            not_working += 1

    return {"working": working, "not_working": not_working}


def plot_working_not_working(dist_working_not_working: dict):
    """
    Desenha grafico de barros mostrando a distribuicao dos
    estudantes da uefs respondendo a pergunta Trabalha? (sim/ não)
    """
    # plt.style.use('_mpl-gallery')
    number_working = dist_working_not_working.get("working")
    number_not_working = dist_working_not_working.get("not_working")
    x = 0.5 + np.arange(2)
    y = [number_working, number_not_working]
    # plot
    fig, ax = plt.subplots()
    bar_labels = ["trabalham", "não trabalham"]
    bar_colors = ["tab:blue", "tab:red"]
    ax.bar(
        x,
        y,
        width=0.5,
        edgecolor="white",
        linewidth=1,
        label=bar_labels,
        color=bar_colors,
    )
    ax.set_title("distribuição considerando os alunos que trabalham e não trabalham")
    ax.set(xlim=(0, 3), xticks=np.arange(1, 10), ylim=(0, 40), yticks=np.arange(1, 40))
    ax.legend(title="distribuicao entre alunos que trabalham/não trabalham")
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()


def run():
    dist_working_not_working = do_you_work()
    plot_working_not_working(dist_working_not_working)


if __name__ == "__main__":
    run()
