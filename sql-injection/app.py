from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Initialize database (for demo)
def init_db():
    conn = sqlite3.connect("test.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS users")
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)")
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    c.execute("INSERT INTO users (username, password) VALUES ('test', 'test123')")
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        # ⚠️ Vulnerable query (SQL injection possible!)
        conn = sqlite3.connect("test.db")
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pwd}'"
        print("Executing:", query)  # Debugging
        c.execute(query)
        result = c.fetchall()
        conn.close()

        if result:
            return "✅ Login successful!"
        else:
            return "❌ Invalid credentials."

    return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
