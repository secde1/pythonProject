# import pandas as pd
#
# # txt = pd.read_csv('example.csv')
# #
# # print(type(txt.values[3]))
#
# data = {
#     'name' : ['Amirkhon', 'Doniyor', 'Jamshid', 'Zoirbek'],
#     'age' : [23, 17, 20, 17],
#     'addres' : ['Samarqand', 'Andijon', 'Toshkent', 'Bekabod' ]
# }
# dt = pd.DataFrame(data)
# # print(dt['name'])
#
# dt.to_csv('example.csv', index=False)


# import csv
#
# f = open('example.csv', 'r')
# f2 = open('example2.csv', 'w')
# reader = csv.reader(f)
# writer = csv.writer(f2)
# for row in reader:
#
#     if row[1].isdigit() and int(row[1]) >= 20:
#         writer.writerow(row)
#         print(row)
# #
# import pandas as pd
# #
# xlsx = pd.read_excel('P14 Python Time table 2(12_06_2023).xlsx')
# f = open('output.txt', 'w')
# f.write(xlsx.to_string(index=False))
# import pandas as pd
#
# xlsx = pd.read_excel('P14 Python Time table 2(12_06_2023).xlsx')
# first_row = xlsx.iloc[0]  # Birinchi qatorni o'qish
#
# f = open('output.txt', 'w')
# f.write('\t'.join(map(str, first_row.values)))



