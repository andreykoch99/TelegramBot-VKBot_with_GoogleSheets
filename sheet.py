import gspread
from pprint import pprint

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('TOKEN')
worksheet = sh.sheet1

res = worksheet.get_all_records()
# pprint(type(res[0]['vk'])) # <class 'str'>
n = len(res)
i = 0
our_list = []
for i in range(0, n):
    our_list.append(res[i]['имя'])
pprint(our_list)

# find_me = 'Шанц'
#
# if find_me in our_list:
#     pprint('Нашёл!')
# else:
#     pprint('Не нашёл!')