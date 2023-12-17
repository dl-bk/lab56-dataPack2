# Реалізація програми для додавання, видалення та
# відстеження завдань/заміток. Зберігати ці завдання у
# форматі JSON у файлі. Можливість завантаження
# раніше збережених завдань для подальшої роботи з
# ними.


import json

FILE = "notes.json"
data = {}

def save_data(data, file):
    with open(file, 'w') as wfile:
        json.dump(data, wfile)
    print("data saved")

def load_data(file):
    try:
        with open(file, 'r') as rfile:
            loaded_data = json.load(rfile)
        print("data loaded")
    except FileNotFoundError:
        return None
    return loaded_data

def add_note(key, note):
    data[key] = note


def remove_data(key):
    del data[key]

def show_notes():
    for key, value in data.items():
        print(f"{key}: {value}")

add_note("some title", "do something, please")
show_notes()
save_data(data, FILE)
add_note("moses", "ne zabludis")
save_data(data, FILE)
old_data = load_data(FILE)
print(old_data)
remove_data("some title")
save_data(data, FILE)
old_data = load_data(FILE)
print(old_data)
