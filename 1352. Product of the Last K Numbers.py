class ProductOfNumbers:
    def __init__(self):
        self.prefix = [1]

    def add(self, a: int) -> None:
        if a == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * a)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix):
            return 0
        return self.prefix[-1] // self.prefix[-(k+1)]
