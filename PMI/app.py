from flask import Flask, render_template, request, redirect, url_for, session
import pyodbc

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configuración de la base de datos
server = 'SSDD'
database = 'PMI'
username = 'sa'
password = 'DCast24*'
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Ruta de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        Confirmpassword = request.form['Confirmpassword'] 
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM USERS WHERE username=?", username)
            user = cursor.fetchone()
            if user:
                return 'Ya existe ese usuario'
            if password != Confirmpassword:
                return 'Contraseñas no coinciden'
            cursor.execute("INSERT INTO USERS (username, pass) VALUES (?, ?)", username, password)
            conn.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM USERS WHERE username=? AND pass=?", username, password)
            user = cursor.fetchone()
            if user:
                session['username'] = user[0]
                session['password'] = user[1]
                return redirect(url_for('home'))
            else:
                return 'Datos incorrectos'
    return render_template('login.html')

# Ruta de home
@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

# Ruta de logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)