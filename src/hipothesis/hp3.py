import _fix_import

import statistics as st
import utils.dataset as dataset
import utils.prob as prob
import utils.plot as plot
from natsort import natsorted


if __name__ == "__main__":
    check = []
    for i in range(1, 13, 1):
        for yes_no in ["Não"]:
            check.append((yes_no, str(i)))
    check = tuple(check)

    result = prob.sum_(
        dataset.file,
        ("Você trabalha?", "Tempo de estudo diário horas"),
        check,
    )

    legend = {}
    for key in result["and"].keys():
        hrs = int(key.replace("Não && ", ""))
        legend[key] = "%s hora(s)" % (hrs)

    legend = dict(natsorted(legend.items()))

    plot.bar(
        title="Quantidade de horas de estudo dos estudantes que não trabalham",
        data=result["probability_and"],
        raw_data=result["and"],
        total_data=62,
        legend=legend,
        color_type=plot.COLOR_TYPE_RAINBOW,
    )
