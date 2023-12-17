# До вже реалізованого класу «Годинник» додайте
# мож-ливість стиснення та розпакування даних з
# використан-ням json та pickle.

import json
import pickle
import gzip

class Clock:
    def __init__(self, model, manufacturer, year, price, type) -> None:
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price 
        self.type = type
    
    def __sub__(self, other):
        return self.price - other.price
    
    def __add__(self, other):
        return self.price + other.price
    
    def __lt__(self, other) -> bool:
        return self.price < other.price
    
    def __gt__(self, other) -> bool:
        return self.price > other.price
    
    def __eq__(self, other) -> bool:
        return self.price == other.price
    
    def print_info(self) -> None:
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")
    

def save_data_pickle(lst):
    dict_obj = []
    for el in lst:
        dct_el = obj_to_dict(el)
        dict_obj.append(dct_el)
    with gzip.open("fractions.pkl.gz", 'wb') as wfile:
        pickle.dump(dict_obj, wfile)
        print("data saved")

def load_data_pickle():
    try:
        with gzip.open("fractions.pkl.gz", 'rb') as rfile:
            data = pickle.load(rfile)
    except FileNotFoundError:
        return None
    return data

def save_data_json(lst):
    dict_obj = []
    for el in lst:
        dct_el = obj_to_dict(el)
        dict_obj.append(dct_el)

    with open("fractions.json", 'w') as wfile:
        json.dump(dict_obj, wfile)
        print("data saved")

def load_data_json():
    try:
        with open("fractions.json", 'r') as rfile:
            data = json.load(rfile)
    except FileNotFoundError:
        return None
    return data

def obj_to_dict(obj) -> dict:
    return obj.__dict__


f1 = [Clock('model1', "somebody", 1860, 2000, "type1"),
      Clock('model2', "somebody", 1930, 12000, "type2")]



save_data_json(f1)
data = load_data_json()
print(data)

save_data_pickle(f1)
data_pkl = load_data_pickle()
print(data_pkl)


