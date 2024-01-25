def study_hours(file) -> list:
    real_answers = []
    for answer in file["Tempo de estudo diário horas"]:
        # print(type(answer))
        filtered_answer = str(answer).split("horas")[0]
        real_answers.append(int(filtered_answer))
    return real_answers


def answers(file, column, map_key=None):
    rows = file[column]
    result = {}
    for row in rows:
        key = map_key[row] if map_key != None and row in map_key else row
        result[key] = 1 if key not in result.keys() else result[key] + 1
    return result
