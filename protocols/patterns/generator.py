def generator():
    for i in range(3):
        x = yield i
        print(x)

g = generator()
next(g)
g.send("foo bar!")
next(g)
next(g)
next(g)
next(g)
next(g)
# also raise StopIteration at end

