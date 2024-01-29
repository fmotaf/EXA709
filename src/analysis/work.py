import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot


def do_you_work():
    return filters.answers(
        dataset.file, "Você trabalha?", {"Não": "not_working", "Sim": "working"}
    )


def run():
    dist_working_not_working = do_you_work()

    plot.bar(
        title="Distribuição considerando os alunos que trabalham e não trabalham",
        legend={
            "working": "Trabalham",
            "not_working": "Não trabalham",
        },
        data=dist_working_not_working,
        legend_title="Distribuicao entre alunos que trabalham/não trabalham",
        color_type=plot.COLOR_TYPE_RAINBOW,
    )


if __name__ == "__main__":
    run()
