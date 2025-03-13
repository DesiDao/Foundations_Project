class StackTest:
    @staticmethod
    def run_tests():
        s = Stack()
        assert s.is_empty() == True, "Test 1 Failed"
        assert s.size() == 0, "Test 2 Failed"
        
        s.push(10)
        s.push(20)
        s.push(30)
        assert s.is_empty() == False, "Test 3 Failed"
        assert s.size() == 3, "Test 4 Failed"
        assert s.peek() == 30, "Test 5 Failed"
        
        assert s.pop() == 30, "Test 6 Failed"
        assert s.size() == 2, "Test 7 Failed"
        assert s.peek() == 20, "Test 8 Failed"
        
        assert s.pop() == 20, "Test 9 Failed"
        assert s.pop() == 10, "Test 10 Failed"
        assert s.is_empty() == True, "Test 11 Failed"
        
        try:
            s.pop()
            assert False, "Test 12 Failed - Should have raised an exception"
        except IndexError:
            pass
        
        try:
            s.peek()
            assert False, "Test 13 Failed - Should have raised an exception"
        except IndexError:
            pass
        
        print("All tests passed!")

# Run tests
StackTest.run_tests()

