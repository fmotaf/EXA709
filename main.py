import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

file = pd.read_excel("Respostas.xlsx")
# CONFIGURACOES DO MATPLOTLIB
plt.style.use("_mpl-gallery-nogrid")

def calculate_avg(column):
    sum = 0
    for row in column:
        sum += row
    avg = sum/len(column)

def avg_age():
    sum = 0
    print(type(file["Idade"]))
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
    
    # print("males =",males, "females =",females)
    return {
        "males": males,
        "females": females
    }


def plot_females_males():
    number_males = number_of_male_female().get("males")
    number_females = number_of_male_female().get("females")

    print('number_Males', number_males)
    print('number_feMales', number_females)

    data = [number_males, number_females]
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(data)))
    #plot
    fig, ax = plt.subplots()
    ax.pie(data, colors=colors, radius=3, center=(4,4), wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    men_patch = mpatches.Patch(color='#d0e1f2', label="Homens = 36")
    women_patch = mpatches.Patch(color='#2e7ebc', label="Mulheres = 27")
    ax.legend(handles=[women_patch, men_patch])
    plt.show()

# def plot_pie(legend:list, data:dict):
#     print(legend[0], legend[1])
#     print(type(legend[0]))
#     data = [data.get(legend[0]), data.get(legend[1])]
#     print(data)
#     colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(data)))
#     fig, ax = plt.subplots()
#     ax.pie(data, colors=colors, radius=3, center=(4,4), wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
#     ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#            ylim=(0, 8), yticks=np.arange(1, 8))
#     men_patch = mpatches.Patch(color='#d0e1f2', label=legend[0])
#     women_patch = mpatches.Patch(color='#2e7ebc', label=legend[1])
#     ax.legend(handles=[women_patch, men_patch])
#     plt.show()


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
    return {
            "working": working, 
            "not_working": not_working
        }

def plot_working_not_working():

    number_working = number_of_male_female().get("males")
    number_not_working = number_of_male_female().get("females")

    print('number_Males', number_males)
    print('number_feMales', number_females)

    data = [number_males, number_females]
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(data)))
    #plot
    fig, ax = plt.subplots()
    ax.pie(data, colors=colors, radius=3, center=(4,4), wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    men_patch = mpatches.Patch(color='#d0e1f2', label="Homens = 36")
    women_patch = mpatches.Patch(color='#2e7ebc', label="Mulheres = 27")
    ax.legend(handles=[women_patch, men_patch])
    plt.show()

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

def get_most_used_device():
    column_device = file["Qual o dispositivo que você mais acessa?"]

    computer_count   = 0
    smartphone_count = 0
    tablet_count     = 0
    
    occurrences = {
        "computer_counter": 0,
        "smartphone_counter": 0,
        "tablet_counter": 0
    }

    for occurrence in column_device:
        if occurrence == "Computador/Notebook":
            occurrences["computer_counter"] += 1
        elif occurrence == "Celular":
            occurrences["smartphone_counter"] += 1
        else:
            occurrences["tablet_counter"] += 1
    
    # greatest_occurrence = max(occurrences["computer_count"], occurrences["smartphone_count"], occurrences["tablet_count"])
    # print(">>>>",max(occurrences.values()))
    # print("aaaah = ",occurrences.keys(max(occurrences.values())))
    print("occurrences")
    print(occurrences)
    return occurrences
    # return occurrences[occurrences[max(occurrences.values())]]

def get_period():
    column_period = file["Período"]
    
    students_verspetine_counter = 0
    students_night_counter = 0

    for occurrence in column_period:
        if occurrence == "Noturno":
            students_night_counter += 1
        else:
            students_verspetine_counter += 1

    return {
        "students_verspetine_counter": students_verspetine_counter, 
        "students_night_counter": students_verspetine_counter
    }


# HIPOTESES:
# 1: A maioria dos estudantes que trabalha estuda pela noite?

def confirm_hpt_1():
    period = file["Período"]
    work = file["Você trabalha?"]

    hpt1_true = 0
    trabalha_e_noturno = 0
    trabalha_e_vespertino = 0

    nao_trabalha_e_noturno = 0
    nao_trabalha_e_vespertino = 0

    for row_work, row_period in zip(work, period):
        if row_work == "Sim": 
            if row_period == "Noturno":
                trabalha_e_noturno += 1
            else:
                trabalha_e_vespertino += 1
        else:
            if row_period == "Noturno":
                nao_trabalha_e_noturno += 1
            else:
                nao_trabalha_e_vespertino += 1
                
    print("qtd. de estudantes que trabalham e estudam DE NOITE/DE DIA", trabalha_e_noturno, "/", trabalha_e_vespertino)
    print("qtd. de estudantes que NAO trabalham e estudam DE NOITE/DE DIA", nao_trabalha_e_noturno, "/", nao_trabalha_e_vespertino)

# HIPOTESE 2:
# O NUMERO DE ESTUDANTES QUE USAM INTERNET ATRAVES DE DISPOSITIVOS MOVEIS EH MAIOR QUE OS QUE USAM VIA DESKTOP/ PC DE MESA

def confirm_hpt_2(dispositivos_mais_usados:dict):

    valor_mais_usado = max(dispositivos_mais_usados, key=dispositivos_mais_usados.get)
    return valor_mais_usado
    
    # print("valor_mais_usado")
    # print(valor_mais_usado)
    # print(dispositivos_mais_usados.get(valor_mais_usado))
    # print(dispositivos_mais_usados.values())

if __name__ == "__main__":
    # avg_age()
    # number_of_male_female()
    # do_you_work()
    # who_do_you_live_with()
    # answers_filtered = filter_study_hours()
    # print(get_avg_study_hours(answers_filtered))
    # frequencies = get_study_hours_frequencies(answers_filtered)
    # # print("trend counter = ", get_trend_study_hours(answers_filtered))
    # stdy_hrs_trend = get_trend_study_hours(frequencies)
    # print("A qtd. de horas de estudo que mais aparece eh: ",stdy_hrs_trend )
    # print("O dispositivo mais usado eh: ", get_most_used_device())
    # confirm_hpt_1()
    # dispositivo_mais_usado = get_most_used_device()
    # confirm_hpt_2(dispositivo_mais_usado)
    # plot_females_males()
    male_female = number_of_male_female()
    plot_pie(legend=["males","females"], data=male_female)