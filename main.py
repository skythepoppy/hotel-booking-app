import pandas

df = pandas.read_csv("hotels.csv")
class Hotel:
    def __init__(self,id):
        pass
    def book(self):
        pass

    def available(self):
        pass


class ReservationTicket:
    def __init__(self, user_name, hotel_obj):
        pass

    def generate(self):
        pass


print(df)
id = input("Enter the ID of the hotel: ")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    user_name = input("Please enter your name: ")
    reservation_ticket = ReservationTicket(user_name, hotel)
    reservation_ticket.generate()
    print(reservation_ticket.generate())
else:
    print("Hotel is not free")