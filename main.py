import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})    # takes in all 'id' values as str
class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
    def book(self):
        """Books a hotel by changing its availability to 'no' """
        df.loc[df["id"] == self.hotel_id,"available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, user_name, hotel_obj):
        pass

    def generate(self):
        pass


print(df)
hotel_id = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    user_name = input("Please enter your name: ")
    reservation_ticket = ReservationTicket(user_name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free")