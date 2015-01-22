import gspread
from google.appengine.ext import ndb
from models import *

def add_member(name, stuyId, email):
    config = ndb.Key(Settings, 'config').get()
    if not config:
        config = Settings(id='config')

    gc = gspread.login(config.google_username, config.google_password)
    spread = gc.open_by_key('0AsEXd0jvRpeidDBQU0p2UGtUNmo0aEJ0WFM5UkMzLVE')
    sheet = spread.get_worksheet(0)

    values_list = sheet.col_values(1)
    index = len(values_list) + 1

    new_member = sheet.range("A%d:C%d" % (index, index))
    print new_member
    new_member[0].value = name
    new_member[1].value = stuyId
    new_member[2].value = email
    sheet.update_cells(new_member)