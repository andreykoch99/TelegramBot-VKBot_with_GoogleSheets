import gspread
from pprint import pprint

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('TOKEN')
worksheet = sh.sheet1

res = worksheet.get_all_records()
# pprint(type(res[0]['vk'])) # <class 'str'>
n = len(res)
i = 0
find_me = 'Ш'
ans = []
for i in range(0, n):
    if res[i]['имя'].find(find_me) != -1:
        ans.append(i)
        # print('Нашёл, это {}, её номер телефона: {}'.format(res[i]['имя'], res[i]['телефон']))
pprint(ans)