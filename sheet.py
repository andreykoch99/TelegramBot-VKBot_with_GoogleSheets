import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1UNZorZ_QGAVFU3rXtjcHL9i3LOV9Y4dEWBrxk0r0CHA')
worksheet = sh.sheet1

res = worksheet.get_all_records()
# print(res)
print(type(res))