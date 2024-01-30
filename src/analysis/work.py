import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot
import utils.prob as prob


def do_you_work():
    return filters.answers(
        dataset.file, "Você trabalha?", {"Não": "not_working", "Sim": "working"}
    )


def run():
    result = prob.sum_(dataset.file, ("Você trabalha?",))
    print(
        "SIM: ",
        (
            dataset.file["Você trabalha?"][dataset.file["Você trabalha?"] == "Sim"]
        ).count(),
    )
    print(
        "Não",
        (
            dataset.file["Você trabalha?"][dataset.file["Você trabalha?"] == "Não"]
        ).count(),
    )
    plot.bar(
        title="Estudantes que trabalham",
        data=result["probability_raw"],
        raw_data=result["raw"],
        legend={
            "Você trabalha? -> Sim": "Sim",
            "Você trabalha? -> Não": "Não",
        },
        color_type=plot.COLOR_TYPE_RAINBOW,
    )


if __name__ == "__main__":
    run()
