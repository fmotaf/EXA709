import _fix_import

import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot

QUESTION = "Há quanto tempo utliliza computador em anos"

def get_answers():
    return filters.answers(dataset.file, QUESTION)


if __name__ == "__main__":
    time_in_years = get_answers()
    print(time_in_years)