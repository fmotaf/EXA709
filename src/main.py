import analysis.most_used_device as most_used_device
import analysis.student_period as student_period
import analysis.work as work
import analysis.study as study
import analysis.males_females as males_females
import analysis.study_hours as study_hours
import analysis.habitation as habitation

# plt.subplots_adjust(left=0.04, bottom=0.04, right=0.94, top=0.94) ??

if __name__ == "__main__":
    most_used_device.run()
    student_period.run()
    work.run()
    study.run()
    males_females.run()
    study_hours.run()
    habitation.run()
