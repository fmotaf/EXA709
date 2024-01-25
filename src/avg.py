import dataset

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
    return avg
