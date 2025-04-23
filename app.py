from flask import Flask, render_template, json

app = Flask(__name__)

def load_data(name_file):
    with open(f'data/{name_file}', 'r', encoding='utf-8') as f:
        return json.load(f)
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/education')
def education():
    datos = load_data('education.json')
    return render_template('education.html', education=datos)

@app.route('/experience')
def experience():
    datos = load_data('experience.json')
    return render_template('experience.html', experience=datos)

@app.route('/projects')
def projects():
    datos = load_data('projects.json')
    return render_template('projects.html', projects=datos)

@app.route('/about')
def about_me():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)