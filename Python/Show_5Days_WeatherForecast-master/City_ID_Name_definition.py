import json

class cl_City_ID_Name_definition:
    #Properties

    #constructor
    def __init__(self):
        f = open('city.list.json','r', encoding='utf-8')
        self.jsonData = json.load(f)
        f.close()
    #method
    def City_ID_Name_sel(self):
        city_id = []
        city_name = []
        country_name = []
        for item in range(len(self.jsonData)):
            city_id.append(self.jsonData[item]["id"])
            city_name.append(self.jsonData[item]["name"].replace('-','_'))
            country_name.append(self.jsonData[item]["country"])

        return city_id, city_name, country_name