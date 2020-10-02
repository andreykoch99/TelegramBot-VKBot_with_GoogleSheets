import gspread
from pprint import pprint

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('TOKEN')
worksheet = sh.sheet1

res = worksheet.get_all_records()
# print(type(res))
pprint(type(res[0]['vk'])) # <class 'str'>
pprint(res[0].items())
n = len(res)
i = 0
our_list  = []
while n != i:
    our_list.append(res[i]['имя'])
    i += 1
pprint(our_list)



# if find_me in res[0]:
#     pprint('Нашёл!')
# else:
#     pprint('Не нашёл!')