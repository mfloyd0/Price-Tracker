from TrackerInterface import ITracker



class NewEgg(ITracker):

    def track_price(self):
        print("Getting price from NewEgg")