#!/usr/bin/env python
# -*- coding: utf-8 -*-
from xml.sax.handler import ContentHandler

__author__ = 'Tobias.Obermayer'


class ArticleHandler(ContentHandler):
    inArticle = 0
    inBody = 0
    isMatch = 0
    title = ""
    body = ""

    def startElement(self, name, attrs):
        if name == "webArticle":
          subcat = attrs.get("subcategory", "")
          if "tech" in subcat:
            self.inArticle = 1
            self.isMatch = 1

        print 'tobi startet dumm mit:' + name

    def endElement(self, name):
        print 'tobi endet dumm mit:' + name


def main():
    from xml.sax import make_parser

    aHandler = ArticleHandler()
    saxparser = make_parser()
    saxparser.setContentHandler(aHandler)
    saxparser.parse(open('xmlSource.xml', 'r'))
    print ArticleHandler.inArticle


if __name__ == '__main__':
    main()