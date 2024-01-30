import analysis.most_used_device as most_used_device
import analysis.work as work
import analysis.study as study
import analysis.study_hours as study_hours
import analysis.habitation as habitation
import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot

# PERGUNTAS:
# 1: A maioria dos estudantes que trabalha estuda pela noite?
def question1() -> dict:
    """
    Variavel independente: Se o estudante trabalha (Sim/Não)
    Variavel dependente: Periodo de estudo (Vespertino/Noturno)
    """

    period = dataset.file["Período"]
    work = dataset.file["Você trabalha?"]
    
    total_students = len(work)
    
    # hpt1_true = false
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

    print(
        "qtd. de estudantes que trabalham e estudam DE NOITE/ DE DIA",
        trabalha_e_noturno,
        "/",
        trabalha_e_vespertino,
    )
    print(
        "qtd. de estudantes que NAO trabalham e estudam DE NOITE/ DE DIA",
        nao_trabalha_e_noturno,
        "/",
        nao_trabalha_e_vespertino,
    )

    return {
        "work_stdy_vespertine": trabalha_e_vespertino,
        "work_stdy_night": trabalha_e_noturno,
        # "dont_work_stdy_vespertine": nao_trabalha_e_vespertino,
        # "dont_work_stdy_night": nao_trabalha_e_noturno,
    }


# def plot_hpt_1(data = hpt_1_results: dict):
#     pass


# PERGUNTA 2:
# O NUMERO DE ESTUDANTES QUE USAM INTERNET ATRAVES DE DISPOSITIVOS MOVEIS É MAIOR QUE OS QUE USAM VIA DESKTOP/ PC DE MESA
def question2(dispositivos_mais_usados: dict):
    valor_mais_usado = max(dispositivos_mais_usados, key=dispositivos_mais_usados.get)
    print(valor_mais_usado)
    return valor_mais_usado

    # print("valor_mais_usado")
    # print(valor_mais_usado)
    # print(dispositivos_mais_usados.get(valor_mais_usado))
    # print(dispositivos_mais_usados.values())


if __name__ == "__main__":
    """
    work.do_you_work()
    habitation.who_do_you_live_with()
    answers_filtered = filters.study_hours(dataset.file)
    print(study.get_avg_study_hours(answers_filtered))
    frequencies = study_hours.get_study_hours_frequencies(answers_filtered)
    # print("trend counter = ", get_trend_study_hours(answers_filtered))
    stdy_hrs_trend = study_hours.get_trend_study_hours(frequencies)
    print("A qtd. de horas de estudo que mais aparece eh: ", stdy_hrs_trend)
    print("O dispositivo mais usado eh: ", most_used_device.get_most_used_device())
    confirm_hpt_1()
    dispositivo_mais_usado = most_used_device.get_most_used_device()
    confirm_hpt_2(dispositivo_mais_usado)
    """
    q1 = question1()
    plot.pie(
        title="A maioria dos estudantes que trabalha estuda de noite?", 
        data = q1, 
        legend= {
            "work_stdy_vespertine": "trabalha e estuda de dia", 
            "work_stdy_night": "trabalha e estuda de noite", 
            # "dont_work_stdy_vespertine": "nao trabalha e estuda de dia", 
            # "dont_work_stdy_night": "nao trabalha e estuda de noite"
        }, 
        color_type=plot.COLOR_TYPE_RAINBOW
    )

    q2 = question2()