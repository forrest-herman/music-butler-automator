# python utilities
import json


def save_json_to_file(data, file_name='data.json'):
    with open(file_name, 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def write_to_file(data, file_name='data.txt'):
    with open(file_name, 'w', encoding='utf8') as f:
        f.write(data)


def read_from_file(file_name='data.txt'):
    with open(file_name, 'a+') as f:
        f.seek(0)
        return f.read()


def get_12hr_time_format_for_os(os_name):
    if os_name == 'Windows_NT':
        return "%#I:%M %p"
    else:
        return "%-I:%M %p"
