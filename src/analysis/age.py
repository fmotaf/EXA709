import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.prob as prob
import utils.plot as plot
import statistics


def run():
    result = prob.sum_(dataset.file, ("Idade",))

    print("Mean: ", statistics.mean(dataset.file["Idade"]))
    print("Mode: ", statistics.mode(dataset.file["Idade"]))

    plot.bar(
        title="Idade dos estudantes entrevistados",
        data=result["probability_raw"],
        raw_data=result["raw"],
        legend={
            "Idade -> 18": "18 Anos",
            "Idade -> 19": "19 Anos",
            "Idade -> 20": "20 Anos",
            "Idade -> 21": "21 Anos",
            "Idade -> 22": "22 Anos",
            "Idade -> 23": "23 Anos",
            "Idade -> 24": "24 Anos",
            "Idade -> 25": "25 Anos",
            "Idade -> 26": "26 Anos",
            "Idade -> 27": "27 Anos",
            "Idade -> 28": "28 Anos",
            "Idade -> 29": "29 Anos",
        },
        color_type=plot.COLOR_TYPE_RAINBOW,
    )


if __name__ == "__main__":
    run()
