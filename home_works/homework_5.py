class Distance:
    def init(self, value, unit):
        self.value = value
        self.unit = unit

    def str(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        if self.unit == "mm":
            return self.value / 1000
        elif self.unit == "cm":
            return self.value / 100
        elif self.unit == "m":
            return self.value
        elif self.unit == "km":
            return self.value * 1000
        else:
            raise ValueError("Неизвестная единица измерения")

    def add(self, other):
        total_meters = self.to_meters() + other.to_meters()
        return Distance(total_meters, "m")

a = Distance(10, "m")
b = Distance(2, "km")
c = Distance(150, "cm")

print(a)
print(b)
print(c)
print(a + b)
print(a + c)