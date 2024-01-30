import _fix_import
import matplotlib.pyplot as plt
import numpy as np
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot


def what_your_family_imcome():
    return filters.answers(
        dataset.file,
        "Renda familiar",
        {
            "Menos de um salário mínimo": "less_than_1",
            "Entre 1 e 2 salários mínimos": "between_1_2",
            "Entre 2 e 3 salários mínimos": "between_2_3",
            "Entre 3 e 4 salários mínimos": "between_3_4",
            "Entre 4 e 5 salários mínimos": "between_4_5",
            "Entre 5 e 6 salários mínimos": "between_5_6",
            "Mais de 6 salários mínimos": "more_then_6",
        },
    )


def run():
    family_income = what_your_family_imcome()

    plot.bar(
        title="Renda familiar",
        legend_title="Distribuição entre a renda familiar dos estudantes",
        data=family_income,
        legend={
            "less_than_1": "Menos de um salário mínimo",
            "between_1_2": "Entre 1 e 2 salários mínimos",
            "between_2_3": "Entre 2 e 3 salários mínimos",
            "between_3_4": "Entre 3 e 4 salários mínimos",
            "between_4_5": "Entre 4 e 5 salários mínimos",
            "between_5_6": "Entre 5 e 6 salários mínimos",
            "more_then_6": "Mais de 6 salários mínimos",
        },
        use_grid=True,
        color_type=plot.COLOR_TYPE_RAINBOW,
    )


if __name__ == "__main__":
    run()
