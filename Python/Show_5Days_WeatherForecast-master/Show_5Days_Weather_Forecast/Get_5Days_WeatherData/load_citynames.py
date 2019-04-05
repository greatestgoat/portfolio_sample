# from . import DB_Manipulate
from .DB_Manipulate import cl_DB_Manipulate

def load_citynames():
    db = cl_DB_Manipulate()
    db .DB_activate('test')
    citynames = db.SELECT_Column('city_data','*')

    return citynames
# citynames = load_citynames()
# CHOICE = []
# for i in range(len(citynames)):
#     CHOICE.append((str(i), str(citynames[i][1])))
# print(CHOICE)