import time
from datetime import date

class Book:
    title = ''
    pages = 0

    def __init__(self, title='', pages=0):
        self.title = title
        self.pages = pages

    def __str__(self):
        return self.title

    def __radd__(self,other):
        return self.pages + other

    def __add__(self,other):
        return self.pages + other

book1 = Book('Fluency',381)
book2 = Book('The Martian',385)
book3 = Book('Ready Player One',386)
