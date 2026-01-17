from flask import Flask, render_template_string, abort
import markdown
import os

app = Flask(__name__)

NOTES_DIR = 'notes'

def get_md_files():
    files = []
    for root, dirs, filenames in os.walk(NOTES_DIR):
        for filename in filenames:
            if filename.endswith('.md'):
                rel_path = os.path.relpath(os.path.join(root, filename), NOTES_DIR)
                files.append(rel_path)
    return sorted(files)

@app.route('/')
def index():
    files = get_md_files()
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Coding Algo Notes</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            ul { list-style-type: none; }
            li { margin: 10px 0; }
            a { text-decoration: none; color: #007bff; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>Coding Algorithm Notes</h1>
        <p>Welcome to my algorithm notes collection.</p>
        <h2>Available Notes:</h2>
        <ul>
        {% for file in files %}
            <li><a href="/view/{{ file }}">{{ file }}</a></li>
        {% endfor %}
        </ul>
    </body>
    </html>
    """
    return render_template_string(template, files=files)

@app.route('/view/<path:filepath>')
def view_file(filepath):
    # Security check: ensure no .. in path
    if '..' in filepath or not filepath.endswith('.md'):
        abort(404)
    
    full_path = os.path.join(NOTES_DIR, filepath)
    if not os.path.isfile(full_path):
        abort(404)
    
    with open(full_path, 'r') as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'tables'])
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>{{ title }}</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            pre { background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }
            code { background: #f4f4f4; padding: 2px 4px; border-radius: 3px; }
            table { border-collapse: collapse; width: 100%; margin: 20px 0; }
            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
            .back-link { margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <div class="back-link"><a href="/">← Back to Index</a></div>
        {{ content|safe }}
    </body>
    </html>
    """
    title = filepath
    return render_template_string(template, content=html_content, title=title)

if __name__ == '__main__':
    app.run(debug=True)