class Money:
    def __init__(self, amount, currency='KGS'):
        self.amount = amount
        self.currency = currency

    def __str__(self):
        return f'[{self.amount} {self.currency}]'

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __gt__(self, other):
        if self.currency != other.currency:
            return "Нельзя сравнивать разные валюты"
        return self.amount > other.amount

    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Разные валюты")
        return Money(self.amount + other.amount, self.currency)

money_n = Money(100, 'KGS')
money_a = Money(200, 'KGS')

print(money_n + money_a)  # [300 KGS]
print(money_a > money_n)   # True
