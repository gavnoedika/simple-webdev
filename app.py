from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/html')
def html_info():
    return render_template('html.html')

@app.route('/css')
def css_info():
    return render_template('css.html')

@app.route('/javascript')
def javascript_info():
    return render_template('javascript.html')

@app.route('/python')
def python_info():
    return render_template('python.html')

if __name__ == '__main__':
    app.run(debug=True)
