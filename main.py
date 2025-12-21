import transport.vehicle
import transport.client
import transport.transportCompany
import transport.ship
import transport.van

#Переменная для экземпляра транспортной компании
transport_company = 0


#####################################
#Функция главного меню и выбора пункта
def main_menu():
    print("#############=-МЕНЮ-=############")
    print("# 1. Создать компанию           #")
    print("# 2. Меню компании              #")
    print("# 3. Выйти                      #")
    print("#################################")
    print("\n\n\n                           ")

    funcs_main_menu[(int(input("Выбериту пункт меню: "))) - 1]()


###################################################
#Функция меню транспортной компании и выбора пункта
def company_menu():
    if check_company() == False:
        return False

    print("1. Добавить транспорт")
    print("2. Список транспорта")
    print("3. Добавить клиента")
    print("4. Список клиентов")
    print("5. Оптимизировать загрузку")
    print("6. Назад\n\n")

    choice = int(input("Выберите пункт меню: "))
    print("\n")
    funcs_company[choice - 1]()


######################################################
#Функция для проверки создана ли транспортная компания
def check_company():
    global transport_company

    if transport_company == 0:
        return False


###########################################
#Функция для добавления транспорта в список
def cmp_add_vehicle():
    #Проверка компании
    if check_company() == False:
        return False

    #Ввод данных для добавления транспорта
    veh_type = int(input("Введите тип (1. Ship / 2. Van): "))
    veh_id = int(input("Введите id:"))
    veh_capacity = float(input("Введите грузоподъемность: "))
    veh_current_load = float(input("Введите вес текущего груза в т/с:"))
    
    #Проверка введенных данных
    if((veh_type > 2) or (veh_type < 1) or (veh_id < 0) or (veh_capacity < 0) or (veh_current_load < 0)):
        print("Ошибка! Данные некорректны!")
        return False

    #Добавление корабля
    if (veh_type == 1 or veh_type == "1. Ship"):
        ship_name = str(input("Введите имя корабля: ")) #Ввод имени

        nv = transport.ship.Ship(ship_name) #Создание экземпляра класса

        #Присвоение данных экземпляру
        nv.vehicle_id = veh_id
        nv.capacity = veh_capacity
        nv.current_load = veh_current_load

        #Добавления транспорта в список
        transport_company.add_vehicle(nv, f"Ship - {ship_name}")
        transport_company.add_vehicle_obj(nv)


        print("Корабль добавлен!")

    #Создание фургона
    if (veh_type == 2 or veh_type == "2. Van"):
        is_refrigerated = bool(input("Есть ли холодильник (True / False): "))   #Ввод доп. данных
        
        nv = transport.van.Van(is_refrigerated) #Создание экземпляра класса

        #Присвоение данных экземпляру
        nv.vehicle_id = veh_id
        nv.capacity = veh_capacity
        nv.current_load = veh_current_load

        #Добавление в список
        if is_refrigerated:
            transport_company.add_vehicle(nv, f"Van + refr.")   #Если есть холодильник
            transport_company.add_vehicle_obj(nv)
        else:
            transport_company.add_vehicle(nv, f"Van")   #Если нет холодильника
            transport_company.add_vehicle_obj(nv)

        print("Фургон добавлен!")


################################################
#Функция для вывода списка транспорта в компании
def cmp_veh_list():
    global transport_company

    transport_company.list_vehicles()

################################################
#Функция для добавления клиента
def cmp_add_client():
    global transport_company

    if check_company() == False:
        return False


    client = transport.client.Client(
    name=str(input("Введите имя клиента: ")),
    cargo_weight=float(input("Введите вес груза клиента: ")),
    is_vip=bool(input("Является ли VIP (True / False): "))
    )


    transport_company.add_client(client)
    transport_company.add_client_obj(client)

################################################
#Функция для просмотра списка клиентов
def cmp_client_list():
    global transport_company

    if check_company() == False:
        return False

    transport_company.list_clients()


################################################
#Функция для оптимизации загрузки
def cmp_optimize_cargo():
    global transport_company

    if check_company() == False:
        return False

    transport_company.optimize_cargo_distribution()


##############################
#Функция для создания компании
def cmp_create():
    global transport_company

    #Проверка компании
    if check_company() != False:
        print("Компания уже создана!")
        return False

    transport_company = transport.transportCompany.TransportCompany()   #Создание экземпляра класса
    transport_company.name = str(input("Ведите имя компании: "))    #Ввод данных и присвоение их экземпляру
    

####################################################################################
funcs_main_menu = [cmp_create, company_menu, exit] #Список для пунктов главного меню
funcs_company = [cmp_add_vehicle, cmp_veh_list, cmp_add_client, cmp_client_list, cmp_optimize_cargo]    #Список для пунктов меню компании
####################################################################################


#Бесконечный цикл
while True:
    main_menu() #Вывод на экран главного меню