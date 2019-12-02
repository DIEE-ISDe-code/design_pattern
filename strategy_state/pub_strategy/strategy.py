from abc import ABC, abstractmethod
class Strategy(ABC):

    @abstractmethod
    def getActualPrice(self, value):
        pass  # DO NOTHING


class NormalStrategy(Strategy):
    def getActualPrice(self, value):
        return value


class HappyHourStrategy(Strategy):
    def getActualPrice(self, value):
        # (50 % discount)
        return value*0.5




