from flask import Flask,render_template,request
from core import attendance_calc
app = Flask(__name__, template_folder="public",static_folder="static")


@app.route("/",methods=["POST","GET"])
def home():
    if request.method == "POST":
        print(request.form.get("attended"))
        try:
            
            attended = int(request.form.get("attended"))
            total = int(request.form.get("total"))
            minperc = int(request.form.get("minpercentage"))
            result = attendance_calc(total_periods=total,attended_periods=attended,min_percentage=minperc)
            return render_template("index.html",attend = result)
        except:
            return render_template("index.html",attend=[],context="Invalid Entry")
    else:
        return render_template("index.html",attend=[])

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=80, use_reloader=True, threaded=True,debug=False)
