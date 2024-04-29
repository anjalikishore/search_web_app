from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    uploaded_file = request.files['file']
    query = request.form['query']
    if uploaded_file.filename != '':
        file_contents = uploaded_file.read().decode('utf-8')
        search_results = search_data(file_contents, query)
        return render_template('index.html', search_results=search_results)
    else:
        return render_template('index.html', error='Please select a file.')

def search_data(file_contents, query):
    results = []
    lines = file_contents.split('\n')
    for i, line in enumerate(lines, start=1):
        if query.lower() in line.lower():
            results.append({'line_number': i, 'content': line.strip().replace('\t', ' ')})
    return results

if __name__ == '__main__':
    app.run(debug=True)
