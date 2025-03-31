import math

def add_vectors(self, other, factor=1):
    if not isinstance(other, Vector):
        raise TypeError("Can not add a vector type to a non vector type")
    values1 = [value for name, value in vars(self).items()]
    values2 = [value for name, value in vars(other).items()]
    if len(values1) != len(values2):
        raise ValueError("Can not add vectors of different dimensions")
    added_values = [values1[index] + values2[index] * factor for index in range(len(values1))]
    return Vector(*added_values)


def multiply_vectors(self, other):
    values1 = [value for name, value in vars(self).items()]
    values2 = [value for name, value in vars(other).items()]
    if len(values1) != len(values2):
        raise ValueError("Can not multiply vectors of different dimensions")
    multiplied = [values1[i] * values2[i] for i in range(len(values1))]
    return sum(multiplied)


def scalar_multiply(self, scale):
    values = [round(value * scale, 4) for name, value in vars(self).items()]
    return Vector(*values)


def multiply(self, other):
    if isinstance(other, Vector):
        return multiply_vectors(self, other)
    elif isinstance(other, (int, float)):
        return scalar_multiply(self, other)
    else:
        raise TypeError("Vector can be multiplied only by vector, int or float type")


class Vector:

    def __init__(self, *args):
        for index, value in enumerate(args):
            setattr(self, f"attr{index + 1}", value)

    def __repr__(self):
        out = "Vector("
        for i, value in vars(self).items():
            out += f"{value}, "
        out = out[:-2]
        out += ')'
        return out

    def __add__(self, other):
        return add_vectors(self, other)

    def __radd__(self, other):
        return add_vectors(self, other)

    def __sub__(self, other):
        return add_vectors(self, other, -1)

    def __rsub__(self, other):
        return add_vectors(self, other, -1)

    def __mul__(self, other):
        return multiply(self, other)

    def __rmul__(self, other):
        return multiply(self, other)

    def magnitude(self):
        return math.sqrt(sum(attr_value ** 2 for attr_name, attr_value in vars(self).items()))

    def normalize(self):
        length = self.magnitude()
        return scalar_multiply(self, 1/length)


# Create vectors
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)  # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)  # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)  # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product)  # Output: 32

# Scalar multiplication
v5 = 3 * v1
print(v5)  # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)  # Output: Vector(0.267, 0.534, 0.801)
