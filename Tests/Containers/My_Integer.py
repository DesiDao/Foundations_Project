class TestInteger:
    def test_initialization(self):
        try:
            i1 = Integer(10)
            i2 = Integer(-5)
            i3 = Integer(0)
            print("Initialization Test Passed")
        except Exception as e:
            print(f"Initialization Test Failed: {e}")

    def test_arithmetic_operations(self):
        try:
            i1 = Integer(10)
            i2 = Integer(5)
            assert (i1 + i2).value == 15
            assert (i1 - i2).value == 5
            assert (i1 * i2).value == 50
            assert (i1 / i2).value == 2
            assert (i1 // i2).value == 2
            assert (i1 % i2).value == 0
            assert (i1 ** i2).value == 100000
            print("Arithmetic Operations Test Passed")
        except AssertionError as e:
            print(f"Arithmetic Operations Test Failed: {e}")

    def test_comparison_operations(self):
        try:
            i1 = Integer(10)
            i2 = Integer(5)
            assert i1 == Integer(10)
            assert i1 != i2
            assert i1 > i2
            assert i1 >= i2
            assert i2 < i1
            assert i2 <= i1
            print("Comparison Operations Test Passed")
        except AssertionError as e:
            print(f"Comparison Operations Test Failed: {e}")

    def test_miscellaneous_methods(self):
        try:
            i1 = Integer(-10)
            assert i1.is_positive() == False
            assert i1.is_negative() == True
            assert i1.is_zero() == False
            assert i1.absolute().value == 10
            assert i1.to_string() == "-10"
            print("Miscellaneous Methods Test Passed")
        except AssertionError as e:
            print(f"Miscellaneous Methods Test Failed: {e}")

    def run_tests(self):
        self.test_initialization()
        self.test_arithmetic_operations()
        self.test_comparison_operations()
        self.test_miscellaneous_methods()


# Running the test class
test = TestInteger()
test.run_tests()

