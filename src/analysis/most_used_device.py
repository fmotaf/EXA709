import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot
import utils.prob as prob


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
    """devices_answers = get_most_used_device()

    plot.pie(
        title="Dispositivos mais usados",
        legend={
            "computer_counter": "Computador",
            "smartphone_counter": "Celular",
            "tablet_counter": "Tablet",
        },
        data=devices_answers,
        color_type=plot.COLOR_TYPE_RAINBOW,
    )"""

    result = prob.sum_(dataset.file, ("Qual o dispositivo que você mais acessa?",))
    plot.pie(
        title="Dispositivos mais usados",
        legend={
            "Qual o dispositivo que você mais acessa? -> Computador/Notebook": "Computador/Notebook",
            "Qual o dispositivo que você mais acessa? -> Celular": "Celular",
            "Qual o dispositivo que você mais acessa? -> Tablet": "Tablet",
        },
        data=result["probability_raw"],
        raw_data=result["raw"],
        color_type=plot.COLOR_TYPE_RAINBOW,
    )


if __name__ == "__main__":
    run()
