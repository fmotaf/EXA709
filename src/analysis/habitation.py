import _fix_import

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot


def who_do_you_live_with():
    return filters.answers(
        dataset.file,
        "Mora com quem?",
        {
            "Família": "parents",
            "Pais": "parents",
            "Só": "solo",
            "Sozinho": "solo",
            "Amigos": "friends",
        },
    )


def run():
    habitation = who_do_you_live_with()

    plot.pie(
        title="Habitação",
        legend={"parents": "Pais", "solo": "Só", "friends": "Amigos"},
        data=habitation,
    )


if __name__ == "__main__":
    run()
