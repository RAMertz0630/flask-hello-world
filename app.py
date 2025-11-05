from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from rame4494 in 3308!'

@app.route('/db_test')
def db_test():
    # Use the internal URL on Render
    dbURLInt = 'postgresql://rame4494_lab10_db_user:1DyTHdBhetYk8VRr2DrEv2hbVJuqcGxK@dpg-d45s5q7diees738fufdg-a/rame4494_lab10_db'
    con = psycopg2.connect(dbURLInt)
    
    con.close()
    return 'Database connection successful!'

@app.route('/db_create')
def db_create():
    dbURLInt = 'postgresql://rame4494_lab10_db_user:1DyTHdBhetYk8VRr2DrEv2hbVJuqcGxK@dpg-d45s5q7diees738fufdg-a/rame4494_lab10_db'
    con = psycopg2.connect(dbURLInt)
    
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')

    con.commit()
    con.close()
    return 'Basketball table successfully created!'
