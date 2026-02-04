from flask import Flask , render_template

app = Flask('Questions for my future WIFEYYYYYY')

@app.route("/questions_aaapke_liye")
def service():
    name='Vibhooti'
    return render_template('qna_for_parul.html',username=name)


app.run(debug=True)