import json

def save_dict_to_json(data):
    try:
        with open('data.json', 'w') as file:
            json.dump(data, file)
        print("Dictionary saved successfully.")
    except Exception as e:
        print(f"Error saving dictionary: {e}")

def load_dict_from_json():
    try:
        with open('data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON.")
    except Exception as e:
        print(f"Error loading dictionary: {e}")

def find_max_age_person(data):
    max_age = -1
    max_age_names = []
    for name, age in data.items():
        if age > max_age:
            max_age = age
            max_age_names = [name]
        elif age == max_age:
            max_age_names.append(name)
    if max_age_names:
        print(f"Person(s) with the maximum age {max_age}: {', '.join(max_age_names)}")
    else:
        print("No data found.")

try:
    user_data = {}
    n = int(input("Enter the number of entries: "))
    for _ in range(n):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        user_data[name] = age

    save_dict_to_json(user_data)
    loaded_data = load_dict_from_json()
    if loaded_data:
        find_max_age_person(loaded_data)
except ValueError:
    print("Invalid input.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
