import os
from flask import Flask, render_template, json, request

app = Flask(__name__)

def load_data(name_file):
    file_path = os.path.join('data', name_file)
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def get_file_for_language(filename, lang):
    return f'{filename}_{lang}.json' if lang in ['es', 'en'] else f'data/{filename}_es.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/education')
def education():
    lang = request.args.get('lang', 'es')
    if lang not in ['es', 'en']:
        lang = 'es'
    file = get_file_for_language('education', lang)
    datos = load_data(file)
    return render_template('education.html', education=datos, lang=lang)

@app.route('/experience')
def experience():
    lang = request.args.get('lang', 'es')
    if lang not in ['es', 'en']:
        lang = 'es'
    file = get_file_for_language('experience', lang)
    datos = load_data(file)
    return render_template('experience.html', experience=datos, lang=lang)

@app.route('/projects')
def projects():
    lang = request.args.get('lang', 'es')
    if lang not in ['es', 'en']:
        lang = 'es'
    file = get_file_for_language('projects', lang)
    datos = load_data(file)
    return render_template('projects.html', projects=datos, lang=lang)

@app.route('/about')
def about_me():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)