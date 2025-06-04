from abc import ABC, abstractmethod

class PaymentMethod(ABC):

    @abstractmethod
    
    def pay(self, amount):

        pass

class Paypal(PaymentMethod):

    def pay(self, amount):

        return print(f"The amount you pay is {amount} via paypal")

class GooglePay(PaymentMethod):

    def pay(self, amount):

        return print(f"The amount you pay is {amount} via GooglePay")
    
class BankCard(PaymentMethod):

    def pay(self, amount):

        return print(f"The amount you pay is {amount} via your Bank Card")
    

class Payment:

    def __init__(self, Payment_Method: PaymentMethod):

        self.Payment_Method = Payment_Method
    
    def pay(self, amount):

        return self.Payment_Method.pay(amount)

if __name__=="__main__":

    print('Give me the amount and the payment Method')

    user = input()

    cart = Payment(GooglePay())
