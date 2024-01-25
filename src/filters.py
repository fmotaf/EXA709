import dataset

def study_hours() -> list:
    real_answers = []
    for answer in dataset.file["Tempo de estudo diário horas"]:
        # print(type(answer))
        filtered_answer = str(answer).split("horas")[0]
        real_answers.append(int(filtered_answer))
    return real_answers
