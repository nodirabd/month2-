class Distance:
    conversion = {'cm': 0.01, 'm': 1, 'km': 1000}

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def __add__(self, other):
        self_in_meters = self.value * self.conversion[self.unit]
        other_in_meters = other.value * self.conversion[other.unit]
        total_meters = self_in_meters + other_in_meters

        result_value = total_meters / self.conversion[self.unit]
        return Distance(result_value, self.unit)

d1 = Distance(10, 'm')
d2 = Distance(2, 'km')
d3 = Distance(5004, 'cm')
d4 = Distance(23, 'km')
print(f"Первая дистанция: {d1}")
print(f"Вторая дистанция: {d2}")
print(f"Результат сложения в метрах: {d1+d2+d3+d4}")
