class Location:
    def __init__(self,lat,long):
        self.lat=lat
        self.long=long

    def __repr__(self):
        return f"location(lat={self.lat},long={self.long}"