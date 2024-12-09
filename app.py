from flask import Flask, render_template

app = Flask(__name__)

@app.route('/who')
def who_am_i():
    name = "梁棠勛"
    student_id = "B11203135"
    return render_template('index.html', name=name, student_id=student_id)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
