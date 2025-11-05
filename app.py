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

@app.route('/db_insert')
def db_insert():
    dbURLInt = 'postgresql://rame4494_lab10_db_user:1DyTHdBhetYk8VRr2DrEv2hbVJuqcGxK@dpg-d45s5q7diees738fufdg-a/rame4494_lab10_db'
    con = psycopg2.connect(dbURLInt)
    
    cur = con.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')

    con.commit()
    con.close()
    return 'Basketball Table Populated!'

@app.route('/db_select')
def db_select():
    dbURLInt = 'postgresql://rame4494_lab10_db_user:1DyTHdBhetYk8VRr2DrEv2hbVJuqcGxK@dpg-d45s5q7diees738fufdg-a/rame4494_lab10_db'
    con = psycopg2.connect(dbURLInt)
    
    cur = con.cursor()
    cur.execute('SELECT * FROM Basketball;')
    records = cur.fetchall()
    con.close()

    tbl_attr = ''
    tbl_attr += '<table>'
    for row in records:
        tbl_attr += '<tr>'
        for item in row:
            tbl_attr += '<td>{}</td>'.format(item)
        tbl_attr += '</tr>'
    tbl_attr += '</table>'

    return tbl_attr

@app.route('/db_drop')
def db_drop():
    dbURLInt = 'postgresql://rame4494_lab10_db_user:1DyTHdBhetYk8VRr2DrEv2hbVJuqcGxK@dpg-d45s5q7diees738fufdg-a/rame4494_lab10_db'
    con = psycopg2.connect(dbURLInt)
    
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS Basketball;')
    
    con.commit()
    con.close()

    return 'Basketball table successfully dropped!'