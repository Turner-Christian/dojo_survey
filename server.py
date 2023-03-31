from flask import Flask,render_template,redirect,session,request
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['lang'] = request.form['lang']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)