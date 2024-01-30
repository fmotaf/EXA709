def study_hours(file) -> list:
    real_answers = []
    for answer in file["Tempo de estudo diário horas"]:
        filtered_answer = str(answer).split("horas")[0]
        real_answers.append(int(filtered_answer))
    return real_answers

def time_wasted_on_internet(file) -> list:
    real_answers = {}
    for answer in file["Em geral, quanto tempo por dia você permanece conectado à Internet em horas?"]:
        filtered_answer = str(answer).split("horas")[0]
        real_answers.update({int(filtered_answer)})
    return real_answers

def filter_hours(file, column_title:str) -> list:
    real_answers = {}
    for answer in file[column_title]:
        filtered_answer = str(answer).split("horas")[0]
        real_answers[filtered_answer] = 1 if filtered_answer not in real_answers.keys() else real_answers[filtered_answer] + 1 
    return real_answers



def answers(file, column, map_key=None):
    rows = file[column]
    result = {}
    for row in rows:
        if str(row).endswith("horas"):
            row = int(str(row).split("horas")[0])
        key = map_key[row] if map_key != None and row in map_key else row
        result[key] = 1 if key not in result.keys() else result[key] + 1
    return result
