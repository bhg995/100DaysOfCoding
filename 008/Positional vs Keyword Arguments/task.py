# Functions with input

## Positional argument, error-prone
def greet_with_name(location, name, celsius):
    print(f"Hello {name}")
    print(f"It's about {celsius} degrees celsius in {location}")


greet_with_name("New York", "John", 23)


## Keyword argument, Longer lines of code
def greet_with_name(location, name, celsius):
    print(f"Hello {name}")
    print(f"It's about {celsius} degrees celsius in {location}")


greet_with_name(name="John", location="New York", celsius=23)

