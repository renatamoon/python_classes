import json
from typing import List
from pydantic import BaseModel
from typing import Optional
import pydantic

# ------------ raising exception

class ISBNFormatError(Exception):
    """Custom error that is raised when ISBN 10 doesn't have the right format"""
    
    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


# ------------ Book Model

class Book(BaseModel):
    title: str
    author: str
    publisher: str
    price: float
    isbn_10: Optional[str]
    isbn_13: Optional[str]
    subtitle: Optional[str]
    
    # using the decorators and validators to validate the isbn numbers
    @pydantic.validator("isbn_10")
    @classmethod
    def isbn_10_validator(cls, value):
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars != 10):
            raise ISBNFormatError(value=value, message="ISBN 10 should be 10 digits")
        
        def char_to_int(char: str) -> int:
            if char in "Xx":
                return 10
            return int(char)
        weighted_sum = sum((10 - i) * char_to_int(x) for i, x in enumerate(chars))
        if weighted_sum % 11 != 0:
            raise ISBNFormatError(value=value, message="ISBN 10 digit sum should be divisible by 11")
        return value


# ------------ Main Function
def main() -> None:
    """Main Function"""
    
    # reading the data from JSON file    
    with open("./data.json") as file:
        data = json.load(file)
        
        books: List[Book] = [Book(**item) for item in data]
        print(books[0])
        print(books[0].title)
        
        # print(data[0]) # printing the first book
        # print(data[0]["title"]) # printing the first title
        

if __name__ == "__main__":
    main()