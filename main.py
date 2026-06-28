from TrackerFactory import TrackerFactory








if __name__ == "__main__":
    factory = TrackerFactory()
    track = factory.choose_tracker("Amazon")
    track.track_price()
