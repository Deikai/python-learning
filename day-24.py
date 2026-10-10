car = {
    "brand": "Jeep",
    "model": "Compass",
    "year": 2025
}

def get_color(car):
    return car.get("color", "Unknown")


def show_keys(data):
    for key in data:
        print(key)

def show_value(data):
    for value in data.values():
        print(value)

def show_items(data):
    for key, value in data.items():
        print(key, value)

def count_key(data):
    keys = 0
    for key in data:
        keys = keys + 1
    return keys

def count_key(data):
    return len(data) # esta hace lo mismo que la de arriba pero la diferencia es el metodo y cuantas lineas se usaron

def  count_string_values(data):
    count = 0
    for value in data.values():
        if isinstance(value, str):
            count = count + 1

    return count

def count_nummeric_values(data):
    count = 0
    for value in data.values():
        if isinstance(value, (int, float)):
            count = count + 1
    return count #este cumple con el requisito pero hay un problema y es que acepta los booleanos

def count_nummeric_values(data):
    count = 0
    for value in data.values():
        if type(value) == int or type(value) == float:
            count = count + 1
    return count # este cumple exactamente con el de arriba pero no acepta los booleanos y con este queda resuelto el problema 

def sum_numeric_value(data):
    sum = 0
    for value in data.values():
        if type(value) == int or type(value) == float:
            sum = sum + value

    return sum # no usar sum como variable porque puede causar error 

def average_numeric_values(data):

    total = 0
    count = 0

    for value in data.values():
        if type(value) == int or type(value) == float:
            total = total  + value
            count = count + 1

        if count == 0:
            return None

    average = total / count
    
    return average 

def keys_with_numeric_values(data):
    new = []
    for key, value in data.items():
        if type(value) == int or type(value) == float:
            new.append(key)
    return new 

def string_values(data):
    new = []
    for key, value in data.items():
        if type(value) == str:
            new.append(value)
    return new

def filter_by_type(data, data_type):
    dic = {}

    for key, value in data.items():
        if type(value) == data_type:
            dic[key] = value

    return dic 

def double_numeric_value(data):
    new_1 = {}
    for key, value in data.items():
        if type(value) == int or type(value) == float:
            new_1[key] = value * 2
        else:
            new_1[key] = value
    return new_1

def rename_key(data, old_key, new_key):
    new = {}

    for key, value in data.items():
        if key == old_key:
            new[new_key] = value
        else:
            new[new_key] = value
    return new

def remove_key(data, target_key):
    new = {}
    for key, value in data.items():
        if key == target_key:
            continue
        else:
            new[key] = value 
    return new

def update_value(data, target_key, new_value):
    new = {}

    for key, value in data.items():
        if key == target_key:
            new[key] = new_value
        else:
            new[key] = value
    return new 

def analyze_data(data):
    new = {}
    count = 0
    numeric = 0
    plus = 0
    for key, value in data.items():

        if type(value) == str:
            count = count + 1

        if type(value) == int or type(value) == float:
            numeric = numeric + 1
            plus = plus + value
      
    new["total_keys"] = len(data)
    new["string_values"] = count
    new["numeric_values"] = numeric
    new["numeric_sum"] = plus
    return new 