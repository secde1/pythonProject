import sqlite3


# con = sqlite3.connect("/home/dilshod/PycharmProjects/p14_group/test.sqlite")
con = sqlite3.connect('/home/kali/PycharmProjects/pythonProject/Pdp-Work/3modul/lesson_5/test.sqlite')
cur = con.cursor()

# query = """insert into users(id , fullname , password) values(1 , 'Mahmud' , '1234')"""
query = """insert into library(id, name, auther) values (2, 'Капитанская дочка', 'Александр Пушкин')"""

cur.execute(query)
con.commit()



