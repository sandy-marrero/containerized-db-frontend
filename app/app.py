from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import requests
import random
app = Flask(__name__)
DB_HOST = "db"
DB_PORT = "5432"
DB_NAME = "postgres"
DB_USER = "your-db-username"
DB_PASSWORD = "your-db-password"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_element = request.form.get("element", "default_value")
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        cur = conn.cursor()
        cur.execute("INSERT INTO my_table (column_name) VALUES (%s);", (new_element,))
        conn.commit()
        conn.close()
        return redirect(url_for("index"))

    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )
    cur = conn.cursor()
    cur.execute("SELECT column_name FROM my_table;")
    items = cur.fetchall()
    conn.close()

    return render_template("index.html", items=items)

@app.route("/adddata",methods=["GET"])
def add():
    newdata = requests.get("192.68.1.22:5000/get").content
    conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
    cur = conn.cursor()
    cur.execute("INSERT INTO my_table (column_name) VALUES (%s);", (newdata,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))

@app.route("/get",methods=["GET"])
def get():
    return "newdata" + str(random.randint(0,100))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
