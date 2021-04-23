class EWallet:
    def __init__(self, name, surname, balance=""):
        self.name = name
        self.surname = surname
        self.balance = balance

    def __str__(self):
        return f"Имя клиента : {self.name}\nФамилия клиента : {self.surname}\nНа лицевом счете : {self.balance} "


first_client = EWallet("Иван", "Петров", "50 долларов")
print(first_client)

# Выполняем создание гостей наследуя имя и фамилию из класса EWallet


class Guest(EWallet):
    def __init__(self, name, surname, city, status):
        self.city = city
        self.status = status
        EWallet.__init__(self, name, surname)

    def __str__(self):
        return f"\nГость: {self.name} {self.surname}, {self.city}. Статус : {self.status}"


guest_1 = Guest("Иван", "Петров", "Москва", "Наставник")
print(guest_1)
