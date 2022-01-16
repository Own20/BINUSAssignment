"""
# class - blueprint for an object
# object - self governing entity that hasattr
# operations (methods)

# Class Description

# class definition

class Xxx:
    # initializer method - set up an object
    # self parameter - allows interpreter to know which
    # object it is working with
    def _init_(self):
        # creates and initializes instance variables/attributes
        # private use __varName
    
    # mutator methods - aka setter allow you to update attributes
    def setxXx(self):
                            self.xxx = xxx
    # accessor methods - aka getter allows you to retrieve data
    def getxXx(self):
        return              return self.xxx
    
    # other methods specific to the Book object

    def _str_(self):
        return              return "{}".format(self.getxXx())
"""

"""
Class Description
Book which contains 3 attributes
title,author,price  
"""
# class Book:
#     def __init__(self, title="", author="", price=0.0):
#         self.title = title
#         self.author = author
#         self.price = price
    
#     def setTitle(self, title):
#         self.__title = title
#     def setAuthor(self, author):
#         self.__author = author
#     def setPrice(self, price):
#         if price > 0:
#             self.__price = price
#         else:
#             self.__price = 0
    
#     def getTitle(self):
#         return self.__title
#     def getAuthor(self):
#         return self.__author
#     def getPrice(self):
#         return self.__price
    
#     def __str__(self):
#         return "Title: {} Author: {} Price: {}".format(self.getTitle, self.getAuthor, self.getPrice)

"""
Class Description
"""
from _typeshed import Self

class Song:
    def __init__(self, artist="", title="", genre="", duration=0.0):
        self.__artist = artist
        self.__title = title
        self.__genre = genre
        self.setDuration(duration)
    
    def setDuration(self, duration):
        if (duration > 0):
            self.__duration = duration
        else:
            self.__duration = 0.0
    
    def setArtist(self, artist):
        self.__artist = artist
    def setTitle(self, title):
        self.__title = title
    def setGenre(self, genre):
        self.__genre = genre
    
    def getArtist(self):
        return self.__artist
    def getTitle(self):
        return self.__title
    def getGenre(self):
        return self.__genre
    def getDuration(self):
        return self.__duration
    
    def __str__(self):
        return "Artist: {} Title: {} Genre: {} Duration {:.2f}".format(self.getArtist(),self.getTitle(),self.getGenre(), +\
        self.getDuration())