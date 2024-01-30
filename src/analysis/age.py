import _fix_import

import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot

def calculate_avg(column):
    sum = 0
    for row in column:
        sum += row
    avg = sum / len(column)
    return avg


def avg_age():
    sum = 0
    print(type(dataset.file["Idade"]))
    for age in dataset.file["Idade"]:
        sum += age

    avg = sum / len(dataset.file["Idade"])
    print (avg)
    return avg


def get_age_students():
    return filters.answers(
        dataset.file, 
        "Idade",
        {
            "18":"18 anos",
            "19":"19 anos",
            "20":"20 anos",
            "21":"21 anos",
            "22":"22 anos",
            "23":"23 anos",
            "24":"24 anos",
            "25":"25 anos",
            "26":"26 anos",
            "27":"27 anos",
            "28":"28 anos",
            "29":"29 anos",
        }
    )

def run():
    ages = get_age_students()
    plot.bar(
        title="Idade dos estudantes entrevistados",
        data = ages,
        use_grid=True,
        legend={
            "18":"18 anos",
            "19":"19 anos",
            "20":"20 anos",
            "21":"21 anos",
            "22":"22 anos",
            "23":"23 anos",
            "24":"24 anos",
            "25":"25 anos",
            "26":"26 anos",
            "27":"27 anos",
            "28":"28 anos",
            "29":"29 anos",
        },
    )

if __name__ == "__main__":
    ages = set()
    for row in dataset.file["Idade"]:
        ages.add(row)
    avg_age()
    print(ages)
    run()
