class Booking:
    def __init__(self, username, origin, destination, price):
        self.username = username
        self.origin = origin
        self.destination = destination
        self.price = price

    def to_dict(self):
        return {
            "username": self.username,
            "origin": self.origin,
            "destination": self.destination,
            "price": self.price
        }