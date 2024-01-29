import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.plot as plot
import utils.filters as filters


def number_of_male_female():
    return filters.answers(
        dataset.file, "Gênero", {"Masculino": "males", "Feminino": "females"}
    )


def run():
    male_female = number_of_male_female()
    plot.pie(
        title="Homes e Mulheres",
        legend={"males": "Homens", "females": "Mulheres"},
        data=male_female,
    )


if __name__ == "__main__":
    run()
