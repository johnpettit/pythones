class EVBase:
    """Base Class for EV Data Objects"""
    internalCount = 0

    def __init__(self):
        self.internalCount = self.internalCount + 1

    def showCount(self):
        return self.internalCount


# self test

jp = EVBase()
print(jp.__doc__)
print(jp.showCount())