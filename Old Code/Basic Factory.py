from abc import ABC, abstractmethod, ABCMeta


class ITracker(metaclass=ABCMeta):

    @abstractmethod
    def track_price(self):
        """ Interface Method """

class NewEgg(ITracker):

    def track_price(self):
        print("Getting price from NewEgg")

class Amazon(ITracker):

    def track_price(self):
        print("Getting price from Amazon")

class BestBuy(ITracker):

    def track_price(self):
        print("Getting price from BestBuy")



class TrackerFactory:

    @staticmethod
    def choose_tracker(choice):
        if choice == "NewEgg":
            return NewEgg()
        elif choice == "Amazon":
            return Amazon()
        elif choice == "BestBuy":
            return BestBuy()
        else:
            raise ValueError("Invalid choice")



if __name__ == "__main__":
    choice = input("Please enter your choice: ")
    track = TrackerFactory.choose_tracker(choice)
    track.track_price()