from time import time
import time
from flask import Flask, request, render_template
from volleyball import volleyballsnap
from volleyball2 import volleyballsnap2

send_volleyball  = volleyballsnap()
send_volleyball2  = volleyballsnap2()

app=Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    try:
        timee = request.form['text2']
        time2 = str(int(timee)+2)
        id = request.form['idd']
        password = request.form['pas']
        datee = request.form['datee']
        court = request.form['court']
        speed = request.form['speed']
        print("Date:",datee," Court:",court," Time:",timee, "Speed:",speed, "ID:",id," Password:",password)
        result = send_volleyball.apply(datee, court, timee, id, password , speed)
        return render_template('index.html', time = timee, result = result,time2 = time2)
    except Exception as e: 
        result = "你484輸入有錯誤(｀-_ゝ-)"
        #result = e
        return render_template('index.html', time = 999,result = result,time2 = 999)
    #result = "OK"

@app.route('/index2')
def my_form2():
    return render_template('index2.html')

@app.route('/index2', methods=['POST'])
def my_form_post2():
    try:
        timee = request.form['text2']
        time2 = str(int(timee)+2)
        id = request.form['idd']
        password = request.form['pas']
        datee = request.form['datee']
        court = request.form['court']
        print("Date:",datee," Court:",court," Time:",timee," ID:",id," Password:",password)
        result = send_volleyball2.apply2(datee,court,timee, id, password)
        return render_template('index2.html', time = timee, result = result,time2 = time2)
    except Exception as e: 
        result = "你484輸入有錯誤(｀-_ゝ-)"
        #result = e
        return render_template('index2.html', time = 999,result = result,time2 = 999)
    #result = "OK"


if __name__ == '__main__':
    app.run(debug=True)