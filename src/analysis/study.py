import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot


def get_avg_study_hours(answers_in_hours: list) -> float:
    sum = 0
    print(answers_in_hours)

    for answer in answers_in_hours:
        sum += int(answer)

    return sum / len(answers_in_hours)



def run():
    filtered_answers_study_hours = filters.study_hours(dataset.file)
    avg_study_hours = get_avg_study_hours(filtered_answers_study_hours)

    plot.bar(
        title="Numero medio de estudo em horas",
        data={"average": avg_study_hours},
        legend_title="Valor médio do tempo dedicado aos estudos pelos participantes",
        legend={"average": "Média de horas de estudo"},
        color_type=plot.COLOR_TYPE_RAINBOW,
        use_grid=True,
    )


if __name__ == "__main__":
    run()
