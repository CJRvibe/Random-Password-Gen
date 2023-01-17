import random
import string


class RandomPasswordGen:
    upper_case_alphabets = list(string.ascii_uppercase)
    lower_case_alphabets = list(string.ascii_lowercase)
    numbers = list(string.digits)
    punctuation = list(string.punctuation)

    def __generate_password(self, elements, length):
        generated_password = ''
        result = random.choices(elements, k=length)
        for i in result: generated_password += i
        return generated_password

    
    def __length_checker(self, length):
        if length < 8:
            raise ValueError("length of password given must be longer than 8 characters")
        elif length > 50:
            raise ValueError("Length of password cannot be more than 50 characters")


    def generate(
        self, 
        length=20,
        *, 
        exclude_lowercase: bool=False,
        exclude_uppercase: bool=False,
        exclude_symbols: bool=False,
        exclude_numbers: bool=False
    ):
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

        return self.__generate_password(elements=elements, length=length)