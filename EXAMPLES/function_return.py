def get_hello():
    return "Hello, world"

h = get_hello() 
print(f"{h = }")

def hello():
    print("Hello, world")
    # return None

h = hello()
print(f"{h = }")

def double(x):
    return x * 2

d = double(10)
print(f"{d = }")

def doit(a, b):
    print(f"{a = } {b = }")

doit(5, 10)
doit('spam', 'ham')
# doit(8)  INVALID 
