
#2
class BankAccount:
    def __init__(self, owner, balance, currency):
        self.owner = owner
        self.balance = balance
        self.currency = currency

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, pul):
        if pul >= 0:
            self.__balance = pul
        else:
            print('Balans manfiy bolmasligi kk')

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, valyuta):
        if valyuta == "UZS" or valyuta == "USD" or valyuta == "EUR":
            self.__currency = valyuta
        else:
            print('Siz umuman boshqa valyuta kiritdingiz shuning ucun biz USER valyutasidan foydalanzmiz')
            self.__currency = "UZS"


info = BankAccount("Lobar", 500, "GBP")

print(info.currency)
