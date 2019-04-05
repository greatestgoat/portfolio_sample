import DB_Manipulate

db = DB_Manipulate.cl_DB_Manipulate()
db .DB_activate('test')
city_data = db.SELECT_Column('city_data','*')
print(city_data)