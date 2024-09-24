
import pytest
from lib.stack import Stack  # Make sure the path is correct

class TestStack:
    '''Class to test Stack in Stack.py'''

    def test_init(self):
        '''Initialize Stack with a list of items'''
        stk = Stack([1, 2, 3, 4, 5])
        expected = [1, 2, 3, 4, 5]
        for index in range(len(expected)):
            assert expected[index] == stk.items[index]

    def test_push(self):
        '''Push an item onto the stack'''
        stk = Stack([1, 2, 3, 4, 5])
        stk.push(0)
        expected = [1, 2, 3, 4, 5, 0]
        for index in range(len(expected)):
            assert expected[index] == stk.items[index]

    def test_pop(self):
        '''Pop an item off the stack'''
        stk = Stack([1, 2, 3, 4, 5])
        stk.pop()
        expected = [1, 2, 3, 4]
        for index in range(len(expected)):
            assert expected[index] == stk.items[index]

    def test_size(self):
        '''Test the size() method of the stack'''
        stk = Stack([1, 2, 3, 4, 5])
        expected_size = len([1, 2, 3, 4, 5])
        assert stk.size() == expected_size

    def test_is_empty_and_pop(self):
        '''Test the is_empty() method and pop() when empty'''
        stk = Stack()
        assert stk.is_empty()
        assert stk.size() == 0
        with pytest.raises(IndexError):
            stk.pop()
        stk.push(1)
        assert not stk.is_empty()
        assert stk.size() == 1
        assert stk.pop() == 1

    def test_full(self):
        '''Test the full() method'''
        stk = Stack([1], 1)  # Stack initialized with 1 item, max_size of 1
        assert stk.full()     # Stack is full
        assert stk.size() == 1
        assert stk.pop() == 1  # Popping should work

        stk.push(1)  # Restore stack to "full" state
        # Pushing another item should raise IndexError
        with pytest.raises(IndexError):
            stk.push(2)

    def test_search(self):
        '''Test the search() method to find element distance'''
        stk = Stack([5, 6, 7, 8, 9, 10])  # Stack elements
        assert stk.search(5) == 5  # 5 is at the bottom, 5 places away from the top
        assert stk.search(6) == 4
        assert stk.search(7) == 3
        assert stk.search(8) == 2
        assert stk.search(9) == 1
        assert stk.search(10) == 0  # 10 is at the top

        # Case with target not in stack
        assert stk.search(15) == -1  # Item not found
