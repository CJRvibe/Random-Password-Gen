import secrets
import string
from typing import List


class CurrentState:
    """
A class to represent the current state of the password generator.
This class stores the most recent information about the specifics of generating the password.
    """
    def __init__(self):
        self.elements: List[str]
        self.length: int

    
    def edit_state(self, elements: List[str], length: int) -> None:
        self.elements = elements
        self.length = length

class RandomPasswordGen:
    """
A class that holds all functionalities to generate random password    
    """
    upper_case_alphabets = list(string.ascii_uppercase)
    lower_case_alphabets = list(string.ascii_lowercase)
    numbers = list(string.digits)
    punctuation = list(string.punctuation)

    def __init__(self) -> None:
        self.__current_state: CurrentState = CurrentState()


    def __generate_password(self, elements: List[str], length: int) -> str:
        result = "".join(secrets.choice(elements) for i in range(length+1))
        return result

    
    def __length_checker(self, length: int) -> None:
        if length < 8:
            raise ValueError("length of password given must be longer than 8 characters")
        elif length > 50:
            raise ValueError("Length of password cannot be more than 50 characters")


    def generate(
        self, 
        length: int=20,
        *, 
        exclude_lowercase: bool=False,
        exclude_uppercase: bool=False,
        exclude_symbols: bool=False,
        exclude_numbers: bool=False
    ) -> str:
        self.__length_checker(length)
        elements = []
        if exclude_lowercase is False:
            elements += self.lower_case_alphabets
        if exclude_uppercase is False:
            elements += self.upper_case_alphabets
        if exclude_symbols is False:
            elements += self.punctuation
        if exclude_numbers is False:
            elements += self.numbers

        if elements == []: raise ValueError("You must allow at least one type of password variable to be accepted")

        self.__current_state.edit_state(elements, length)
        return self.__generate_password(elements=elements, length=length)

    
    def regenerate(self) -> str:
        """
Regenerate the password based on the most recent specified details for the previous password generation
        """
        elements = self.__current_state.elements
        length = self.__current_state.length
        return self.__generate_password(elements=elements, length=length)