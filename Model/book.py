class Book:
    def __init__(self, id, title, genre, price, discount):
        self.book = [
            id,
            title,
            genre,
            price,
            discount
        ]

    def get_book(self):
        return self.book

    def get_id(self):
        return self.book[0]

    def get_title(self):
        return self.book[1]

    def get_genre(self):
        return self.book[2]

    def get_price(self):
        return self.book[3]

    def get_discount(self):
        return self.book[4]
