""" pycalc contains calculator class for basic arthimetic.

The module contains the Calculator class. The calculator class performs simple
arthimetic functions with both a float and integer.

Singleton Class:
    Calculator

Non-Classes:
    None
"""

from typing import Any
from typing import Tuple



class Calculator():
    """ A calculator to perform simple arthimetic functions with integers and floats

    Methods:
    add - add two numbers and return the value.
    subtract - subtract two numbers and return the value
    multiply - multiply number a by number b
    divide - divide number a by number b
    mod - return the remainder of number a divided by number b

    Exceptions:
        TypeError

    """

    _singleton = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        if not cls._singleton:
            cls._singleton = super(Calculator, cls).__new__(cls,
                                                      *args, **kwargs)
        return cls._singleton

    def add(self, num_a: Tuple[int, float], num_b: Tuple[int, float]) -> Tuple[int, float]:
        """ Get the sum of of two numbers
        
        num_a: An integer or float
        num_b: An integer or float

        Return:
            return an integer or a float. If a float is in problem, float will be returned.

        Exceptions:
            TypeError - if value is not integer or float.
        """
        if not isinstance(num_a, (int, float)):
            raise TypeError("Must be either a float or integer")
        if not isinstance(num_b, (int, float)):
            raise TypeError("Must be either a float or integer")
        return num_a + num_b

    def subtract(self, num_a: Tuple[int, float], num_b: Tuple[int, float]) -> Tuple[int, float]:
        """ Get the difference of two numbers
        
        num_a: An integer or float
        num_b: An integer or float

        Return:
            return an integer or a float. If a float is in problem, float will be returned.

        Exceptions:
            TypeError - if value is not integer or float.
        """
        if not isinstance(num_a, (int, float)):
            raise TypeError("Must be either a float or integer")
        if not isinstance(num_b, (int, float)):
            raise TypeError("Must be either a float or integer")
        return num_a - num_b

    def multiply(self, num_a: Tuple[int, float], num_b: Tuple[int, float]) -> Tuple[int, float]:
        """ Get the product of two numbers
        
        num_a: An integer or float
        num_b: An integer or float

        Return:
            return an integer or a float. If a float is in problem, float will be returned.

        Exceptions:
            TypeError - if value is not integer or float.
        """
        if not isinstance(num_a, (int, float)):
            raise TypeError("Must be either a float or integer")
        if not isinstance(num_b, (int, float)):
            raise TypeError("Must be either a float or integer")
        return num_a * num_b

    def divide(self, num_a: Tuple[int, float], num_b: Tuple[int, float]) -> Tuple[int, float]:
        """ Get the quotient of two numbers
        
        num_a: An integer or float
        num_b: An integer or float

        Return:
            return an integer or a float. If a float is in problem, float will be returned.

        Exceptions:
            TypeError - if value is not integer or float.
        """
        if not isinstance(num_a, (int, float)):
            raise TypeError("Must be either a float or integer")
        if not isinstance(num_b, (int, float)):
            raise TypeError("Must be either a float or integer")
        if num_b == 0:
            raise ValueError("Cannot divide by zero")
        return num_a / num_b

    def mod(self, num_a: Tuple[int, float], num_b: Tuple[int, float]) -> Tuple[int, float]:
        """ Get the remainder of a number divide by another
        
        num_a: An integer or float
        num_b: An integer or float

        Return:
            return an integer or a float. If a float is in problem, float will be returned.

        Exceptions:
            TypeError - if value is not integer or float.
        """
        if not isinstance(num_a, (int, float)):
            raise TypeError("Must be either a float or integer")
        if not isinstance(num_b, (int, float)):
            raise TypeError("Must be either a float or integer")
        if num_b == 0:
            raise ValueError("Cannot divide by zero")
        return num_a % num_b
