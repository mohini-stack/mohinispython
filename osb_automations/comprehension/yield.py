def gen123():
    print("About to print yield 2")
    yield 2
    print("About to print yield 3")
    yield 3
g=gen123()
try:
    next(g)
    next(g)
    next(g)
    next(g)
except StopIteration:
    print("Oyye itne hain he nahi iterator main")
