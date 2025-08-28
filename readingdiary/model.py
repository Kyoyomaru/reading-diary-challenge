from datetime import datetime
from typing import Optional


class Note:
    def __init__(self, text: str, page: int, date: datetime):
        self.text: str = text
        self.page: int = page
        self.date: datetime = date

    def __str__(self) -> str:
        # _str que devuelve formato
        return f"{self.date} - page {self.page}: {self.text}"


class Book:
    EXCELLENT: int = 3
    GOOD: int = 2
    BAD: int = 1
    UNRATED: int = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn: str = isbn
        self.author: str = author
        self.title: str = title
        self.pages: int = pages
        self.rating: int = Book.UNRATED
        # La lista de notas debe inicializarse vacia.
        self.notes: list = []

    # metodo_de_instancia
    def add_note(self, text: str, page: int, date: datetime) -> bool:
        if page > self.pages:
            return False
        else:
            # Aqui se crea un nuevo objeto Note
            new_note = Note(text, page, date)
            self.notes.append(new_note)
            return True

    # instancia
    def set_rating(self, rating: int) -> bool:
        # Los ratings validos son las constantes de la clase.
        valid_ratings = (Book.EXCELLENT, Book.GOOD, Book.BAD)
        # La condicion verifica si el rating no esta en la tupla de ratings validos.
        if rating not in valid_ratings:
            return False
        else:
            # Si el rating es valido, se asigna al atributo de la instancia.
            self.rating = rating
            return True

    def get_notes_of_page(self, page: int) -> list:
        notes_of_page = []
        for note in self.notes:
            if note.page == page:
                notes_of_page.append(note)
        return notes_of_page

    def page_with_most_notes(self) -> int:
        if not self.notes:
            return -1

        note_counts = {}
        for note in self.notes:
            note_counts[note.page] = note_counts.get(note.page, 0) + 1

        page_with_max_notes = max(note_counts, key=note_counts.get)
        return page_with_max_notes

    # -> str es una anotacion de tipo que indica que el metodo devolvera una cadena de texto.
    def __str__(self) -> str:
        # Aqui se usa un if para mapear el rating numerico a texto.
        if self.rating == Book.EXCELLENT:
            rating_text = "excellent"
        elif self.rating == Book.GOOD:
            rating_text = "good"
        elif self.rating == Book.BAD:
            rating_text = "bad"
        else:
            rating_text = "unrated"

        # Necesitas declarar los atributos con .self para que funcionen correctamente.
        return f"ISBN: {self.isbn}Title: {self.title}Author: {self.author}Pages: {self.pages}Rating: {rating_text}"


class ReadingDiary:
    def __init__(self):
        # Asi se crea un diccionario como lo pide el paso
        # Completa la clase ReadingDiary teniendo en cuenta los siguientes requisitos:
        # La clase debe tener un metodo __init__ que inicialice el atributo books de tipo dict[str, Book] como un diccionario vacio.
        self.books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        # Aqui se revisa si el ISBN ya esta en el diccionario.
        # Usa el metodo search_by_isbn para mantener la logica de busqueda en un solo lugar.
        book = self.search_by_isbn(isbn)
        if book is not None:
            return False
        else:
            # Aqui se crea un nuevo objeto "new_book".
            new_book = Book(isbn, title, author, pages)
            # añade el objeto al diccionari books usando el isbn como clave.
            self.books[isbn] = new_book
            return True

    def search_by_isbn(self, isbn: str) -> Optional[Book]:
        # Este metodo busca el libro por su ISBN y devuelve el objeto o None.
        return self.books.get(isbn)

    def add_note_to_book(self, isbn: str, text: str, page: int, date: datetime) -> bool:
        # Busca el libro. Si no existe, devuelve False.
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        # Si el libro existe, lleva la accion a su metodo add_Note devuelve su resultado.
        return book.add_note(text, page, date)

    def rate_book(self, isbn: str, rating: int) -> bool:
        # Busca el libro. Si no existe, devuelve False.
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        # Si el libro existe, delega la accion a su metodo set_rating.
        return book.set_rating(rating)

    def book_with_most_notes(self) -> Optional[Book]:
        # Si no hay libros en el diario, devuelve None.
        if not self.books:
            return None

        book_with_max_notes: Optional[Book] = None
        max_notes = -1

        # Recorre cada libro en el diccionario.
        for book in self.books.values():
            num_notes = len(book.notes)

            # Si el libro actual tiene mas notas que el maximo registrado,
            # actualiza el maximo y el libro de referencia.
            if num_notes > max_notes:
                max_notes = num_notes
                book_with_max_notes = book

        # Si el maximo de notas es 0 o menos, significa que no se encontro ninguna nota en ningun libro.
        if max_notes <= 0:
            return None

        return book_with_max_notes