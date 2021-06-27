class Atm (object):
    def __init__(self, cardNumber, pinNumber):
        self.a=cardNumber
        self.b=pinNumber
   
    def check_balance(self):
        print("Your balance is 0")

    def depositAmount(self, amount):
        new_amount=0+amount   
        print("You have deposited "+str(amount)+" in your bank. Your current balance is "+str(new_amount))

    def withdrawlMoney(self,amount):
        new_amount=0-amount
        print("You have withdrawl"+str(amount)+"from your bank. Your current balance is"+str(new_amount))

def main():
    Card_number = input("insert your card number:- ")
    pin_number  = input("enter your pin number:- ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1. Deposit money   2. Withdrawl 3. Check balance")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        amount = int(input("enter the amount:- "))
        new_user.depositAmount(amount)
        
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawlMoney(amount)
       
    elif (activity == 3):
       new_user.check_balance()
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()
