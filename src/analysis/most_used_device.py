import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot


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


def run():
    devices_answers = get_most_used_device()

    plot.pie(
        title="Dispositivos mais usados",
        legend={
            "computer_counter": "Computador",
            "smartphone_counter": "Celular",
            "tablet_counter": "Tablet",
        },
        data=devices_answers,
    )


if __name__ == "__main__":
    run()
