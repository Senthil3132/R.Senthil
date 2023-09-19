class Bank_Account:
  def __init__(self,account_number,account_holder_name,initial_balance=0):
    self.__account_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance
  
  def deposit (self,amount):
    if amount>0:
       self.__account_balance+=amount
       print ("Deposit ₹{} new balance ₹{}".format(amount,self.__account_balance))
    else:
        print ("invalid deposit amount")
  def withdraw (self,amount):
    if amount>0 and amount<=self.__account_balance:
      self.__account_balance-=amount
      print ("Withdraw ₹{}.New balance ₹{}".format (amount,self.__account_balance))
    else:
      print ("Invalid Withdrawal amount or Insufficient balance. ")

  def display_balance (self):
    print (" Account Holder Name for {} account Number {} New Balance₹{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))



Account=Bank_Account(account_number=1235778899,account_holder_name='Sanjay', initial_balance=5000.0)

Account. display_balance () 
Account. deposit(500.0)
Account. withdraw(200.0)
Account. display_balance ()