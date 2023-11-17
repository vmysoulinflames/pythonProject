#цикл для записи нескольких пользователей
while True:
    name = input("Insert your name (or 'exit' to stop): ")

    # Проверяем, не введено ли 'exit' для завершения
    if name.lower() == 'exit':
        break

    surname = input("Insert your surname: ")
    age = int(input("Insert your age: "))

    # Открываем файл в режиме добавления
    with open("user_info.txt", "a") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Surname: {surname}\n")
        file.write(f"Age: {age}\n")
        file.write("-" * 20 + "\n")  #Разделитель между пользователями

    # Выводим сообщение для пользователя
    print(f"{name} {surname}, thank you for registration.")

    # Проверяем возраст и выводим соответствующее сообщение
    if age >= 18:
        print("You are registered!")
    else:
        print("Access denied!")
