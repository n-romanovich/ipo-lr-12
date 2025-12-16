class Vehicle:
    vehicle_id = 0
    capacity = 0
    current_load = 0
    clients_list = []

    def load_cargo(self, client, veh):
        if (veh.current_load + client.carge_weight) > capacity:
            print("Груз не вместится!")
        else:
            veh.current_load += client.cargo_weight
            client.cargo_weight = 0

    def __str__(self):
        return f"Транспорт id: {self.id} \nВместимость: {self.capacity} \nТекущая загрузка: {self.current_load}"
    