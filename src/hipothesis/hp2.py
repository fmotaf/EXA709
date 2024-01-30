import _fix_import

import statistics as st
import utils.dataset as dataset
import utils.prob as prob
import utils.plot as plot


if __name__ == "__main__":
    check = (
        ("Noturno", "Sim"),
        ("Noturno", "Não"),
        ("Diurno", "Sim"),
        ("Diurno", "Não"),
    )
    result = prob.sum_(dataset.file, ("Período", "Você trabalha?"), check)
    plot.bar(
        title="Estudantes que trabalham/não trabalham e estudam",
        data=result["probability_and"],
        raw_data=result["and"],
        legend={
            "Noturno && Sim": "Noturno e Trabalha",
            "Noturno && Não": "Noturno e Não trabalha",
            "Diurno && Sim": "Diurno e Trabalha",
            "Diurno && Não": "Diurno e Não trabalha",
        },
        color_type=plot.COLOR_TYPE_RAINBOW,
    )
