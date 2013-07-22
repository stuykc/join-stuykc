import gspread

def add_member(name, stuyId, email):
    gc = gspread.login('joinstuykc@gmail.com','stuykc123')
    spread = gc.open_by_key('0AsEXd0jvRpeidDBQU0p2UGtUNmo0aEJ0WFM5UkMzLVE')
    sheet = spread.get_worksheet(0)

    values_list = sheet.col_values(1)
    index = len(values_list) + 1
    
    sheet.update_cell(index, 1, name)
    sheet.update_cell(index, 2, stuyId)
    sheet.update_cell(index, 3, email)
