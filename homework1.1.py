import datetime


class Comment:

    def __init__(self, user, book, comment):
        self.user = user
        self.book = book
        self.date = datetime.date.today()
        self.comment = comment

    def __str__(self):
        return '%s writes about %s : %s. %s.' % (self.user, self.book, self.comment, self.date)

com1 = Comment('Steave', 'Yellow Fang', 'I do not like this book')
com2 = Comment('Joy', 'Pollyanna', 'very interesting book')
com3 = Comment('Zoe', 'Charlie and the Chocolate Factory', 'Good')
com4 = Comment('Mark', 'Pollyanna', 'I think it is quite boring book')
com5 = Comment('Lisa', 'Yellow Fang', 'very oldfashion')
com6 = Comment('Sofia', 'Pollyanna', 'I like it')
com7 = Comment('Mickle', 'Charlie and the Chocolate Factory', 'Not bad')
com8 = Comment('Anna', 'Yellow Fang', 'exciting book')
com9 = Comment('Boris', 'Charlie and the Chocolate Factory', 'my favorite book')



class Book:
    """
    Class that describes a book.
    """
    def __init__(self, author, name, year, edition, genre, *comments):
        self.author = author
        self.name = name
        self.year = year
        self.edition = edition
        self.genre = genre
        self.comments = comments

    def print_comments(self):
        comments = ''
        for n, c in enumerate(self.comments, start=1):
            comments += '%d.%s\n' % (n, str(c))
        return comments

    def __eq__(self, other):
        return self.author == other.author and self.name == other.name

    def __repr__(self):
        return '%s_%s_%d' % ('_'.join(self.author.split(' ')), '_'.join(self.name.split(' ')), self.year)

    def __str__(self):
        return '%s - %s(%d).%s edition.\nComments:\n%s ' % (self.author, self.name, self.year,
                                                            self.num(self.edition), self.print_comments())

    def num(self,number):
        num_dict ={
            '1': 'st',
            '2': 'nd',
            '3': 'rd',
            '4': 'th'
        }
        last_digit = str(number)[-1:]
        last_2_digits = str(number)[-2:]
        if 20 >= int(last_2_digits) >= 4 :
            return '%s-%s' % (number, num_dict['4'])
        elif int(last_digit) >= 4:
            return '%s-%s' % (number, num_dict['4'])
        else:
            return '%s-%s' % (number, num_dict[last_digit])

book1 = Book("Roald Dahl", "Charlie and the Chocolate Factory", 1964, 4, "Fantasy novel", com3, com7, com9)
book2 = Book("Jack Jordan", "Yellow Fang", 1992, 5, "Comedy", com1, com5, com8)
book3 = Book("Eleanor H. Porter", "Pollyanna", 1913, 10, "Novel", com2, com4, com6)

print(book1)
print(book2)
print(book3)
