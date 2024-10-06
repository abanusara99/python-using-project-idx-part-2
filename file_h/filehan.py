from flask import Flask, request, jsonify, render_template_string
import os
from datetime import datetime

app = Flask(__name__)

# Directory to store the text files
DATA_DIR = 'data_files'

# Ensure the data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

@app.route('/')
def index():
    """Render the main page with forms."""
    return render_template_string('''
        <h1>File Handling with Flask</h1>
        
        <h2>Create New File</h2>
        <form action="/create" method="post">
            <input type="text" name="filename" placeholder="Enter filename" required>
            <br>
            <br>
            <textarea name="data" placeholder="Enter data to write" required></textarea>
            <br>
            <br>
            <button type="submit">Create File</button>
        </form>

        <h2>Remove File</h2>
        <form action="/remove" method="post">
            <input type="text" name="filename" placeholder="Enter filename to remove" required>
            <br>
            <br>
            <button type="submit">Remove File</button>
        </form>

        <h2>List Files</h2>
        <form action="/list" method="get">
            <button type="submit">List Files</button>
        </form>
    ''')

@app.route('/create', methods=['POST'])
def create_file():
    """Create a new file with user-defined name and data."""
    filename = request.form.get('filename')
    data = request.form.get('data')

    if not filename or not data:
        return jsonify({"error": "Filename and data are required."}), 400

    file_path = os.path.join(DATA_DIR, f"{filename}.txt")

    # Write data to the file
    with open(file_path, 'w') as file:
        file.write(data)

    return jsonify({"message": f"File '{filename}.txt' created successfully."}), 201

@app.route('/remove', methods=['POST'])
def remove_file():
    """Remove a specific file."""
    filename = request.form.get('filename')
    
    if not filename:
        return jsonify({"error": "Filename is required."}), 400

    file_path = os.path.join(DATA_DIR, f"{filename}.txt")

    try:
        os.remove(file_path)
        return jsonify({"message": f"File '{filename}.txt' removed successfully."}), 200
    except FileNotFoundError:
        return jsonify({"error": "File not found."}), 404

@app.route('/list', methods=['GET'])
def list_files():
    """List all files with their creation dates and contents."""
    files_info = []
    
    for filename in os.listdir(DATA_DIR):
        if filename.endswith('.txt'):
            file_path = os.path.join(DATA_DIR, filename)
            creation_time = os.path.getctime(file_path)
            creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
            
            with open(file_path, 'r') as file:
                contents = file.read()

            files_info.append({
                "name": filename,
                "creation_date": creation_date,
                "contents": contents
            })

    return render_template_string('''
        <h1>Files List</h1>
        <table border="1">
            <tr>
                <th>Filename</th>
                <th>Creation Date</th>
                <th>Contents</th>
            </tr>
            {% for file in files_info %}
            <tr>
                <td>{{ file.name }}</td>
                <td>{{ file.creation_date }}</td>
                <td>{{ file.contents }}</td>
            </tr>
            {% endfor %}
        </table>
        <a href="/">Go Back</a>
    ''', files_info=files_info)

if __name__ == '__main__':
    app.run(debug=True)