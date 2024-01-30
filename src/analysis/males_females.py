import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.plot as plot
import utils.filters as filters
import utils.prob as prob


def run():
    result = prob.sum_(dataset.file, ("Gênero",))
    plot.pie(
        title="Gênero",
        legend={"Gênero -> Masculino": "Homens", "Gênero -> Feminino": "Mulheres"},
        data=result["probability_raw"],
        raw_data=result["raw"],
        color_type=plot.COLOR_TYPE_RAINBOW,
    )


if __name__ == "__main__":
    run()
