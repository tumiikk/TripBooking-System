class Flight:
    def __init__(self, origin, destination, price):
        self.data = (origin, destination, price)

    def to_dict(self):
        return {
            "origin": self.data[0],
            "destination": self.data[1],
            "price": self.data[2]
        }