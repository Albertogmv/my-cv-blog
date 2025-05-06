import os
from flask import Flask, render_template, json, request, make_response

app = Flask(__name__)

# Cargar datos desde un archivo
def load_data(name_file):
    try:
        file_path = os.path.join('data', name_file)
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

# Obtener el nombre del archivo JSON según el idioma
def get_file_for_language(filename, lang):
    return f'{filename}_{lang}.json' if lang in ['es', 'en'] else f'data/{filename}_es.json'

# Función para obtener el idioma de la cookie
def get_lang_from_cookie():
    lang = request.cookies.get('lang', 'es')
    return lang if lang in ['es', 'en'] else 'es'

# Cargar datos del menú según el idioma
@app.context_processor
def inject_menu():
    lang = get_lang_from_cookie()
    menu_file = get_file_for_language("menu", lang)
    menu_labels = load_data(menu_file)
    return dict(menu=menu_labels)

# Función común para cargar datos de una página
def load_page_data(page_name):
    lang = get_lang_from_cookie()
    file = get_file_for_language(page_name, lang)
    return load_data(file), lang

@app.route('/')
def home():
    datos, lang = load_page_data('home')
    return render_template('home.html', home=datos, lang=lang)

@app.route('/education')
def education():
    datos, lang = load_page_data('education')
    return render_template('education.html', education=datos.get('education', []), labels=datos.get('labels', {}), lang=lang)

@app.route('/experience')
def experience():
    datos, lang = load_page_data('experience')
    return render_template('experience.html', experience=datos.get('experience', []), labels=datos.get('labels', {}), lang=lang)

@app.route('/projects')
def projects():
    datos, lang = load_page_data('projects')
    return render_template('projects.html', projects=datos.get('projects', []), labels=datos.get('labels', {}), lang=lang)

@app.route('/about')
def about():
    datos, lang = load_page_data('about')
    return render_template('about.html', about=datos, lang=lang)

# Ruta para cambiar el idioma
@app.route('/set_lang/<lang>')
def set_lang(lang):
    if lang not in ['es', 'en']:
        lang = 'es'  # Si el idioma no es válido, se establece 'es' por defecto
    file = get_file_for_language('home', lang)
    datos = load_data(file)
    resp = make_response(render_template('home.html', home=datos, lang=lang))  # Solo una respuesta básica para cambiar el idioma
    resp.set_cookie('lang', lang)  # Establecemos la cookie con el idioma seleccionado
    return resp

if __name__ == '__main__':
    app.run(debug=True)
