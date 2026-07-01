from sitetrackers import newegg, bestbuy
from sitetrackers import amazon
from urllib.parse import urlsplit





class TrackerFactory:

    @staticmethod
    def choose_tracker(product):
        # Extract the full hostname string
        hostname = urlsplit(product["URL"]).hostname

        if hostname == "www.newegg.com":
            return newegg.NewEgg()
        elif hostname == "www.amazon.com":
            print("Amazon Tracker Started")
            return amazon.Amazon()
        elif hostname == "www.bestbuy.com":
            print("Best Buy Tracker Started")
            return bestbuy.BestBuy()
        else:
            raise ValueError("Invalid choice")

