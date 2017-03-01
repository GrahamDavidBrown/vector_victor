import math

class NotSameShapeError(ValueError):
    pass


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def shape(self):
        return ((len(self.vector), ))

    def __add__(self, other):
        if self.shape != other.shape:
            raise NotSameShapeError
        else:
            new_vector = Vector([])
            zipped = zip(self.vector, other.vector)
            new_vector.vector += [(pair[0] + pair[1]) for pair in zipped]
            return new_vector

    def vector_add(self, other):
        return(self + other)

    def __sub__(self, other):
        new_vector = Vector([])
        zipped = zip(self.vector, other.vector)
        new_vector.vector += [(pair[0] - pair[1]) for pair in zipped]
        return new_vector

    def vector_sum(self, *args):
        print(type(self))
        new_vector = self
        for arg in args:
            new_vector += arg
        return new_vector

    def dot(self, other):
        if self.shape[0] != other.shape[0]:
            raise NotSameShapeError
        else:
            new_vector = Vector([])
            zipped = zip(self.vector, other.vector)
            new_vector.vector += [(pair[0] * pair[1]) for pair in zipped]
            scalar = 0
            for num in new_vector.vector:
                scalar += num
        return new_vector

    def vector_multiply(self, exponent):
        new_vector = self
        new_vector.vector = [num * exponent for num in new_vector.vector]
        return new_vector

    def vector_mean(self, *args):
        new_vector = ([])
        count = 1
        count += [1 for arg in args]
        new_vector.vector = new_vector.vector_add(*args)
        new_vector.vector = new_vector.vector_multiply((1 / count))
        return new_vector

    def magnitude():
        new_vector = ([])
        count = 1
        new_vector.vector = [new_vector.vector_multiply(num) for num in new_vector.vector]
        new_vector.vector = [(num) ** .5 for num in new_vector.vector]


v1 = Vector([1, 2, 3, 4, 5])
v2 = Vector([6, 7, 8, 9, 10])
v3 = Vector([1, 1, 1, 1, 1])
v6 = Vector([2, 2, 2, 2, 2])
v5 = Vector([v1.vector_sum(v2, v3, v6)])
v4 = ((v1 + v2 + v3))
print(sqrt(4))
