import pandas

df = pandas.read_csv("hotels.csv", dtype={"id":str})    # takes in all 'id' values as str
class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
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
    def __init__(self, customer_name, hotel_obj):
        self.customer_name = customer_name
        self.hotel = hotel_obj

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """

        return content

print(df)
hotel_id = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    user_name = input("Please enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=user_name, hotel_obj=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free")