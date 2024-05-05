class Jar():
    def __init__(self, coo_capacity=12):
        try:
            coo_capacity = int(coo_capacity)
            if coo_capacity < 0:
                raise ValueError
        except:
            raise ValueError

        self.coo_capacity = coo_capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if self.cookies + n > self.coo_capacity:
            raise ValueError
        else:
            self.cookies += n

    def withdraw(self, n):
        if self.cookies - n < 0:
            raise ValueError
        else:
            self.cookies -= n

    @property
    def capacity(self):
        return self.coo_capacity

    @property
    def size(self):
        return self.cookies
