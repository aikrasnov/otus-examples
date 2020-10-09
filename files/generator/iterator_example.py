class Squares(object):

    def __init__(self, start, stop):
       self.start = start
       self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
       if self.start >= self.stop:
           raise StopIteration
       current = self.start * self.start
       self.start += 1
       return current

    def __getitem__(self, item):
        print(item)

iterator = Squares(1, 10)
iterator[1]

# for item in iterator:
#     print(item)