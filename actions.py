import sys

# Extra functions:
# ----------------------------------------------------------------------------

def get_info():
    name, surname = input("Введите имя и фамилию через пробел: ").split(" ")
    phone = int(input("Введите номер: +"))
    comment = input("Введите комментарий: ")
    return f"{name} {surname} - {phone} ({comment})\n"

def check_presence(sample):
    with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
        contacts = phonebook.readlines()
        count = 0
        for contact in contacts:
            if len(contact.split(" ")) > 5:
                if sample == contact.split(" ")[:-3]:
                    count += 1
            else:
                if sample == contact[:-1].split(" "):
                    count += 1
        if count == 0:
            return False
        return count
    
# ----------------------------------------------------------------------------
    

# Main functions:
# ----------------------------------------------------------------------------

def show_phonebook():
    try:
        with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
            contacts = phonebook.readlines()
            if len(contacts) > 1:
                for number, contact in enumerate(contacts[1:], 1):
                    print(f"{number}. {contact}"[:-1])
            else:
                print("Справочник пустой!")
                return "absence"
    except FileNotFoundError:
        with open('phonebook.txt', 'a', encoding='utf-8') as phonebook:
            phonebook.write("Телефонный справочник: \n")
        show_phonebook()
            
def add_contact():
    with open('phonebook.txt', 'a', encoding='utf-8') as phonebook:
        contact_to_add = get_info()
        if check_presence(contact_to_add[:-1].split(" ")) != False:
            amount = check_presence(contact_to_add[:-1].split(" "))
            submit = input("Такой контакт уже существует. Вы уверены, что хотите его добавить? (Да или нет): ")
            if submit.lower() == "да":
                phonebook.write(f"{contact_to_add[:-1]} - {amount + 1} раз\n")
        else:
            phonebook.write(contact_to_add)

def delete_contact():
    if show_phonebook() != "absence":
        with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
            contacts = phonebook.readlines()
            contact_to_delete = int(input("Введите номер контакта для удаления: "))
            if contact_to_delete <= 0 or contact_to_delete >= len(contacts):
                print("Неверно введен номер строки - такой строки не существует! Попробуйте еще раз!")
                delete_contact()
            for contact in range(len(contacts)):
                if contact == contact_to_delete:
                    contacts[contact] = ''
        with open ('phonebook.txt', 'w', encoding='utf-8') as phonebook:
            phonebook.writelines(contacts)


def change_contact():
    if show_phonebook() != "absence":
        with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
            contacts = phonebook.readlines()
            contact_to_change = int(input("Введите номер контакта для изменения: "))
            if contact_to_change <= 0 or contact_to_change >= len(contacts):
                print("Неверно введен номер строки - такой строки не существует! Попробуйте еще раз!")
                change_contact()
            for contact in range(len(contacts)):
                if contact == contact_to_change:
                    contacts[contact] = get_info()
        with open ('phonebook.txt', 'w', encoding='utf-8') as phonebook:
            phonebook.writelines(contacts)

def delete_all():
    if show_phonebook() != "absence":
        with open('phonebook.txt', 'w', encoding='utf-8') as phonebook:
            phonebook.write('')
            phonebook.write("Телефонный справочник: \n")

def find_contact():
    if show_phonebook() != "absence":
        with open('phonebook.txt', 'r', encoding='utf-8') as phonebook:
            print("Как вы хотите искать контакт?")
            print(''' 
                1. По имени;
                2. По фамилии;
                3. По номеру;
                4. По комментарию.
                Для объединения нескольких способов, введите их цифры подряд:
            ''')
            samples = set(list(map(int, input())))
            if max(samples) > 4 or min(samples) < 1:
                print("Пожалуйста, введите корректный(е) способ(ы) поиска!")
                find_contact()
            else:
                dict = {}
                count_lines = 0
                count_suitable = 0
                # line_num = 0
                for way in samples:
                    if way == 1:
                        name = input("Введите имя: ")
                        dict[name] = 0
                    elif way == 2:
                        surname = input("Введите фамилию: ")
                        dict[surname] = 1
                    elif way == 3:
                        number = input("Введите номер: ")
                        dict[number] = 3
                    else:
                        comment = input("Введите комментарий: ")
                        dict[f"({comment})"] = 4
                contacts = phonebook.readlines()
                for contact in contacts[1:]:
                    for key in dict:
                        if key == contact[:-1].split(" ")[dict.get(key)]:
                            count_suitable += 1
                    if count_suitable == len(dict):
                        print(contact[:-1])
                        count_lines += 1
                    count_suitable = 0
                if count_lines == 0:
                    print("По вашему запросу ничего не найдено!")
    
def exit():
    sys.exit()

# ----------------------------------------------------------------------------
