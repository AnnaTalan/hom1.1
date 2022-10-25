import datetime


class Comment:

    def __init__(self, user, book, comment):
        self.user = user
        self.book = book
        self.date = datetime.date.today()
        self.comment = comment

    def __str__(self):
        return '%s writes about %s : %s. %s.' % (self.user, self.book, self.comment, self.date)

com1 = Comment('Steave', 'Harry Potter', 'I do not like this book')
com2 = Comment('Joy', 'Harry Potter', 'very interesting book')
com3 = Comment('Zoe', 'Harry Potter', 'I think it is quite boring book')
book = map(str, input().split())
print(com1)
print(com2)
print(com3)