import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot
import utils.prob as prob


def run():
    result = prob.sum_(dataset.file, ("Mora com quem?",))
    print(result)
    plot.pie(
        title="Mora com quem?",
        legend={
            "Mora com quem? -> Pais": "Pais",
            "Mora com quem? -> Só": "Só",
            "Mora com quem? -> Amigos": "Amigos",
        },
        data=result["probability_raw"],
        raw_data=result["raw"],
        color_type=plot.COLOR_TYPE_RAINBOW,
    )


if __name__ == "__main__":
    run()
