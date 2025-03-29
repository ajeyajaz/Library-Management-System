from collections import  defaultdict

class Library:

    def __init__(self):
        self.books = defaultdict(list)

    def add_book(self,category,book_id,title,author):

        book = Book(category,book_id,title,author) # used a composition concept to add a book
        self.books[book.category].append(book)
        print('Book added successfully...')


    def display_book(self):

        if self.books:
            for categories ,books in self.books.items(): # iterating etarating over categories
                print(f'Category : {categories}')

                for book in books: # iterating over the book objects
                    print(f"Title : {book.title} ,Book Id : {book.book_id} ,Author : {book.author}")
        else:
            print("Book list is empty..")


    def remove_book(self,category,id):

        book = self.is_book_available(category,id)
        if book:
                print(f'{book.title} removed successfully...')
                self.books[category].remove(book) # removing that book object

                if not self.books[category]: # if the category empty remove it
                    del self.books[category]
                return
        print('Book has not found...')


    def borrow_book(self ,category,id):

            book = self.is_book_available(category,id)
            if book:
                if book.borrowed():
                    print(f'{book.title} is borrowd successfully')
                else:
                    print(f'{book.title} is already borrowd,cannot borrow twice')
            else:
                print('Book has not found...')


    def is_book_available(self,category ,id):

                for book in self.books[category]:
                    if book.book_id == id:
                        return book
                return False


    def return_book(self,category,id):

        book = self.is_book_available(category,id)
        if book :
            if book.return_book():
                print("Book is returned succesfully..")
            else:
                print("you don't have a such book to return..")
            return
        else:
            print('Book has not found...')

class Book:

    def __init__(self,category,book_id,title,author ,is_borrowed=False):

        self.category = category
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed



    def borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True

        return False

    def return_book(self):

        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False



def main():
        library = Library()

        while True:

            print("""
                1. Add Book
                2. Remove Book
                3. Display Books
                4. Borrow Book
                5. Return Book
                6. Exit""")
            choice = int(input("enter your choice : "))


            match choice:

                case 1 :
                        print('Enter the details to add a Book')
                        category = input('Enter the Category Name : ')
                        book_id = input("Enter the Book Id : ")
                        title = input("Enter the Name of the Book : ")
                        author = input("Enter the Author of the Book : ")
                        library.add_book(category,book_id,title,author)

                case 2 :
                        category = input('Enter Category : ')
                        book_id = input('Enter Book ID')
                        library.remove_book(category, book_id)

                case 3 :
                        library.display_book()
                case 4 :
                        category = input('Enter Category : ')
                        book_id = input('Enter Book ID')
                        library.borrow_book(category,book_id)

                case 5 :
                        category = input('Enter Category : ')
                        book_id = input('Enter Book ID')
                        library.return_book(category,book_id)
                case 6 :
                         exit()
                case _:
                        print('invalid choice')


if __name__ == '__main__' :

    main()











