import dearpygui.dearpygui as dpg
from transport.client import Client
from transport.ship import Ship
from transport.van import Van
from transport.transportCompany import TransportCompany

# Создаём компанию
company = TransportCompany()
company.name = "My Company"

# ------------------- CALLBACKS -------------------

def add_client_callback(sender, app_data, user_data):
    name = dpg.get_value("client_name")
    weight = dpg.get_value("client_weight")
    vip = dpg.get_value("client_vip")

    # Валидация данных клиента
    if not name.isalpha() or len(name) < 2:
        dpg.configure_item("status", default_value="Error: invalid name")
        return
    if weight <= 0 or weight > 10000:
        dpg.configure_item("status", default_value="Error: invalid weight")
        return

    # Создание клиента и добавление в компанию
    client = Client(name, weight, vip)
    company.add_client(client)
    company.add_client_obj(client)

    # Добавляем строку в таблицу клиентов
    with dpg.table_row(parent="clients_table"):
        dpg.add_text(client.name)
        dpg.add_text(str(client.cargo_weight))
        dpg.add_text(str(client.is_vip))

    dpg.configure_item("status", default_value="Client added!")

def add_vehicle_callback(sender, app_data, user_data):
    veh_type = dpg.get_value("veh_type")
    capacity = dpg.get_value("veh_capacity")
    load = dpg.get_value("veh_load")

    # Валидация транспорта
    if capacity <= 0 or load < 0:
        dpg.configure_item("status", default_value="Error: invalid capacity/load")
        return

    # Создание объекта транспорта
    if veh_type == "Ship":
        name = dpg.get_value("ship_name")
        vehicle = Ship(name)
    else:
        refr = dpg.get_value("van_refr")
        vehicle = Van(refr)

    vehicle.vehicle_id = len(company.vehicles_obj) + 1
    vehicle.capacity = capacity
    vehicle.current_load = load

    company.add_vehicle(vehicle, veh_type)
    company.add_vehicle_obj(vehicle)

    # Добавляем строку в таблицу транспорта
    with dpg.table_row(parent="vehicles_table"):
        dpg.add_text(str(vehicle.vehicle_id))
        dpg.add_text(veh_type)
        dpg.add_text(str(vehicle.capacity))
        dpg.add_text(str(vehicle.current_load))

    dpg.configure_item("status", default_value=f"{veh_type} added!")

def distribute_callback():
    # Оптимизация распределения грузов
    company.optimize_cargo_distribution()
    dpg.configure_item("status", default_value="Cargo distributed!")

def export_callback():
    # Экспорт результатов в файл
    with open("result.txt", "w", encoding="utf-8") as f:
        f.write("Distribution results:\n")
        for veh in company.vehicles_obj:
            f.write(f"id: {veh.vehicle_id}, load: {veh.current_load}\n")
    dpg.configure_item("status", default_value="Results saved to result.txt")

# ------------------- GUI -------------------

dpg.create_context()

with dpg.window(label="Main Window", width=800, height=600):
    # Меню
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Export Results", callback=export_callback)
        with dpg.menu(label="Help"):
            dpg.add_menu_item(label="About", callback=lambda: dpg.show_item("about_modal"))

    # Панель управления
    dpg.add_button(label="Add Client", callback=lambda: dpg.show_item("client_window"))
    dpg.add_button(label="Add Vehicle", callback=lambda: dpg.show_item("vehicle_window"))
    dpg.add_button(label="Distribute Cargo", callback=distribute_callback)

    # Таблица клиентов
    with dpg.table(header_row=True, tag="clients_table"):
        dpg.add_table_column(label="Name")
        dpg.add_table_column(label="Weight")
        dpg.add_table_column(label="VIP")

    # Таблица транспорта
    with dpg.table(header_row=True, tag="vehicles_table"):
        dpg.add_table_column(label="ID")
        dpg.add_table_column(label="Type")
        dpg.add_table_column(label="Capacity")
        dpg.add_table_column(label="Load")

    # Статусная строка
    dpg.add_text("", tag="status")

# Окно добавления клиента
with dpg.window(label="Add Client", modal=True, show=False, tag="client_window"):
    dpg.add_input_text(label="Client Name", tag="client_name")
    dpg.add_input_float(label="Cargo Weight", tag="client_weight")
    dpg.add_checkbox(label="VIP", tag="client_vip")
    dpg.add_button(label="Save", callback=add_client_callback)
    dpg.add_button(label="Cancel", callback=lambda: dpg.hide_item("client_window"))

# Окно добавления транспорта
with dpg.window(label="Add Vehicle", modal=True, show=False, tag="vehicle_window"):
    dpg.add_combo(["Ship", "Van"], label="Vehicle Type", tag="veh_type")
    dpg.add_input_float(label="Capacity", tag="veh_capacity")
    dpg.add_input_float(label="Current Load", tag="veh_load")
    dpg.add_input_text(label="Ship Name", tag="ship_name")
    dpg.add_checkbox(label="Refrigerator (for Van)", tag="van_refr")
    dpg.add_button(label="Save", callback=add_vehicle_callback)
    dpg.add_button(label="Cancel", callback=lambda: dpg.hide_item("vehicle_window"))

# О программе
with dpg.window(label="About", modal=True, show=False, tag="about_modal"):
    dpg.add_text("Lab Work 13, Variant 3, Name: Nikita")
    dpg.add_button(label="Close", callback=lambda: dpg.hide_item("about_modal"))

dpg.create_viewport(title="GUI Lab 13", width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
