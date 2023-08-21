import pandas


""" Initialize data frames"""
df = pandas.read_csv("hotels.csv", dtype={"id":str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv", dtype=str)


class Hotel:
    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()
    def book(self):
        """Books a hotel and changes its availability to 'no' """
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
        """Generate a message sent to the user"""
        content = f"""
        Thank you for your reservation!
        Here is your booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """

        return content


class CreditCard:
    def __init__(self, number):
        self.number = number
    def validate(self, expiration, holder, cvc):
        """Validate card information from .csv file"""
        card_data={"number": self.number, "expiration": expiration,
                   "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        """Authenticate card information based on security information in .csv file"""
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


print(df)
hotel_id = input("Enter the ID of the hotel: ")
hotel = Hotel(hotel_id)

if hotel.available():
    credit_card = SecureCreditCard(number="1254767899128446")
    if credit_card.validate(expiration="4/27", holder="JAYCE PILTOVER", cvc="603"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            user_name = input("Please enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=user_name, hotel_obj=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication failed!")
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not free")