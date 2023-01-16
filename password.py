import random
import string


class RandomPasswordGen:
    upper_case_alphabets = list(string.ascii_uppercase)
    lower_case_alphabets = list(string.ascii_lowercase)
    numbers = list(string.digits)
    punctuation = list(string.punctuation)

    def generate_password(self, elements, length):
        generated_password = ''
        result = random.choices(elements, length)
        for i in result: generated_password += i
        return generated_password

    
    def length_checker(self, length):
        if length < 8:
            raise ValueError("length of password given must be longer than 8 characters")
        elif length > 50:
            raise ValueError("Length of password cannot be more than 50 characters")


    def generate(
        self, 
        length=20, 
    ):
        self.length_checker(length)


generator = RandomPasswordGen()
generator.generate()