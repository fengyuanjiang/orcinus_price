__author__ = 'nothi'

class BookGoodsInfo:
    attrs = ["isbn","link","platform","instant_price", "crawling_time"]
    def __init__(self):
        self.isbn = ''
        self.link = ''
        self.platform = ''
        self.instant_price = 0.0
        self.crawling_time = ''