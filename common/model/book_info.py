__author__ = 'nothi'

class BookInfo:
    attrs = ["isbn", "price", "title", "author", "press","description","cover" ]

    def __init__(self):
        self.isbn = ''
        self.price = 0.0
        self.title = ''
        self.author = ''
        self.press = ''
        self.description= ''
        self.cover = ''
        self.goods_list = []