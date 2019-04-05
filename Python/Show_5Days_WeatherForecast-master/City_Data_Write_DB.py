import City_ID_Name_definition, DB_Manipulate
import numpy as np

test = City_ID_Name_definition.cl_City_ID_Name_definition()
[city_id, city_name, country_name] = test.City_ID_Name_sel()

city_data = list(zip(city_id,city_name,country_name))
# print(city_data)
db_test = DB_Manipulate.cl_DB_Manipulate()
db_test.DB_activate('test')
db_test.CREATETABLE_City_ID_Name('city_data')
db_test.INSERT_City_ID_Name(city_data)