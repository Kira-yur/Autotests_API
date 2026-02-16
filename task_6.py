class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Пополнение: +{amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"Снятие: -{amount}")

        else:
            print(f"Ошибка сняти.Недостаточно средств. Пытались снять: {amount}", "Баланс:",self.balance)

    def transfer(self, person_2, amount):
        if self.balance >= amount:
            self.balance -= amount
            person_2.balance += amount
            self.history.append(f"Перевод: списание -{amount} на счет {person_2.owner}")
            person_2.history.append(f"Перевод: зачисление +{amount} от {self.owner}")

        else:
            print("Недостаточно средств. Текущий баланс:", self.balance, "Сумма перевода:", amount)

    def info(self):
        print("Owner", self.owner, "Balance:", self.balance)

    def print_history(self):
        print("История транзакций", self.history)


acc_1 = BankAccount("Kirill", 100)
acc_1.info()

acc_1.deposit(50)
acc_1.info()

acc_1.withdraw(100)
acc_1.info()

acc_1.withdraw(160)
acc_1.info()

acc_2 = BankAccount("Alex", 1000)
acc_2.info()

acc_2.deposit(50)
acc_2.info()

acc_2.withdraw(100)
acc_2.info()

acc_2.withdraw(160)
acc_2.info()

print("Переводы:")

acc_2.transfer(acc_1, 47)
acc_2.info()
acc_1.info()

acc_1.transfer(acc_2, 4700)
acc_2.info()
acc_1.info()
print("История:")
acc_1.print_history()
acc_2.print_history()