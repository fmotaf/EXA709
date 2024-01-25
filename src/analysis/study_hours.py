import _fix_import

import matplotlib.pyplot as plt
import numpy as np
import utils.dataset as dataset
import utils.filters as filters


def get_study_hours_frequencies(answers_in_hours: list):
    occurrences = {}

    for answer in answers_in_hours:
        occurrences[answer] = occurrences.get(answer, 0) + 1
    return occurrences


def get_trend_study_hours(occurrences: dict):
    greater_value = 0

    print(occurrences)

    print(occurrences.values())
    for occurrence in occurrences:
        if occurrences[occurrence] > greater_value:
            greater_value = occurrences[occurrence]
            trend = occurrence
            print("the greater value is", occurrences[occurrence])

    print("o numero de horas de estudo que mais aparece eh = ", trend)
    return trend


def plot_stdy_hours_frequencies(occurrences: dict):
    plt.style.use("_mpl-gallery")
    print("len(occurrences)", len(occurrences))
    x = [str(value) + "hora(s)" for value in occurrences.keys()]
    y = [value for value in occurrences.values()]
    # plot
    fig, ax = plt.subplots()
    ax.bar(x, y, width=0.5, edgecolor="white", linewidth=1, color="tab:blue")
    ax.set_ylabel("quantidade de ocorrências/respostas")
    ax.set_title(
        "distribuição das horas de estudo de acordo com as respostas dos estudantes"
    )
    ax.set(
        xlim=(0, len(occurrences)),
        xticks=[value for value in occurrences.keys()],
        ylim=(0, 20),
        yticks=np.arange(1, 20),
    )
    # ax.legend(title="legenda")
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()


def run():
    stdy_hrs = filters.study_hours(dataset.file)
    stdy_hours_frequencies = get_study_hours_frequencies(stdy_hrs)
    print(stdy_hours_frequencies)
    plot_stdy_hours_frequencies(stdy_hours_frequencies)
    print("trend value in stdy hours:", get_trend_study_hours(stdy_hours_frequencies))


if __name__ == "__main__":
    run()
