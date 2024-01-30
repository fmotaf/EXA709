import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot


def get_period() -> dict:
    return filters.answers(
        dataset.file,
        "Período",
        {
            "Noturno": "students_night_counter",
            "Diurno": "students_verspetine_counter",
        },
    )


def run():
    student_periods = get_period()
    plot.pie(
        title="Período",
        legend={
            "students_verspetine_counter": "Vespertino",
            "students_night_counter": "Noturno",
        },
        data=student_periods,
    )


if __name__ == "__main__":
    run()
