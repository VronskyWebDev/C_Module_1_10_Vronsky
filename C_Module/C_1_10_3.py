class EWallet:
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance

    def __str__(self):
        return f"Имя клиента : {self.name}\nФамилия клиента : {self.surname}\nНа лицевом счете : {self.balance} "


first_client = EWallet("Иван", "Петров", "50 долларов")
print(first_client)
