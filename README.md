# search_web_app

First, create a folder for search_web_app project and navigate into it. Then, create the following files:
1.	search_web_app.py (for the Flask backend)
2.	index.html (for the HTML structure)
3.	styles.css (for the CSS styling)
Here's the content for each file:
1. search_web_app.py:
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
2. index.html:
Create a folder called templates, in side it create a index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Web Application</title>
    <link rel="stylesheet" href="static/styles.css">
</head>
<body>
    <div class="container">
        <h1>Search Web Application</h1>
        <form action="/search" method="post" enctype="multipart/form-data">
            <input type="file" name="file" accept="">
            <input type="text" name="query" placeholder="Enter search query">
            <button type="submit">Search</button>
        </form>
        <div id="searchResults">
            {% if search_results %}
                <h2>Search Results:</h2>
                <ul>
                    {% for result in search_results %}
                        <li>{{ result }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        </div>
        {% if error %}
            <p class="error">{{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
3. styles.css:
Create a folder in root directory called static, in side it create a styles.css
.container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
}

h1 {
    text-align: center;
}

form {
    margin-bottom: 20px;
	margin: 30px;
	padding-bottom: 20px;
}

input[type="file"], input[type="text"] {
    margin-right: 10px;
	padding-bottom: 20px;
}

button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    cursor: pointer;
	text-align: center;
	margin-top: 5px;
}

button:hover {
    background-color: #0056b3;
}

#searchResults {
    margin-top: 20px;
}
Make sure we have Flask installed (pip install Flask). Then we can run the Flask app by executing python app.py in our terminal. Use this url http://127.0.0.1:5000/ in web browser to see the simple interest calculator in action.
https://github.com/anjalikishore/search_web_app 

