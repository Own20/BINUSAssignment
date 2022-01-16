# import Week8
from Week8 import Book
from Week8 import Song

b1 = Book ("Raging Bulls", "Jessica", 3.50)

print (b1.__str__())

b2 = Book()
b2.setTitle("Fade to Black")
b2.setAuthor("Jisu")
b2.setPrice(4.50)

# b2.__author = Alsyha
b2.setAuthor("Alysha")
print(b2.__str__())

title = input("Enter song title: ")
artist = input("Enter artist: ")
genre = input("Enter genre: ")

s1 = Song(artist, title, genre)

print(s1.__str__())