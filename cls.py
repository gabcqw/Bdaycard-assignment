from typing import Any


class Human:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.bag = {}
        self.counter = 0

    # double underscore -> __  / dunder / _ _
    def __str__(self):
        # <Human: Anna, 24>
        return self.name

    def __repr__(self):
        # \/Human: Anna, 24\/
        return f"<{self.name}, {self.age}>"

    def __int__(self):
        half_age = self.age / 2
        half_age = int(half_age)
        return half_age

    def __float__(self):
        return self.weight

    def __bool__(self):
        # Check if somebody is 18 years old or older
        return self.age >= 18

    def __setitem__(self, key, value):
        """Allows to set count of certain elements in a bag."""
        # dict_obj[key] = value  ->   dict_obj.__setitem__(key, value)
        # print(f"I am assigning {value} to {key}.")
        self.bag[key] = value

    def __getitem__(self, key):
        """Allows to check for a count of certain elements of a bag."""
        # dict_obj[key]   ->   return dict_obj.__getitem__(key)
        return self.bag[key]

    def __iter__(self):
        """Allows to go through the content of the bag."""
        for product in self.bag:
            yield product
        # return iter(self.bag)
        # return self

    def __next__(self):
        if self.counter == len(self.bag):
            raise StopIteration
        retval = list(self.bag)[self.counter]
        self.counter += 1
        return retval

    def generator(self):
        for product in self.bag:
            yield product

    def values(self):
        for val in self.bag.values():
            yield val

    def generate_tuples_names_counts(self):
        for product, count in self.bag.items():
            yield product, count


hum = Human(name="Anna", age=24, weight=54.2)
hum2 = Human(name="Carl", age=24, weight=80.0)
hum3 = Human(name="Monique", age=15, weight=40.0)

# hum.bag["books"] = 2
hum["books"] = 2
hum["t-shirts"] = 6
hum["shampoos"] = 1
hum["toothbrush"] = 2

# print(hum.name, "has books:", hum.bag["books"])
# print(f"{hum} has books:", hum["books"])


for product in hum:
    print(product)

# for counts in hum.values():
#     print(counts)

# print("Generate pairs:")
# for product, count in hum.generate_tuples_names_counts():
#     print(f"{product}: {count}")


# print(str(hum))
# print(repr(hum))

# print("Integer of object:", hum.__int__())
# print("Integer of object:", int(hum))
# print("Float of object:", float(hum))

# combined_ages = int(hum) + int(hum2)
# print("Combined ages:", combined_ages)

# print()
# print(f"{hum.name} can enter the club: {bool(hum)}")
# print(f"{hum2.name} can enter the club: {bool(hum2)}")
# print(f"{hum3.name} can enter the club: {bool(hum3)}")


def list_people_in_queue():
    max_people = 20
    current_people = 18
    while True:
        name = input("Add your name: ")
        if current_people >= max_people:
            print("Limit has been reached. Ending...")
            return
        if not name:
            return
        age = int(input("Add your age: "))
        current_people += 1
        yield Human(name=name, age=age, weight=0.0)


# for person in list_people_in_queue():
#     print(f"{person.name} can enter the club: {bool(person)}")


class WeatherForecast:
    pass


wf = WeatherForecast()

# set item
wf["2023-01-01"] = "not raining"

# get item
print(wf["2023-01-01"])

# iter
for date in wf:
    print(date)

# items
for date, forecast in wf.items():
    print(date, forecast)
