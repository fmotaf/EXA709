import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot
import utils.prob as prob


def run():
    result = prob.sum_(dataset.file, ("Você costuma acessar a internet?",))
    plot.pie(
        title="Estudantes que acessam internet",
        data=result["probability_raw"],
        raw_data=result["raw"],
        legend={
            "Você costuma acessar a internet? -> Sim": "Sim",
            "Você costuma acessar a internet? -> Não": "Não",
        },
        color_type=plot.COLOR_TYPE_RAINBOW,
    )


if __name__ == "__main__":
    run()
