from flask import Flask, render_template, request, redirect, url_for, session, flash
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'segredo-ultra-secreto-dos-mcs'

USER_FILE = 'users.json'

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, 'r') as f:
        return json.load(f)
    
def save_users(users):
    with open(USER_FILE, 'w') as f:
        json.dump(users, f)

@app.route('/')
def index():
    if 'username' in session:
        return f'Bem-vindo, {session["username"]}! <a href="/logout">Sair</a>'
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        users = load_users()
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Usuário ou senha inválidos')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    users = load_users()
    if username in users:
        flash('Escolha seu próprio vulgo...')
    else:
        users[username] = password
        save_users(users)
        flash('Cadastro completo! Faça login.')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)