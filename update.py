from models import Author, Book

new_author = Author.get(Author.name == 'Julio Verne')
book = Book.get(Book.title=="Vinte Mil Leguas Submarinas")

book.author = new_author

# Salvamos a alteração no banco
book.save()