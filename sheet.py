import gspread
from pprint import pprint

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1UNZorZ_QGAVFU3rXtjcHL9i3LOV9Y4dEWBrxk0r0CHA')
worksheet = sh.sheet1

res = worksheet.get_all_records()
print(type(res))
# pprint(res)
pprint(type(res[0]['vk']))
# pprint(res[0].items())
# pprint(dict(res))
# pprint(res[0])
find_me = 'maldenser@yandex.ru'
# if find_me in res:
#     pprint('Нашёл!')
# else:
#     pprint('Не нашёл!')

# pprint(res)
# pprint(type(res))
# pprint(worksheet.findall('maldenser@yandex'))
#
# def find_element(tree, element_name):
#     if element_name in tree:
#         return tree[element_name]
#     for key, sub_tree in tree.items():
#         if isinstance(sub_tree, dict):
#             result = find_element(tree=sub_tree, element_name=element_name)
#             if result:
#                 break
#     else:
#         result = None
#     return result