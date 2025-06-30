# Balance check, deposit, withdraw (store balance in file)

class Account:
    def __init__(self, AcNo):
        self.AcNo = AcNo
        self.filename = f"{self.AcNo}_balance.txt"

        try:
            with open(self.filename, "r") as file:
                content = file.read().strip()
                self.balance = float(content) if content else 100000
        except FileNotFoundError:
            self.balance = 100000
            self.balance_upadate()

    def balance_upadate(self):
        with open(self.filename, "w") as file:
            file.write(str(f"Balance :{self.balance}"))
            print(f"✅Current Balance : ₹{self.balance}.")

    def deposite(self, amount):
        if (amount > 0):
            self.amount = amount
            self.balance += self.amount
            self.balance_upadate()
            print(f"✅ ₹{amount} Deposite successfully.")
            print(f"✅Current Balance : ₹{self.balance}.")
        else:
            print("❌ Invalid amount.")
            
    def Withdraw(self, amount):
        if(0 < amount <= self.balance): 
            self.amount = amount
            self.balance -= self.amount
            self.balance_upadate()
            print(f"✅ ₹{amount} withdrawn successfully.")
            print(f"✅Current Balance : ₹{self.balance}.")
        else:
            print("Insufficient balance or invalid amount")

acno = int(input("Eter last four digit of your acc No : "))
acc = Account(acno)
while True:
    print("\n=========== Welcome to smart and simple ATM ===========")
    print("=========== Choice Number :===========")
    print("=========== 1. Check Balance===========")
    print("=========== 2. Deposite Money===========")
    print("=========== 3. Withdraw Money===========")
    print("=========== 4. Exit===========")
    
    choice_number = input("Enter Your Choice : ")
    
    if choice_number == '1':
        acc.balance_upadate()
        
    elif choice_number == '2':
        amount = int(input("Enter deposite amount :"))
        acc.deposite(amount)
        
    elif choice_number == '3':
        amount = int(input("Enter withdrawal amount :"))
        acc.Withdraw(amount)
    elif choice_number == '4':
        break
    
