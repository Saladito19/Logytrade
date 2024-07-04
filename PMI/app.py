from flask import Flask, render_template, request, redirect, url_for, session
import pyodbc

app = Flask(__name__)
app.secret_key = '1980'

# Configuración de la base de datos
server = 'SSDD'
database = 'PMI'
username = 'sa'
password = 'DCast24*'
driver = '{ODBC Driver 17 for SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# region ACCESO Y REGISTRO
# Ruta de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password'] 
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ACCESO WHERE email=?", email)
            user = cursor.fetchone()
            if user:
                return 'Ya existe ese usuario'
            if password != confirm_password:
                return 'Contraseñas no coinciden'
            cursor.execute("EXEC AgregarAcceso @Correo = ?, @Contraseña = ?;", email, password)
            conn.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# Ruta de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        with pyodbc.connect(connection_string) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ACCESO WHERE email=? AND pass=?", email, password)
            user = cursor.fetchone()
            if user:
                session['email'] = user[1]
                session['password'] = user[2]
                return redirect(url_for('index'))
            else:
                return 'Datos incorrectos'
    return render_template('login.html')
# endregion

# region INDEX RUTAS
# Ruta de inicio
@app.route('/home')
def index():
    return render_template('index.html')

# Ruta de logout
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

#Ruta de inventario plantilla
@app.route('/inventario')
def inventario():
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Inventario")
        inventario = cursor.fetchall()
    return render_template('inventario.html', inventario=inventario)
#endregion

if __name__ == '__main__':
    app.run(debug=True)