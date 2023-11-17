from flask import Flask, render_template

app = Flask(__name__)

app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mitglied-werden')
def mitglied_werden():
    return render_template('mitglied-werden.html')


if __name__ == '__main__':
    app.run(debug=True)
