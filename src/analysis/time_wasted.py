import _fix_import

import utils.dataset as dataset
import utils.filters as filters
import utils.plot as plot

QUESTION = "Em geral, quanto tempo por dia você permanece conectado à Internet em horas?"

def avg_time_spent():
    return filters.answers(dataset.file, QUESTION)

def time_spent():
    return filters.filter_hours(dataset.file, QUESTION, {
        "4": "4 horas",
        "5": "5 horas", 
        "6": "6 horas", 
        "7": "7 horas", 
        "8": "8 horas", 
        "9": "9 horas", 
        "10": "10 horas", 
        "11": "11 horas", 
        "12": "12 horas", 
    }
)

if __name__ == "__main__":
    time_spent_ = dict(sorted(avg_time_spent().items(), key=lambda item: item[0]))
    time_spent_keys = avg_time_spent().keys()
    time_spent_values = avg_time_spent().values()
    print("time spent = ",time_spent_)
    print("time spent keys= ",time_spent_keys)
    print("time spent values= ",time_spent_values)
    plot.bar(
        title=QUESTION,
        data=time_spent_,
        color_type=plot.COLOR_TYPE_RAINBOW,
        legend={
            "4": "4 horas",
            "5": "5 horas", 
            "6": "6 horas", 
            "7": "7 horas", 
            "8": "8 horas", 
            "9": "9 horas", 
            "10": "10 horas", 
            "11": "11 horas", 
            "12": "12 horas", 
        },
        use_grid=True
    )
    # times = {}
    # for row in dataset.file[QUESTION]:
    #     times.update({str(row)+" hora(s)":row})

    # print(times)
    # plot.bar(
    #     title=QUESTION,
    #     data=time_spent,
    #     legend=times,
    #     color_type=plot.COLOR_TYPE_RAINBOW,
    #     use_grid=True,
    # )