import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot
import utils.prob as prob


def join_result(result):
    new_result = {}
    for key in result.keys():
        value = result[key]
        if key == "Mora com quem? -> Família" or key == "Mora com quem? -> Pais":
            if new_result.get("Mora com quem? -> Pais") == None:
                new_result["Mora com quem? -> Pais"] = value
            else:
                new_result["Mora com quem? -> Pais"] += value
        elif key == "Mora com quem? -> Só" or key == "Mora com quem? -> Sozinho":
            if new_result.get("Mora com quem? -> Só") == None:
                new_result["Mora com quem? -> Só"] = value
            else:
                new_result["Mora com quem? -> Só"] += value
        else:
            new_result[key] = value
    return new_result


def run():
    result = prob.sum_(dataset.file, ("Mora com quem?",))
    plot.pie(
        title="Mora com quem?",
        legend={
            "Mora com quem? -> Pais": "Pais",
            "Mora com quem? -> Só": "Só",
            "Mora com quem? -> Amigos": "Amigos",
        },
        data=join_result(result["probability_raw"]),
        raw_data=join_result(result["raw"]),
        color_type=plot.COLOR_TYPE_RAINBOW,
    )


if __name__ == "__main__":
    run()
