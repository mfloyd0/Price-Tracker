from sitetrackers import  newegg
from sitetrackers import amazon




class TrackerFactory:

    @staticmethod
    def choose_tracker(choice):
        if choice == "NewEgg":
            return newegg.NewEgg()
        elif choice == "Amazon":
            print("Amazon Tracker Started")
            return amazon.Amazon()
        else:
            raise ValueError("Invalid choice")

