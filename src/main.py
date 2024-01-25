import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
file = pd.read_excel("Respostas.xlsx")

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
    """
        Coleta as respostas a pergunta
        Gênero (masculino/ feminino)
    """

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


def plot_females_males(dist_males_females:dict):
    """
        Desenha um grafico de pizza mostrando a 
        distribuição dos alunos que responderam
        entre os gêneros masculino/ feminino
    """
    
    plt.style.use("_mpl-gallery-nogrid")
    number_males = dist_males_females.get("males")
    number_females = dist_males_females.get("females")

    print('number_Males', number_males)
    print('number_feMales', number_females)

    data = [number_males, number_females]
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(data)))
    sizes = np.array(data)
    def absolute_value(val):
        a = np.round(val/100.*sizes.sum(), 0)
        return a
    #plot
    fig, ax = plt.subplots()
    ax.pie(data, colors=colors, radius=3, center=(4,4), wedgeprops={"linewidth": 1, "edgecolor": "white"}, autopct=absolute_value ,frame=True)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    men_patch = mpatches.Patch(color='#d0e1f2', label="Homens")
    women_patch = mpatches.Patch(color='#2e7ebc', label="Mulheres")
    ax.legend(handles=[men_patch, women_patch])
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
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
    """
        Coleta as respostas a pergunta 
        Trabalha? (sim/ não) em um dicionário
    """
    
    working = 0
    not_working = 0

    for answer in file["Você trabalha?"]:
        if answer == "Sim":
            working += 1 
        else:
            not_working += 1
    
    return {
            "working": working, 
            "not_working": not_working
        }

def plot_working_not_working(dist_working_not_working:dict):
    """
        Desenha grafico de barros mostrando a distribuicao dos 
        estudantes da uefs respondendo a pergunta Trabalha? (sim/ não)
    """
    # plt.style.use('_mpl-gallery')
    number_working = dist_working_not_working.get("working")
    number_not_working = dist_working_not_working.get("not_working")
    x = 0.5 + np.arange(2)
    y = [number_working, number_not_working]
    # plot
    fig, ax = plt.subplots()
    bar_labels = ["trabalham", "não trabalham"]
    bar_colors = ["tab:blue", "tab:red"]
    ax.bar(x, y, width=0.5, edgecolor="white", linewidth=1, label=bar_labels, color=bar_colors)
    ax.set_title("distribuição considerando os alunos que trabalham e não trabalham")
    ax.set(xlim=(0, 3), xticks=np.arange(1, 10),
        ylim=(0, 40), yticks=np.arange(1, 40))
    ax.legend(title="distribuicao entre alunos que trabalham/não trabalham")
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
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

    return {
        "parents":parents, 
        "solo": solo, 
        "friends": friends
    }


 
def plot_habitation(answer_habitation:dict):
    """
        Desenha grafico de pizza contendo as distribuicoes 
        de moradia conforme os estudantes da UEFS respondem
        (com os pais/ sozinho/ amigos)
    """

    number_parents = answer_habitation.get("parents")
    number_solo = answer_habitation.get("solo")
    number_friends = answer_habitation.get("friends")

    data = [number_parents, number_solo, number_friends]
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(data)))
    sizes = np.array(data)
    def absolute_value(val):
        a = np.round(val/100.*sizes.sum(), 0)
        return a
    #plot
    fig, ax = plt.subplots()
    ax.pie(data, colors=colors, radius=3, center=(4,4), wedgeprops={"linewidth": 1, "edgecolor": "white"}, autopct=absolute_value ,frame=True)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    parents_patch = mpatches.Patch(color='#d0e1f2', label="Pais")
    solo_patch = mpatches.Patch(color='#7fb9da', label="Sozinho")
    friends_patch = mpatches.Patch(color='#2e7ebc', label="Amigos")
    ax.legend(handles=[parents_patch, solo_patch, friends_patch])
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()


def filter_study_hours() -> list:
    real_answers = []
    for answer in file["Tempo de estudo diário horas"]:
        # print(type(answer))
        filtered_answer = str(answer).split("horas")[0]
        real_answers.append(int(filtered_answer))
    return real_answers

def get_avg_study_hours(answers_in_hours:list) -> float:
    sum = 0
    print(answers_in_hours)

    for answer in answers_in_hours:
        sum += int(answer)
    
    return sum/len(answers_in_hours)

def plot_avg_study_hours(avg_stdy_hours:float):
    plt.style.use('_mpl-gallery')
    x = 0.5 + np.arange(1)
    y = [avg_stdy_hours]
    # plot
    fig, ax = plt.subplots()
    bar_labels = ["Media de horas de estudo"]
    ax.bar(x, y, width=0.5, edgecolor="white", linewidth=1, label=bar_labels, color="tab:blue")
    ax.set_title("Numero medio de estudo em horas")
    ax.set(xlim=(0, 3), xticks=np.arange(1, 5),
        ylim=(0, 10), yticks=np.arange(1, 10))
    ax.legend(title="Valor médio do tempo dedicado aos estudos pelos participantes")
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()

def plot_trend_study_hours():
    pass

def get_study_hours_frequencies(answers_in_hours:list):
    occurrences = {}
    
    for answer in answers_in_hours:
        occurrences[answer] = occurrences.get(answer, 0) + 1
    return occurrences


def get_trend_study_hours(occurrences:dict):
    greater_value = 0
    
    print(occurrences)
    
    print(occurrences.values())
    for occurrence in occurrences:
        if occurrences[occurrence] > greater_value:
            greater_value = occurrences[occurrence]
            trend = occurrence
            print("the greater value is", occurrences[occurrence])
    
    print('o numero de horas de estudo que mais aparece eh = ',trend)
    return trend


def plot_stdy_hours_frequencies(occurrences:dict):
    plt.style.use('_mpl-gallery')
    print('len(occurrences)', len(occurrences))
    x = [str(value)+"hora(s)" for value in occurrences.keys()]
    y = [value for value in occurrences.values()]
    # plot
    fig, ax = plt.subplots()
    ax.bar(x, y, width=0.5, edgecolor="white", linewidth=1, color="tab:blue")
    ax.set_ylabel("quantidade de ocorrências/respostas")
    ax.set_title("distribuição das horas de estudo de acordo com as respostas dos estudantes")
    ax.set(xlim=(0, len(occurrences)), xticks=[value for value in occurrences.keys()],
        ylim=(0, 20), yticks=np.arange(1, 20))
    # ax.legend(title="legenda")
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()
    

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


def plot_most_used_device(devices_result:dict):
    """
        Desenha um grafico de pizza mostrando a 
        distribuição dos alunos que responderam
        a pergunta turno (vespertino / noturno)
    """
    plt.style.use("_mpl-gallery-nogrid")
    computer   = devices_result.get("computer_counter")
    smartphone = devices_result.get("smartphone_counter")
    tablet = devices_result.get("tablet_counter")

    data = [computer, smartphone, tablet]
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(data)))
    sizes = np.array(data)
    def absolute_value(val):
        a = np.round(val/100.*sizes.sum(), 0)
        return a
    #plot
    fig, ax = plt.subplots()
    ax.pie(data, colors=colors, radius=3, center=(4,4), wedgeprops={"linewidth": 1, "edgecolor": "white"}, autopct=absolute_value ,frame=True)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    computer_patch = mpatches.Patch(color='#d0e1f2', label="Vespertino")
    smartphone_patch = mpatches.Patch(color='#2e7ebc', label="Noturno")
    ax.legend(handles=[computer_patch, smartphone_patch])
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()


def get_period() -> dict:
    """
        Returna um dicionario contendo as
        respostas para a pergunta Turno (vespertino / noturno)
    """

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
        "students_night_counter": students_night_counter
    }


def plot_student_period(dist_vespertine_night:dict):
    """
        Desenha um grafico de pizza mostrando a 
        distribuição dos alunos que responderam
        a pergunta turno (vespertino / noturno)
    """
    plt.style.use("_mpl-gallery-nogrid")
    number_vespertine = dist_vespertine_night.get("students_verspetine_counter")
    number_night = dist_vespertine_night.get("students_night_counter")

    print('number_vespertine', number_vespertine)
    print('number_night', number_night)

    data = [number_vespertine, number_night]
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(data)))
    sizes = np.array(data)
    def absolute_value(val):
        a = np.round(val/100.*sizes.sum(), 0)
        return a
    #plot
    fig, ax = plt.subplots()
    ax.pie(data, colors=colors, radius=3, center=(4,4), wedgeprops={"linewidth": 1, "edgecolor": "white"}, autopct=absolute_value ,frame=True)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))
    men_patch = mpatches.Patch(color='#d0e1f2', label="Vespertino")
    women_patch = mpatches.Patch(color='#2e7ebc', label="Noturno")
    ax.legend(handles=[men_patch, women_patch])
    plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94)
    plt.show()


# HIPOTESES:
# 1: A maioria dos estudantes que trabalha estuda pela noite?
def confirm_hpt_1() -> dict:
    period = file["Período"]
    work = file["Você trabalha?"]

    hpt1_true = false
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
    
    return {
        "work_stdy_vespertine": trabalha_e_vespertino,
        "work_stdy_night": trabalha_e_noturno,
        "dont_work_stdy_vespertine": nao_trabalha_e_vespertino,
        "dont_work_stdy_night": nao_trabalha_e_noturno,
    }


def plot_hpt_1(hpt_1_results:dict):
    """
        Variavel independente: Se o estudante trabalha (Sim/Não)
        Variavel dependente: Periodo de estudo (Vespertino/Noturno)
    """
    pass


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


########################################################################################################################
    devices_answers = get_most_used_device()
    plot_most_used_device(devices_answers)

########################################################################################################################
    # cria grafico das resposta a pergunta turno (vespertino/noturno)
    # student_periods = get_period()
    # plot_student_period(student_periods)


########################################################################################################################    
    # cria grafico das respostas a pergunta (quantas horas de estudo?)
    # stdy_hrs = filter_study_hours()
    # stdy_hours_frequencies = get_study_hours_frequencies(stdy_hrs)
    # print(stdy_hours_frequencies)
    # plot_stdy_hours_frequencies(stdy_hours_frequencies)
    # print("trend value in stdy hours:", get_trend_study_hours(stdy_hours_frequencies))


########################################################################################################################
    # cria grafico das respostas a pergunta trabalha? (sim/ nao)    
    # dist_working_not_working = do_you_work()
    # plot_working_not_working(dist_working_not_working)


########################################################################################################################
    # cria grafico da distribuicao do tipo de habitacao (sozinho, familia, amigos)
    # habitation = who_do_you_live_with()
    # plot_habitation(habitation)


########################################################################################################################
    # cria grafico de tempo medio de estudo
    # filtered_answers_study_hours = filter_study_hours()
    # avg_study_hours = get_avg_study_hours(filtered_answers_study_hours)
    # plot_avg_study_hours(avg_study_hours)


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
    # male_female = number_of_male_female()
    # plot_pie(legend=["males","females"], data=male_female)
