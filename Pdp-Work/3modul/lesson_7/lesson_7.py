import time

import bcrypt
# import smtplib
# from email.message import EmailMessage
#
# start = time.time()
#
# # 'ndqtqyzvzkmzpixr'
# email_address = "turgunovjamshid32@gmail.com"
# email_password = "ndqtqyzvzkmzpixr"
#
# # create email
# msg = EmailMessage()
# msg['Subject'] = "Email subject"
# msg['From'] = email_address
# # msg['To'] = "turgunovjamshid32@gmail.com"
# msg['To'] = [
#     "saidakbaruraimov7@gmail.com",
#     "mohirmirahmadov@gmail.com",
#     "zoirbekergashev4567@gmail.com",
#     "khayrullo.devs@gmail.com",
#     "imonqulovf1234@gmail.com",
#     "samidilloravshanov13@gmail.com",
#     "shahrizodaxakimova12@gmail.com",
#     "9140380@gmail.com",
#     "shohjahonobruyev3@gmail.com",
#     "diyorbekdilmurodov1@gmail.com",
#     "suratovdoniyor@gmail.com",
#     "turgunovjamshid32@gmail.com",
#     "dilshodbekakhmatov@gmail.com",
#     "nurillayevezozbek@gmail.com",
#     "azamovshahboz06082001@gmail.com",
#     "zoirbekergashev4567@gmail.com",
#     "isomiddinwtu@gmail.com"
# ]
# msg.set_content("kmga bordi etvorilar")
#
# # send email
# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(email_address, email_password)
#     smtp.send_message(msg)
# end = time.time()
# print(f"{end - start}")







#
# import smtplib
# import time
# from email.message import EmailMessage
#
# start = time.time()
#
# email_address = "turgunovjamshid32@gmail.com"
# email_password = "ndqtqyzvzkmzpixr"
#
# # elektron pochta yaratish
# msg = EmailMessage()
# msg['Subject'] = "Email mavzusi"
# msg['From'] = email_address
# msg['To'] = ["shahrizodaxakimova12@gmail.com"]
# # [
# #     "saidakbaruraimov7@gmail.com",
# #     "mohirmirahmadov@gmail.com",
# #     "zoirbekergashev4567@gmail.com",
# #     "khayrullo.devs@gmail.com",
# #     "imonqulovf1234@gmail.com",
# #     "samidilloravshanov13@gmail.com",
# #     "shahrizodaxakimova12@gmail.com",
# #     "9140380@gmail.com",
# #     "shohjahonobruyev3@gmail.com",
# #     "diyorbekdilmurodov1@gmail.com",
# #     "suratovdoniyor@gmail.com",
# #     "turgunovjamshid32@gmail.com",
# #     "dilshodbekakhmatov@gmail.com",
# #     "nurillayevezozbek@gmail.com",
# #     "azamovshahboz06082001@gmail.com",
# #     "zoirbekergashev4567@gmail.com",
# #     "isomiddinwtu@gmail.com"
# # ]
# msg.set_content("while Truega qobqoyganman 😂")
# while True:
#     # elektron pochta yuborish
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(email_address, email_password)
#         smtp.send_message(msg)
#
#     end = time.time()
#     print(f"{end - start} soniya") # elektron pochtani yuborish uchun sarf etilgan vaqtni chiqaradi

#3.327145576477051 soniya


# import requests
# import sqlite3
#
# # JSON ma'lumotlarni olish
# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# data = response.json()
#
# # SQLite ma'lumotlar bazasini yaratish va bog'lanishni olish
# connection = sqlite3.connect("posts.db")
# cursor = connection.cursor()
#
# # "posts" jadvalini yaratish
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS posts (
#         id INTEGER PRIMARY KEY,
#         userId INTEGER,
#         title TEXT,
#         body TEXT
#     )
# """)
#
# # JSON ma'lumotlarni SQLite jadvalida yozish
# for post in data:
#     cursor.execute("""
#         INSERT INTO posts (id, userId, title, body)
#         VALUES (?, ?, ?, ?)
#     """, (post['id'], post['userId'], post['title'], post['body']))
#
# # Ma'lumotlarni saqlash va bog'lanishni yopish
# connection.commit()
# connection.close()


#
# def count_(a, b):
#     count = 0
#     for i in b:
#         if i == a:
#             count += 1
#     return count
#
# my_string = input(">>>")
# target_char = input(">>>")
# result = count_(target_char, my_string)
# print(f"'{target_char}' belgisi '{my_string}' satrda {result} ta bor.")
#
