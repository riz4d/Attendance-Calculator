from flask import Flask,render_template,request

app = Flask(__name__, template_folder="public",static_folder="static")

def attendance_calc(total_periods,attended_periods,min_percentage):
    attend_perc_eqn = (attended_periods / total_periods) * 100
    attend_perc_eqn = round(attend_perc_eqn,2)
    print(f"you've {attend_perc_eqn}% Attendance")
    current_attendance = f"you've {attend_perc_eqn}% Attendance"
    i = 1 
    print(f"you've only {532-total_periods} lectures or {int((532-total_periods)/8)} days")
    lectures_left = f"you've only {532-total_periods} lectures or {int((532-total_periods)/8)} days"
    if attend_perc_eqn < min_percentage:
        while True:
            total_periods+=1
            attended_periods+=1
            attend_perc_eqn = (attended_periods / total_periods) * 100
            attend_perc_eqn = round(attend_perc_eqn,2)
            i += 1
            if attend_perc_eqn >= min_percentage:
                print(f"you wanna to attend {i} lectures or {int(i/8)} days {532-total_periods} to reach {attend_perc_eqn}")
                wanna2attend = f"you wanna to attend {i} lectures or {int(i/8)} days to reach {attend_perc_eqn}"
                return current_attendance,lectures_left,wanna2attend
                break
            if total_periods >= 532:
                print(f"you can only achieve {attend_perc_eqn}%")
                achieve_only = f"you can only achieve {attend_perc_eqn}%"
                print("you can't reach the minimum attendance in this sem so take leave and make condensation fees")
                advice = "You are unable to meet the minimum attendance requirement for this semester, so you should consider taking a leave of absence to work and earn money to cover the condonation fees."
                return current_attendance,lectures_left,achieve_only,advice
                break
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
        print(f"you can bunk {i} lectures or {int(i/8)} days")
        bunks = f"you can bunk {i} lectures or {int(i/8)} days"
        return current_attendance,lectures_left,bunks

@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        print(request.form.get("attended"))
        attended = int(request.form.get("attended"))
        total = int(request.form.get("total"))
        minperc = int(request.form.get("minpercentage"))
        result = attendance_calc(total_periods=total,attended_periods=attended,min_percentage=minperc)
        return render_template("index.html",attend = result)
    else:
        return render_template("index.html",attend=[])

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=80, use_reloader=True, threaded=True,debug=False)
