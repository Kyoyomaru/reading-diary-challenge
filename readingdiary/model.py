from datetime import datetime
class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date
#metodo_init
    def __str__(self) -> str:
#_str que devuelve formato
        return f"{self.text} {self.page} {self.date}"



class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self,isbn:str,title:str,author:str,pages: int):
        rating: int=Book.UNRATED
        notes: list=[Note]

#metodo_de_instancia
       def add_note(text:str,page:int,date:datetime = bool):
           if (page > book.total_pages):
















