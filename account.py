from datetime import datetime



class Account:
   def __init__(self,name,account_number):
    self.name=name
    self.account_number=account_number
    self.balance=0
    self.deposit=[]
    self.withdrawal=[]
    self.time=datetime.now().strftime("%x")
    self.combine=[]
    self.loan=0



    # Modify the deposit method to append each successful deposit to self.deposits
   def deposits(self,amount):
      if amount<=0:
        return f"You have deposited Ksh{amount} and your balance now is {self.balance}"
      else:
        self.balance+=amount
        self.deposit.append(amount)  
        self.track={}
        self.track.update({"date":self.time})
        self.track.update({"amount":amount})
        self.track.update({"narration":"deposit"})
        print(self.track)
        self.combine.append(self.track)
        print(self.combine)
        return f"You have deposited {amount}. Your new balance is {self.balance}"
# Modify the withdrawal method to append each successful withdrawal to self.withdrawals
   def withdraw(self,amount):
       if amount>=self.balance:
        return f"Your balance is ksh{self.balance}, you cannot withdraw {amount}"
       elif amount<=0:
        return f"You cannot withdraw the amount should be more than 0"
       else:
        transaction=100
        self.balance-=amount + transaction
        self.withdrawal.append(amount) 
        self.minus={}
        self.minus.update({"date":self.time})
        self.minus.update({"amount":amount})
        self.minus.update({"narration":"withdrawal"}) 
        print(self.minus)
        self.combine.append(self.minus)
        print(self.minus)
        return f"You have withdrawn {amount} and your current balance is {self.balance}"        

# Add a new method called withdrawals_statement which prints each withdrawal in a new line
   def withdrawals_statement(self): 
        for i in self.withdrawal:
            return f"Your withdrawals are {i}"
#  Add a new method called deposits_statement which prints each deposit in a new line 
   def deposits_statement(self):
      for x in self.deposit:
         return f"Your deposits are {x}"
#add a method to show the current balance
   def current_balance(self):
     return f"Your current balance is {self.balance}"

def borrow(self,amount):
        if len(self.deposits)<10:
            return f"Add more deposits"
        if amount <100:
            return f"Inqure for mor than 100 loan" 
        for x in self.deposit:
            sum = 0
            sum +=x["amount"]  
        if amount>sum/3:
            return f"Dear {self.name} you can borrow money up to {sum/3}"
        if self.balance!=0:
            return f"Dear {self.name} you still  have balance of {self.balance}" 
        if self.loan_balance !=0:
            return f"Dear {self.name} you still have the balance of {self.loan_balance}, hence repay to borrow" 
        else:
            interest= amount*0.03
            self.loan_balance+=amount+interest
            return f"Dear {self.name} you have borrowed {self.loan_balance} and your balance is {self.balance}"

def loan_repayment(self,amount):
        if amount<0:
            return f"Amount is invald"
        if amount > self. loan_balance:
            self.balance += amount-self.loan_balance
            return f"Dear {self.name} thank you for repaying your load of {amount-self.loan_balance} and your account  balance is {self.balance}"
        else:
            self.loan_balance-=amount
            return f"Dear {self.balance} thank you, you've loan of {amount} and your current loan balance is {self.loan_balance}"
def transfer(self,amount,instance_account):
        if amount<=0:
            return f"invalid"
        if amount>= self.balance:
            return f"insufficient amount in your account"
        if isinstance(instance_account,Account):
            self.balance-=amount
            instance_account.balance += amount
            return f"you have transfered {amount} to {instance_account} account with the name {instance_account.name} and your new balance is {self.balance}"
            
   
         


  