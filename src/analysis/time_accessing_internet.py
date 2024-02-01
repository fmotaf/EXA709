import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot
import utils.prob as prob
from natsort import natsorted


def run():
    check = []
    for i in range(1, 13, 1):
        check.append((str(i)))

    check = tuple(check)

    result = prob.sum_(
        dataset.file,
        (
            "Em geral, quanto tempo por dia você permanece conectado à Internet em horas?",
        ),
    )
    
    legend = {}
    for key in result["raw"].keys():
        hrs = int(key.replace("Em geral, quanto tempo por dia você permanece conectado à Internet em horas? -> ", ""))
        legend[key] = "%s hora(s)" % (hrs)
    legend = dict(natsorted(legend.items()))

    plot.bar(
        title="Quanto tempo por dia os estudantes permanecem conectados à Internet",
        data=result["probability_raw"],
        raw_data=result["raw"],
        legend=legend,
        color_type=plot.COLOR_TYPE_RAINBOW,
    )


if __name__ == "__main__":
    run()
