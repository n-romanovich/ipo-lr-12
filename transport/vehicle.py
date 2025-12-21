class Vehicle:
    vehicle_id = 0
    capacity = 0
    current_load = 0
    clients_list = []

    def load_cargo(self, client):
        if self.current_load + client.cargo_weight > self.capacity:
            print("Груз не вместится!")
        else:
            self.current_load += client.cargo_weight
            self.clients_list.append(client)
            client.cargo_weight = 0


    def __str__(self):
        return f"Транспорт id: {self.id} \nВместимость: {self.capacity} \nТекущая загрузка: {self.current_load}"
    