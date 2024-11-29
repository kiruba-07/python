class bankAccount():
    def __init__(self,name,accountnum):
     self.name=name
     self.__accountnum=accountnum
    def get_balance(self):
        
       return self.__accountnum()
    def get_account_details(self):
        return self.name
    def get_account_details(self):
        return self.__accountnum
    def deposit(self,amount):
      pass
       
class customer(bankAccount):
        def __init__(self,name,accountnum,balance):
         super().__init__(name,accountnum)
         self.balance=0
        def deposit(self,amount):
         self.amount=amount
         print(f"${amount} is deposited to customer account")
         
        def withdraw (self,amount):
         self.amount=amount+self.balance
         print(f"withdrawn {self.amount} from customer account")
        
class transaction(bankAccount):
   def __init__(self,name,accountnum,money):
      super().__init__(name,accountnum)
      self.money=0
   def check_balance(self,balance_amt):
      self.balance_amt=0
      return self.check_balance
      print("The balance amount of bank account is {self.balance_amt}")  

   def loan_system(self,interest):
    self.interest=interest+self.money
    return self.interest
   
if __name__=="__main__":
 a=customer("harish","SH456",200)
 a.deposit(100)
 print(a.get_account_details())
 a.withdraw(50)
 print(a.get_account_details())

 b=transaction("maheswari","AS345",100)
 b.check_balance(100)
 print(a.get_account_details())
 b.loan_system(2.00)
 print(a.get_account_details())











      
      
      



   
       
       
        