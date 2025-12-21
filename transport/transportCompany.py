import string

class TransportCompany:
    name = ""
    vehicles = []
    vehicles_obj = []
    clients = []
    clients_obj = []

    def add_vehicle(self, vehicle, veh_type):
        if vehicle.vehicle_id > 0 and vehicle.capacity > 0 and vehicle.current_load > 0:
            self.vehicles.append(f"{vehicle.vehicle_id}({veh_type})")

    def add_vehicle_obj(self, vehicle):
        if vehicle.vehicle_id > 0 and vehicle.capacity > 0 and vehicle.current_load > 0:
            self.vehicles_obj.append(vehicle)

    def list_vehicles(self):
        print(f"Список транспорта: {self.vehicles}")
        print(self.vehicles_obj)

    def add_client_obj(self, client):
        if client.cargo_weight > 0 and client.name != "":
            self.clients_obj.append(client)

    def add_client(self, client):
            self.clients.append(f"{client.name} - {client.cargo_weight} (VIP - {client.is_vip})")

    def list_clients(self):
        print(f"Список клиентов: {self.clients}")
        print(self.clients_obj)

    def optimize_cargo_distribution(self):
        for client in self.clients_obj:
            if (client.is_vip == True):
                for veh in self.vehicles_obj:
                    if (veh.current_load > client.cargo_weight):
                        veh.load_cargo(client)
        
        for client in self.clients_obj:
            if (client.is_vip == False):
                for veh in self.vehicles_obj:
                    if (veh.current_load > client.cargo_weight):
                        veh.load_cargo(client)

        print("Оптимизация загрузки завершена!")

        print("Текущая загрузка транспорт:")
        for veh in self.vehicles_obj:
            print(f"id: {veh.vehicle_id} - load: {veh.current_load}kg")
    
