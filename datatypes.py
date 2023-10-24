#types of data types
number = 24
second =56.78

ispythonninteresting = True

# multiple values stored in a vsingle ariable
cars = ["toyota", "mazda", "nissan"]  # list -ordered and changeable
fruits = ("banana", "Apple", "Orange")  # tuple -ordered and Unchangeable
country = {"Kenya", " Tanzania", "DRC"}  # set -unordered and unchangeable
details = {
    "firstname": "Mariam",
    "age": 34,
    "course": "Web Development",  # dictionary key-value pair
    "nationality": "Kenya"
}
print(cars)
print(country)
print(details["course"])
# determine the data type
print(type(country))
print(type(fruits))


# typecasting- converting data types

print(float(number))
print(int(second))