class StringTest:
    def __init__(self):
        self.run_tests()

    def run_tests(self):
        self.test_initialization()
        self.test_length()
        self.test_concatenation()
        self.test_equality()
        self.test_to_upper()
        self.test_to_lower()
        self.test_char_at()
        self.test_substring()
        self.test_compare_to()
        print("All tests passed.")

    def test_initialization(self):
        s = String("Hello")
        assert str(s) == "Hello", f"Expected 'Hello', got '{str(s)}'"

    def test_length(self):
        s = String("Hello")
        assert s.length() == 5, f"Expected 5, got {s.length()}"

    def test_concatenation(self):
        s1 = String("Hello")
        s2 = String("World")
        s1.concat(s2)
        assert str(s1) == "HelloWorld", f"Expected 'HelloWorld', got '{str(s1)}'"

    def test_equality(self):
        s1 = String("Hello")
        s2 = String("Hello")
        s3 = String("World")
        assert s1.equals(s2), f"Expected True, got {s1.equals(s2)}"
        assert not s1.equals(s3), f"Expected False, got {s1.equals(s3)}"

    def test_to_upper(self):
        s = String("hello")
        s.to_upper()
        assert str(s) == "HELLO", f"Expected 'HELLO', got '{str(s)}'"

    def test_to_lower(self):
        s = String("HELLO")
        s.to_lower()
        assert str(s) == "hello", f"Expected 'hello', got '{str(s)}'"

    def test_char_at(self):
        s = String("Hello")
        assert s.char_at(1) == 'e', f"Expected 'e', got {s.char_at(1)}"
        try:
            s.char_at(10)
            assert False, "Expected IndexError"
        except IndexError:
            pass

    def test_substring(self):
        s = String("HelloWorld")
        sub = s.substring(0, 5)
        assert str(sub) == "Hello", f"Expected 'Hello', got '{str(sub)}'"
        try:
            s.substring(0, 20)
            assert False, "Expected IndexError"
        except IndexError:
            pass

    def test_compare_to(self):
        s1 = String("apple")
        s2 = String("banana")
        assert s1.compare_to(s2) < 0, f"Expected value < 0, got {s1.compare_to(s2)}"
        assert s2.compare_to(s1) > 0, f"Expected value > 0, got {s2.compare_to(s1)}"
        assert s1.compare_to("apple") == 0, f"Expected 0, got {s1.compare_to('apple')}"

# Run the tests
StringTest()

