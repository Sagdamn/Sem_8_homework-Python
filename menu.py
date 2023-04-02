while True:
    choise = int(input('Введите нужное действие: \n1 - Добавить в справочник \
                    \n2 - Вывести все данные справочника \n3 - Поиск по фамилии \
                    \n4 - Редактировать контакт \n5 - Удалить контакт \n6 - Выход \n'))
    match choise:
        case 1:
            import input_data
            input_data.Add(input('Введите фамилию и имя: '), input('Введите номер телефона: '))
        case 2:
            from output import OutputAll 
            OutputAll()
        case 3:
            from output import Search 
            Search(input('Введите фамилию для поиска: '))
        case 4:
            from modify import Edit 
            Edit(input('Введите фамилию или номер контакта, которые хотите изменить: '))
        case 5:
            from modify import Delete 
            Delete(input('Введите фамилию или номер контакта, которые хотите удалить: '))
        case 6: break
