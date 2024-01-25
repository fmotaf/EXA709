import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import filters


def get_avg_study_hours(answers_in_hours: list) -> float:
    sum = 0
    print(answers_in_hours)

    for answer in answers_in_hours:
        sum += int(answer)

    return sum / len(answers_in_hours)


def plot_avg_study_hours(avg_stdy_hours: float):
    plt.style.use("_mpl-gallery")
    x = 0.5 + np.arange(1)
    y = [avg_stdy_hours]
    # plot
    fig, ax = plt.subplots()
    bar_labels = ["Media de horas de estudo"]
    ax.bar(
        x,
        y,
        width=0.5,
        edgecolor="white",
        linewidth=1,
        label=bar_labels,
        color="tab:blue",
    )
    ax.set_title("Numero medio de estudo em horas")
    ax.set(xlim=(0, 3), xticks=np.arange(1, 5), ylim=(0, 10), yticks=np.arange(1, 10))
    ax.legend(title="Valor médio do tempo dedicado aos estudos pelos participantes")
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()


def run():
    filtered_answers_study_hours = filters.study_hours()
    avg_study_hours = get_avg_study_hours(filtered_answers_study_hours)
    plot_avg_study_hours(avg_study_hours)


if __name__ == "__main__":
    run()
