from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database setup
def get_db_connection():
    conn = sqlite3.connect('base.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['POST'])
def create_post():
    title = request.form['title']
    content = request.form['content']
    
    conn = get_db_connection()
    conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    conn = get_db_connection()
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn.execute('UPDATE posts SET title = ?, content = ? WHERE id = ?', (title, content, post_id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    post = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    
    return render_template('edit.html', post=post)

@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (post_id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Create the database and table if they don't exist
    with get_db_connection() as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)')
    
    app.run(debug=True)