from collections import namedtuple

booking = namedtuple("Bookings", 'No bookingcode gender Names')
book = booking('T1', 'C123141-1', 'F', ('kim', 'aa'))
print(type(book))
print(book)
print(book.Names)
print(book[2])