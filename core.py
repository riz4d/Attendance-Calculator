from config import total_lectures_semester,periods_per_day
def attendance_calc(total_periods,attended_periods,min_percentage):
    attend_perc_eqn = (attended_periods / total_periods) * 100
    attend_perc_eqn = round(attend_perc_eqn,2)
    print(f"you've {attend_perc_eqn}% Attendance")
    current_attendance = f"you've {attend_perc_eqn}% Attendance"
    i = 1 
    print(f"you've only {total_lectures_semester-total_periods} lectures or {int((total_lectures_semester-total_periods)/periods_per_day)} days")
    lectures_left = f"you've only {total_lectures_semester-total_periods} lectures or {int((total_lectures_semester-total_periods)/periods_per_day)} days"
    if attend_perc_eqn < min_percentage:
        while True:
            total_periods+=1
            attended_periods+=1
            attend_perc_eqn = (attended_periods / total_periods) * 100
            attend_perc_eqn = round(attend_perc_eqn,2)
            i += 1
            if attend_perc_eqn >= min_percentage:
                print(f"you wanna to attend {i} lectures or {int(i/periods_per_day)} days {total_lectures_semester-total_periods} to reach {attend_perc_eqn}")
                wanna2attend = f"you wanna to attend {i} lectures or {int(i/periods_per_day)} days to reach {attend_perc_eqn}"
                return current_attendance,lectures_left,wanna2attend
            if total_periods >= total_lectures_semester:
                print(f"you can only achieve {attend_perc_eqn}%")
                achieve_only = f"you can only achieve {attend_perc_eqn}%"
                advice = "You are unable to meet the minimum attendance requirement for this semester, so you should consider taking a leave of absence to work and earn money to cover the condonation fees."
                return current_attendance,lectures_left,achieve_only,advice
    if attend_perc_eqn > min_percentage:
        i=0
        while True:
            total_periods+=1
            attend_perc_eqn = (attended_periods / total_periods) * 100
            attend_perc_eqn = round(attend_perc_eqn,2)
            if int(attend_perc_eqn) == min_percentage-1:
                print(total_periods-1,attended_periods)
                break
            i += 1
        print(f"you can bunk {i} lectures or {int(i/periods_per_day)} days")
        bunks = f"you can bunk {i} lectures or {int(i/periods_per_day)} days"
        return current_attendance,lectures_left,bunks
