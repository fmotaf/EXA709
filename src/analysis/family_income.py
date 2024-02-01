import _fix_import
import matplotlib.pyplot as plt
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot
import utils.prob as prob


def run():
    result = prob.sum_(dataset.file, ("Renda familiar",))
    plot.bar(
        title="Renda familiar",
        legend_title="Distribuição entre a renda familiar dos estudantes",
        data=result["probability_raw"],
        raw_data=result["raw"],
        legend={
            "Renda familiar -> Menos de um salário mínimo": "Menos de um salário mínimo",
            "Renda familiar -> Entre 1 e 2 salários mínimos": "Entre 1 e 2 salários mínimos",
            "Renda familiar -> Entre 2 e 3 salários mínimos": "Entre 2 e 3 salários mínimos",
            "Renda familiar -> Entre 3 e 4 salários mínimos": "Entre 3 e 4 salários mínimos",
            "Renda familiar -> Entre 4 e 5 salários mínimos": "Entre 4 e 5 salários mínimos",
            "Renda familiar -> Entre 5 e 6 salários mínimos": "Entre 5 e 6 salários mínimos",
            "Renda familiar -> Mais de 6 salários mínimos": "Mais de 6 salários mínimos",
        },
        color_type=plot.COLOR_TYPE_RAINBOW,
    )


if __name__ == "__main__":
    run()
