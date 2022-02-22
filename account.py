# account.py

"""Account class definition."""
from decimal import Decimal

class Account: # (Class header, Class names should begin with uppercase letters)
    """Account class for maintaining a bank account balance."""
    
    def __init__(self, name, balance):
        """Initialize an Account object."""
        
        # if balance is less than 0.00, raise and exception   
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')
            
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        """Deposit money to the acount."""
        
        # if amount is less than 0.00 raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')
            
        self.balance += amount
        
        
    def withdraw(self, amount):
        """Withdraw money from account."""
        
        # if amount is less than 0.00 raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('acount must be positive.')
        if amount > self.balance:
            raise ValueError('ammount must be <= balance.')
        
        self.balance -= amount
        
