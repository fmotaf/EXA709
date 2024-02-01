import _fix_import

import statistics as st
import utils.dataset as dataset
import utils.prob as prob
import utils.plot as plot
from natsort import natsorted


if __name__ == "__main__":
    check = []
    for yes_no1 in ["Não", "Sim"]:
        for yes_no2 in ["Não", "Sim"]:
            check.append((yes_no2, str(yes_no1)))
    check = tuple(check)

    result = prob.sum_(
        dataset.file,
        (
            "Você usa a internet para jogos online?",
            "Você acredita que a internet atrapalha a sua formação?",
        ),
        check,
    )

    print(result)

    legend = {}
    for key in result["and"].keys():
        key_replaced = key.replace("Não && ", "").replace("Sim && ", "")
        legend[key] = key_replaced

    legend = dict(natsorted(legend.items()))

    plot.bar(
        title="Estudantes que jogam ou não e acreditam que a internet atrapalha ou não a sua formação",
        data=result["probability_and"],
        raw_data=result["and"],
        total_data=62,
        legend={
            "Sim && Não": "Jogam e acreditam que não atrapalha",
            "Sim && Sim": "Jogam e acreditam que atrapalha",
            "Não && Sim": "Não jogam e acreditam que atrapalha",
            "Não && Não": "Não jogam e acreditam que não atrapalha",
        },
        color_type=plot.COLOR_TYPE_RAINBOW,
    )
