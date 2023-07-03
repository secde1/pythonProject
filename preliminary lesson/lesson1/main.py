# file ko'rinishidagi database
# json -> 1_000_000

# import sqlite3
#
# con = sqlite3.connect('test.sqlite')
# cur = con.cursor()
#
# query1 = """
# create table if not exists post(
#     id integer primary key autoincrement,
#     title varchar(255) not null,
#     description text,
#     created_at date default current_date
# );
# -- primary key(not null , unique, created index)
# """
# query2 = """
# create table if not exists comment(
#     id integer primary key autoincrement,
#     post_id integer,
#     message varchar(255) not null,
#     created_at timestamp default current_timestamp
# );
# """
#
# cur.execute(query1)
# cur.execute(query2)
# con.commit()

#
# import sqlite3
#
# con = sqlite3.connect('test2.sqlite')
# cur = con.cursor()
#
# query1 = """
# create table if not exists city(
#     city_id integer primary key autoincrement,
#     city varchar(255) not null,
#     country_id integer,
#     last_update DATETIME NOT NULL
# );
# -- primary key(not null , unique, created index)
# """
# query2 = """
# create table if not exists country(
#     country_id integer primary key autoincrement,
#     country varchar(255),
#     last_update DATETIME NOT NULL,
# );
# """
#
# cur.execute(query1)
# cur.execute(query2)
# con.commit()