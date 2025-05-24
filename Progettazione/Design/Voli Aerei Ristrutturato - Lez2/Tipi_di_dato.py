from typing import Self, Any

class IntG0(int):
    '''Define an integer that has to be greater than zero (> 0)\n
    Raise an error if you try to create an object that doesn't meet the criteria.'''    
    def __new__(cls, value: int|float|str|bool|Self|'IntG1900') -> Self:
        if value <= 0:
            raise ValueError(f"ValueError: IntG0 does not support integers less or equal to 0 ({value})")
        return super().__new__(cls, value)

class IntGE0(int):
    '''Define an integer that has to be greater or equal to zero (>= 0)\n
    Raise an error if you try to create an object that doesn't meet the criteria.'''    
    def __new__(cls, value: int|float|str|bool|Self|'IntG1900') -> Self:
        if value < 0:
            raise ValueError(f"ValueError: IntGE0 does not support negative integers ({value})")
        return super().__new__(cls, value)

class IntG1900(int):
    '''Define an integer that has to be greater than 1900 (> 1900)\n
    Raise an error if you try to create an object that doesn't meet the criteria.'''    
    def __new__(cls, value: int|float|str|bool|Self|IntGE0) -> Self:
        if value < 0:
            raise ValueError(f"ValueError: IntGE1900 does not support integers less or equal to 1900 ({value})")
        return super().__new__(cls, value)

