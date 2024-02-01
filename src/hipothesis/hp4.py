import _fix_import

import statistics as st
import utils.dataset as dataset
import utils.prob as prob
import utils.plot as plot
from natsort import natsorted
import statistics


if __name__ == "__main__":
    check = []
    for i in range(1, 13, 1):
        for yes_no in ["Sim"]:
            check.append((yes_no, str(i)))
    check = tuple(check)

    result = prob.sum_(
        dataset.file,
        (
            "Você considera as redes sociais um ambiente tóxico?",
            "Quanto tempo estuda na internet em horas",
        ),
        check,
    )
    
    print(statistics.mean(result["and"].values()))

    legend = {}
    for key in result["and"].keys():
        hrs = key.replace("Não && ", "").replace("Sim && ", "")
        hrs = int(hrs)
        legend[key] = "%s hora(s)" % (hrs)

    legend = dict(natsorted(legend.items()))

    plot.bar(
        title="Horas de estudos dos estudantes que não acham redes sociais um ambiente tóxico",
        data=result["probability_and"],
        raw_data=result["and"],
        total_data=62,
        legend=legend,
        color_type=plot.COLOR_TYPE_RAINBOW,
    )
