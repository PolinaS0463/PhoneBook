import actions as act

while True: 

    def open_menu():
        print("Добро пожаловать в телефонный справочник!")
        print(
            '''
            1. Вывести все контакты на экран; 
            2. Добавить контакт; 
            3. Удалить контакт; 
            4. Изменить контакт;
            5. Очистить справочник; 
            6. Найти контакт; 
            7. Выход;
            '''
        )

        action = int(input("Выберите действие: "))

        if 0 < action < 8:
            return action 
        else:
            print("Введите корректное действие!")
            open_menu()

    def commit_action():

        result = open_menu()
        
        match result:
            case 1:
                act.show_phonebook()
            case 2:
                act.add_contact()
            case 3:
                act.delete_contact()
            case 4:
                act.change_contact()
            case 5:
                act.delete_all()
            case 6:
                act.find_contact()
            case _:
                act.exit()
    
    commit_action()