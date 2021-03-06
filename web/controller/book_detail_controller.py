# -*- coding: utf-8 -*-

__author__ = 'nothi'

from os.path import join
from tornado.web import RequestHandler
from web.service.book_service import BookService
from web.settings import *

class BookDetailController(RequestHandler):
    def initialize(self):
        self.service = BookService()

    def get(self, isbn):
        result = self.service.query_by_pair_any({"isbn":isbn})[0]
        for goods_info in result.goods_list:
            if goods_info.platform == 0:
                goods_info.platform = '当当网'
            elif goods_info.platform == 1:
                goods_info.platform = '京东商城'
            elif goods_info.platform == 2:
                goods_info.platform = '亚马逊'

        self.render(os.path.join(template_dir, "bookdetail.html"), book=result)

    def post(self, isbn):
        self.get()
