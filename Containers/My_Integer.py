class Integer:
    def __init__(self, value):
        # Constructor to initialize the Integer with a value
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError("Value must be an integer.")

    def __repr__(self):
        # String representation of the Integer
        return f"Integer({self.value})"

    # Arithmetic Operations
    def __add__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value + other.value)
        raise TypeError("Operand must be an Integer.")

    def __sub__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value - other.value)
        raise TypeError("Operand must be an Integer.")

    def __mul__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value * other.value)
        raise TypeError("Operand must be an Integer.")

    def __truediv__(self, other):
        if isinstance(other, Integer):
            if other.value == 0:
                raise ZeroDivisionError("division by zero")
            return Integer(self.value // other.value)
        raise TypeError("Operand must be an Integer.")

    def __floordiv__(self, other):
        if isinstance(other, Integer):
            if other.value == 0:
                raise ZeroDivisionError("division by zero")
            return Integer(self.value // other.value)
        raise TypeError("Operand must be an Integer.")

    def __mod__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value % other.value)
        raise TypeError("Operand must be an Integer.")

    def __pow__(self, other):
        if isinstance(other, Integer):
            return Integer(self.value ** other.value)
        raise TypeError("Operand must be an Integer.")

    def __neg__(self):
        # Negation of the integer
        return Integer(-self.value)

    # Comparison Operations
    def __eq__(self, other):
        if isinstance(other, Integer):
            return self.value == other.value
        raise TypeError("Operand must be an Integer.")

    def __lt__(self, other):
        if isinstance(other, Integer):
            return self.value < other.value
        raise TypeError("Operand must be an Integer.")

    def __le__(self, other):
        if isinstance(other, Integer):
            return self.value <= other.value
        raise TypeError("Operand must be an Integer.")

    def __gt__(self, other):
        if isinstance(other, Integer):
            return self.value > other.value
        raise TypeError("Operand must be an Integer.")

    def __ge__(self, other):
        if isinstance(other, Integer):
            return self.value >= other.value
        raise TypeError("Operand must be an Integer.")

    def __ne__(self, other):
        if isinstance(other, Integer):
            return self.value != other.value
        raise TypeError("Operand must be an Integer.")

    # Integer-specific methods
    def is_positive(self):
        return self.value > 0

    def is_negative(self):
        return self.value < 0

    def is_zero(self):
        return self.value == 0

    def absolute(self):
        return Integer(abs(self.value))

    def to_string(self):
        return str(self.value)

    # Other utilities
    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)

