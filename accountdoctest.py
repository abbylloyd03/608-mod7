# account.py

"""Account class definition."""
from decimal import Decimal

class Account: # (Class header, Class names should begin with uppercase letters)
    """Account class for maintaining a bank account balance."""
    
    def __init__(self, name, balance):
        """Initialize an Account object.
        
        >>> account1 = Account('John Green', Decimal('50,00'))
        >>> account1.name
        'John Green'
        >>> account1.balance
        Decimal('50.00')
        
        The balance must be greater than or equal to 0.
        >>> account2 = Account('John Green', Decimal('-50.00'))
        Traceback (most recent call last):
            ...
        ValueError: Initial balance must be >= 0.00.
        """
        
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

        
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)