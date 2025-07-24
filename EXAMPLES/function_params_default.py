def hello(target="world"):
    print(f"Hello, {target}")

hello("Mom")
hello("New York")
hello()  # uses default

def foo():
    x = 5  # nonlocal to bar(); local to foo()
    def bar():
        print(x)
