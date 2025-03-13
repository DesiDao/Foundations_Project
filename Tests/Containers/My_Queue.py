class QueueTest:
    @staticmethod
    def run_tests():
        q = Queue()
        assert q.is_empty() == True, "Test 1 Failed"
        assert q.size() == 0, "Test 2 Failed"
        
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        assert q.is_empty() == False, "Test 3 Failed"
        assert q.size() == 3, "Test 4 Failed"
        assert q.peek() == 10, "Test 5 Failed"
        
        assert q.dequeue() == 10, "Test 6 Failed"
        assert q.size() == 2, "Test 7 Failed"
        assert q.peek() == 20, "Test 8 Failed"
        
        assert q.dequeue() == 20, "Test 9 Failed"
        assert q.dequeue() == 30, "Test 10 Failed"
        assert q.is_empty() == True, "Test 11 Failed"
        
        try:
            q.dequeue()
            assert False, "Test 12 Failed - Should have raised an exception"
        except IndexError:
            pass
        
        try:
            q.peek()
            assert False, "Test 13 Failed - Should have raised an exception"
        except IndexError:
            pass
        
        print("All tests passed!")

# Run tests
QueueTest.run_tests()
