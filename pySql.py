import sqlite3
# from flask import render_template, flash, redirect, session, url_for, request, g
# from app import app


# con = sqlite3.connect("🍌.db")

# cur = con.cursor()
# cur.execute("CREATE TABLE IF NOT EXISTS Agendamento(ID integer primary key,NOME,HORARIO,AGENDADO,RESERVA)")

# cur = con.cursor()
# cur.execute("""INSERT INTO Agendamento(ID,NOME,HORARIO,AGENDADO,RESERVA) VALUES(1,"Kaique",DATE('now'), 1, DATE('now'))""")

# res = cur.execute("SELECT NOME FROM Agendamento WHERE NOME='Kaique'")
# print(res.fetchall())

# import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d



def buscaAgendamento():
    con = sqlite3.connect("🍌.db")
    # con.row_factory = dict_factory
    
    cursor = con.cursor()
    cursor.execute("""INSERT INTO Agendamento(ID,NOME,HORARIO,AGENDADO,RESERVA) VALUES(1,"Kaique",TIME('now'), 1, DATE('now'))""")
    res = cursor.execute("SELECT * FROM Agendamento")
    # for item in res:
    #     item['ID']
    # print(item)
    return res.fetchall()

