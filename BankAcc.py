class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Kwota wpłaty musi być większa od 0.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Kwota wypłaty musi być większa od 0.")
        if amount > self.balance:
            raise ValueError("Niewystarczające środki na koncie.")
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance

# Przykładowe użycie
account = BankAccount(100)
print(account.deposit(50))  # Wpłata 50
print(account.withdraw(30))  # Wypłata 30
print(account.check_balance())  # Sprawdzenie salda