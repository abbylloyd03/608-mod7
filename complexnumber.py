# complexnumber.py
"""Complex class with overloaded operators."""

class Complex:
    """Complex class that represents a complex number with real and imaginary parts."""
    
    def __init__(self, real, imaginary):
        """Initialize Complex class's attributes."""
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, right):
        """Overrides the + operator."""
        return Complex(self.real + right.real,
                       self.imaginary + right.imaginary)

    def __iadd__(self, right):
        """Overrides the += operator."""
        self.real += right.real
        self.imaginary += right.imaginary
        return self
    
    def __repr__(self):
        """Return string representation for repr():"""
        return (f'({self.real} ' +
                ('+' if self.imaginary >= 0 else '-') +
                f' {abs(self.imaginary)}i)')