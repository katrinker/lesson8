from csv import DictReader, DictWriter
from os.path import exists


def get_info():
    first_name = 'Ivan'
    last_name = 'Ivanov'
    is_valid_number = False
    while not is_valid_number:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 3:
                print("Невалидная длина")
        except ValueError:
            print("Невалидный номер")
            continue
        else:
            is_valid_number = True

    return [first_name, last_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)


def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    for el in res:
        print(el['телефон'], str(user_data[2]))
        if el['телефон'] == str(user_data[2]):
            print("Такой пользователь уже существует")
            return
    obj = {'имя': user_data[0], 'фамилия': user_data[1], 'телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)


file_name = 'phone.csv'
new_file_name = 'new_phone.csv'


def copy_info(file_name, new_file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        lst_1 = []
        for row in f_r:
            lst_1.append(row)
        flag = False
        while not flag:
            try:
                number = int(input('Введите номер строки: '))
                if number > len(lst_1):
                    print(f"Вводимое число не должно превышать количество строк ()")
                else:
                    flag = True
            except ValueError:
                print("Невалидный номер")
            res = read_file(new_file_name)
            res.append(lst_1[number - 1])
            with open(new_file_name, 'w', encoding='utf-8', newline='') as data:
                f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
                f_writer.writeheader()
                f_writer.writerows(res)

def main():
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'c':
            if not exists(new_file_name):
                create_file(new_file_name)
            copy_info(file_name, new_file_name)
        elif command == 'r':
            if not exists(file_name):
                print("Файл не создан. Создайте файл.")
                continue
            print(*read_file(file_name))


main()
