from abc import ABC, abstractmethod, ABCMeta


class ITracker(metaclass=ABCMeta):

    @abstractmethod
    def track_price(self):
        """ Interface Method """