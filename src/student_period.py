import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import dataset


def get_period() -> dict:
    """
    Returna um dicionario contendo as
    respostas para a pergunta Turno (vespertino / noturno)
    """

    column_period = dataset.file["Período"]

    students_verspetine_counter = 0
    students_night_counter = 0

    for occurrence in column_period:
        if occurrence == "Noturno":
            students_night_counter += 1
        else:
            students_verspetine_counter += 1

    return {
        "students_verspetine_counter": students_verspetine_counter,
        "students_night_counter": students_night_counter,
    }


def plot_student_period(dist_vespertine_night: dict):
    """
    Desenha um grafico de pizza mostrando a
    distribuição dos alunos que responderam
    a pergunta turno (vespertino / noturno)
    """
    plt.style.use("_mpl-gallery-nogrid")
    number_vespertine = dist_vespertine_night.get("students_verspetine_counter")
    number_night = dist_vespertine_night.get("students_night_counter")

    print("number_vespertine", number_vespertine)
    print("number_night", number_night)

    data = [number_vespertine, number_night]
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
    men_patch = mpatches.Patch(color="#d0e1f2", label="Vespertino")
    women_patch = mpatches.Patch(color="#2e7ebc", label="Noturno")
    ax.legend(handles=[men_patch, women_patch])
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()


def run():
    student_periods = get_period()
    plot_student_period(student_periods)


if __name__ == "__main__":
    run()
