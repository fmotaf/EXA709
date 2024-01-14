import pandas as pd

file = pd.read_excel("Respostas.xlsx")

def avg_age():
    sum = 0
    for age in file["Idade"]:
        sum += age

    avg = sum/len(file["Idade"])
    return avg

def number_of_male_female():
    males = 0
    females = 0

    for person in file["Gênero"]:
        if person == "Masculino":
            males += 1
        else:
            females += 1
    
    print("males =",males, "females =",females)

def do_you_work():
    working = 0
    not_working = 0

    for answer in file["Você trabalha?"]:
        if answer == "Sim":
            working += 1 
        else:
            not_working += 1
    
    print("working = ",working)
    print("not working =",not_working)

def who_do_you_live_with():
    parents = 0
    solo = 0
    friends = 0

    for answer in file["Mora com quem?"]:

        if answer == "Família":
            parents += 1
        elif answer == "Só":
            solo += 1
        else:
            friends += 1

    print("parents = ", parents, "solo = ", solo, "friends = ", friends)

def filter_study_hours():
    real_answers = []
    for answer in file["Tempo de estudo diário horas"]:
        # print(type(answer))
        filtered_answer = str(answer).split("horas")[0]
        real_answers.append(int(filtered_answer))
    return real_answers

def get_avg_study_hours(answers_in_hours:list):
    sum = 0
    
    for answer in answers_in_hours:
        sum += answer
    
    return sum/len(answers_in_hours)

def get_study_hours_frequencies(answers_in_hours:list):
    occurrences = {}
    
    for answer in answers_in_hours:
        occurrences[answer] = occurrences.get(answer, 0) + 1
    
    return occurrences

def get_trend_study_hours(occurrences:dict):
    greater_value = 0
    
    print(occurrences)
    
    for occurrence in occurrences:
        print(occurrences.values())
        if occurrences[occurrence] > greater_value:
            greater_value = occurrence
    
    return greater_value

if __name__ == "__main__":
    number_of_male_female()
    do_you_work()
    who_do_you_live_with()
    answers_filtered = filter_study_hours()
    print(get_avg_study_hours(answers_filtered))
    frequencies = get_study_hours_frequencies(answers_filtered)
    # print("trend counter = ", get_trend_study_hours(answers_filtered))
    stdy_hrs_trend = get_trend_study_hours(frequencies)
    print("A qtd. de horas de estudo que mais aparece eh: ",stdy_hrs_trend )