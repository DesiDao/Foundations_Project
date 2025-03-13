class TestLinkedList:
    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.length() == 3
        assert ll.get_last() == 3
        print("Append Test Passed")

    def test_prepend(self):
        ll = LinkedList()
        ll.append(1)
        ll.prepend(0)
        assert ll.length() == 2
        assert ll.head.value == 0
        print("Prepend Test Passed")

    def test_delete(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.delete(2)
        assert ll.length() == 2
        assert not ll.search(2)
        print("Delete Test Passed")

    def test_search(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        assert ll.search(10) == True
        assert ll.search(15) == False
        print("Search Test Passed")

    def test_print_list(self):
        ll = LinkedList()
        ll.append(5)
        ll.append(10)
        ll.append(15)
        ll.print_list()  # Should print 5 -> 10 -> 15 -> None
        print("Print List Test Passed")

    def test_remove_last(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.remove_last()
        assert ll.length() == 2
        assert ll.get_last() == 2
        print("Remove Last Test Passed")

    def test_is_empty(self):
        ll = LinkedList()
        assert ll.is_empty() == True
        ll.append(1)
        assert ll.is_empty() == False
        print("Is Empty Test Passed")

    def run_tests(self):
        self.test_append()
        self.test_prepend()
        self.test_delete()
        self.test_search()
        self.test_print_list()
        self.test_remove_last()
        self.test_is_empty()


# Running the test class
test = TestLinkedList()
test.run_tests()

