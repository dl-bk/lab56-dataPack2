# До вже реалізованого класу «Дріб» додайте можливість стиснення та розпакування даних з
# використанням json та pickle.

import json
import pickle
import gzip


class Fraction:

    _instance_count = 0

    def __init__(self, numerator, denominator) -> None:
        self.numerator = numerator
        self.denominator = denominator
        Fraction._instance_count += 1

    @staticmethod
    def get_instance_count():
        return Fraction._instance_count

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, other):
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        other.denominator, other.numerator = other.numerator, other.denominator
        return Fraction.__mul__(self, other)


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


f1 = [Fraction(5, 4),
      Fraction(10, 11),
      Fraction(12, 14)]



save_data_json(f1)
data = load_data_json()
print(data)

save_data_pickle(f1)
data_pkl = load_data_pickle()
print(data_pkl)